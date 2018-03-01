# DSTC 2
## bot acts
| Act              | Definition                     | Example                                                                                                                                   |
|------------------|:------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------|
|inform            | Confirms slot value filled     | taj tandoori is a nice restaurant in the south of town serving indian food                                                                |
|offer             | Suggests restaurant            | taj tandoori is a nice restaurant in the south of town serving indian food                                                                |
|request           | Ask user how to fill a slot    | What kind of food would you like?                                                                                                         |
|welcomemsg        | Greet the user                 | Hello , welcome to the Cambridge restaurant system? You can ask for restaurants by area , price range or food type . How may I help you?  |
|canthelp          | Inform no results              | I'm sorry but there is no restaurant serving cantonese food                                                                               |
|expl-conf         | Explicit slot confirmation     | Ok , a restaurant in any part of town is that right?                                                                                      |
|select            | Ask user to select slot value* | Sorry would you like romanian or portuguese food?                                                                                         |
|reqmore           | Ask if more info needed        | Can I help you with anything else?                                                                                                        |
|canthelp.exception| Exhausted options offered**    | I am sorry but there is no other spanish restaurant that matches your request                                                             |
|confirm-domain    | Confirm user wants a rest.     | You are looking for a restaurant is that right?                                                                                           |
|impl-conf         | Implicit slot confirmation***  | There are  restaurants in the expensive price range and the south of town . What type of food would you like?                             |
|repeat            | Ask user to repeat query       | Sorry I am a bit confused ; please tell me again what you are looking for .                                                               |

*when user has to pick from amongst n options to fill a slot, bot
utters one select da for each of the n possible values

**canthelp.exception: after user rejects all n options offered, bot
replies with a canthelp da plus one canthelp.exception for each of the n
rejected options. canthelp.exception => canthelp

***When asking the user to provide another slot, bot utters a request da
plus one impl-conf da for each slot already provided. Thus,
impl-conf => request

### bot DA statistics
|  Act             | Trn | Dev | Total |
|------------------|-----|-----|-------|
| inform           |7936 |2448 | 10384 |
| offer            |6077 |1997 | 8074  |
|request           |1910 |631  | 2541  |
|welcomemsg        |1612 |506  | 2118  |
|canthelp          |1286 |478  | 1764  |
|expl-conf         |505  |200  | 705   |
|select            |240  |106  | 346   |
|reqmore           |79   |40   | 119   |
|canthelp.exception|79   |35   | 114   |
|confirm-domain    |78   |21   | 99    |
|impl-conf         |12   |8    | 20    |
|repeat            |10   |8    | 18    |

### bot multi-intents:

### all observed bot act combinations
|  Act Combination             | trn |dev |  Special handling                                                                                                   |
|------------------------------|-----|----|---------------------------------------------------------------------------------------------------------------------|
|welcomemsg                    | 1504|457 | useless, should be deleted from stories                                                                             |
|canthelp                      | 935 |284 | say can't help, listing all the slots provided so far. Map to canthelp                                              |
|offer,inform x2               | 1669|476 | offer option (always by name) and mention every filter used. Map to offer_detailed                                  |
|reqmore                       | 44  |19  | Map to reqmore                                                                                                      |
|offer,inform                  | 3154|1013| same as offer,inform x2                                                                                             |
|request                       | 1494|460 | request value for slot (only 1 slot). One da per informable slot except name(i.e. 3)                                |
|expl-conf                     | 358 |136 | confirm informable slot. Keep latest filled slot as tracker topic. Map to expl-conf                                 |
|select,select                 | 90  |25  | offer user several values to pick for slot. Slot and values random. Map to select                                   |
|confirm-domain                | 60  |16  | ask if user wants a restaurant. Useless but tested in bAbI. Map to confirm-domain                                   |
|offer,inform x3               | 208 |59  | same as offer,inform x2                                                                                             |
|offer                         | 356 |120 | offer restaurant by name. Map to offer                                                                              |
|canthelp,canthelp.exception x2| 9   |3   | same as canthelp (the exceptions have no effect on the output)                                                      |
|repeat                        | 6   |8   | ask user to repeat. Useless, should be deleted. NLU can send repeat signal if needed                                |
|canthelp,canthelp.exception   | 15  |5   | same as canthelp                                                                                                    |
|request,impl-conf x2          | 4   |2   | affirm options available with given slots, request new slot. Map to a request_detailed da per informable except name|
|request,impl-conf             | 3   |0   | same as request,impl-conf x2                                                                                        |
|canthelp,canthelp.exception x3| 1   |0   | same as canthelp                                                                                                    |

## user acts
| Act              | Definition                     | Example                                                                                                                                   |
|------------------|:------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------|

### user DA statistics
|  Act             | Trn | Dev | Total |
|------------------|-----|-----|-------|
| thankyou\|bye    |     |     | 2022  |


