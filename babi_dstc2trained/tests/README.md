# Fabot

## data
download the [dstc2 data](http://camdial.org/~mh521/dstc/). Default location is under dstc2/data/trndev/dstc2/

## run test cases

From project root, run:
```
python -m unittest tests.<path>.<class>.<function>
```
For instance, to test data_processor.TestData_processor.test_act_to_rasa
function, issue:
```
python -m unittest tests.data.data_processor.TestData_processor.test_act_to_rasa
```