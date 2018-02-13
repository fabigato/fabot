def ner_cv(data, n_folds, nlu_config):
    from sklearn import metrics
    from sklearn.model_selection import StratifiedKFold
    from collections import defaultdict
    from rasa_nlu.model import Trainer, TrainingData
    from rasa_nlu.model import Interpreter
    from rasa_nlu.evaluate import get_entity_extractors, align_entity_predictions, merge_labels, substitute_labels, \
        log_evaluation_table
    from rasa_nlu.config import RasaNLUConfig
    import logging
    # type: (List[rasa_nlu.training_data.Message], int, RasaNLUConfig) -> Dict[Text, List[float]]
    """
    Performs Stratified cross validation on NER components

    :param data: list of rasa_nlu.training_data.Message objects
    :param n_folds: integer, number of cv folds
    :param nlu_config: nlu config file. Notice that the pipeline must include the NER components and all of their
    requirements. Other non-NER related components in the pipeline (e.g. intent classifiers) are ignored and result in
    wasted time since all models in the pipeline are trained.
    :return: dictionary with key, list structure, where each entry in list
              corresponds to the relevant result for one fold
    """
    logger = logging.getLogger(__name__)
    trainer = Trainer(nlu_config)
    results = defaultdict(list)

    y_true = [e.get("intent") for e in data]  # Stratified kfold means proportion of labels is preserved in each fold.
    # but what does that mean when your labels are several classes per utterance? How can you preserve 'cuisine' labels
    # while at the same time preserving 'location' if they are both correlated? Here, we assume that 'intent' is a
    # variable that explains the co-occurrence, and therefore, by keeping the proportion of intents, we keep the right
    # proportion of entities per utterance

    skf = StratifiedKFold(n_splits=n_folds, random_state=11, shuffle=True)
    counter = 1
    logger.info("Evaluation started")
    accu_pred, accu_target = [], []
    for train_index, test_index in skf.split(data, y_true):  # repeats n_folds times

        train = [data[i] for i in train_index]  # build our train/test split for this fold
        test = [data[i] for i in test_index]

        logger.debug("Fold: {}".format(counter))
        logger.debug("Training ...")
        trainer.train(TrainingData(training_examples=train))  # train all models in the pipeline
        model_directory = trainer.persist("projects/")  # save model and return the directory the model is stored in

        logger.debug("Evaluation ...")
        interpreter = Interpreter.load(model_directory, nlu_config)  # load the model you just saved

        entity_targets = [e.get("entities", []) for e in test]  # list of lists of dictionaries

        entity_predictions, tokens = [], []
        for e in test:  # get our predictions
            res = interpreter.parse(e.text, only_output_properties=False)
            entity_predictions.append(res['entities'] if 'entities' in res else [])  # list of lists of dictionaries
            tokens.append(res["tokens"])

        extractors = get_entity_extractors(interpreter)  # each ner component will be tested separately

        aligned_predictions = []
        for ts, ps, tks in zip(entity_targets, entity_predictions, tokens):  # all predictions, along with extractors
            aligned_predictions.append(align_entity_predictions(ts, ps, tks, extractors))
            # {'target_labels':List[entities], 'extractor_labels':{'extractor_name':List[entities]}}
            # each token will be associated to an entity. 'Chinese in the south' yields [cuisine, O, O, location]

        merged_targets = merge_labels(aligned_predictions)  # make targets a single concatenated list of slots
        # [[ent11, ent12], [ent21], []] -> [ent11, ent12, ent21]
        merged_targets = substitute_labels(merged_targets, "O", "no_entity")  # replace 'Os' by "no_entity"

        for extractor in extractors:  # now we test each extractor. But their total f1/accuracy/precision are averaged
            merged_predictions = merge_labels(aligned_predictions, extractor)  # we keep each pred along with extractor
            merged_predictions = substitute_labels(merged_predictions, "O", "no_entity")  # put 'O' on empty slots
            logger.info("Evaluation for entity extractor: {} ".format(extractor))
            log_evaluation_table(merged_targets, merged_predictions)  # print a table with metrics for this extractor
            accu_pred += merged_predictions
            accu_target += merged_targets
            results["Accuracy"].append(metrics.accuracy_score(merged_targets, merged_predictions))
            results["F1-score"].append(metrics.f1_score(merged_targets, merged_predictions, average='weighted'))
            results["Precision"].append(metrics.precision_score(merged_targets, merged_predictions, average='weighted'))
    logger.info("Final report across all folds:")
    log_evaluation_table(accu_target, accu_pred)
    return dict(results)