### user multi-intents:
thankyou()|bye() => bye()
affirm()|inform(...): affirm_inform. You can't infer the other by
preserving only one. User could cancel query and start a new one,
so the affirm must be preserved to differentiate from reject|inform.
But sometimes the affirm is just pointless, such as in
data/trndev/dstc2/data/Mar13_S0A0/voip-e8997b10da-20130327_193112/label.json
there, the user randomly starts the conversation with a 'yes', which
doesn't correspond to the pragmatic role of affirm. You can infer this
from the slots associated to that act: empty, so the yes is pointless
(only because the other act is inform. In affirm()|request(...) the
affirm slots are also empty but it corresponds indeed with an affirmation
affirm()|request(...) => request(...)

thankyou()|X => X

deny()|reqalts(...) => reqalts(...). deny is always redundant. User
only requests alternatives when disliking the bot suggestion.

request(phone,type=restaurant) => request(phone). The type=restaurant is
completely meaningless, it was added just with the exchange:
bot: prezzo is a nice place in the west of town and the prices are moderate
human: ok how about a restaurant and phone number

request(phone, name=...) => request(phone). The other parameters are
totally redundant. Example:
bot: bloomsbury restaurant is a great restaurant
human: the phone number for bloomsbury

ack()|request(...) => request(). The ack() is void. Example:
bot: The phone number of golden house is ..:
human: okay and what about the address

inform(=dontcare)|X => X. The inform(=dontcare) is basically meaningless
in all examples

request(... <noninformableslot>=value ...) => request(...)
e.g. request(phone, type=restaurant). There's no 'type' informable slot
in DSTC2. In fact, the user input that produced that act is
"ok how about a restaurant and phone number". So the type can be removed

request(requestables*,informables*) => request(requestables*)_inform(informables*)
e.g. request(addr, pricerange=moderate, type=restaurant, area=south).
Actual user utterance:
"whats the address for moderately priced restaurants in the south part of town"
First, by the previous rule, the type=restaurant is garbage on goes away.
Then, this is not equivalent to inform(pricerange=moderate, area=south)
as that ignores the fact that the user wants the address. It is also not
equivalent to request(address) as that ignores the filters. So you need
a special action to handle this double intent, something like
request(requestables*)_inform(informables*). How you handle this greatly
depends on the task: for bAbI t6, you can totally ignore the request part
as the ground truth bot does:
human: whats the address for moderately priced restaurants in the south part of town
bot: There are restaurants in the moderate price range and the south of town . What type of food would you like?
But for DSTC2, your gold truth is how well you keep the internal state,
which means predicting the method and the requested slots: you need a
deterministic way to convert rasa actions to these two things, and that
can only be possible if you have a request_inform user intent that
triggers that bot action
Do note: you can easily get all those intents from label\[turn\]\[semantics\]\[json\]
which is a list with all the acts and their slots

ack()|X => X. ack() is 100% redundant

thankyou()|bye() => bye()

json = \[... {slots:\[\["this", "dontcare\]\], act:inform} ... {slots:informables*, act:inform} ...\]
=> \[... {slots:informables*, act:inform} ...\]
'this' = dontcare means "don't apply filter to the 'this' slot", where 'this'
is to be inferred by context. In this case, it is sufficient to use the other inform act

json = \[{'slots': \[\['this', 'dontcare'\]\], 'act': 'inform'}, {'slots': *requestables, 'act': 'request'}\]
=> request(*requestables)

json = \[{'slots': \[\['this', 'dontcare']], 'act': 'inform'}, {'slots': *informables, 'act': 'inform'}\]
=> inform(informables*, this=dontcare)
The action must solve the this using context. If it can't, the user must've said
'i don't care' totally out of place and should be ignored

### all user acts observed act combinations
|  Act Combination             | trn |dev |  Special handling                                                                                                        |
|------------------------------|-----|----|--------------------------------------------------------------------------------------------------------------------------|
|*hello                         | 12  | 7  | pointless. This act should be deleted as well as the next bot reply                                                      |
|*reqalts,inform                | 417 |129 | disregard reqalts, keep inform only. Reqalts always empty here. Map to inform da                                         |
|*reqalts                       | 274 | 87 | no slots to keep, map to reqalts action                                                                                  |
|*request x2                    | 294 | 91 | keep only one request with all the requestable slots. Map to request da                                                  |
|*request                       |2588 |787 | keep slots, map to request da                                                                                            |
|*thankyou,bye                  |1406 | 0  | keep no slots, map to bye da                                                                                             |
|*inform                        |2886 |869 |'this'=last dealt slot (always = 'dontcare'), if present map to inform_dontcare da, else to inform. Keep all slots anyway |
|                              | 495 |197 | nothing said, should be deleted from dialogue as well as next bot reply                                                  |
|*request x3                    | 55  | 9  | accumulate all slots in single request. Map to request da                                                                |
|*inform x3                     | 741 | 1  | accumulate all slots in single inform. Map to inform da                                                                  |
|*thankyou                      | 60  | 17 | no slots to keep, map to thankyou da                                                                                     |
|*negate                        | 51  | 20 | no slots to keep, map to negate da                                                                                       |
|*affirm                        | 281 | 99 | no slots to keep, map to affirm da                                                                                       |
|*bye                           | 109 | 31 | no slots to keep, map to bye da                                                                                          |
|*negate,inform                 | 22  | 17 | clear all slots thus far collected. Keep inform slots, map to new correct da                                             |
|*confirm                       | 77  | 27 | keep slots, map to confirm action (see 'dataset limitations', on bot design docs)                                        |
|*request,inform                | 6   | 7  | keep requestables, and informables (except 'this') separately. Map to new act 'query'                                    |
|*inform,request x2             | 1   | 1  | like request,inform                                                                                                      |
|*ack,reqalts                   | 1   | 0  | disregard ack, no slots to keep, map to reqalts da                                                                       |
|*affirm,inform                 | 40  | 7  | keep the inform slots, map to new act 'include_filter'                                                                   |
|*hello,inform                  | 8   | 5  | disregard hello, keep inform slots, map to inform da                                                                     |
|*hello,inform x2               | 10  | 3  | like hello,inform                                                                                                        |
|*deny                          | 2   | 0  | disregard slots, map to deny da                                                                                          |
|*negate,reqalts                | 1   | 0  | disregard negate, keep no slots, map to reqalts da                                                                       |
|*affirm, request               | 2   | 1  | disregard affirm, keep request slots, map to request da                                                                  |
|*negate,bye                    | 1   | 1  | keep no slots, map to bye da                                                                                             |
|*reqalts,inform x2             | 12  | 4  | like reqalts,inform                                                                                                      |
|repeat                        | 10  | 6  | useless, should be deleted as well as the bot utterance that triggered                                                   |
|*reqalts,deny                  | 2   | 0  | disregard deny, keep no slots, map to reqalts da                                                                         |
|*ack                           | 13  | 0  | no slots to keep, map to ack da                                                                                          |
|*reqmore                       | 1   | 0  | no slots to keep, map to reqalts da                                                                                      |
|*inform,bye                    | 1   | 0  | equals bye                                                                                                               |
|*confirm x2                    | 3   | 2  | accumulate slots, keep them, map to inform da                                                                            |
|restart                       | 1   | 1  | ask bot to start over, no slots. Delete entire conversation so far to start from next turn                               |
|*request,inform x2             | 2   | 0  | same as inform,request                                                                                                   |
|*affirm,thankyou,bye           | 1   | 0  | equals bye                                                                                                               |
|*negate,reqalts,inform         | 1   | 2  | 'no, what about <x> food?'. Equals inform, keep its slots                                                                |
|*ack,request                   | 2   | 0  | disregard ack, keep request                                                                                              |
|*affirm, inform x2             | 16  | 5  | same as affirm,inform                                                                                                    |
|*inform,ack                    | 1   | 0  | ack is void of sense. Keep inform                                                                                        |
|*bye,thankyou                  | 2   |426 | just bye                                                                                                                 |
|*inform x2                     | 0   |220 | like inform x3                                                                                                           |
|*hello,inform x2               | 0   | 3  | like hello,inform                                                                                                        |
|*deny,inform                   | 0   | 3  | disregard deny,keep inform slots, map to inform da                                                                       |
|*thankyou,request              | 0   | 1  | disregard thankyou, keep request slots, map to request da                                                                |


### getting the 'this' context
dontcare is a valid value for any informable slot, meaning that shouldn't be a filter in the query
when the bot requests a slot value, you populate some 'context' field. The value
of 'this' will be retrieved from there, and when having the 'dontcare' value,
a mask is applied to the valid actions so as not to request that one


{'inform': 7807, 'request': 4809, 'bye': 2198, 'thankyou': 2139, 'reqalts': 1105, 'affirm': 555, 'negate': 193, 'confirm': 128, 'hello': 54, 'repeat': 25, 'ack': 20, 'deny': 12, 'restart': 7, 'reqmore': 4}


# Conversion to Rasa
## intent mapping

|Rasa        | DSTC2       | Rasa NLU      |
|------------|-------------|---------------|
|request_info|request      | yes           |
|thankyou    |thankyou     | yes           |
|deny        |reqalts      | replace intent|
|deny        |negate       | replace intent|
|deny        |deny         | replace intent|
|reqalts     |reqmore      | no            |
|reqalts     |reqalts      | no            |
|confirm     |confirm      | no            |
|correct     |negate/inform| no            |


## entity mapping
### common entities
|Rasa        | DSTC2     |
|------------|-----------|
|cuisine     |food       |

### rasa only

### DSTC2 only