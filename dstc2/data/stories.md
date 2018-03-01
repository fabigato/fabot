## Mar13_S0A1/voip-f246dfe0f2-20130328_161556
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_food_detailed
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5694f464-20130328_125233
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5694f464-20130328_125916
* include_filter{"area": "north"}
 - request_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8efef4eae9-20130325_233404
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8efef4eae9-20130325_230851
* inform{"food": "halal", "pricerange": "moderate"}
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - request_food
* inform{"food": "halal"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S0A0/voip-8efef4eae9-20130325_234241
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-db80a9e6df-20130328_230519
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-db80a9e6df-20130328_232414
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-db80a9e6df-20130328_233633
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* query{"name": "the missing sock", "requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-db80a9e6df-20130328_230354
* inform{"food": "gastropub", "area": "north"}
 - canthelp
* inform{"food": "chinese", "area": "north"}
 - offer_detailed
* confirm{"food": "chinese"}
 - request_pricerange
* inform{"food": "chinese", "area": "north"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-db80a9e6df-20130328_230211
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-db80a9e6df-20130328_231959
* inform{"area": "north"}
 - request_food
* inform{"pricerange": "moderate"}
 - request_food
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-db80a9e6df-20130328_230014
* inform_dontcare
 - offer_detailed
* confirm{"food": "unusual"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-db80a9e6df-20130328_230811
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* query{"name": "la margherita", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-db80a9e6df-20130328_231545
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* inform{"name": "rice house"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-db80a9e6df-20130328_234234
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-db80a9e6df-20130328_231320
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-597cfafdee-20130402_005639
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-597cfafdee-20130328_230830
* inform{"pricerange": "moderate", "area": "west"}
 - expl-conf
* affirm
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-597cfafdee-20130402_005048
* inform{"food": "korean", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-597cfafdee-20130402_011624
* inform{"food": "venetian"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-597cfafdee-20130402_011135
* inform{"food": "modern european", "pricerange": "cheap"}
 - offer_detailed
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-597cfafdee-20130328_232032
* inform{"food": "african", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-597cfafdee-20130328_233209
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S0A1/voip-597cfafdee-20130328_232942
* inform{"area": "dontcare"}
 - offer_detailed
* inform{"food": "catalan"}
 - canthelp
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-597cfafdee-20130402_011915
* inform{"food": "international"}
 - request_area
* inform{"area": "dontcare"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-597cfafdee-20130328_234346
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "international"}
 - canthelp
* inform{"area": "centre"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-597cfafdee-20130402_011800
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-597cfafdee-20130328_231821
* inform{"food": "french", "pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-597cfafdee-20130402_005342
* inform{"food": "romanian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - select
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-597cfafdee-20130328_231921
* inform{"food": "vegetarian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-597cfafdee-20130328_231005
* negate
 - request_area
* inform{"area": "north"}
 - request_food
* inform{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-597cfafdee-20130402_010910
* inform{"area": "north"}
 - request_food
* inform{"food": "moroccan"}
 - request_food
* inform{"food": "moroccan"}
 - request_food
* inform{"food": "moroccan"}
 - request_food
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-597cfafdee-20130328_233056
* inform_dontcare
 - offer_detailed
* inform{"food": "french"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-597cfafdee-20130402_005918
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-597cfafdee-20130328_231524
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-597cfafdee-20130402_005206
* inform{"food": "austrian", "pricerange": "moderate"}
 - offer_detailed
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-597cfafdee-20130328_234727
* inform{"area": "centre"}
 - request_food
* inform{"food": "eritrean"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7853a398f-20130402_153810
* inform{"food": "world", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - select
* inform_dontcare
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A1/voip-d7853a398f-20130401_154937
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7853a398f-20130401_160153
* inform{"area": "east"}
 - request_food
* inform{"food": "indonesian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7853a398f-20130402_161902
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d7853a398f-20130401_161556
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7853a398f-20130401_152001
* inform{"food": "international", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d7853a398f-20130402_153648
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7853a398f-20130401_152711
* inform{"food": "afghan", "pricerange": "expensive"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d7853a398f-20130401_155154
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7853a398f-20130402_154628
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d7853a398f-20130401_150837
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7853a398f-20130401_152229
* inform{"food": "spanish", "area": "east"}
 - offer_detailed
* confirm{"food": "spanish"}
 - offer_detailed
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7853a398f-20130402_161739
* inform{"food": "creative", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d7853a398f-20130401_153102
* inform{"food": "caribbean", "pricerange": "moderate"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7853a398f-20130402_144000
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7853a398f-20130402_143701
* inform{"food": "spanish", "area": "centre"}
 - expl-conf
* correct{"food": "spanish"}
 - request_area
* inform{"area": "centre"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_area": "True"}
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7853a398f-20130402_153534
* inform{"food": "international", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7853a398f-20130402_162826
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-59bc8a2167-20130325_141534
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - expl-conf
* correct{"area": "north"}
 - request_food
* reqalts
 - request_pricerange
* inform{"pricerange": "cheap"}
 - expl-conf
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - select
* inform{"pricerange": "cheap", "area": "north"}
 - expl-conf
* negate
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-59bc8a2167-20130328_132058
* inform{"food": "japanese"}
 - offer_detailed
* inform{"area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-59bc8a2167-20130328_130310
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"area": "centre"}
 - confirm-domain
* inform{"area": "centre"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-59bc8a2167-20130328_132516
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "german"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-59bc8a2167-20130325_135337
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-59bc8a2167-20130328_132242
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-59bc8a2167-20130328_131211
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "indian"}
 - expl-conf
* negate
 - request_pricerange
* inform{"food": "indian"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"food": "indian"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-59bc8a2167-20130325_143706
* inform{"area": "north"}
 - request_food
* inform{"food": "christmas"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-59bc8a2167-20130325_142656
* inform{"food": "german"}
 - request_area
* inform{"area": "east"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-59bc8a2167-20130325_133605
* inform{"area": "east"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"food": "chinese"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-59bc8a2167-20130328_133527
* inform{"food": "swiss"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-59bc8a2167-20130328_131004
* inform{"food": "irish"}
 - canthelp
* inform{"food": "european"}
 - request_pricerange
* inform_dontcare
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-59bc8a2167-20130328_132714
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-59bc8a2167-20130328_130054
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-59bc8a2167-20130328_130810
* inform{"food": "thai"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "british"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-13ff413553-20130328_175102
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-13ff413553-20130328_172007
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-13ff413553-20130328_180611
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-13ff413553-20130328_173028
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-13ff413553-20130328_174306
* inform{"area": "south"}
 - request_food
* inform{"food": "danish"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-13ff413553-20130328_174952
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-13ff413553-20130328_175302
* inform{"area": "north"}
 - request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"area": "north"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-13ff413553-20130328_172810
* inform{"food": "japanese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - bye

## Mar13_S0A0/voip-13ff413553-20130328_171651
* inform{"food": "bistro"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-13ff413553-20130328_180202
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-13ff413553-20130328_174036
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-13ff413553-20130328_174156
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-13ff413553-20130328_172109
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - expl-conf
* correct{"area": "north"}
 - request_food
* inform_dontcare
 - request_food
* inform{"food": "north american"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - bye

## Mar13_S0A1/voip-d66e12b45c-20130327_172835
* inform{"area": "east"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - reqmore
* request{"requested_phone": "True"}
 - reqmore
* request{"requested_phone": "True"}
 - reqmore
* request{"requested_phone": "True"}
 - reqmore
* inform{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d66e12b45c-20130327_172709
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "british"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d66e12b45c-20130327_173123
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ec3c3aaf98-20130323_141647
* inform{"food": "english", "pricerange": "expensive"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ec3c3aaf98-20130323_142504
* inform{"food": "australasian", "pricerange": "moderate"}
 - confirm-domain
* affirm
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ec3c3aaf98-20130323_141803
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ec3c3aaf98-20130323_141045
* inform{"food": "singaporean", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ec3c3aaf98-20130323_142633
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dd9f7810fd-20130322_222124
* inform{"food": "world", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dd9f7810fd-20130322_225458
* inform{"food": "canapes", "pricerange": "moderate"}
 - offer_detailed
* confirm{"food": "canapes"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dd9f7810fd-20130322_224356
* inform{"food": "eritrean", "area": "centre"}
 - request_pricerange
* inform{"food": "eritrean"}
 - request_food
* inform{"food": "eritrean"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dd9f7810fd-20130322_222331
* inform{"food": "welsh", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dd9f7810fd-20130322_232304
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dd9f7810fd-20130322_223946
* inform{"food": "english"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dd9f7810fd-20130322_225618
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dd9f7810fd-20130322_224705
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dd9f7810fd-20130322_232152
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dd9f7810fd-20130322_231612
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dd9f7810fd-20130322_224223
* inform{"food": "seafood"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "seafood"}
 - offer
* confirm{"food": "seafood"}
 - offer
* inform{"food": "seafood"}
 - offer
* bye
 - bye

## Mar13_S1A1/voip-7fdb5b39e7-20130328_222225
* inform{"food": "spanish"}
 - expl-conf
* correct{"food": "spanish"}
 - request_area
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7fdb5b39e7-20130328_222519
* inform{"pricerange": "moderate", "area": "south"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* query{"name": "pizza hut city centre", "requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7fdb5b39e7-20130328_222006
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* confirm{"food": "mexican"}
 - offer_detailed
* confirm{"area": "centre"}
 - offer_detailed
* inform{"food": "mexican", "area": "centre"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"area": "centre"}
 - offer_detailed
* inform{"food": "asian oriental", "area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-561b472540-20130328_123800
* inform{"food": "greek"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "greek"}
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"area": "north"}
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french", "area": "north"}
 - canthelp
* inform{"area": "north"}
 - canthelp
* request{"requested_area": "True"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* inform{"food": "french", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S1A0/voip-561b472540-20130328_123452
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-561b472540-20130328_123209
* include_filter{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-561b472540-20130328_122315
* inform{"food": "turkish", "area": "dontcare"}
 - offer_detailed
* affirm
 - offer_detailed
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-561b472540-20130328_122903
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-561b472540-20130328_124901
* include_filter{"food": "african", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4660dd9eab-20130329_085548
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4660dd9eab-20130329_080725
* inform{"food": "kosher", "area": "north"}
 - offer_detailed
* confirm{"food": "kosher"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4660dd9eab-20130329_075545
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4660dd9eab-20130329_085136
* inform{"area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "catalan"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4660dd9eab-20130329_085648
* inform{"area": "west"}
 - request_food
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4660dd9eab-20130329_090121
* inform{"food": "french", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - confirm-domain
* affirm
 - offer_detailed
* confirm{"area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4660dd9eab-20130329_085007
* inform{"food": "malaysian", "area": "dontcare"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - canthelp
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4660dd9eab-20130329_080055
* inform_dontcare
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4660dd9eab-20130329_075244
* inform{"food": "australian", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4660dd9eab-20130329_085824
* inform{"pricerange": "expensive", "area": "east"}
 - select
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4660dd9eab-20130329_085958
* inform{"food": "korean"}
 - select
* inform{"food": "korean"}
 - offer_detailed
* confirm{"area": "centre"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4660dd9eab-20130328_202554
* inform{"food": "international"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130402_202812
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130401_152843
* inform{"food": "turkish", "area": "centre"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130402_201920
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130401_153435
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130401_150230
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130402_080342
* inform{"food": "german", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - select
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5b7bf9d9-20130401_155148
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-be5b7bf9d9-20130401_154835
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130402_201818
* inform{"food": "vietnamese", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-be5b7bf9d9-20130401_152612
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5b7bf9d9-20130402_202555
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5b7bf9d9-20130402_203757
* inform{"area": "east"}
 - request_food
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-be5b7bf9d9-20130402_202421
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-be5b7bf9d9-20130401_155038
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5b7bf9d9-20130401_151225
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5b7bf9d9-20130401_152435
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5b7bf9d9-20130402_201144
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "asian oriental"}
 - select
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer
* confirm{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-be5b7bf9d9-20130402_200701
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-be5b7bf9d9-20130402_201007
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-be5b7bf9d9-20130401_155552
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-be5b7bf9d9-20130401_155804
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-29c52c01b6-20130327_180554
* inform{"food": "european", "pricerange": "cheap"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7aef99178-20130328_184019
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7aef99178-20130328_184824
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7aef99178-20130328_184726
* inform{"food": "japanese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d7aef99178-20130328_184628
* inform{"food": "portuguese", "pricerange": "cheap"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d7aef99178-20130328_184453
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-73ce546185-20130324_022749
* inform{"food": "korean", "pricerange": "dontcare"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-73ce546185-20130324_022621
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* affirm
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-73ce546185-20130324_021914
* inform{"food": "austrian", "area": "dontcare"}
 - request_food
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-da10d74c3e-20130326_001406
* inform{"area": "west"}
 - request_food
* inform{"food": "dontcare", "pricerange": "cheap"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-da10d74c3e-20130328_140824
* inform{"food": "traditional", "area": "south"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "italian", "area": "south"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-da10d74c3e-20130328_142725
* inform{"area": "south"}
 - request_food
* inform{"food": "austrian"}
 - request_food
* inform{"food": "austrian"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian", "area": "south"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-da10d74c3e-20130328_142921
* inform{"pricerange": "moderate", "area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da10d74c3e-20130328_153416
* inform{"pricerange": "expensive", "area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "expensive", "area": "east"}
 - offer_detailed
* inform{"pricerange": "expensive", "area": "east"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da10d74c3e-20130325_232243
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da10d74c3e-20130326_002440
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-da10d74c3e-20130328_142413
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da10d74c3e-20130328_141927
* inform{"area": "south"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-da10d74c3e-20130328_152819
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da10d74c3e-20130326_000047
* inform{"area": "east"}
 - request_food
* inform{"food": "indian", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S0A0/voip-da10d74c3e-20130326_002258
* inform{"food": "mexican", "pricerange": "cheap"}
 - offer_detailed
* confirm{"pricerange": "cheap"}
 - offer_detailed
* inform{"food": "vietnamese", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - reqmore
* bye
 - reqmore
* bye
 - bye

## Mar13_S0A0/voip-da10d74c3e-20130328_141826
* inform{"pricerange": "cheap", "area": "west"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-da10d74c3e-20130326_000532
* inform{"pricerange": "expensive", "area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-da10d74c3e-20130328_152552
* inform{"food": "african"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da10d74c3e-20130328_144144
* inform{"food": "lebanese", "area": "centre"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - request_food
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-da10d74c3e-20130328_141500
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "british", "pricerange": "moderate"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da10d74c3e-20130328_141404
* include_filter{"pricerange": "cheap", "area": "south"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-da10d74c3e-20130325_232050
* inform{"food": "moroccan", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S0A0/voip-96f43326a4-20130323_073950
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-96f43326a4-20130323_070356
* inform{"area": "centre"}
 - request_area
* inform{"area": "centre"}
 - offer
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* confirm{"area": "centre"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-96f43326a4-20130323_070939
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* inform{"food": "canapes"}
 - offer_detailed
* confirm{"food": "canapes"}
 - offer_detailed
* inform{"food": "canapes", "pricerange": "cheap"}
 - expl-conf
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "canapes"}
 - expl-conf
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "portuguese", "pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-96f43326a4-20130323_073316
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-96f43326a4-20130323_072452
* inform{"food": "mediterranean"}
 - offer_detailed
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-96f43326a4-20130324_101258
* inform{"area": "dontcare"}
 - expl-conf
* negate
 - expl-conf
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "international"}
 - expl-conf
* inform_dontcare
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-96f43326a4-20130323_071326
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - expl-conf
* correct{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-96f43326a4-20130323_074111
* negate
 - expl-conf
* negate
 - expl-conf
* inform{"food": "polynesian"}
 - select
* inform{"pricerange": "dontcare"}
 - offer_detailed
* confirm{"food": "polynesian"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-96f43326a4-20130323_071538
* inform{"food": "french", "area": "north"}
 - confirm-domain
* affirm
 - request_food
* inform{"food": "french"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130328_172142
* inform{"area": "south"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_food_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130402_200348
* inform{"pricerange": "cheap"}
 - request_food
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130402_200522
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-935947e17b-20130402_202130
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-935947e17b-20130328_152337
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* thankyou
 - bye

## Mar13_S1A1/voip-935947e17b-20130402_194703
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "english", "pricerange": "moderate"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130328_163714
* inform{"food": "european"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130328_153738
* inform{"area": "centre"}
 - request_food
* inform{"food": "spanish"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130402_195840
* inform{"area": "west"}
 - request_food
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130328_153237
* inform{"food": "chinese"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* confirm{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* thankyou
 - reqmore
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130402_195651
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130402_201638
* inform{"area": "south"}
 - request_pricerange
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-935947e17b-20130402_201340
* inform{"food": "persian"}
 - expl-conf
* affirm
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"food": "asian oriental"}
 - request_area
* request{"requested_area": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A0/voip-935947e17b-20130402_200817
* inform{"area": "south"}
 - request_food
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-935947e17b-20130402_202004
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - request_food
* query{"area": "south", "requested_food": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130402_195455
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "german"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* reqalts
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-935947e17b-20130328_164611
* inform{"area": "east"}
 - offer_detailed
* inform{"food": "chinese", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-935947e17b-20130328_163520
* inform{"food": "international"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130402_195123
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "international"}
 - offer_detailed
* inform{"area": "west"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "romanian"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* query{"area": "west", "requested_food": "True"}
 - canthelp
* request{"requested_food": "True"}
 - offer_detailed
* query{"area": "west", "requested_food": "True"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* deny{"food": "romanian"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* reqalts
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-935947e17b-20130328_164334
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130401_162601
* inform{"food": "turkish", "area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130328_130428
* inform{"food": "greek"}
 - offer
* inform{"food": "greek", "area": "north"}
 - offer_detailed
* inform{"food": "greek"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-10beae627f-20130401_163221
* inform{"area": "north"}
 - request_food
* inform{"food": "scandinavian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "scandinavian"}
 - offer_detailed
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-10beae627f-20130328_171027
* inform{"food": "corsica", "area": "centre"}
 - canthelp
* inform{"food": "north american"}
 - confirm-domain
* inform{"food": "north american"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-10beae627f-20130401_164239
* inform{"pricerange": "expensive", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130401_165213
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-10beae627f-20130328_165757
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-10beae627f-20130401_164954
* inform{"food": "gastropub"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "gastropub"}
 - expl-conf
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-10beae627f-20130401_163410
* inform{"area": "north"}
 - request_food
* inform{"food": "catalan"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-10beae627f-20130328_165245
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130329_154245
* inform{"area": "north"}
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130401_163556
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-10beae627f-20130328_171149
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-10beae627f-20130329_155112
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130328_170907
* inform{"food": "seafood", "pricerange": "cheap"}
 - request_food
* inform{"food": "seafood"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-10beae627f-20130401_162723
* inform{"food": "asian oriental", "pricerange": "moderate"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "british"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* confirm{"food": "persian"}
 - canthelp
* inform{"food": "persian"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - expl-conf
* inform{"food": "british"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-10beae627f-20130328_171313
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-10beae627f-20130329_154519
* inform{"food": "greek"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - request_area
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130328_165908
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "fusion"}
 - offer_detailed
* inform{"food": "fusion"}
 - offer_detailed
* negate
 - reqmore
* inform{"area": "west"}
 - offer_detailed
* inform{"food": "fusion"}
 - offer_detailed
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-10beae627f-20130329_154826
* inform{"area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2e134ee190-20130401_225214
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2e134ee190-20130401_230615
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2e134ee190-20130401_230728
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dcaeb62b29-20130327_084207
* inform{"food": "barbeque", "area": "west"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dcaeb62b29-20130327_082012
* inform{"food": "spanish"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dcaeb62b29-20130327_081209
* inform{"area": "south"}
 - request_food
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* inform{"food": "portuguese"}
 - expl-conf
* inform{"food": "portuguese"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dcaeb62b29-20130327_081541
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dcaeb62b29-20130327_083709
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dcaeb62b29-20130327_082220
* inform{"food": "scandinavian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dcaeb62b29-20130326_041709
* inform_dontcare
 - request_food
* inform{"food": "belgian"}
 - request_food
* inform{"food": "belgian"}
 - request_food
* inform{"food": "belgian"}
 - expl-conf
* correct{"food": "belgian"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - reqmore
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dcaeb62b29-20130326_043007
* affirm
 - request_food
* inform{"food": "singaporean"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - expl-conf
* negate
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - canthelp
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dcaeb62b29-20130327_082853
* inform{"food": "basque", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* query{"name": "curry prince", "requested_addr": "True"}
 - offer
* query{"name": "curry prince", "requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* inform{"food": "indian", "area": "east"}
 - select
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dcaeb62b29-20130327_082120
* inform{"area": "south"}
 - request_food
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dcaeb62b29-20130326_033832
* inform{"pricerange": "expensive", "area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dcaeb62b29-20130326_034447
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dcaeb62b29-20130326_042721
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dcaeb62b29-20130327_082345
* inform{"area": "west"}
 - offer
* inform{"food": "barbeque", "area": "west"}
 - offer_detailed
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dcaeb62b29-20130326_035616
* inform{"pricerange": "moderate"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer
* inform{"food": "cuban"}
 - offer
* inform{"food": "cuban"}
 - offer
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-dcaeb62b29-20130327_083948
* inform{"food": "moroccan", "area": "west"}
 - request_food
* inform{"food": "moroccan"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "moroccan"}
 - offer_detailed
* inform{"food": "moroccan"}
 - offer_detailed
* inform{"food": "moroccan"}
 - offer_detailed
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dcaeb62b29-20130327_084757
* inform{"pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"pricerange": "cheap"}
 - canthelp
* affirm
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* affirm
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"pricerange": "cheap"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-dcaeb62b29-20130327_083422
* inform{"pricerange": "moderate", "area": "west"}
 - request_area
* inform{"area": "west"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dcaeb62b29-20130326_033336
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ddcaad92a1-20130326_012016
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ddcaad92a1-20130325_234956
* inform{"food": "scandinavian"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "scandinavian"}
 - request_pricerange
* inform_dontcare
 - reqmore
* inform{"food": "scandinavian"}
 - reqmore
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - select
* inform{"food": "thai"}
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ddcaad92a1-20130325_234752
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ddcaad92a1-20130325_222532
* inform{"area": "north"}
 - request_food
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* reqalts
 - offer
* inform{"area": "north"}
 - select
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ddcaad92a1-20130326_010701
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_food
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ddcaad92a1-20130325_222005
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ddcaad92a1-20130325_222137
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ddcaad92a1-20130326_002225
* inform{"area": "west"}
 - request_pricerange
* inform{"food": "international"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ddcaad92a1-20130326_012409
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d76851034e-20130326_222422
* include_filter{"food": "british", "pricerange": "moderate"}
 - request_food
* inform{"food": "british"}
 - request_area
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d76851034e-20130326_221320
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-187c1708f2-20130325_134301
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-187c1708f2-20130325_135219
* inform{"food": "portuguese"}
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-187c1708f2-20130325_134444
* inform{"food": "scottish", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british", "pricerange": "expensive"}
 - expl-conf
* affirm
 - request_area
* inform_dontcare
 - expl-conf
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-187c1708f2-20130325_133552
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-187c1708f2-20130327_130329
* inform{"food": "korean", "pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean", "pricerange": "expensive"}
 - select
* inform{"pricerange": "expensive"}
 - expl-conf
* inform_dontcare
 - select
* inform{"pricerange": "expensive"}
 - select
* inform{"food": "korean", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-187c1708f2-20130327_132135
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-187c1708f2-20130325_133750
* inform{"food": "european"}
 - request_area
* inform{"area": "dontcare"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-187c1708f2-20130325_134104
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-187c1708f2-20130325_131829
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-187c1708f2-20130327_130928
* inform{"food": "irish"}
 - canthelp
* inform{"food": "irish"}
 - canthelp
* inform{"food": "irish"}
 - canthelp
* inform{"food": "irish"}
 - canthelp
* inform{"food": "irish"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-187c1708f2-20130327_130141
* inform{"pricerange": "moderate", "area": "west"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-187c1708f2-20130326_114238
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-187c1708f2-20130327_132257
* inform{"food": "barbeque", "area": "west"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-187c1708f2-20130325_131253
* inform{"food": "catalan", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-187c1708f2-20130327_132654
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer
* inform{"pricerange": "expensive", "area": "east"}
 - select
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-187c1708f2-20130327_131445
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer
* query{"name": "nandos", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-72e50baa85-20130326_051956
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-72e50baa85-20130326_053934
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-72e50baa85-20130326_045411
* inform{"food": "cuban"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "cuban", "pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "cuban"}
 - offer_detailed
* inform{"food": "cuban"}
 - offer_detailed
* inform{"food": "cuban"}
 - offer_detailed
* confirm{"food": "cuban"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "modern european"}
 - select
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - expl-conf
* bye
 - bye

## Mar13_S0A1/voip-72e50baa85-20130327_061724
* inform{"food": "modern european"}
 - request_pricerange
* inform_dontcare
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-72e50baa85-20130326_045105
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-72e50baa85-20130327_061918
* inform{"food": "gastropub"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "gastropub"}
 - expl-conf
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-72e50baa85-20130327_062822
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-72e50baa85-20130327_061457
* inform{"food": "indian", "pricerange": "moderate"}
 - confirm-domain
* inform{"food": "indian", "pricerange": "moderate"}
 - offer
* reqalts
 - offer
* reqalts
 - offer
* inform{"food": "indian", "pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"food": "indian", "pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-72e50baa85-20130327_060348
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-72e50baa85-20130327_060626
* inform{"area": "centre"}
 - request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "asian oriental"}
 - request_area
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-72e50baa85-20130327_062939
* inform{"pricerange": "cheap"}
 - request_area
* request{"requested_area": "True"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-72e50baa85-20130326_052829
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "russian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-72e50baa85-20130326_052642
* inform{"food": "chinese"}
 - expl-conf
* include_filter{"area": "south"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-72e50baa85-20130326_053156
* inform{"area": "centre"}
 - request_area
* inform{"area": "centre"}
 - request_area
* inform{"area": "centre"}
 - request_area
* inform{"area": "centre"}
 - request_food
* inform{"area": "centre"}
 - select
* inform{"area": "centre"}
 - request_food
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-72e50baa85-20130327_063159
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-72e50baa85-20130327_060812
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-72e50baa85-20130326_051315
* inform{"food": "australian"}
 - canthelp
* inform{"food": "italian"}
 - request_area
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A0/voip-72e50baa85-20130326_044704
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform{"food": "chinese"}
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fbd422ad18-20130328_182406
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fbd422ad18-20130328_182833
* inform{"food": "turkish", "area": "centre"}
 - offer_detailed
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fbd422ad18-20130328_182117
* inform{"food": "creative", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fbd422ad18-20130328_185220
* inform{"area": "centre"}
 - request_food
* inform{"food": "mediterranean"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* inform{"area": "dontcare"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fbd422ad18-20130328_181401
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fbd422ad18-20130328_184129
* inform{"area": "east"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fbd422ad18-20130328_181748
* inform{"pricerange": "expensive"}
 - expl-conf
* inform{"pricerange": "expensive"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fbd422ad18-20130328_185340
* inform{"area": "west"}
 - request_food
* inform{"food": "european"}
 - offer_detailed
* inform{"food": "european"}
 - reqmore
* inform{"area": "west"}
 - offer_detailed
* inform{"food": "european"}
 - reqmore
* inform{"food": "european"}
 - offer_detailed
* inform{"food": "italian"}
 - reqmore
* inform{"food": "italian"}
 - reqmore
* inform{"food": "italian"}
 - reqmore
* inform{"food": "italian", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fbd422ad18-20130328_183717
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fbd422ad18-20130328_184603
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fbd422ad18-20130328_181029
* inform{"food": "vietnamese", "area": "dontcare"}
 - confirm-domain
* affirm
 - offer_detailed
* affirm
 - reqmore
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fbd422ad18-20130328_181932
* inform{"food": "vietnamese", "area": "north"}
 - canthelp
* inform{"area": "west"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fbd422ad18-20130328_184715
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "australasian"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e07d8f0f5-20130327_180143
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7e07d8f0f5-20130327_175716
* inform{"food": "traditional"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e07d8f0f5-20130327_175257
* inform{"area": "north"}
 - request_food
* inform{"area": "west"}
 - canthelp
* bye
 - bye

## Mar13_S1A1/voip-7e07d8f0f5-20130327_180412
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* bye
 - bye

## Mar13_S0A0/voip-7e07d8f0f5-20130327_175344
* inform{"area": "south"}
 - confirm-domain
* affirm
 - offer
* bye
 - bye

## Mar13_S1A1/voip-7e07d8f0f5-20130327_181435
* inform{"area": "west"}
 - request_food
* inform{"food": "international"}
 - request_food
* inform{"food": "international"}
 - canthelp
* inform{"area": "centre"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e07d8f0f5-20130328_154253
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7e07d8f0f5-20130327_181135
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* thankyou
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e07d8f0f5-20130328_192245
* inform{"pricerange": "expensive"}
 - request_area
* request{"requested_area": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* bye
 - bye

## Mar13_S0A1/voip-7e07d8f0f5-20130327_180533
* inform{"pricerange": "moderate", "area": "south"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e07d8f0f5-20130328_184338
* inform{"food": "polish"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e07d8f0f5-20130327_175626
* inform{"food": "mexican"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e07d8f0f5-20130327_180809
* inform{"food": "english", "area": "south"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "english"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7e07d8f0f5-20130328_185739
* affirm
 - select
* inform{"area": "north"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e07d8f0f5-20130328_192048
* inform{"food": "tuscan", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7e07d8f0f5-20130328_184956
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform{"pricerange": "expensive"}
 - expl-conf
* include_filter{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e07d8f0f5-20130327_181229
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7e07d8f0f5-20130328_185855
* inform{"food": "french", "pricerange": "expensive"}
 - offer_detailed
* inform{"food": "french", "pricerange": "expensive"}
 - offer_detailed
* negate
 - offer_detailed
* inform{"food": "french"}
 - canthelp
* inform{"food": "french", "area": "dontcare"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e07d8f0f5-20130328_185114
* inform{"food": "seafood", "area": "north"}
 - request_food
* inform{"food": "seafood"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b20968d1ea-20130323_110813
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - reqmore
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b20968d1ea-20130323_113731
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_area
* affirm
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* affirm
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-b20968d1ea-20130323_110621
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "english"}
 - canthelp
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* confirm{"food": "turkish"}
 - expl-conf
* confirm{"food": "turkish"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b20968d1ea-20130323_113345
* inform{"pricerange": "moderate"}
 - request_area
* inform{"food": "unusual"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b20968d1ea-20130323_112309
* inform{"area": "centre"}
 - request_pricerange
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* correct{"food": "italian"}
 - request_pricerange
* inform_dontcare{"area": "centre"}
 - canthelp
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b20968d1ea-20130323_105949
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b20968d1ea-20130323_111539
* inform_dontcare
 - request_area
* inform{"area": "dontcare"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "french"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer
* query{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b20968d1ea-20130323_112930
* inform{"area": "centre"}
 - request_pricerange
* inform{"food": "thai"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* correct{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* reqalts
 - offer_detailed
* negate
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* correct{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - reqmore
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b20968d1ea-20130323_112130
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b20968d1ea-20130323_105540
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform{"pricerange": "cheap"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-48c12815b3-20130402_052233
* inform{"food": "japanese", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-48c12815b3-20130402_045222
* inform{"pricerange": "moderate"}
 - expl-conf
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-48c12815b3-20130326_011113
* inform{"food": "turkish", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-48c12815b3-20130326_012654
* inform{"food": "australian", "pricerange": "expensive"}
 - confirm-domain
* inform{"food": "australian", "pricerange": "expensive"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-48c12815b3-20130402_051808
* inform{"food": "greek", "area": "centre"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* confirm{"food": "french"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-48c12815b3-20130402_050736
* inform{"food": "malaysian", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-48c12815b3-20130402_052405
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-48c12815b3-20130326_023109
* inform{"food": "asian oriental"}
 - expl-conf
* inform{"area": "east"}
 - request_food
* inform{"food": "asian oriental"}
 - expl-conf
* correct{"food": "asian oriental"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "asian oriental", "area": "east"}
 - offer_detailed
* inform{"food": "chinese"}
 - expl-conf
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-48c12815b3-20130402_045814
* inform{"food": "international", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-48c12815b3-20130326_005929
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-48c12815b3-20130326_021219
* inform{"food": "russian", "area": "centre"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-48c12815b3-20130402_050517
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-48c12815b3-20130402_050043
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-48c12815b3-20130402_050617
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-48c12815b3-20130326_034052
* inform{"food": "tuscan", "area": "dontcare"}
 - canthelp
* inform{"food": "asian oriental"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-48c12815b3-20130402_045915
* inform{"food": "cantonese", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-48c12815b3-20130326_011743
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-48c12815b3-20130402_052119
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-48c12815b3-20130402_045503
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - expl-conf
* correct{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b57f8ee22b-20130325_173942
* inform{"pricerange": "moderate"}
 - expl-conf
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b57f8ee22b-20130325_185940
* inform{"food": "indonesian", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b57f8ee22b-20130325_185315
* inform{"pricerange": "expensive"}
 - request_area
* inform{"food": "thai"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "thai"}
 - expl-conf
* negate
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b57f8ee22b-20130327_000138
* inform{"area": "north"}
 - request_food
* inform{"food": "scottish"}
 - request_food
* inform{"food": "scottish"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b57f8ee22b-20130325_173725
* inform{"area": "west"}
 - request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b57f8ee22b-20130325_183850
* inform{"pricerange": "moderate"}
 - request_area
* inform{"food": "halal"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "halal"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "halal"}
 - canthelp
* affirm
 - canthelp
* inform_dontcare
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b57f8ee22b-20130325_184849
* inform{"area": "south"}
 - request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b57f8ee22b-20130325_185743
* inform{"area": "west"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b57f8ee22b-20130326_234206
* inform{"food": "japanese"}
 - request_food
* inform{"food": "japanese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b57f8ee22b-20130325_174455
* inform{"area": "south"}
 - request_pricerange
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b57f8ee22b-20130325_184420
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b57f8ee22b-20130327_000010
* inform{"pricerange": "expensive", "area": "south"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b57f8ee22b-20130326_235132
* inform_dontcare
 - request_food
* inform{"food": "french"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* reqalts
 - canthelp
* inform{"pricerange": "expensive"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b57f8ee22b-20130326_235430
* inform{"food": "cuban", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b57f8ee22b-20130325_185141
* inform{"pricerange": "moderate", "area": "north"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7f9c1c8411-20130328_173449
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7f9c1c8411-20130328_173956
* inform{"food": "chinese", "area": "south"}
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7f9c1c8411-20130328_164730
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7f9c1c8411-20130401_170036
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7f9c1c8411-20130328_210227
* inform{"food": "indian"}
 - expl-conf
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "mediterranean"}
 - expl-conf
* correct{"area": "dontcare"}
 - canthelp
* inform{"food": "mediterranean"}
 - expl-conf
* negate
 - canthelp
* inform{"area": "dontcare"}
 - select
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7f9c1c8411-20130328_212116
* inform{"food": "swedish"}
 - canthelp
* inform{"area": "north"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7f9c1c8411-20130401_161411
* include_filter{"food": "international", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7f9c1c8411-20130328_164602
* inform{"food": "steakhouse"}
 - offer
* inform{"food": "steakhouse", "area": "dontcare"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7f9c1c8411-20130401_162408
* inform{"food": "italian", "area": "south"}
 - canthelp
* inform{"food": "italian", "area": "south"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S0A1/voip-7f9c1c8411-20130328_204059
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "east"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7f9c1c8411-20130328_135911
* inform{"food": "barbeque"}
 - request_area
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7f9c1c8411-20130401_161233
* include_filter{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "catalan"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7f9c1c8411-20130401_165623
* affirm
 - request_area
* inform{"food": "greek"}
 - canthelp
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7f9c1c8411-20130401_165234
* affirm
 - request_area
* inform{"food": "polynesian"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7f9c1c8411-20130401_161953
* inform{"food": "tuscan"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7f9c1c8411-20130401_163716
* affirm
 - request_area
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7f9c1c8411-20130328_210507
* include_filter{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7f9c1c8411-20130401_170332
* affirm
 - request_area
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7f9c1c8411-20130328_200359
* inform{"food": "turkish"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7f9c1c8411-20130328_195010
* include_filter{"food": "swedish", "area": "dontcare"}
 - canthelp
* inform{"food": "swedish"}
 - expl-conf
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "north american"}
 - select
* inform{"food": "north american"}
 - canthelp
* inform{"food": "north american"}
 - canthelp
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "swedish"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "north american"}
 - canthelp
* inform{"food": "north american"}
 - canthelp
* inform{"food": "swedish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e54437a6f0-20130325_131749
* inform{"food": "mexican"}
 - offer
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e54437a6f0-20130325_133942
* inform{"food": "swedish", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e54437a6f0-20130325_141052
* inform{"area": "south"}
 - request_pricerange
* inform{"food": "swedish"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e54437a6f0-20130325_133648
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* negate
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* affirm
 - canthelp
* request{"requested_addr": "True"}
 - offer
* confirm{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e54437a6f0-20130325_140049
* inform_dontcare
 - expl-conf
* inform{"pricerange": "expensive"}
 - expl-conf
* include_filter{"food": "danish"}
 - expl-conf
* correct{"food": "danish"}
 - canthelp
* inform{"food": "danish"}
 - offer_detailed
* inform{"food": "danish"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e54437a6f0-20130326_195611
* inform{"food": "brazilian"}
 - canthelp
* inform{"food": "korean"}
 - confirm-domain
* include_filter{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e54437a6f0-20130325_134159
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e54437a6f0-20130325_132940
* inform{"area": "south"}
 - request_food
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e54437a6f0-20130326_194636
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e54437a6f0-20130326_195047
* inform{"food": "african"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer
* confirm{"food": "african"}
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - offer
* confirm{"pricerange": "moderate"}
 - offer
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - expl-conf
* correct{"food": "spanish"}
 - request_area
* inform_dontcare{"pricerange": "moderate"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e54437a6f0-20130326_210856
* inform{"pricerange": "cheap"}
 - request_area
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e54437a6f0-20130325_140819
* inform{"food": "spanish"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"food": "spanish"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e54437a6f0-20130325_140347
* inform{"pricerange": "expensive", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-936ec6902a-20130328_133128
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-936ec6902a-20130328_140211
* inform{"area": "north"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-936ec6902a-20130328_133638
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"food": "british"}
 - canthelp
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-936ec6902a-20130328_132836
* request{"requested_pricerange": "True"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-936ec6902a-20130328_133008
* inform_dontcare
 - offer_detailed
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-936ec6902a-20130328_133502
* inform{"food": "traditional"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5a464ca603-20130401_130854
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - expl-conf
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5a464ca603-20130401_170359
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5a464ca603-20130401_192625
* inform{"food": "spanish"}
 - expl-conf
* correct{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - expl-conf
* affirm
 - request_area
* inform_dontcare
 - expl-conf
* negate
 - expl-conf
* correct{"area": "dontcare"}
 - expl-conf
* negate
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5a464ca603-20130401_193533
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - expl-conf
* inform{"food": "vietnamese", "pricerange": "cheap"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5a464ca603-20130401_165953
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5a464ca603-20130401_193155
* inform{"area": "centre"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5a464ca603-20130401_170156
* inform{"area": "north"}
 - request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A0/voip-5a464ca603-20130401_131710
* inform{"food": "jamaican", "area": "north"}
 - request_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5a464ca603-20130401_165744
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5a464ca603-20130401_193321
* inform{"pricerange": "expensive"}
 - request_area
* inform{"food": "portuguese"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5a464ca603-20130401_131414
* inform{"food": "persian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* inform{"food": "british", "pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5a464ca603-20130401_193933
* inform{"food": "brazilian"}
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - request_food
* inform{"food": "brazilian"}
 - canthelp
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - expl-conf
* inform{"pricerange": "dontcare"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* affirm
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-6dbc3573bc-20130329_035437
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-6dbc3573bc-20130328_193322
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-6dbc3573bc-20130328_191519
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-6dbc3573bc-20130328_193508
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-6dbc3573bc-20130328_193216
* inform{"food": "gastropub", "pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-6dbc3573bc-20130329_035304
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-6dbc3573bc-20130328_191808
* inform{"area": "dontcare"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-6dbc3573bc-20130328_191939
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "steakhouse"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fe4b6ef58f-20130325_224823
* inform{"food": "kosher", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fe4b6ef58f-20130325_233144
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fe4b6ef58f-20130325_233447
* inform{"area": "north"}
 - select
* correct{"area": "north"}
 - request_food
* inform{"food": "world"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fe4b6ef58f-20130325_234625
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fe4b6ef58f-20130325_234527
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fe4b6ef58f-20130325_234737
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fe4b6ef58f-20130325_233655
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fe4b6ef58f-20130325_224609
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fe4b6ef58f-20130325_233912
* inform{"area": "centre"}
 - request_pricerange
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fe4b6ef58f-20130325_223854
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fe4b6ef58f-20130328_231737
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare{"food": "thai"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-9f989824fd-20130324_080929
* inform{"food": "polynesian"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"name": "venue"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9f989824fd-20130324_074759
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9f989824fd-20130324_074224
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9f989824fd-20130325_202120
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9f989824fd-20130324_075152
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9f989824fd-20130325_200940
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9f989824fd-20130325_201803
* inform{"area": "east"}
 - request_pricerange
* inform{"food": "asian oriental"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9f989824fd-20130325_204229
* inform{"area": "west"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "fusion"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9f989824fd-20130325_203925
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9f989824fd-20130324_075833
* inform{"food": "international", "area": "dontcare"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-9f989824fd-20130325_201640
* inform{"food": "caribbean", "area": "centre"}
 - offer_detailed
* inform{"food": "caribbean"}
 - offer_detailed
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-9f989824fd-20130325_204124
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9f989824fd-20130325_204551
* inform{"food": "spanish"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "spanish"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9f989824fd-20130325_201956
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9f989824fd-20130325_203533
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9f989824fd-20130325_204439
* inform{"food": "steakhouse"}
 - request_food
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9f989824fd-20130324_074401
* inform{"food": "indian", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9f989824fd-20130324_073857
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9f989824fd-20130324_080805
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "european"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9f989824fd-20130325_201440
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9f989824fd-20130324_073316
* inform{"food": "asian oriental", "area": "south"}
 - canthelp
* inform{"food": "asian oriental", "area": "south"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian", "area": "south"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9f989824fd-20130324_080528
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* inform{"name": "venue"}
 - offer_detailed
* inform{"name": "venue"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b772dbf437-20130402_143019
* inform{"food": "swedish", "pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* reqalts
 - reqmore
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b772dbf437-20130402_142118
* inform{"area": "centre"}
 - request_food
* inform{"food": "catalan"}
 - request_food
* inform{"food": "catalan"}
 - request_food
* inform{"food": "italian"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b772dbf437-20130402_141805
* inform{"area": "dontcare"}
 - expl-conf
* inform{"pricerange": "dontcare"}
 - request_area
* inform{"food": "world"}
 - canthelp
* inform{"food": "mediterranean"}
 - select
* inform{"food": "mediterranean"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b772dbf437-20130402_141105
* inform{"area": "west"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b772dbf437-20130402_142550
* inform{"area": "east"}
 - request_food
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b772dbf437-20130402_141548
* inform{"area": "centre"}
 - request_food
* inform{"food": "spanish"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ec87351630-20130328_162752
* inform{"food": "mexican", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* thankyou
 - reqmore
* negate
 - reqmore
* negate
 - bye

## Mar13_S1A0/voip-ec87351630-20130328_162916
* inform{"food": "lebanese", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-14cb91bc48-20130327_202138
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-14cb91bc48-20130328_162839
* inform{"pricerange": "expensive"}
 - request_area
* negate
 - expl-conf
* inform{"food": "portuguese"}
 - request_food
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "mediterranean"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-14cb91bc48-20130328_163311
* inform{"food": "korean"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-14cb91bc48-20130328_194336
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-14cb91bc48-20130327_190340
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_food
* inform{"food": "japanese"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-14cb91bc48-20130328_163437
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "indian"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-14cb91bc48-20130328_161626
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "thai"}
 - request_pricerange
* inform{"area": "west"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - reqmore
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-14cb91bc48-20130328_163139
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-14cb91bc48-20130328_165532
* inform{"food": "venetian"}
 - request_pricerange
* inform{"area": "centre"}
 - request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-14cb91bc48-20130327_204058
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c0d36762a-20130328_213330
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4c0d36762a-20130328_204534
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c0d36762a-20130328_210737
* inform{"area": "east"}
 - request_food
* inform{"food": "greek"}
 - request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4c0d36762a-20130328_202045
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4c0d36762a-20130328_212300
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "polish"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c0d36762a-20130328_204720
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4c0d36762a-20130328_205236
* inform{"food": "indonesian", "pricerange": "expensive"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform_dontcare
 - expl-conf
* negate
 - expl-conf
* inform_dontcare
 - canthelp
* inform{"food": "british"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c0d36762a-20130328_212449
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4c0d36762a-20130328_204956
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4c0d36762a-20130328_203937
* inform{"pricerange": "cheap", "area": "west"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e2a895cfe5-20130327_020622
* inform{"area": "east"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e2a895cfe5-20130325_233852
* inform{"area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e2a895cfe5-20130325_231121
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "world"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e2a895cfe5-20130327_021102
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e2a895cfe5-20130326_232941
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e2a895cfe5-20130326_233604
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e2a895cfe5-20130325_234115
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e2a895cfe5-20130326_233655
* inform{"area": "dontcare"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "jamaican"}
 - request_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e2a895cfe5-20130326_233829
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e2a895cfe5-20130325_230900
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e2a895cfe5-20130325_230741
* inform{"area": "centre"}
 - request_food
* inform{"food": "hungarian"}
 - expl-conf
* correct{"food": "hungarian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* confirm{"food": "hungarian"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e2a895cfe5-20130327_021619
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e2a895cfe5-20130326_232742
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* query{"area": "west", "requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e2a895cfe5-20130325_232606
* inform{"food": "kosher", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e2a895cfe5-20130325_233234
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fce37b0ccb-20130328_151459
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer
* reqalts
 - offer
* reqalts
 - offer
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fce37b0ccb-20130328_145245
* inform{"food": "persian"}
 - request_food
* inform{"food": "persian"}
 - offer
* confirm{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fce37b0ccb-20130328_145831
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A1/voip-fce37b0ccb-20130328_143529
* inform{"area": "north"}
 - request_food
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fce37b0ccb-20130328_145418
* include_filter{"pricerange": "moderate"}
 - request_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fce37b0ccb-20130328_145014
* inform{"food": "basque"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* affirm
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fce37b0ccb-20130328_144400
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fce37b0ccb-20130328_144745
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8991b7bff6-20130401_180409
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8991b7bff6-20130401_174504
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8991b7bff6-20130327_192101
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8991b7bff6-20130401_175934
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8991b7bff6-20130401_174957
* inform{"pricerange": "cheap"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8991b7bff6-20130326_232407
* inform{"area": "centre"}
 - request_food
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8991b7bff6-20130326_231508
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S0A1/voip-8991b7bff6-20130401_161851
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8991b7bff6-20130326_230316
* inform_dontcare
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8991b7bff6-20130401_174811
* inform_dontcare
 - request_food
* inform{"food": "canapes"}
 - request_food
* inform{"food": "turkish"}
 - request_food
* inform{"food": "turkish"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8991b7bff6-20130401_160325
* inform_dontcare
 - select
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8991b7bff6-20130326_230200
* inform{"food": "european"}
 - expl-conf
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8991b7bff6-20130401_163110
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ef9aa63b85-20130329_131927
* inform{"pricerange": "cheap", "area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ef9aa63b85-20130328_223357
* inform{"area": "north"}
 - request_food
* inform{"food": "unusual"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - select
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ef9aa63b85-20130329_132421
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ef9aa63b85-20130329_125741
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ef9aa63b85-20130328_190444
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ef9aa63b85-20130329_130049
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ef9aa63b85-20130328_210319
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ef9aa63b85-20130329_131544
* inform_dontcare
 - request_food
* inform{"food": "eritrean"}
 - select
* negate
 - select
* inform{"food": "eritrean"}
 - select
* deny{"food": "vietnamese"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - reqmore
* inform{"food": "french"}
 - reqmore
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S0A1/voip-ef9aa63b85-20130328_184027
* inform{"area": "west"}
 - request_food
* inform{"food": "italian"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ef9aa63b85-20130328_211048
* inform_dontcare
 - request_food
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ef9aa63b85-20130329_131415
* inform{"food": "hungarian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-22a181cad5-20130326_023529
* inform{"food": "lebanese", "area": "centre"}
 - expl-conf
* inform{"food": "lebanese"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "lebanese"}
 - request_food
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-22a181cad5-20130326_022324
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_184430
* inform{"food": "english"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3cf7bd870d-20130327_180414
* inform{"food": "indonesian", "pricerange": "cheap"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3cf7bd870d-20130328_212502
* inform{"area": "centre"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "kosher"}
 - request_food
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_174017
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3cf7bd870d-20130328_211947
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3cf7bd870d-20130328_212749
* inform{"food": "malaysian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* correct{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3cf7bd870d-20130328_150815
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_183049
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "french", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_175817
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3cf7bd870d-20130327_175213
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3cf7bd870d-20130327_174155
* inform{"food": "tuscan", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* inform{"food": "gastropub"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3cf7bd870d-20130327_180852
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3cf7bd870d-20130327_181243
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3cf7bd870d-20130328_212136
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3cf7bd870d-20130327_184051
* inform{"food": "crossover", "area": "west"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3cf7bd870d-20130327_174526
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* correct{"area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4f069a4136-20130402_032014
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4f069a4136-20130327_205937
* inform{"food": "vietnamese", "pricerange": "cheap"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* inform_dontcare
 - reqmore
* inform{"pricerange": "moderate"}
 - reqmore
* inform_dontcare
 - reqmore
* request{"requested_pricerange": "True"}
 - reqmore
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4f069a4136-20130402_031309
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4f069a4136-20130327_205819
* inform{"area": "west"}
 - request_food
* inform_dontcare{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4f069a4136-20130327_204405
* inform{"food": "afghan"}
 - expl-conf
* inform{"pricerange": "expensive"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4f069a4136-20130327_211252
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4f069a4136-20130402_030948
* inform{"food": "portuguese"}
 - offer_detailed
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4f069a4136-20130327_210318
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* confirm{"area": "centre"}
 - offer_detailed
* inform{"food": "british"}
 - offer_detailed
* confirm{"area": "centre"}
 - offer_detailed
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4f069a4136-20130402_032750
* inform{"food": "international"}
 - request_area
* inform{"area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4f069a4136-20130402_031636
* inform{"area": "south"}
 - request_food
* inform{"food": "danish"}
 - canthelp
* correct{"food": "danish"}
 - select
* inform{"food": "danish"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4f069a4136-20130327_204947
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4f069a4136-20130402_030550
* inform{"food": "thai"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform{"food": "thai"}
 - expl-conf
* inform_dontcare
 - request_pricerange
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* negate
 - offer_detailed
* confirm{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4f069a4136-20130327_205654
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - expl-conf
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4f069a4136-20130402_033307
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "turkish"}
 - select
* inform{"food": "turkish"}
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4f069a4136-20130327_204639
* inform{"food": "scandinavian"}
 - request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4f069a4136-20130402_034737
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4f069a4136-20130402_032149
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - expl-conf
* inform{"food": "swiss"}
 - expl-conf
* inform{"food": "swiss"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - expl-conf
* negate
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4f069a4136-20130327_205501
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fdf8b50918-20130326_051637
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fdf8b50918-20130329_014245
* inform{"area": "centre"}
 - request_food
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fdf8b50918-20130327_024718
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fdf8b50918-20130329_013736
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fdf8b50918-20130327_024110
* inform{"food": "european", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fdf8b50918-20130329_042606
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fdf8b50918-20130329_035324
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fdf8b50918-20130326_050512
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fdf8b50918-20130329_014041
* inform{"food": "bistro", "pricerange": "moderate"}
 - request_food
* inform{"food": "bistro"}
 - request_food
* inform{"food": "bistro"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fdf8b50918-20130326_051438
* inform{"food": "indian", "area": "east"}
 - canthelp
* inform{"food": "indian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fdf8b50918-20130327_024909
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "jamaican"}
 - offer_detailed
* inform{"food": "jamaican"}
 - offer_detailed
* confirm{"food": "jamaican"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fdf8b50918-20130327_023811
* inform{"food": "jamaican", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* bye
 - bye

## Mar13_S1A1/voip-fdf8b50918-20130329_013925
* inform{"food": "spanish"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fdf8b50918-20130326_051921
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fdf8b50918-20130326_052504
* inform{"food": "italian", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fdf8b50918-20130326_052355
* inform{"pricerange": "expensive", "area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fdf8b50918-20130329_042348
* inform{"food": "european", "pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fdf8b50918-20130327_024453
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-249d0f617b-20130328_161219
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-249d0f617b-20130326_005503
* inform{"pricerange": "moderate"}
 - select
* affirm
 - select
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-249d0f617b-20130326_010500
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "british"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-249d0f617b-20130328_161812
* inform{"area": "west"}
 - request_food
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9819537952-20130328_232353
* inform{"area": "west"}
 - request_food
* inform{"food": "singaporean"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9819537952-20130327_022757
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - offer_detailed
* bye
 - offer_detailed
* bye
 - canthelp
* thankyou
 - offer_detailed
* thankyou
 - offer
* bye
 - canthelp
* bye
 - bye

## Mar13_S0A1/voip-9819537952-20130328_230928
* inform{"pricerange": "cheap"}
 - request_food
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9819537952-20130328_231209
* inform{"pricerange": "cheap"}
 - request_food
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-9819537952-20130327_023104
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9819537952-20130328_235404
* request{"requested_pricerange": "True"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-9819537952-20130327_024815
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9819537952-20130327_023856
* inform{"area": "west"}
 - request_food
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-9819537952-20130327_021901
* inform{"area": "west"}
 - request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "british"}
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S0A1/voip-9819537952-20130328_235607
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9819537952-20130328_234847
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-9f447ce48e-20130328_115123
* inform_dontcare
 - expl-conf
* affirm
 - canthelp
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-05e7a5440b-20130328_214746
* inform{"food": "italian", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-05e7a5440b-20130328_211013
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-05e7a5440b-20130328_220724
* inform_dontcare
 - request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "european"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-05e7a5440b-20130328_215502
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-05e7a5440b-20130328_213943
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-05e7a5440b-20130328_220901
* inform{"food": "vegetarian"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-05e7a5440b-20130328_213636
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-05e7a5440b-20130328_211620
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - canthelp
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-05e7a5440b-20130328_211413
* inform{"area": "east"}
 - request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-05e7a5440b-20130328_215138
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-05e7a5440b-20130328_222114
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-05e7a5440b-20130328_211839
* inform{"food": "cuban", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-05e7a5440b-20130328_212037
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-583e7cede5-20130323_060529
* inform{"food": "polish", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-583e7cede5-20130324_060002
* inform{"food": "italian", "area": "west"}
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-583e7cede5-20130324_063315
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-583e7cede5-20130324_055306
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-583e7cede5-20130323_052525
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - expl-conf
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-583e7cede5-20130323_143756
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* inform{"food": "north american"}
 - offer
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-583e7cede5-20130324_060901
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - select
* inform_dontcare
 - request_food
* inform{"food": "turkish"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-583e7cede5-20130323_061037
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - expl-conf
* affirm
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S1A1/voip-583e7cede5-20130324_062107
* inform{"food": "european", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-583e7cede5-20130323_062756
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-583e7cede5-20130324_060405
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-583e7cede5-20130323_055421
* inform{"area": "north"}
 - request_food
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-583e7cede5-20130324_063452
* inform{"food": "turkish", "pricerange": "expensive"}
 - request_food
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-583e7cede5-20130323_060100
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-583e7cede5-20130323_051824
* inform{"food": "seafood", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_name": "True"}
 - offer_detailed
* request{"requested_name": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-583e7cede5-20130323_054735
* inform{"area": "centre"}
 - request_area
* inform{"area": "centre"}
 - request_pricerange
* inform{"food": "english", "area": "centre"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-583e7cede5-20130324_061500
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-583e7cede5-20130324_062248
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-583e7cede5-20130324_063717
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-869dd52548-20130401_183901
* inform{"food": "hungarian", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-869dd52548-20130401_175459
* inform{"food": "catalan", "area": "east"}
 - request_food
* inform{"food": "catalan"}
 - request_food
* inform{"food": "catalan"}
 - request_food
* inform{"food": "catalan"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-869dd52548-20130401_184505
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-869dd52548-20130401_175746
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-869dd52548-20130326_000755
* inform{"food": "moroccan", "pricerange": "moderate"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-869dd52548-20130401_180217
* inform{"pricerange": "expensive", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-869dd52548-20130401_184747
* inform{"area": "north"}
 - request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-869dd52548-20130401_180331
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-869dd52548-20130401_184008
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_area": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-869dd52548-20130326_000655
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-869dd52548-20130401_184240
* inform_dontcare
 - request_food
* inform{"food": "portuguese"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - canthelp
* request{"requested_pricerange": "True"}
 - offer
* inform{"food": "portuguese", "pricerange": "dontcare"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* reqalts
 - canthelp
* bye
 - bye

## Mar13_S0A1/voip-869dd52548-20130326_001137
* inform{"food": "asian oriental", "area": "south"}
 - request_food
* inform{"food": "asian oriental"}
 - request_food
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-869dd52548-20130401_175624
* inform{"food": "spanish", "pricerange": "expensive"}
 - offer_detailed
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-869dd52548-20130326_000910
* inform{"food": "african", "pricerange": "dontcare"}
 - confirm-domain
* include_filter{"food": "african"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-869dd52548-20130401_184559
* inform{"food": "japanese", "area": "centre"}
 - request_food
* inform{"food": "cantonese"}
 - request_food
* inform{"food": "cantonese"}
 - request_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-869dd52548-20130401_175253
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-a7ddefaeb3-20130327_174327
* inform{"area": "centre"}
 - request_area
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a7ddefaeb3-20130327_174908
* inform{"food": "barbeque", "pricerange": "cheap"}
 - request_food
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a7ddefaeb3-20130328_172838
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - select
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a7ddefaeb3-20130328_172708
* inform{"pricerange": "moderate", "area": "north"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a7ddefaeb3-20130328_173142
* affirm
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - select
* inform_dontcare
 - select
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A1/voip-8d5173f3a6-20130324_183442
* inform{"food": "fusion"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8d5173f3a6-20130324_185406
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8d5173f3a6-20130323_012203
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "international"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8d5173f3a6-20130323_011736
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8d5173f3a6-20130324_183623
* bye
 - request_area
* inform{"area": "west"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8d5173f3a6-20130323_012048
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8d5173f3a6-20130323_015026
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8d5173f3a6-20130324_190545
* inform{"food": "mexican", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8d5173f3a6-20130324_190350
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8d5173f3a6-20130324_184915
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8d5173f3a6-20130323_011549
* inform{"pricerange": "cheap"}
 - request_area
* request{"requested_area": "True"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8d5173f3a6-20130323_013323
* inform{"food": "seafood", "pricerange": "expensive"}
 - request_food
* inform{"food": "seafood"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8d5173f3a6-20130324_184603
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8d5173f3a6-20130323_015902
* inform{"area": "west"}
 - request_food
* inform{"food": "british"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8d5173f3a6-20130324_185203
* inform{"area": "east"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8d5173f3a6-20130323_013205
* inform{"food": "greek", "area": "south"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8d5173f3a6-20130323_015159
* request{"requested_pricerange": "True"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8d5173f3a6-20130324_190231
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8d5173f3a6-20130324_183949
* inform{"food": "creative"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8d5173f3a6-20130324_184438
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-58047f5227-20130327_032952
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-58047f5227-20130327_034311
* inform{"food": "seafood"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "seafood"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-58047f5227-20130326_032713
* inform{"food": "swedish", "area": "dontcare"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "north american"}
 - canthelp
* inform{"food": "north american"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-58047f5227-20130326_031756
* inform{"pricerange": "cheap", "area": "north"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-58047f5227-20130326_030552
* inform{"food": "danish", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-58047f5227-20130326_031502
* inform{"food": "australian", "area": "west"}
 - request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-58047f5227-20130327_032049
* inform{"food": "venetian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-58047f5227-20130327_033611
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-58047f5227-20130326_032849
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-58047f5227-20130327_032257
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-58047f5227-20130326_032210
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-58047f5227-20130327_033352
* inform{"food": "european", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-58047f5227-20130327_034209
* inform{"food": "mexican"}
 - request_food
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-58047f5227-20130327_032835
* inform{"food": "unusual", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-58047f5227-20130326_030421
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-58047f5227-20130327_004644
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-58047f5227-20130327_033220
* inform{"food": "russian", "area": "dontcare"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "russian"}
 - canthelp
* inform{"food": "north american"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-58047f5227-20130326_030155
* inform{"food": "traditional", "area": "centre"}
 - request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-58047f5227-20130327_032739
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-da4a08ad84-20130328_154258
* inform{"food": "korean", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da4a08ad84-20130328_160004
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_postcode": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-da4a08ad84-20130328_154358
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-da4a08ad84-20130328_155250
* inform{"food": "traditional", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-da4a08ad84-20130328_155023
* inform{"food": "turkish", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-da4a08ad84-20130328_155120
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-da4a08ad84-20130328_160315
* inform{"pricerange": "expensive", "area": "south"}
 - request_area
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-14f776f781-20130328_140514
* inform{"food": "vietnamese", "area": "north"}
 - request_food
* inform{"food": "vietnamese"}
 - canthelp
* inform{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - canthelp
* thankyou
 - offer_detailed
* bye
 - expl-conf
* bye
 - bye

## Mar13_S0A1/voip-14f776f781-20130328_141638
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* inform{"food": "north american"}
 - confirm-domain
* affirm
 - offer_detailed
* inform{"food": "north american"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-14f776f781-20130328_115724
* inform{"food": "polish"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-14f776f781-20130329_033249
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-14f776f781-20130328_123358
* inform{"food": "australian", "area": "east"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"food": "australian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-14f776f781-20130328_151904
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-14f776f781-20130328_121622
* inform{"food": "vegetarian", "pricerange": "expensive"}
 - request_pricerange
* thankyou
 - canthelp
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-14f776f781-20130328_142356
* inform{"food": "basque", "pricerange": "expensive"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-14f776f781-20130328_123813
* inform{"food": "creative", "pricerange": "moderate"}
 - offer_detailed
* inform{"food": "british"}
 - offer_detailed
* inform{"food": "creative"}
 - offer_detailed
* inform{"food": "creative"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-1b51204ef5-20130401_173145
* inform{"food": "indian"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* reqalts
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-1b51204ef5-20130401_172934
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "centre"}
 - confirm-domain
* include_filter{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - reqmore
* bye
 - bye

## Mar13_S1A0/voip-1b51204ef5-20130401_145241
* inform{"food": "steakhouse"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "turkish"}
 - expl-conf
* inform{"food": "turkish"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-1b51204ef5-20130401_150524
* inform{"food": "unusual"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* bye
 - bye

## Mar13_S1A1/voip-1b51204ef5-20130401_145742
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "international"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-1b51204ef5-20130401_145115
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fd0c0fb514-20130328_114840
* negate
 - expl-conf
* inform_dontcare
 - expl-conf
* inform_dontcare
 - request_area
* inform{"area": "west"}
 - expl-conf
* inform_dontcare
 - request_food
* inform{"food": "italian"}
 - offer_detailed
* inform_dontcare
 - offer
* inform_dontcare
 - offer
* inform{"food": "polynesian"}
 - offer
* inform_dontcare
 - offer
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* confirm{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - expl-conf
* inform_dontcare
 - expl-conf
* inform{"pricerange": "expensive"}
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - canthelp
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fd0c0fb514-20130328_114152
* inform{"pricerange": "moderate", "area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fd0c0fb514-20130328_114024
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e3b4879e0d-20130327_030628
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e3b4879e0d-20130327_181026
* inform{"area": "centre"}
 - request_food
* inform{"food": "french", "area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e3b4879e0d-20130327_182147
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e3b4879e0d-20130326_024455
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e3b4879e0d-20130326_021022
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e3b4879e0d-20130326_024336
* inform{"area": "centre"}
 - request_pricerange
* inform{"food": "english"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e3b4879e0d-20130326_020631
* inform{"food": "english", "area": "west"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "english"}
 - request_food
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - reqmore
* bye
 - reqmore
* bye
 - reqmore
* negate
 - reqmore
* bye
 - reqmore
* inform_dontcare
 - offer_detailed
* bye
 - reqmore
* bye
 - bye

## Mar13_S1A0/voip-e3b4879e0d-20130327_181509
* inform{"food": "european", "area": "centre"}
 - request_food
* inform{"food": "european"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e3b4879e0d-20130326_215515
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e3b4879e0d-20130326_022732
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - canthelp
* bye
 - bye

## Mar13_S0A0/voip-e3b4879e0d-20130327_030803
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - offer_detailed
* bye
 - canthelp
* bye
 - bye

## Mar13_S1A1/voip-e3b4879e0d-20130327_181715
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e3b4879e0d-20130326_023327
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-560cbd32a5-20130401_144308
* inform{"food": "afghan"}
 - request_food
* inform{"food": "afghan"}
 - request_food
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform_dontcare
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* inform{"food": "vietnamese", "area": "dontcare"}
 - offer_detailed
* confirm{"pricerange": "cheap"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-560cbd32a5-20130401_143827
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - bye

## Mar13_S1A0/voip-62cc0cc55d-20130323_155832
* inform{"area": "north"}
 - request_food
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-62cc0cc55d-20130328_143213
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-62cc0cc55d-20130323_155313
* inform{"food": "world", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-62cc0cc55d-20130328_141332
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "vietnamese"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-62cc0cc55d-20130323_155046
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* query{"name": "da vinci pizzeria", "requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-62cc0cc55d-20130328_140957
* inform{"food": "polynesian", "area": "dontcare"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* reqalts
 - canthelp
* inform{"food": "modern european"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-62cc0cc55d-20130323_160732
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "indian", "pricerange": "cheap"}
 - request_area_detailed
* inform{"area": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-62cc0cc55d-20130323_160541
* inform{"area": "centre"}
 - request_food
* inform{"food": "portuguese"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-62cc0cc55d-20130323_161217
* inform{"area": "centre"}
 - request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "international"}
 - canthelp
* inform{"area": "centre"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* query{"name": "bloomsbury restaurant", "requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-62cc0cc55d-20130328_143025
* inform_dontcare
 - offer_detailed
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "italian", "area": "west"}
 - canthelp
* inform{"food": "italian", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ab4f1dbb59-20130325_214245
* inform{"food": "cuban", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ab4f1dbb59-20130328_180542
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ab4f1dbb59-20130325_214609
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ab4f1dbb59-20130325_214838
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ab4f1dbb59-20130325_214441
* inform{"food": "kosher", "area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-158a881c88-20130328_152500
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-158a881c88-20130328_153956
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-158a881c88-20130328_151638
* inform{"pricerange": "expensive", "area": "east"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-158a881c88-20130328_150912
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-158a881c88-20130328_151847
* inform{"food": "lebanese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-158a881c88-20130328_151021
* inform{"pricerange": "moderate"}
 - select
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - expl-conf
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-39a25ab2f8-20130326_122045
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-39a25ab2f8-20130326_120526
* inform{"food": "european"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-39a25ab2f8-20130328_131901
* inform{"area": "west"}
 - request_food
* inform{"pricerange": "moderate"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-39a25ab2f8-20130326_131509
* inform{"pricerange": "cheap", "area": "west"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - request_food
* inform{"pricerange": "cheap"}
 - request_food
* bye
 - bye

## Mar13_S1A1/voip-30772678da-20130328_193916
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-30772678da-20130328_192354
* inform{"pricerange": "moderate", "area": "north"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-30772678da-20130328_192819
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "english"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-30772678da-20130328_200455
* inform{"food": "portuguese", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-30772678da-20130328_200202
* inform{"food": "world"}
 - canthelp
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-30772678da-20130328_195730
* inform{"area": "west"}
 - request_food
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-30772678da-20130328_193458
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d76f6e4f82-20130327_195041
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d76f6e4f82-20130327_193430
* inform{"area": "centre"}
 - request_food
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d76f6e4f82-20130327_201839
* inform{"area": "south"}
 - request_food
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d76f6e4f82-20130327_184807
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d76f6e4f82-20130327_184557
* inform{"food": "creative"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d76f6e4f82-20130327_185043
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "east"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d76f6e4f82-20130327_185328
* inform{"pricerange": "expensive"}
 - request_pricerange
* inform_dontcare
 - offer
* thankyou
 - offer
* inform_dontcare
 - offer
* confirm{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d76f6e4f82-20130327_194817
* inform{"pricerange": "expensive"}
 - request_area
* request{"requested_area": "True"}
 - confirm-domain
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d76f6e4f82-20130327_190022
* inform{"area": "north"}
 - request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d76f6e4f82-20130327_193247
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-21ec2b7850-20130327_043931
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-21ec2b7850-20130327_033947
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-21ec2b7850-20130327_034759
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-21ec2b7850-20130326_021426
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-21ec2b7850-20130327_044255
* inform{"area": "north"}
 - request_food
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-21ec2b7850-20130327_040209
* inform{"pricerange": "moderate"}
 - select
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-21ec2b7850-20130327_040416
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-21ec2b7850-20130326_114409
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - expl-conf
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-21ec2b7850-20130327_042044
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "chinese"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-21ec2b7850-20130325_143118
* inform{"area": "south"}
 - request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-21ec2b7850-20130326_021614
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-21ec2b7850-20130327_040626
* inform{"pricerange": "expensive"}
 - request_food
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-21ec2b7850-20130325_132551
* inform{"area": "east"}
 - request_food
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - expl-conf
* negate
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-21ec2b7850-20130326_024646
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-21ec2b7850-20130325_145025
* inform{"food": "hungarian"}
 - offer_detailed
* inform{"food": "hungarian"}
 - offer_detailed
* negate
 - offer
* inform{"area": "south"}
 - offer
* inform{"area": "south"}
 - offer_detailed
* inform{"food": "hungarian"}
 - offer_detailed
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-21ec2b7850-20130326_025529
* inform{"food": "german"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "german"}
 - canthelp
* inform{"food": "european", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-21ec2b7850-20130325_154906
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"area": "north"}
 - select
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-21ec2b7850-20130326_025736
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "spanish"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-21ec2b7850-20130326_022849
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"food": "gastropub"}
 - offer
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-21ec2b7850-20130327_045035
* inform{"area": "east"}
 - offer_detailed
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-21ec2b7850-20130327_044903
* inform{"food": "persian"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-21ec2b7850-20130325_162417
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b27a230d2e-20130323_050439
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130329_032627
* inform{"food": "cantonese", "area": "south"}
 - request_food
* inform{"food": "cantonese"}
 - canthelp
* affirm
 - select
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-b27a230d2e-20130323_042544
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "seafood"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b27a230d2e-20130323_053403
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S0A1/voip-b27a230d2e-20130329_035828
* inform{"area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b27a230d2e-20130329_031831
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "west"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b27a230d2e-20130323_053029
* inform{"area": "south"}
 - request_food
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b27a230d2e-20130329_034847
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b27a230d2e-20130323_043046
* inform{"area": "centre"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform_dontcare
 - offer
* inform_dontcare
 - offer
* inform{"area": "centre"}
 - offer_detailed
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130323_050944
* inform{"food": "unusual", "pricerange": "moderate"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130329_031627
* inform{"food": "danish"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130323_041953
* inform{"food": "german", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* inform{"food": "asian oriental"}
 - expl-conf
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - offer_detailed
* inform_dontcare
 - offer
* inform_dontcare
 - offer
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b27a230d2e-20130329_040014
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130329_043420
* inform{"food": "indian", "area": "east"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "indian", "area": "east"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130329_035413
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* inform{"name": "chiquito restaurant bar"}
 - offer_detailed
* inform{"pricerange": "expensive", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b27a230d2e-20130329_031256
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130323_050830
* inform{"food": "seafood", "pricerange": "expensive"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b27a230d2e-20130329_033804
* inform{"food": "chinese", "pricerange": "cheap"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b27a230d2e-20130323_045538
* inform{"pricerange": "expensive"}
 - offer_detailed
* confirm{"food": "seafood"}
 - offer_detailed
* inform{"food": "seafood"}
 - offer_detailed
* request{"requested_addr": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - reqmore
* request{"requested_area": "True"}
 - reqmore
* request{"requested_area": "True"}
 - reqmore
* inform{"food": "seafood", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b27a230d2e-20130329_030940
* inform{"food": "vietnamese", "pricerange": "moderate"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "indian"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b27a230d2e-20130329_031422
* inform{"area": "centre"}
 - request_food
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b27a230d2e-20130329_030324
* inform{"food": "christmas", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "christmas"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* inform{"food": "christmas"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b27a230d2e-20130323_050551
* inform{"food": "korean", "area": "north"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d2d103292-20130326_041300
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d2d103292-20130329_041636
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d2d103292-20130326_041008
* inform{"food": "indonesian"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d2d103292-20130326_041541
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "basque"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d2d103292-20130329_041521
* inform{"food": "russian", "area": "centre"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2d2d103292-20130326_042921
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d2d103292-20130326_041959
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d2d103292-20130326_041815
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d2d103292-20130326_043748
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2d2d103292-20130326_044020
* inform_dontcare
 - offer_detailed
* inform{"area": "centre"}
 - offer_detailed
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d2d103292-20130329_041255
* inform{"food": "bistro", "area": "centre"}
 - canthelp
* inform{"food": "north american"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d2d103292-20130329_035727
* inform{"food": "world"}
 - canthelp
* inform{"food": "spanish"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d2d103292-20130329_040958
* inform{"food": "moroccan", "area": "centre"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "thai"}
 - expl-conf
* affirm
 - expl-conf
* correct{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - canthelp
* inform{"pricerange": "dontcare"}
 - offer_detailed
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai", "pricerange": "moderate"}
 - expl-conf
* affirm
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d2d103292-20130326_043352
* inform{"food": "mediterranean"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d2d103292-20130329_040656
* inform{"food": "japanese", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d2d103292-20130329_041424
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d2d103292-20130329_035835
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d2d103292-20130329_042056
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d2d103292-20130328_195634
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d2d103292-20130329_041951
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d2d103292-20130328_195103
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d2d103292-20130329_035601
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2d2d103292-20130326_040723
* inform{"area": "centre"}
 - offer_detailed
* confirm{"food": "fusion"}
 - offer_detailed
* inform{"food": "fusion"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-908884f5fd-20130326_224812
* inform{"food": "belgian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-908884f5fd-20130326_215916
* inform{"food": "scandinavian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "mediterranean"}
 - request_area
* inform_dontcare{"pricerange": "cheap"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - expl-conf
* inform{"pricerange": "cheap"}
 - offer
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8586129f35-20130328_160121
* inform{"food": "romanian", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - expl-conf
* affirm
 - expl-conf
* inform{"food": "mediterranean"}
 - select
* inform{"food": "mediterranean"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03c59ba692-20130325_183305
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03c59ba692-20130324_034930
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03c59ba692-20130324_034507
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03c59ba692-20130402_054245
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03c59ba692-20130324_034058
* inform{"food": "vegetarian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03c59ba692-20130324_033629
* inform{"food": "afghan", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03c59ba692-20130324_180022
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S0A1/voip-03c59ba692-20130402_060307
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03c59ba692-20130402_053545
* inform{"food": "brazilian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03c59ba692-20130324_180433
* inform{"food": "romanian", "area": "centre"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03c59ba692-20130402_060050
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03c59ba692-20130324_034712
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03c59ba692-20130325_180735
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03c59ba692-20130324_033821
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-aaa44b4121-20130326_060013
* inform{"food": "danish"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental", "pricerange": "expensive"}
 - request_area
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-aaa44b4121-20130326_055316
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-aaa44b4121-20130326_055608
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform{"pricerange": "cheap"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-aaa44b4121-20130326_051152
* inform{"pricerange": "moderate"}
 - select
* inform{"food": "british"}
 - select
* inform{"food": "british"}
 - select
* inform{"area": "north"}
 - canthelp
* inform{"area": "south"}
 - canthelp
* inform{"food": "british"}
 - expl-conf
* affirm
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-aaa44b4121-20130326_055421
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-aaa44b4121-20130327_170849
* inform{"area": "south"}
 - request_food
* inform{"pricerange": "cheap"}
 - request_food
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-aaa44b4121-20130327_171453
* inform{"food": "korean"}
 - offer_detailed
* inform{"area": "dontcare"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-aaa44b4121-20130327_170337
* inform{"food": "moroccan", "pricerange": "moderate"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "indian"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-aaa44b4121-20130326_051458
* inform{"food": "european"}
 - request_area
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-aaa44b4121-20130327_171321
* inform{"pricerange": "cheap", "area": "south"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-aaa44b4121-20130327_002455
* inform{"area": "west"}
 - request_food
* inform{"food": "british"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-aaa44b4121-20130327_165758
* inform{"food": "european"}
 - offer
* negate
 - offer
* inform{"food": "european"}
 - offer
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* inform{"food": "portuguese", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-aaa44b4121-20130326_050817
* inform{"pricerange": "cheap"}
 - request_food
* inform{"area": "north"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-aaa44b4121-20130327_172530
* inform{"pricerange": "cheap"}
 - request_food
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-aaa44b4121-20130327_170541
* inform{"food": "malaysian", "area": "centre"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-aaa44b4121-20130327_172225
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-aaa44b4121-20130327_170209
* inform{"food": "world", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-aaa44b4121-20130327_171617
* inform{"food": "international"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-aaa44b4121-20130327_170719
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-aaa44b4121-20130326_060838
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-aaa44b4121-20130326_054647
* inform{"food": "traditional", "area": "south"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-aaa44b4121-20130327_171958
* inform{"area": "south"}
 - request_food
* inform{"pricerange": "expensive"}
 - request_food
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-affbf578cf-20130401_162946
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-affbf578cf-20130401_163655
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e61fa89add-20130327_074357
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e61fa89add-20130326_013340
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - request_area_detailed
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e61fa89add-20130327_075222
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e61fa89add-20130326_100409
* inform{"food": "basque", "pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e61fa89add-20130327_072313
* inform{"food": "korean", "area": "north"}
 - canthelp
* inform{"food": "persian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e61fa89add-20130327_075612
* inform{"food": "tuscan", "pricerange": "expensive"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e61fa89add-20130327_074017
* inform_dontcare
 - request_food
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e61fa89add-20130326_013931
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "asian oriental"}
 - select
* inform{"food": "asian oriental"}
 - request_area
* inform{"area": "dontcare"}
 - request_pricerange
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e61fa89add-20130327_080334
* inform{"food": "romanian", "area": "centre"}
 - request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "british"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e61fa89add-20130326_011204
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform{"food": "chinese"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "cheap"}
 - expl-conf
* inform{"pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e61fa89add-20130326_100750
* inform{"food": "greek", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - confirm-domain
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e61fa89add-20130327_074526
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e61fa89add-20130326_013737
* inform{"food": "eritrean", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e61fa89add-20130326_100617
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e61fa89add-20130327_071630
* inform{"food": "danish", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-c8ec8c76dd-20130328_205311
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-c8ec8c76dd-20130328_205953
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-c8ec8c76dd-20130328_180054
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-c8ec8c76dd-20130328_175715
* inform{"food": "scottish"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "international"}
 - request_area
* inform{"area": "dontcare"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-c8ec8c76dd-20130328_174742
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-c8ec8c76dd-20130328_175504
* inform{"food": "bistro", "area": "centre"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-c8ec8c76dd-20130328_210403
* inform{"food": "malaysian", "area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-c8ec8c76dd-20130328_181909
* inform{"area": "east"}
 - request_food
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* inform{"food": "gastropub", "area": "east"}
 - select
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-c8ec8c76dd-20130328_205558
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-c8ec8c76dd-20130328_205041
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5cf59cc660-20130327_144955
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5cf59cc660-20130328_161517
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5cf59cc660-20130328_163609
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5cf59cc660-20130327_145314
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-5cf59cc660-20130328_143501
* inform{"food": "thai"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5cf59cc660-20130328_164112
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5cf59cc660-20130328_161200
* inform{"food": "cuban", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - expl-conf
* correct{"food": "spanish"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-5cf59cc660-20130328_161054
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - confirm-domain
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5cf59cc660-20130328_143758
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"area": "north"}
 - offer
* confirm{"area": "north"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-5cf59cc660-20130327_144735
* inform{"food": "korean"}
 - confirm-domain
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5cf59cc660-20130328_172318
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5cf59cc660-20130327_145222
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5cf59cc660-20130327_144604
* inform{"food": "japanese", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5cf59cc660-20130328_151124
* inform{"food": "chinese", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5cf59cc660-20130327_143126
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-5cf59cc660-20130328_171914
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-5cf59cc660-20130327_145740
* inform{"food": "creative"}
 - canthelp
* inform{"food": "north american"}
 - confirm-domain
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5cf59cc660-20130328_145134
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5cf59cc660-20130328_160837
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* correct{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5cf59cc660-20130327_144338
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5cf59cc660-20130328_160946
* inform{"food": "european", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5cf59cc660-20130327_143308
* inform{"food": "greek"}
 - canthelp
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5cf59cc660-20130328_172556
* inform{"food": "persian", "area": "south"}
 - request_food
* inform{"food": "persian"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* confirm{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-5749b16764-20130328_145900
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-5749b16764-20130328_150143
* inform{"food": "asian oriental", "area": "dontcare"}
 - canthelp
* inform{"food": "international"}
 - canthelp
* inform{"food": "international"}
 - expl-conf
* inform{"pricerange": "dontcare"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-5749b16764-20130328_151730
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-5749b16764-20130328_145608
* inform{"food": "unusual", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-5749b16764-20130328_151234
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b59a0391b-20130401_135225
* inform{"food": "vietnamese"}
 - offer
* inform{"food": "vietnamese"}
 - offer_detailed
* reqalts
 - reqmore
* inform{"food": "vietnamese"}
 - offer_detailed
* reqalts
 - reqmore
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b59a0391b-20130401_133524
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b59a0391b-20130401_133038
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - canthelp
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b59a0391b-20130401_133238
* inform{"food": "chinese"}
 - select
* inform{"area": "south"}
 - expl-conf
* negate
 - expl-conf
* correct{"area": "south"}
 - request_food
* inform{"food": "chinese"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - canthelp
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b59a0391b-20130401_135704
* inform{"area": "west"}
 - request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b59a0391b-20130401_132324
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* ack
 - offer_detailed
* ack
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b59a0391b-20130401_134901
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b59a0391b-20130401_134053
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b20b6e847a-20130326_222313
* inform{"food": "gastropub", "area": "dontcare"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b20b6e847a-20130326_222030
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b20b6e847a-20130326_222936
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b20b6e847a-20130326_224116
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "north"}
 - confirm-domain
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b20b6e847a-20130326_222829
* inform{"food": "japanese", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-199d62165b-20130402_123401
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-199d62165b-20130402_122050
* inform{"food": "russian"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - expl-conf
* affirm
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-199d62165b-20130402_122711
* inform{"area": "centre"}
 - request_food
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-199d62165b-20130402_123507
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-199d62165b-20130402_115733
* inform{"pricerange": "moderate"}
 - request_area
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-199d62165b-20130402_120922
* inform{"food": "korean", "area": "centre"}
 - expl-conf
* include_filter{"food": "korean"}
 - expl-conf
* inform{"food": "korean", "area": "centre"}
 - canthelp
* inform{"food": "korean", "pricerange": "dontcare", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-199d62165b-20130402_121352
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-199d62165b-20130402_120456
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-199d62165b-20130402_122354
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-199d62165b-20130402_122214
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-199d62165b-20130402_121601
* inform{"area": "west"}
 - request_food
* inform{"food": "turkish"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-199d62165b-20130402_115850
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3860c915c2-20130328_164046
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3860c915c2-20130328_164431
* inform{"food": "corsica", "pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* reqalts
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22c938c8ba-20130325_134402
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform_dontcare
 - offer_detailed
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* negate
 - offer_detailed
* inform{"food": "chinese"}
 - canthelp
* inform{"area": "north"}
 - canthelp
* reqalts
 - canthelp
* inform{"pricerange": "cheap", "area": "north"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform_dontcare
 - canthelp
* inform_dontcare
 - canthelp
* bye
 - bye

## Mar13_S1A0/voip-22c938c8ba-20130325_130740
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-22c938c8ba-20130325_123407
* inform{"food": "british", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* thankyou
 - canthelp
* inform{"food": "indian"}
 - canthelp
* thankyou
 - canthelp
* ack
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-22c938c8ba-20130325_130445
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* inform_dontcare
 - offer_detailed
* inform_dontcare
 - offer_detailed
* bye
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-22c938c8ba-20130325_134206
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-22c938c8ba-20130325_142552
* inform{"food": "afghan"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "afghan"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform_dontcare
 - offer_detailed
* inform_dontcare
 - offer_detailed
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* bye
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* bye
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-22c938c8ba-20130325_143621
* inform{"food": "european", "pricerange": "cheap"}
 - canthelp
* inform{"food": "european", "pricerange": "expensive"}
 - select
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_area": "True"}
 - offer
* inform{"area": "north"}
 - offer
* inform{"area": "south"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22c938c8ba-20130325_125039
* inform{"food": "asian oriental"}
 - request_food
* inform{"food": "asian oriental"}
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22c938c8ba-20130325_130208
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52d599db9c-20130327_175215
* thankyou
 - request_area
* inform{"food": "german"}
 - canthelp
* inform{"food": "french"}
 - request_area
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52d599db9c-20130402_001953
* inform{"food": "chinese", "area": "south"}
 - request_food
* inform{"food": "chinese"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52d599db9c-20130323_054632
* inform{"pricerange": "expensive", "area": "east"}
 - request_area
* inform{"area": "east"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52d599db9c-20130326_214515
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52d599db9c-20130326_213117
* inform{"area": "east"}
 - request_food
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-52d599db9c-20130326_214326
* inform{"area": "south"}
 - request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52d599db9c-20130326_212814
* inform{"food": "japanese", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52d599db9c-20130326_214615
* inform{"area": "north"}
 - request_food
* inform{"food": "catalan"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform{"food": "indian"}
 - request_pricerange
* affirm
 - request_pricerange
* inform{"food": "indian"}
 - request_pricerange
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52d599db9c-20130402_001838
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-52d599db9c-20130402_002245
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52d599db9c-20130325_135450
* inform{"food": "italian", "pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52d599db9c-20130328_154633
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52d599db9c-20130326_010952
* inform{"food": "mexican", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - select
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-52d599db9c-20130323_054736
* inform{"pricerange": "moderate"}
 - request_area
* request{"requested_pricerange": "True"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-52d599db9c-20130402_002522
* inform{"food": "crossover", "area": "west"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform{"food": "crossover"}
 - request_food
* inform{"food": "crossover"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52d599db9c-20130326_212959
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52d599db9c-20130402_000814
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52d599db9c-20130326_011106
* inform{"food": "vietnamese", "pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_141848
* inform_dontcare
 - offer_detailed
* inform{"food": "swedish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0fa32b1e78-20130328_234145
* inform{"pricerange": "moderate", "area": "north"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_151950
* inform{"area": "south"}
 - expl-conf
* negate
 - expl-conf
* negate
 - expl-conf
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_140213
* inform{"area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0fa32b1e78-20130401_151332
* inform_dontcare
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_234804
* inform{"area": "east"}
 - request_food
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0fa32b1e78-20130328_151140
* inform{"area": "south"}
 - request_pricerange
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_233916
* inform{"area": "east"}
 - request_food
* inform{"food": "turkish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130402_132031
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_233625
* inform{"food": "turkish"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0fa32b1e78-20130402_142351
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_233747
* inform{"food": "portuguese"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_142234
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130402_142022
* inform{"food": "austrian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_151336
* inform_dontcare
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "singaporean"}
 - offer_detailed
* inform{"food": "north american"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_235008
* inform{"area": "north"}
 - request_food
* inform{"food": "polish"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_153725
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0fa32b1e78-20130402_140846
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_152808
* inform{"food": "brazilian"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "brazilian"}
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_140739
* inform{"area": "west"}
 - request_food
* inform{"food": "polish"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0fa32b1e78-20130402_140356
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - select
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0fa32b1e78-20130402_141117
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-09733d9e4c-20130327_123942
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7e4cdce06a-20130323_130200
* inform{"area": "south"}
 - request_food
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e4cdce06a-20130323_131109
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7e4cdce06a-20130323_130824
* inform{"area": "west"}
 - request_food
* inform{"food": "international"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e4cdce06a-20130323_130520
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-edb8609855-20130327_183456
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-edb8609855-20130327_183200
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-edb8609855-20130327_183323
* inform{"food": "danish"}
 - canthelp
* inform{"food": "chinese"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-edb8609855-20130327_183802
* inform{"area": "south"}
 - request_pricerange
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b6618de447-20130328_152114
* inform{"pricerange": "moderate", "area": "east"}
 - expl-conf
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b6618de447-20130328_160617
* inform{"food": "vietnamese", "area": "south"}
 - canthelp
* inform{"food": "indian", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b6618de447-20130329_131207
* inform{"food": "jamaican", "pricerange": "cheap"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b6618de447-20130328_160419
* inform{"food": "traditional", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* confirm{"food": "spanish"}
 - offer_detailed
* inform{"food": "spanish", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b6618de447-20130326_211132
* inform{"area": "north"}
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b6618de447-20130328_160315
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b6618de447-20130326_211551
* inform{"area": "west"}
 - request_food
* inform{"food": "halal"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b6618de447-20130328_154703
* inform{"food": "greek", "pricerange": "expensive"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b6618de447-20130328_160810
* inform{"food": "basque", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b6618de447-20130328_151251
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b6618de447-20130328_155353
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b6618de447-20130328_151535
* include_filter{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "french", "pricerange": "expensive"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b6618de447-20130328_154027
* inform{"food": "vietnamese", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b6618de447-20130325_145518
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b6618de447-20130328_152908
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b6618de447-20130328_155531
* inform{"food": "hungarian", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "hungarian"}
 - expl-conf
* negate
 - offer_detailed
* confirm{"food": "hungarian"}
 - offer_detailed
* inform{"food": "hungarian", "pricerange": "expensive"}
 - offer_detailed
* confirm{"food": "hungarian"}
 - offer_detailed
* inform{"food": "british"}
 - offer
* inform{"pricerange": "expensive"}
 - select
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b6618de447-20130328_153612
* inform{"food": "belgian", "area": "centre"}
 - canthelp
* inform{"food": "korean", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b6618de447-20130328_153132
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2d3d74d091-20130328_134757
* inform{"food": "belgian"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "malaysian"}
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - canthelp
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* bye
 - bye

## Mar13_S0A1/voip-2d3d74d091-20130401_235307
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d3d74d091-20130328_143735
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "world"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2d3d74d091-20130328_191642
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d3d74d091-20130328_135311
* affirm
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d3d74d091-20130328_135137
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "european"}
 - canthelp
* inform{"area": "centre"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d3d74d091-20130328_140026
* inform{"area": "north"}
 - request_food
* inform{"food": "indian"}
 - request_food
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* bye
 - bye

## Mar13_S1A1/voip-2d3d74d091-20130401_234343
* inform_dontcare
 - request_food
* inform{"food": "korean"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2d3d74d091-20130328_153522
* inform{"area": "west"}
 - select
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d3d74d091-20130401_234151
* inform{"pricerange": "expensive"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_food
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2d3d74d091-20130328_144241
* inform{"area": "centre"}
 - request_area
* inform{"area": "centre"}
 - offer
* inform{"food": "italian"}
 - offer
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2d3d74d091-20130325_224245
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fe60dae302-20130328_191353
* inform{"food": "polynesian"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-fe60dae302-20130328_192329
* inform{"area": "south"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - offer_detailed
* bye
 - canthelp
* bye
 - canthelp
* inform{"area": "east"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* bye
 - canthelp
* bye
 - canthelp
* bye
 - bye

## Mar13_S1A0/voip-4c25da9a27-20130327_141855
* inform{"food": "african"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c25da9a27-20130327_135709
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4c25da9a27-20130325_184604
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "north american"}
 - expl-conf
* negate
 - expl-conf
* negate
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* reqalts
 - canthelp
* inform{"food": "north american"}
 - expl-conf
* bye
 - bye

## Mar13_S0A1/voip-4c25da9a27-20130325_182216
* inform{"food": "mediterranean"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4c25da9a27-20130327_140750
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S0A0/voip-4c25da9a27-20130325_183726
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4c25da9a27-20130325_183445
* inform{"food": "moroccan", "area": "south"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* confirm{"food": "modern european"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "european"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c25da9a27-20130327_141034
* inform{"food": "australasian"}
 - offer_detailed
* inform{"food": "australasian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* confirm{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c25da9a27-20130327_140554
* inform{"pricerange": "moderate"}
 - offer_detailed
* confirm{"food": "gastropub"}
 - offer_detailed
* confirm{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4c25da9a27-20130327_140246
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c25da9a27-20130325_184738
* inform{"area": "dontcare"}
 - offer
* confirm{"food": "christmas"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4c25da9a27-20130327_141556
* inform{"food": "cuban", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* confirm{"food": "chinese"}
 - confirm-domain
* include_filter{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4c25da9a27-20130325_181340
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4c25da9a27-20130325_181011
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4c25da9a27-20130327_140126
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4c25da9a27-20130325_183247
* inform{"food": "mediterranean", "pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4c25da9a27-20130327_140438
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4c25da9a27-20130325_181701
* inform{"food": "polynesian", "area": "north"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-317a1436fe-20130325_171203
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-317a1436fe-20130325_172154
* inform{"food": "turkish"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "turkish"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-317a1436fe-20130325_171718
* inform{"food": "jamaican", "pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "jamaican"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* deny{"food": "chinese"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "jamaican"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"food": "jamaican"}
 - offer
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S1A1/voip-317a1436fe-20130325_171321
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "basque"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "basque"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "basque"}
 - offer_detailed
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-317a1436fe-20130325_173537
* inform{"pricerange": "moderate"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - reqmore
* request{"requested_addr": "True"}
 - reqmore
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - reqmore
* negate
 - reqmore
* bye
 - bye

## Mar13_S0A1/voip-317a1436fe-20130325_174012
* inform{"food": "african", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - reqmore
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-317a1436fe-20130325_171950
* inform{"food": "traditional"}
 - request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-317a1436fe-20130325_173122
* inform{"pricerange": "expensive"}
 - request_food
* inform{"area": "south"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-88f198881b-20130326_032712
* inform{"food": "irish", "area": "centre"}
 - request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-88f198881b-20130326_014111
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-88f198881b-20130326_014812
* inform{"food": "steakhouse", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-88f198881b-20130326_032851
* inform{"area": "north"}
 - request_food
* inform{"food": "chinese"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0f41c16f2f-20130402_005145
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0f41c16f2f-20130325_213659
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "mediterranean"}
 - request_area
* inform{"area": "north"}
 - canthelp
* bye
 - bye

## Mar13_S1A0/voip-0f41c16f2f-20130401_235338
* inform{"pricerange": "moderate", "area": "east"}
 - select
* inform{"pricerange": "moderate"}
 - select
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0f41c16f2f-20130402_005015
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0f41c16f2f-20130325_213819
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0f41c16f2f-20130402_004841
* inform{"pricerange": "expensive"}
 - request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0f41c16f2f-20130325_213951
* inform{"food": "fusion"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0f41c16f2f-20130401_235748
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "north"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "fusion"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0f41c16f2f-20130401_235017
* inform{"food": "thai"}
 - request_area
* inform{"area": "centre"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0f41c16f2f-20130401_235542
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform{"food": "german"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0f41c16f2f-20130401_235916
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0f41c16f2f-20130402_000226
* inform{"pricerange": "cheap"}
 - expl-conf
* affirm
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0f41c16f2f-20130325_193614
* inform{"food": "seafood"}
 - request_area
* inform{"area": "south"}
 - offer
* bye
 - bye

## Mar13_S1A0/voip-0f41c16f2f-20130402_004415
* inform{"food": "international"}
 - request_area
* inform{"area": "dontcare"}
 - expl-conf
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0f41c16f2f-20130325_193856
* inform{"food": "italian"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - canthelp
* bye
 - bye

## Mar13_S0A1/voip-87de4f7a80-20130324_154621
* inform{"food": "basque", "area": "west"}
 - request_area
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* confirm{"food": "basque"}
 - offer_detailed
* confirm{"food": "basque"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-87de4f7a80-20130324_154113
* inform{"food": "indian", "pricerange": "moderate"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_area": "True"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* confirm{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-87de4f7a80-20130324_153705
* inform{"area": "west"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-87de4f7a80-20130324_155006
* inform{"food": "korean", "area": "centre"}
 - expl-conf
* include_filter{"food": "korean"}
 - offer_detailed
* confirm{"food": "korean"}
 - canthelp
* confirm{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-87de4f7a80-20130324_154807
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-202b6a3cc4-20130327_185502
* inform{"pricerange": "moderate"}
 - request_area
* request{"requested_pricerange": "True"}
 - offer
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-202b6a3cc4-20130327_185351
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-202b6a3cc4-20130327_184215
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - select
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-202b6a3cc4-20130327_184721
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ccf48b9a6a-20130329_042239
* inform{"area": "east"}
 - select
* inform{"area": "east"}
 - request_food
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ccf48b9a6a-20130329_041327
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform{"food": "italian"}
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* thankyou
 - offer_detailed
* thankyou
 - bye

## Mar13_S0A1/voip-ccf48b9a6a-20130329_053509
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ccf48b9a6a-20130329_052518
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "north american"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ccf48b9a6a-20130329_053241
* inform{"area": "centre"}
 - request_area
* inform{"area": "centre"}
 - request_food
* inform{"food": "world"}
 - canthelp
* request{"requested_area": "True"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "european"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ccf48b9a6a-20130329_053050
* inform{"food": "cantonese", "area": "west"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "italian"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ccf48b9a6a-20130329_041830
* inform{"food": "french"}
 - request_area
* inform{"area": "centre"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "french"}
 - request_food
* inform{"food": "french"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ccf48b9a6a-20130329_043420
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-15d8a89cec-20130327_021458
* inform{"food": "asian oriental", "area": "north"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-15d8a89cec-20130327_015041
* inform{"food": "australian", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-15d8a89cec-20130327_020255
* inform{"food": "international", "area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-15d8a89cec-20130327_020852
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - expl-conf
* negate
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-15d8a89cec-20130327_014753
* inform{"food": "brazilian", "pricerange": "moderate"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - canthelp
* inform{"food": "asian oriental"}
 - select
* bye
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-15d8a89cec-20130327_022535
* inform_dontcare
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-15d8a89cec-20130327_015432
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - reqmore
* query{"food": "mexican", "name": "chiquito restaurant bar", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-15d8a89cec-20130327_020057
* inform{"pricerange": "moderate", "area": "west"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* query{"name": "prezzo", "requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f1e8236264-20130323_002501
* inform{"pricerange": "moderate", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f1e8236264-20130323_003719
* inform{"food": "venetian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f1e8236264-20130323_003057
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f1e8236264-20130323_002130
* inform{"food": "lebanese", "pricerange": "cheap"}
 - request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f1e8236264-20130323_004330
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f1e8236264-20130323_002326
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f1e8236264-20130323_004442
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f1e8236264-20130323_005548
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f1e8236264-20130323_003523
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7c3a08072d-20130326_005842
* inform{"food": "english"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* confirm{"area": "centre"}
 - offer
* confirm{"area": "centre"}
 - offer_detailed
* inform{"food": "british", "area": "centre"}
 - expl-conf
* affirm
 - request_pricerange
* inform{"food": "british"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7c3a08072d-20130326_005512
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7c3a08072d-20130326_010113
* inform{"food": "gastropub"}
 - request_food
* inform{"food": "gastropub"}
 - offer
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7c3a08072d-20130326_005642
* inform{"food": "afghan"}
 - canthelp
* inform{"area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b08f15a787-20130402_072347
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "european"}
 - request_area
* inform_dontcare{"pricerange": "expensive"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b08f15a787-20130402_075759
* inform{"area": "west"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b08f15a787-20130326_021953
* inform{"pricerange": "moderate", "area": "north"}
 - select
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b08f15a787-20130402_071415
* inform{"food": "unusual"}
 - request_food
* inform{"food": "unusual"}
 - offer
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"food": "unusual"}
 - offer_detailed
* inform{"food": "unusual"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-b08f15a787-20130326_023412
* inform{"food": "german"}
 - canthelp
* inform{"food": "european"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b08f15a787-20130402_074900
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-b08f15a787-20130326_023936
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b08f15a787-20130402_075211
* inform{"food": "british"}
 - request_pricerange
* inform_dontcare{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b08f15a787-20130326_021438
* inform{"pricerange": "cheap"}
 - request_area
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b08f15a787-20130402_074726
* inform{"food": "european"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b08f15a787-20130402_072532
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare{"pricerange": "moderate"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b08f15a787-20130326_022327
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform_dontcare{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b08f15a787-20130402_072705
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-b08f15a787-20130402_065804
* inform_dontcare
 - offer_detailed
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-b08f15a787-20130402_070704
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-22756d9e8f-20130329_045435
* inform{"pricerange": "moderate"}
 - request_area
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-22756d9e8f-20130329_044955
* inform{"food": "african", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-22756d9e8f-20130329_043954
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22756d9e8f-20130329_045117
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-22756d9e8f-20130329_050412
* inform{"food": "swedish", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* confirm{"food": "korean"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-22756d9e8f-20130328_170312
* inform{"food": "canapes", "pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* confirm{"food": "canapes"}
 - offer
* inform{"pricerange": "moderate"}
 - offer
* confirm{"food": "canapes"}
 - offer
* inform{"food": "indian"}
 - offer
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian"}
 - expl-conf
* confirm{"pricerange": "moderate"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-22756d9e8f-20130329_044234
* inform{"area": "south"}
 - request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22756d9e8f-20130329_050743
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-22756d9e8f-20130329_050114
* inform{"area": "centre"}
 - request_food
* inform{"food": "romanian"}
 - request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* confirm{"food": "thai"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-22756d9e8f-20130329_044622
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22756d9e8f-20130329_050612
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22756d9e8f-20130329_044511
* inform{"area": "centre"}
 - request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-22756d9e8f-20130329_043814
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "persian"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0999e9bb30-20130325_124910
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform{"food": "scottish"}
 - request_food
* inform{"food": "north american"}
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0999e9bb30-20130325_124715
* inform{"area": "dontcare"}
 - offer
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-dda7c88c6e-20130323_052950
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dda7c88c6e-20130323_055048
* inform{"pricerange": "expensive"}
 - request_food
* request{"requested_area": "True"}
 - request_food
* inform{"food": "eritrean"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-dda7c88c6e-20130323_053057
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - canthelp
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-dda7c88c6e-20130323_053928
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9735278861-20130401_153620
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9735278861-20130401_160849
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9735278861-20130401_154740
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9735278861-20130401_161036
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9735278861-20130401_161717
* inform{"food": "lebanese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9735278861-20130401_151648
* inform{"area": "south"}
 - request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "chinese"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9735278861-20130401_161215
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-9735278861-20130401_154605
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9735278861-20130402_140608
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9735278861-20130401_155528
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-9735278861-20130401_154251
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9735278861-20130401_152826
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-9735278861-20130401_160600
* inform{"food": "english"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e22911804-20130327_200922
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e22911804-20130324_184015
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7e22911804-20130324_193050
* negate
 - request_area
* inform{"food": "indonesian", "area": "north"}
 - expl-conf
* correct{"area": "north"}
 - expl-conf
* include_filter{"area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-7e22911804-20130326_142538
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* confirm{"food": "chinese"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7e22911804-20130324_173542
* inform{"food": "greek"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7e22911804-20130328_164203
* inform{"food": "swedish", "pricerange": "cheap"}
 - offer_detailed
* confirm{"food": "swedish"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* confirm{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e22911804-20130325_202948
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7e22911804-20130324_184843
* inform{"food": "brazilian"}
 - request_area
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S0A0/voip-7e22911804-20130328_162243
* inform{"pricerange": "cheap", "area": "south"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - request_food
* thankyou
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* correct{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e22911804-20130328_162140
* inform{"food": "lebanese", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7e22911804-20130327_202516
* inform{"food": "thai", "area": "centre"}
 - request_food
* inform{"food": "thai"}
 - offer
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* negate
 - offer
* negate
 - offer
* inform{"food": "thai"}
 - offer_detailed
* include_filter{"food": "thai"}
 - offer_detailed
* confirm{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-7e22911804-20130328_204851
* inform{"pricerange": "cheap", "area": "east"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer
* confirm{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e22911804-20130328_161325
* inform{"area": "west"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - request_pricerange
* inform_dontcare
 - offer
* confirm{"area": "west"}
 - offer_detailed
* inform{"food": "thai", "area": "west"}
 - offer_detailed
* confirm{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-7e22911804-20130328_204150
* inform_dontcare{"food": "traditional"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french"}
 - expl-conf
* include_filter{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e22911804-20130328_162643
* inform{"pricerange": "expensive", "area": "east"}
 - request_area
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-7e22911804-20130324_190421
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e22911804-20130325_200320
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e22911804-20130328_203706
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* negate
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-7e22911804-20130328_204351
* affirm
 - request_pricerange
* inform{"pricerange": "cheap", "area": "north"}
 - confirm-domain
* affirm
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-876ef67873-20130402_032159
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "african"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-876ef67873-20130327_035756
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-876ef67873-20130402_030352
* inform{"area": "east"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-876ef67873-20130327_040247
* inform{"pricerange": "moderate"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-876ef67873-20130327_035558
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-876ef67873-20130327_035101
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "singaporean"}
 - offer_detailed
* inform{"food": "singaporean"}
 - offer_detailed
* inform{"food": "european"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - canthelp
* bye
 - bye

## Mar13_S1A1/voip-876ef67873-20130402_031718
* affirm
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "danish"}
 - canthelp
* inform{"food": "mediterranean"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-876ef67873-20130402_033525
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-876ef67873-20130402_033954
* inform{"area": "west"}
 - request_food
* inform{"food": "thai"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A1/voip-876ef67873-20130402_030744
* inform{"food": "world", "pricerange": "moderate"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d225fad9df-20130328_201024
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d225fad9df-20130328_183716
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "italian"}
 - canthelp
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "dontcare", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d225fad9df-20130328_200758
* inform{"area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d225fad9df-20130328_205512
* inform{"pricerange": "expensive"}
 - request_food
* inform{"area": "south"}
 - request_food
* inform{"food": "north american"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"area": "south"}
 - canthelp
* inform{"pricerange": "expensive", "area": "south"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d225fad9df-20130328_205817
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d225fad9df-20130328_175010
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d225fad9df-20130328_201303
* inform{"food": "english", "area": "west"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d225fad9df-20130328_183352
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d225fad9df-20130328_175805
* inform{"food": "moroccan", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d225fad9df-20130328_203254
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d225fad9df-20130328_175224
* inform{"food": "german"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31d9d1a567-20130402_042843
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-31d9d1a567-20130402_035757
* inform{"food": "korean", "pricerange": "dontcare"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-31d9d1a567-20130402_042614
* inform{"area": "north"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31d9d1a567-20130402_041025
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31d9d1a567-20130402_035524
* inform{"food": "belgian", "area": "north"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-31d9d1a567-20130402_041209
* inform{"pricerange": "moderate"}
 - request_food
* inform{"area": "north"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-31d9d1a567-20130402_040402
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-31d9d1a567-20130402_035950
* inform{"food": "canapes", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-31d9d1a567-20130402_034546
* inform{"pricerange": "moderate", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-31d9d1a567-20130402_042138
* inform{"food": "turkish", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31d9d1a567-20130402_034915
* inform{"food": "gastropub", "pricerange": "dontcare"}
 - expl-conf
* include_filter{"food": "gastropub"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-31d9d1a567-20130402_034022
* inform{"food": "tuscan", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian", "pricerange": "cheap"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a31ca3e355-20130324_190654
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "swiss"}
 - offer
* inform{"food": "swiss"}
 - offer
* inform{"food": "british"}
 - offer
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a31ca3e355-20130323_223152
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - reqmore
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a31ca3e355-20130323_223338
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a31ca3e355-20130323_222931
* inform{"area": "east"}
 - request_food
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* inform{"food": "scandinavian"}
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - canthelp
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - canthelp
* request{"requested_phone": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a31ca3e355-20130324_190831
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a31ca3e355-20130323_223643
* inform{"food": "international"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-a31ca3e355-20130323_234926
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - canthelp
* bye
 - bye

## Mar13_S0A0/voip-3b3edac94d-20130326_004101
* inform{"food": "german", "area": "centre"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b3edac94d-20130326_003522
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b3edac94d-20130326_004002
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b3edac94d-20130324_211737
* inform{"food": "caribbean", "pricerange": "cheap"}
 - offer_detailed
* confirm{"food": "caribbean"}
 - offer_detailed
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b3edac94d-20130324_201732
* inform{"food": "french", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b3edac94d-20130323_203121
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b3edac94d-20130324_202932
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b3edac94d-20130323_201535
* inform{"pricerange": "moderate", "area": "north"}
 - expl-conf
* affirm
 - request_food
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b3edac94d-20130323_202936
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b3edac94d-20130324_210908
* inform{"food": "austrian", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b3edac94d-20130324_203209
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b3edac94d-20130324_211848
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b3edac94d-20130326_004204
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b3edac94d-20130323_202743
* inform{"food": "french"}
 - offer_detailed
* reqalts
 - confirm-domain
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b3edac94d-20130324_202415
* inform{"food": "jamaican", "area": "south"}
 - request_food
* inform{"food": "jamaican"}
 - request_food
* inform{"food": "jamaican"}
 - select
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese", "area": "south"}
 - canthelp
* inform{"food": "chinese", "area": "south"}
 - select
* correct{"food": "chinese"}
 - select
* inform{"food": "chinese"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b3edac94d-20130324_202802
* inform{"food": "swiss", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b3edac94d-20130326_004303
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b3edac94d-20130323_203738
* inform{"food": "mediterranean", "area": "dontcare"}
 - request_food
* inform{"food": "mediterranean"}
 - offer_detailed
* confirm{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a352cb5ca5-20130401_234557
* inform{"pricerange": "moderate"}
 - offer
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a352cb5ca5-20130401_232817
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a352cb5ca5-20130401_234753
* inform{"area": "centre"}
 - request_pricerange
* inform{"area": "centre"}
 - request_pricerange
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a352cb5ca5-20130401_231740
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a352cb5ca5-20130401_234216
* inform_dontcare
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "barbeque"}
 - request_food
* inform{"food": "barbeque"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a352cb5ca5-20130401_234944
* inform{"food": "singaporean"}
 - offer_detailed
* inform{"food": "singaporean"}
 - offer_detailed
* inform{"area": "south"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a352cb5ca5-20130401_231236
* inform{"area": "west"}
 - request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8f9fb7a86b-20130328_183857
* inform{"food": "tuscan", "area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "tuscan"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-8f9fb7a86b-20130328_185140
* inform{"food": "scandinavian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8f9fb7a86b-20130328_182235
* inform{"pricerange": "moderate"}
 - request_area
* inform{"food": "moroccan"}
 - request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-8f9fb7a86b-20130328_184241
* inform{"food": "japanese", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8f9fb7a86b-20130328_184820
* inform{"food": "portuguese", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "portuguese"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-8f9fb7a86b-20130328_182710
* inform{"food": "danish", "area": "south"}
 - expl-conf
* include_filter{"area": "south"}
 - canthelp
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A1/voip-8f9fb7a86b-20130328_184504
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-8f9fb7a86b-20130328_181534
* inform{"area": "west"}
 - request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "thai"}
 - select
* inform{"food": "thai"}
 - select
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* inform{"name": "prezzo"}
 - select
* inform{"food": "creative"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"name": "prezzo"}
 - canthelp
* request{"requested_name": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* ack
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A0/voip-155e939ebc-20130327_203952
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-155e939ebc-20130327_204114
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-155e939ebc-20130327_202425
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-155e939ebc-20130327_203006
* inform{"area": "east"}
 - request_food
* inform{"food": "european"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-155e939ebc-20130327_203543
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-155e939ebc-20130327_211511
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-155e939ebc-20130327_203128
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-00d76b791d-20130327_011740
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-00d76b791d-20130327_005023
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "modern european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* bye
 - bye

## Mar13_S1A0/voip-00d76b791d-20130327_004513
* inform{"food": "creative", "pricerange": "moderate"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-00d76b791d-20130327_012807
* inform{"food": "venetian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-00d76b791d-20130327_012331
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-00d76b791d-20130327_010416
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-00d76b791d-20130327_010906
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-00d76b791d-20130327_011609
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-00d76b791d-20130327_012711
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-00d76b791d-20130327_011116
* inform{"food": "lebanese", "area": "west"}
 - request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - reqmore
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-00d76b791d-20130327_003853
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0abf414c0c-20130327_000359
* inform{"food": "gastropub"}
 - request_food
* inform{"food": "gastropub"}
 - offer
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0abf414c0c-20130326_235444
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0abf414c0c-20130326_235059
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_addr": "True"}
 - reqmore
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - reqmore
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4b7e22cc07-20130401_185110
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4b7e22cc07-20130401_185640
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "crossover"}
 - request_food
* inform{"food": "crossover"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - expl-conf
* inform{"food": "modern european"}
 - select
* inform{"food": "modern european"}
 - select
* inform{"food": "modern european"}
 - select
* inform{"food": "european"}
 - select
* inform{"food": "modern european"}
 - select
* inform{"food": "modern european"}
 - select
* bye
 - expl-conf
* negate
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "modern european"}
 - expl-conf
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f32f2cfdae-20130327_013132
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - expl-conf
* affirm
 - request_area
* inform{"area": "dontcare"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f32f2cfdae-20130328_195839
* inform{"food": "eritrean", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f32f2cfdae-20130327_013402
* inform{"food": "african"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f32f2cfdae-20130327_015652
* inform{"food": "catalan", "pricerange": "cheap"}
 - request_food
* inform{"food": "catalan"}
 - request_food
* inform{"food": "catalan"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f32f2cfdae-20130328_195220
* inform{"area": "centre"}
 - offer_detailed
* inform{"food": "romanian"}
 - offer_detailed
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f32f2cfdae-20130327_020400
* inform{"food": "caribbean", "area": "south"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_192506
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f32f2cfdae-20130328_193321
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* inform{"food": "gastropub"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f32f2cfdae-20130327_012823
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f32f2cfdae-20130328_195409
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f32f2cfdae-20130328_192703
* inform{"food": "chinese"}
 - request_area
* inform{"food": "seafood"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "seafood"}
 - request_food
* inform{"food": "seafood"}
 - offer_detailed
* inform{"food": "seafood"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f32f2cfdae-20130327_015332
* inform{"food": "polish"}
 - confirm-domain
* affirm
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f32f2cfdae-20130328_194348
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f32f2cfdae-20130328_200054
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_200431
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* inform{"food": "portuguese", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f32f2cfdae-20130328_194814
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_194522
* inform{"food": "japanese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f32f2cfdae-20130327_015213
* inform{"food": "crossover", "area": "north"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f32f2cfdae-20130327_014628
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f32f2cfdae-20130328_193841
* bye
 - request_area
* inform{"food": "turkish"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "turkish"}
 - offer
* inform{"food": "turkish"}
 - offer_detailed
* inform{"food": "turkish"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f32f2cfdae-20130327_014457
* inform{"food": "english", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_193606
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f32f2cfdae-20130327_013713
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-381a50592b-20130326_035922
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-381a50592b-20130326_040146
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-381a50592b-20130323_234808
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-381a50592b-20130324_000124
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - offer
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-381a50592b-20130324_000330
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-381a50592b-20130323_233220
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "seafood"}
 - offer_detailed
* inform{"food": "seafood"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-381a50592b-20130326_043646
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-381a50592b-20130323_233439
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-381a50592b-20130326_040928
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-381a50592b-20130326_040539
* inform{"food": "danish"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-381a50592b-20130326_043059
* inform{"area": "north"}
 - request_food
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-381a50592b-20130326_044413
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform{"food": "cuban"}
 - request_food
* inform{"food": "cuban"}
 - request_food
* inform{"food": "cuban"}
 - request_food
* inform{"food": "cuban"}
 - expl-conf
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-381a50592b-20130326_044146
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-381a50592b-20130326_043457
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-381a50592b-20130323_234249
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-381a50592b-20130323_235612
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-381a50592b-20130326_040051
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-381a50592b-20130323_234506
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-381a50592b-20130326_041040
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - request_area
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-381a50592b-20130326_041932
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - canthelp
* request{"requested_phone": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-922209b777-20130325_160523
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-922209b777-20130325_162603
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-922209b777-20130327_004402
* inform{"area": "west"}
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-922209b777-20130325_163924
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-922209b777-20130325_162222
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-922209b777-20130325_160004
* inform{"food": "canapes", "area": "west"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-922209b777-20130327_012955
* inform{"food": "seafood", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-922209b777-20130327_013531
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-922209b777-20130327_004226
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-922209b777-20130327_011149
* inform{"food": "thai", "pricerange": "moderate"}
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-922209b777-20130325_160141
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-922209b777-20130325_155209
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-922209b777-20130327_011354
* inform{"area": "east"}
 - offer
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-922209b777-20130327_005342
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-922209b777-20130325_161023
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-922209b777-20130327_011455
* inform{"food": "european", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-922209b777-20130325_162946
* inform{"food": "international", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-922209b777-20130325_162423
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-922209b777-20130327_012258
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - request_area
* inform{"food": "thai"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - canthelp
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S0A0/voip-922209b777-20130326_140616
* inform{"food": "gastropub", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ccc459b689-20130327_002730
* inform{"area": "north"}
 - confirm-domain
* affirm
 - offer
* inform{"area": "north"}
 - offer_detailed
* inform{"food": "japanese", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ccc459b689-20130327_004851
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ccc459b689-20130327_004727
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ccc459b689-20130327_004458
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* confirm{"food": "european"}
 - offer_detailed
* confirm{"food": "european"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ccc459b689-20130327_004041
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "modern european"}
 - expl-conf
* affirm
 - select
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bde2721237-20130326_200257
* inform{"pricerange": "expensive", "area": "south"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bde2721237-20130325_162942
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bde2721237-20130326_194753
* inform{"food": "moroccan"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "moroccan"}
 - request_food
* inform{"food": "moroccan"}
 - request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bde2721237-20130326_194022
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bde2721237-20130326_193127
* inform{"food": "irish", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bde2721237-20130325_164032
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bde2721237-20130326_193025
* inform{"food": "world"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bde2721237-20130326_192751
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bde2721237-20130325_154829
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bde2721237-20130326_200505
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bde2721237-20130325_161826
* inform{"food": "french", "area": "centre"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bde2721237-20130325_162740
* inform{"food": "belgian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - request_area
* inform{"area": "north"}
 - canthelp
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bde2721237-20130325_162622
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bde2721237-20130325_155806
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bde2721237-20130326_195337
* inform{"food": "gastropub"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bde2721237-20130326_193743
* inform{"pricerange": "expensive"}
 - request_food
* inform{"food": "english"}
 - canthelp
* inform{"food": "italian"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bde2721237-20130326_195733
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bde2721237-20130325_155143
* inform{"area": "south"}
 - request_food
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "mexican"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-78f497f314-20130323_184557
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-78f497f314-20130324_202309
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-78f497f314-20130323_184435
* inform{"area": "dontcare"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-78f497f314-20130324_201554
* inform{"food": "creative", "pricerange": "cheap"}
 - canthelp
* inform{"food": "creative"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - select
* inform{"food": "mediterranean"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-78f497f314-20130324_201211
* inform{"food": "persian", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-78f497f314-20130324_200748
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-78f497f314-20130324_203101
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-78f497f314-20130323_143533
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-78f497f314-20130323_184250
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-78f497f314-20130324_200619
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* correct{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-78f497f314-20130323_184110
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-78f497f314-20130323_144139
* inform{"pricerange": "moderate"}
 - offer_detailed
* confirm{"food": "indonesian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-78f497f314-20130323_142856
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A0/voip-88b68a9a41-20130322_221424
* inform{"food": "canapes", "area": "dontcare"}
 - request_food
* inform{"food": "canapes"}
 - request_food
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "modern european"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-88b68a9a41-20130323_114000
* inform{"area": "north"}
 - request_food
* inform{"food": "turkish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-88b68a9a41-20130322_223613
* inform{"food": "australian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-88b68a9a41-20130324_002417
* inform{"food": "mediterranean", "area": "centre"}
 - canthelp
* inform{"food": "mediterranean", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-88b68a9a41-20130324_004148
* inform{"food": "cuban", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-88b68a9a41-20130324_004748
* inform{"food": "traditional", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-88b68a9a41-20130324_004031
* inform{"food": "cuban", "area": "south"}
 - request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-88b68a9a41-20130322_221603
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-88b68a9a41-20130322_221256
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - confirm-domain
* affirm
 - offer_detailed
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-88b68a9a41-20130322_222845
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-88b68a9a41-20130324_002917
* inform{"area": "west"}
 - request_food
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-88b68a9a41-20130322_224608
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-88b68a9a41-20130324_003144
* inform{"food": "japanese", "area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "japanese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-88b68a9a41-20130324_002132
* inform{"food": "danish", "area": "west"}
 - canthelp
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-88b68a9a41-20130322_222725
* inform{"area": "north"}
 - request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-88b68a9a41-20130324_004639
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-88b68a9a41-20130324_003412
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-88b68a9a41-20130324_002251
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-88b68a9a41-20130322_224115
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-88b68a9a41-20130324_003525
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-88b68a9a41-20130322_222344
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - select
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bb1fd497eb-20130325_165023
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bb1fd497eb-20130325_131052
* inform{"food": "turkish", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_232136
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bb1fd497eb-20130326_230444
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bb1fd497eb-20130325_132300
* inform{"food": "hungarian", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bb1fd497eb-20130326_232439
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bb1fd497eb-20130325_164823
* inform{"pricerange": "moderate"}
 - request_area
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bb1fd497eb-20130326_120755
* inform{"food": "vegetarian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bb1fd497eb-20130325_123757
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_233411
* inform{"area": "dontcare"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bb1fd497eb-20130325_163241
* inform{"food": "malaysian", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bb1fd497eb-20130325_164128
* inform{"food": "african"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bb1fd497eb-20130325_163635
* inform{"food": "basque", "area": "east"}
 - request_food
* inform{"food": "basque"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_223048
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_230746
* inform{"food": "spanish", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - confirm-domain
* affirm
 - offer_detailed
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - bye

## Mar13_S0A0/voip-bb1fd497eb-20130326_231219
* inform{"food": "seafood"}
 - request_food
* inform{"food": "seafood"}
 - offer
* request{"requested_pricerange": "True"}
 - offer
* inform{"food": "seafood"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-bb1fd497eb-20130325_164421
* inform{"food": "brazilian"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bb1fd497eb-20130326_233115
* inform{"food": "venetian"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "venetian"}
 - request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-bb1fd497eb-20130326_231928
* inform{"area": "north"}
 - request_food
* inform{"food": "british"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* affirm
 - request_pricerange
* inform{"area": "north"}
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-bb1fd497eb-20130326_230547
* inform{"food": "corsica", "area": "west"}
 - request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - select
* inform{"food": "thai"}
 - offer_detailed
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-bb1fd497eb-20130325_163956
* inform{"food": "vietnamese"}
 - confirm-domain
* affirm
 - offer
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - reqmore
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03c2655d43-20130327_194746
* inform{"food": "international", "pricerange": "moderate"}
 - offer_detailed
* reqalts
 - confirm-domain
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03c2655d43-20130327_195421
* inform{"food": "basque", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - confirm-domain
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03c2655d43-20130327_195546
* inform{"food": "creative", "area": "west"}
 - expl-conf
* include_filter{"food": "creative"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* include_filter{"area": "west"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* bye
 - bye

## Mar13_S0A0/voip-03c2655d43-20130327_193309
* inform{"food": "persian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03c2655d43-20130327_201323
* inform{"food": "seafood"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03c2655d43-20130327_193528
* inform{"food": "welsh", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - expl-conf
* inform{"food": "british"}
 - request_area
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03c2655d43-20130327_194221
* inform{"food": "international", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03c2655d43-20130327_191742
* inform{"food": "european", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* thankyou
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03c2655d43-20130327_200522
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03c2655d43-20130327_194616
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03c2655d43-20130327_192312
* inform{"area": "west"}
 - request_food
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03c2655d43-20130327_200023
* inform{"food": "chinese", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03c2655d43-20130327_195308
* inform{"area": "north"}
 - request_area
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d0341706f2-20130329_022056
* inform{"food": "italian", "area": "west"}
 - request_area
* inform{"area": "west"}
 - request_pricerange
* negate
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d0341706f2-20130329_053021
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d0341706f2-20130329_012808
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d0341706f2-20130329_052240
* inform{"food": "afghan", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* inform{"area": "east"}
 - select
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d0341706f2-20130329_021540
* query{"pricerange": "moderate", "area": "south", "requested_addr": "True"}
 - request_food_detailed
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d0341706f2-20130329_021425
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d0341706f2-20130329_052605
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d0341706f2-20130329_051653
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d0341706f2-20130329_052031
* inform{"food": "bistro", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d0341706f2-20130329_021901
* inform{"pricerange": "cheap", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b81cbb287-20130324_215534
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b81cbb287-20130324_015653
* inform{"food": "world"}
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b81cbb287-20130326_030605
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b81cbb287-20130326_030827
* inform{"food": "african", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b81cbb287-20130326_031714
* inform{"food": "world"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai", "pricerange": "dontcare"}
 - expl-conf
* inform{"food": "thai"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b81cbb287-20130324_020817
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b81cbb287-20130324_014336
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b81cbb287-20130324_020125
* inform{"food": "basque", "pricerange": "expensive"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b81cbb287-20130326_024829
* inform{"food": "thai", "area": "centre"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b81cbb287-20130324_014713
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b81cbb287-20130326_025919
* inform{"food": "malaysian", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* confirm{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b81cbb287-20130324_020944
* inform{"food": "international", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b81cbb287-20130326_024219
* inform{"food": "basque", "pricerange": "moderate"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b81cbb287-20130326_025552
* inform{"food": "japanese", "pricerange": "moderate"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* inform{"food": "european", "pricerange": "moderate"}
 - select
* affirm
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "modern european"}
 - request_area
* inform_dontcare
 - expl-conf
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "modern european"}
 - expl-conf
* confirm{"pricerange": "moderate"}
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3b81cbb287-20130326_031529
* inform{"food": "danish", "area": "centre"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3b81cbb287-20130324_022110
* inform{"food": "french"}
 - offer_detailed
* query{"pricerange": "dontcare", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b81cbb287-20130324_021600
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3b81cbb287-20130324_014857
* inform{"food": "traditional", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3b81cbb287-20130324_015234
* inform{"food": "scottish", "area": "west"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "scottish"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* confirm{"food": "indian"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3be3bda933-20130326_132152
* inform{"food": "french", "pricerange": "moderate"}
 - request_food
* inform{"food": "french"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - request_area_detailed
* inform_dontcare
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3be3bda933-20130326_125503
* inform{"pricerange": "moderate", "area": "west"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3be3bda933-20130326_131833
* inform{"pricerange": "moderate", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "west"}
 - offer
* inform{"area": "west"}
 - offer
* inform_dontcare
 - offer_detailed
* inform{"area": "east"}
 - select
* inform{"area": "south"}
 - select
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-3be3bda933-20130327_014120
* inform{"pricerange": "expensive", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform_dontcare
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* reqalts
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* inform{"area": "west"}
 - expl-conf
* inform{"area": "west"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer
* inform_dontcare
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3be3bda933-20130327_015627
* inform{"food": "french", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "french"}
 - canthelp
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-3be3bda933-20130327_014928
* inform{"food": "international", "area": "east"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-3be3bda933-20130326_131651
* inform{"pricerange": "cheap", "area": "north"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-3be3bda933-20130326_125353
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130401_222446
* inform{"food": "english"}
 - canthelp
* inform{"food": "italian"}
 - request_area
* inform{"area": "south"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130401_221503
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-90732b027d-20130401_215559
* inform{"food": "italian"}
 - request_area
* inform{"area": "dontcare"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130401_194905
* inform{"area": "east"}
 - request_food
* inform{"pricerange": "moderate"}
 - request_food
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130401_195256
* inform{"area": "west"}
 - request_food
* inform{"food": "asian oriental"}
 - request_food
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-90732b027d-20130327_183400
* inform{"area": "east"}
 - offer
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-90732b027d-20130401_215804
* inform{"food": "seafood"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-90732b027d-20130327_190536
* inform{"pricerange": "dontcare"}
 - offer_detailed
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-90732b027d-20130327_174703
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "british"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-90732b027d-20130401_222250
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-90732b027d-20130327_180737
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "portuguese"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-90732b027d-20130327_181557
* inform{"food": "greek"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-90732b027d-20130327_181126
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-90732b027d-20130401_215925
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "modern european"}
 - request_area
* inform{"area": "dontcare"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130327_170938
* inform{"food": "danish", "area": "west"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130401_220530
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130327_184229
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* negate
 - expl-conf
* negate
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* inform{"pricerange": "dontcare"}
 - expl-conf
* negate
 - expl-conf
* negate
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-90732b027d-20130328_164236
* inform{"food": "tuscan"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "thai"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-90732b027d-20130401_222034
* inform{"food": "mexican"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-90732b027d-20130327_190004
* inform{"food": "greek"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* inform{"area": "centre"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-90732b027d-20130401_195651
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-90732b027d-20130327_190315
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer
* inform{"pricerange": "cheap"}
 - offer
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-90732b027d-20130401_221049
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-90732b027d-20130327_183925
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-90732b027d-20130327_173620
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "asian oriental"}
 - select
* inform{"food": "asian oriental"}
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f091d0e461-20130327_210252
* inform{"area": "east"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f091d0e461-20130327_211411
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f091d0e461-20130327_205009
* include_filter{"food": "kosher", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S0A1/voip-f091d0e461-20130327_210653
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f091d0e461-20130327_211146
* inform{"food": "lebanese"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f091d0e461-20130327_205249
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f091d0e461-20130327_210851
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* correct{"food": "asian oriental"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-340dbb333e-20130327_011501
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-340dbb333e-20130325_230536
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-340dbb333e-20130325_231720
* inform{"food": "turkish", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-340dbb333e-20130327_004847
* inform{"pricerange": "expensive"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer
* inform{"area": "south"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-340dbb333e-20130325_233510
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "mediterranean"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-340dbb333e-20130327_011550
* inform{"food": "indian", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-340dbb333e-20130325_231846
* inform{"pricerange": "cheap", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-340dbb333e-20130325_232333
* inform{"food": "eritrean", "area": "west"}
 - request_food
* inform{"food": "eritrean"}
 - request_food
* inform{"food": "italian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-340dbb333e-20130327_011403
* inform{"food": "international"}
 - request_food
* inform{"food": "international"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-340dbb333e-20130325_231614
* inform{"food": "african"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "african"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-340dbb333e-20130327_012037
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-340dbb333e-20130327_004741
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "british"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-340dbb333e-20130327_011703
* inform{"food": "canapes", "area": "north"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-340dbb333e-20130325_233348
* inform{"food": "japanese", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-340dbb333e-20130325_233821
* inform{"food": "indian", "pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-318851c80b-20130328_224338
* inform{"food": "basque"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "basque"}
 - canthelp
* inform{"food": "spanish"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-318851c80b-20130328_220608
* inform{"food": "greek"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-318851c80b-20130328_214947
* inform{"food": "european", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-318851c80b-20130328_214609
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-318851c80b-20130328_224511
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "canapes"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-318851c80b-20130328_224701
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-318851c80b-20130328_214057
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-318851c80b-20130328_220743
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-318851c80b-20130328_220341
* inform{"food": "hungarian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* negate
 - canthelp
* inform{"food": "modern european"}
 - expl-conf
* inform{"food": "modern european"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-36440f7305-20130326_201757
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "asian oriental"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-36440f7305-20130327_201555
* inform{"food": "thai"}
 - request_pricerange
* inform{"area": "west"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-36440f7305-20130326_140907
* inform{"food": "tuscan"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-36440f7305-20130327_200335
* inform{"food": "japanese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - reqmore
* request{"requested_phone": "True"}
 - reqmore
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - reqmore
* bye
 - reqmore
* bye
 - bye

## Mar13_S1A0/voip-36440f7305-20130327_200608
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-36440f7305-20130327_201745
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-36440f7305-20130327_195221
* inform{"food": "spanish", "area": "west"}
 - request_area
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "spanish"}
 - request_food
* inform{"food": "spanish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer
* thankyou
 - offer
* ack
 - offer
* bye
 - bye

## Mar13_S0A0/voip-36440f7305-20130326_141231
* inform{"food": "mexican"}
 - request_food
* inform{"food": "mexican"}
 - offer_detailed
* affirm
 - reqmore
* request{"requested_pricerange": "True", "requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-36440f7305-20130327_194928
* inform{"area": "south"}
 - request_food
* inform{"pricerange": "expensive"}
 - offer
* reqalts
 - offer
* reqalts
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* bye
 - bye

## Mar13_S0A1/voip-36440f7305-20130327_200102
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-36440f7305-20130326_200035
* inform{"food": "mexican"}
 - request_food
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-36440f7305-20130326_142415
* inform{"food": "kosher", "area": "centre"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-a8649977cf-20130323_161909
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "british"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a8649977cf-20130323_161257
* inform{"pricerange": "moderate"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "italian"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a8649977cf-20130323_155614
* inform{"food": "international", "area": "dontcare"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a8649977cf-20130323_160436
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-a8649977cf-20130323_155424
* inform{"pricerange": "cheap"}
 - request_food
* inform{"area": "north"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a8649977cf-20130323_160845
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a8649977cf-20130323_160201
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - confirm-domain
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a8649977cf-20130323_160311
* inform{"food": "mediterranean", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2f209793f4-20130326_005104
* inform{"food": "basque"}
 - canthelp
* inform{"food": "international"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2f209793f4-20130326_005217
* inform{"area": "east"}
 - request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "chinese", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2f209793f4-20130326_004451
* inform{"food": "european", "pricerange": "dontcare"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "european"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2f209793f4-20130326_004858
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2f209793f4-20130326_012033
* inform{"food": "hungarian", "pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2f209793f4-20130326_003256
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f17e3b578c-20130328_174844
* inform{"area": "north"}
 - request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f17e3b578c-20130328_173556
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f17e3b578c-20130328_171738
* affirm
 - request_area
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - request_food
* inform{"food": "british"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - canthelp
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* thankyou
 - offer
* ack
 - offer
* bye
 - bye

## Mar13_S0A1/voip-f17e3b578c-20130328_180105
* inform{"food": "cuban", "area": "dontcare"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f17e3b578c-20130328_174548
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A0/voip-f17e3b578c-20130328_174111
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f17e3b578c-20130328_173326
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "french"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_151857
* inform{"food": "german", "area": "north"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130328_125036
* inform{"food": "spanish", "area": "centre"}
 - select
* inform{"area": "centre"}
 - expl-conf
* include_filter{"food": "spanish"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130329_151950
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130328_124608
* inform{"food": "spanish"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer
* reqalts
 - offer
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130328_125150
* inform{"food": "basque"}
 - canthelp
* inform{"food": "spanish"}
 - select
* inform{"food": "spanish"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130328_121012
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130329_153643
* inform{"food": "lebanese", "area": "centre"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_151331
* inform{"food": "japanese", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130328_124458
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "french"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130329_153749
* inform{"pricerange": "moderate", "area": "north"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130328_121706
* inform{"food": "african", "area": "centre"}
 - canthelp
* inform{"food": "african"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130328_120337
* inform{"food": "spanish"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"food": "spanish"}
 - offer_detailed
* negate
 - offer_detailed
* reqalts
 - offer_detailed
* inform{"food": "spanish"}
 - offer_detailed
* negate
 - offer_detailed
* negate
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130328_124342
* inform{"food": "hungarian", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - request_pricerange
* inform_dontcare
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_124921
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "indian"}
 - confirm-domain
* include_filter{"food": "indian"}
 - request_pricerange
* inform_dontcare{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_154425
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_123700
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_153858
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130329_152505
* inform{"food": "christmas", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - request_area
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_120628
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_153244
* inform{"pricerange": "cheap", "area": "west"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130328_121528
* inform{"food": "creative", "area": "south"}
 - expl-conf
* include_filter{"area": "south"}
 - canthelp
* inform{"food": "chinese", "area": "south"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer
* confirm{"food": "chinese"}
 - offer_detailed
* inform{"food": "chinese"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_120903
* inform{"food": "gastropub", "area": "east"}
 - request_food
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130329_154219
* inform{"food": "russian", "pricerange": "moderate"}
 - offer_detailed
* inform{"food": "russian"}
 - canthelp
* inform{"food": "chinese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0241bbae39-20130327_201053
* inform_dontcare
 - request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "indian"}
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "cheap"}
 - expl-conf
* negate
 - expl-conf
* affirm
 - expl-conf
* negate
 - offer_detailed
* inform{"area": "south"}
 - expl-conf
* correct{"pricerange": "cheap"}
 - canthelp
* inform_dontcare
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* inform{"food": "indian"}
 - expl-conf
* affirm
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0241bbae39-20130327_193939
* inform{"area": "north"}
 - request_food
* inform{"food": "eritrean"}
 - canthelp
* inform{"food": "eritrean"}
 - canthelp
* inform{"food": "eritrean"}
 - offer_detailed
* inform{"food": "asian oriental", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0241bbae39-20130327_190942
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0241bbae39-20130327_204651
* inform{"pricerange": "cheap", "area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0241bbae39-20130327_191625
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare{"food": "vegetarian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian", "pricerange": "cheap"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0241bbae39-20130327_204233
* inform{"pricerange": "expensive"}
 - request_area
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0241bbae39-20130327_194703
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-afd3aa91f0-20130325_225729
* inform{"area": "centre"}
 - expl-conf
* inform{"food": "kosher"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-afd3aa91f0-20130327_190135
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-afd3aa91f0-20130327_185906
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-afd3aa91f0-20130325_224112
* inform{"food": "french", "pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-afd3aa91f0-20130325_230434
* inform{"pricerange": "moderate", "area": "south"}
 - confirm-domain
* affirm
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-afd3aa91f0-20130325_231946
* inform{"area": "west"}
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-afd3aa91f0-20130325_224706
* inform{"food": "european", "pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-afd3aa91f0-20130325_224842
* inform{"food": "japanese", "area": "dontcare"}
 - request_food
* inform{"food": "japanese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-afd3aa91f0-20130325_223728
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-afd3aa91f0-20130325_225303
* inform{"food": "french", "area": "south"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian", "area": "south"}
 - canthelp
* inform{"food": "indian", "area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-afd3aa91f0-20130327_190234
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-afd3aa91f0-20130326_015648
* inform{"area": "east"}
 - request_food
* inform{"food": "international"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-afd3aa91f0-20130325_224235
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-afd3aa91f0-20130326_015124
* inform{"food": "japanese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-afd3aa91f0-20130327_211102
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_food
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-cfd5fa34d9-20130402_073524
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-cfd5fa34d9-20130402_073021
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-cfd5fa34d9-20130402_073351
* inform{"pricerange": "cheap", "area": "west"}
 - expl-conf
* include_filter{"area": "west"}
 - request_food
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-cfd5fa34d9-20130402_072808
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "seafood"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-cfd5fa34d9-20130402_074254
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d6f8c4271e-20130326_221007
* inform{"food": "scottish"}
 - canthelp
* inform{"food": "scottish"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d6f8c4271e-20130326_220359
* inform{"pricerange": "moderate"}
 - request_area
* inform{"food": "mexican"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130402_080841
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "hungarian"}
 - offer_detailed
* inform{"food": "european"}
 - canthelp
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-50af5438f1-20130402_085506
* inform{"pricerange": "expensive"}
 - request_food
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-50af5438f1-20130402_084641
* inform{"pricerange": "expensive"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer
* inform{"food": "irish"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130327_034500
* inform{"food": "world"}
 - canthelp
* inform{"food": "modern european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130402_085256
* inform{"pricerange": "moderate"}
 - select
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-50af5438f1-20130402_085647
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "italian"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-50af5438f1-20130402_090250
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130402_081930
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130402_082750
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-50af5438f1-20130402_084400
* inform{"food": "gastropub"}
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - request_food
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-50af5438f1-20130402_081345
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - select
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "basque"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-50af5438f1-20130327_032137
* inform{"pricerange": "cheap"}
 - request_food
* inform{"pricerange": "cheap"}
 - request_food
* inform{"area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130327_043337
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-50af5438f1-20130402_081208
* inform{"food": "thai"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130327_032335
* inform{"area": "east"}
 - request_food
* inform{"food": "singaporean"}
 - canthelp
* inform{"food": "indian"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-50af5438f1-20130402_085904
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "chinese"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-50af5438f1-20130327_041542
* inform_dontcare
 - offer_detailed
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-50af5438f1-20130327_041921
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - confirm-domain
* inform{"food": "italian"}
 - offer_detailed
* inform{"food": "italian"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-50af5438f1-20130327_031854
* inform{"area": "centre"}
 - request_food
* inform{"food": "spanish"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-eaef6f434c-20130323_025453
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "modern european"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-eaef6f434c-20130323_030832
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "italian", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-eaef6f434c-20130323_025316
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-eaef6f434c-20130323_031257
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-eaef6f434c-20130323_031356
* request{"requested_pricerange": "True"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - expl-conf
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-eaef6f434c-20130323_025154
* inform_dontcare
 - request_food
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-eaef6f434c-20130323_024502
* inform{"food": "world"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-eaef6f434c-20130323_025614
* include_filter{"food": "steakhouse", "area": "north"}
 - canthelp
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "chinese", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-eaef6f434c-20130323_025908
* include_filter{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "asian oriental", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e8997b10da-20130329_011058
* include_filter{"food": "french"}
 - request_area
* inform{"area": "centre"}
 - expl-conf
* include_filter{"food": "french"}
 - expl-conf
* affirm
 - offer_detailed
* ack
 - canthelp
* request{"requested_pricerange": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* ack
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* ack
 - canthelp
* ack
 - expl-conf
* request{"requested_addr": "True"}
 - offer_detailed
* ack
 - offer
* thankyou
 - bye

## Mar13_S0A0/voip-e8997b10da-20130327_193112
* include_filter{"food": "vegetarian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_food": "True"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* confirm{"food": "british"}
 - confirm-domain
* include_filter{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* ack
 - reqmore
* bye
 - bye

## Mar13_S1A0/voip-e8997b10da-20130329_001748
* include_filter{"food": "chinese", "area": "east"}
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e8997b10da-20130401_152342
* include_filter{"food": "korean", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e8997b10da-20130401_152530
* include_filter{"food": "malaysian"}
 - canthelp
* inform{"food": "french"}
 - expl-conf
* include_filter{"pricerange": "dontcare"}
 - select
* inform_dontcare
 - request_area
* inform_dontcare
 - offer_detailed
* ack
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e8997b10da-20130329_011626
* include_filter{"area": "north"}
 - request_food
* inform{"pricerange": "cheap"}
 - select
* inform{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e8997b10da-20130401_151850
* include_filter{"food": "lebanese", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - reqmore
* negate
 - bye

## Mar13_S1A1/voip-e8997b10da-20130327_194306
* include_filter{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e8997b10da-20130329_010926
* include_filter{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e8997b10da-20130329_001948
* include_filter{"food": "italian", "pricerange": "expensive"}
 - request_area
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e8997b10da-20130329_000534
* include_filter{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* ack
 - canthelp
* bye
 - bye

## Mar13_S1A1/voip-e8997b10da-20130327_200112
* inform{"food": "scottish"}
 - canthelp
* inform{"food": "british"}
 - expl-conf
* correct{"food": "british"}
 - request_area
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e8997b10da-20130329_012511
* inform{"food": "african"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e8997b10da-20130329_010205
* include_filter{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e8997b10da-20130329_000658
* affirm
 - request_area
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e8997b10da-20130327_194901
* include_filter{"food": "brazilian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* ack
 - offer_detailed
* inform{"food": "gastropub", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e8997b10da-20130327_195713
* include_filter{"food": "turkish", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e8997b10da-20130327_193641
* include_filter{"pricerange": "expensive", "area": "east"}
 - confirm-domain
* include_filter{"pricerange": "expensive"}
 - request_food
* inform_dontcare{"pricerange": "expensive"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* ack
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e8997b10da-20130329_012334
* include_filter{"food": "turkish"}
 - offer_detailed
* inform{"food": "turkish", "pricerange": "cheap"}
 - confirm-domain
* affirm
 - offer_detailed
* inform{"food": "turkish", "pricerange": "cheap"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e8997b10da-20130401_152228
* include_filter{"pricerange": "cheap", "area": "west"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* include_filter{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e8997b10da-20130329_012706
* include_filter{"food": "danish"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "danish"}
 - canthelp
* inform{"food": "international"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e8997b10da-20130401_152019
* include_filter{"food": "danish"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "danish"}
 - canthelp
* inform{"food": "international"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-31de0daa7b-20130402_133530
* inform{"food": "creative"}
 - canthelp
* inform{"food": "modern european"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31de0daa7b-20130402_133216
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* affirm
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - expl-conf
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - request_area
* inform{"pricerange": "expensive"}
 - offer_detailed
* negate
 - canthelp
* inform{"food": "european"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* bye
 - bye

## Mar13_S1A0/voip-31de0daa7b-20130401_205355
* inform{"food": "kosher", "pricerange": "moderate"}
 - request_area
* inform{"food": "kosher", "pricerange": "moderate"}
 - request_area
* inform{"area": "north"}
 - select
* inform{"area": "west"}
 - expl-conf
* affirm
 - request_food
* inform{"food": "kosher"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31de0daa7b-20130401_204415
* inform{"food": "creative"}
 - request_area
* inform{"area": "north"}
 - request_food
* inform{"food": "creative"}
 - offer_detailed
* inform{"food": "international"}
 - canthelp
* inform{"food": "creative"}
 - canthelp
* inform{"area": "centre"}
 - expl-conf
* correct{"area": "centre"}
 - expl-conf
* negate
 - canthelp
* inform{"area": "centre"}
 - expl-conf
* affirm
 - canthelp
* bye
 - bye

## Mar13_S0A1/voip-31de0daa7b-20130401_220541
* inform{"food": "kosher", "area": "dontcare"}
 - request_food
* inform{"food": "kosher"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31de0daa7b-20130401_220728
* inform{"pricerange": "moderate", "area": "south"}
 - expl-conf
* affirm
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-31de0daa7b-20130401_205633
* inform{"food": "international", "area": "south"}
 - expl-conf
* affirm
 - canthelp
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-31de0daa7b-20130401_221101
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* bye
 - bye

## Mar13_S1A1/voip-31de0daa7b-20130402_133047
* inform{"food": "seafood", "pricerange": "moderate"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-31de0daa7b-20130401_203534
* include_filter{"pricerange": "cheap"}
 - offer_detailed
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52eb280e7b-20130325_130820
* inform{"food": "christmas", "area": "west"}
 - request_food
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52eb280e7b-20130326_212826
* inform{"food": "british"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52eb280e7b-20130325_124240
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52eb280e7b-20130326_215158
* inform{"food": "korean"}
 - request_food
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52eb280e7b-20130326_211923
* inform{"food": "international"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52eb280e7b-20130326_212733
* inform{"food": "italian", "pricerange": "cheap"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52eb280e7b-20130325_131334
* inform{"food": "turkish", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52eb280e7b-20130325_125522
* inform{"area": "north"}
 - request_food
* inform{"pricerange": "cheap"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52eb280e7b-20130326_213528
* inform{"food": "thai"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52eb280e7b-20130326_213227
* inform{"food": "japanese"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52eb280e7b-20130325_130645
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-52eb280e7b-20130325_125355
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52eb280e7b-20130325_132224
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-52eb280e7b-20130325_123856
* inform{"food": "korean", "pricerange": "expensive"}
 - offer_detailed
* inform{"food": "creative"}
 - canthelp
* inform{"food": "italian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52eb280e7b-20130326_214342
* inform{"food": "portuguese"}
 - confirm-domain
* inform{"food": "portuguese", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-52eb280e7b-20130325_130950
* inform{"food": "polynesian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-52eb280e7b-20130326_215044
* inform{"food": "international"}
 - request_area
* inform{"area": "centre"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-52eb280e7b-20130325_125157
* inform{"food": "cantonese"}
 - offer_detailed
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "thai"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* inform{"food": "thai"}
 - offer
* bye
 - bye

## Mar13_S0A1/voip-2c217000af-20130328_224808
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2c217000af-20130328_223711
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2c217000af-20130328_224934
* inform{"food": "singaporean", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2c217000af-20130325_221252
* inform{"food": "british", "area": "east"}
 - request_area
* inform{"area": "east"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2c217000af-20130325_222647
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2c217000af-20130328_224449
* inform{"food": "lebanese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2c217000af-20130325_221701
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "french", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2c217000af-20130325_222430
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2c217000af-20130325_221525
* inform{"food": "traditional", "pricerange": "expensive"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2c217000af-20130328_224206
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e9b53d6ace-20130324_223617
* inform{"area": "north"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "european"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_190230
* inform{"food": "jamaican", "area": "north"}
 - offer_detailed
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* inform{"food": "chinese"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e9b53d6ace-20130324_221046
* inform{"food": "hungarian", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e9b53d6ace-20130324_222525
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e9b53d6ace-20130401_190004
* inform{"area": "south"}
 - request_food
* inform{"food": "european"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e9b53d6ace-20130324_222855
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e9b53d6ace-20130401_210057
* inform{"area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_202424
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_202659
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_184931
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e9b53d6ace-20130324_221924
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_212753
* inform{"food": "caribbean", "area": "centre"}
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_204254
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e9b53d6ace-20130401_201306
* inform{"food": "australian", "area": "east"}
 - request_food
* inform{"food": "australian"}
 - request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_200405
* inform{"area": "south"}
 - request_food
* inform{"food": "chinese"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e9b53d6ace-20130324_220844
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130324_222746
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_194326
* inform{"food": "welsh", "area": "dontcare"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e9b53d6ace-20130324_223300
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e9b53d6ace-20130324_222642
* inform{"food": "korean", "area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e9b53d6ace-20130324_220734
* inform{"food": "turkish"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_190135
* inform{"pricerange": "cheap", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e9b53d6ace-20130324_221520
* inform{"area": "centre"}
 - request_food
* inform{"food": "halal"}
 - canthelp
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_205843
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f4026333dc-20130327_175843
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f4026333dc-20130327_180235
* inform{"food": "welsh", "pricerange": "expensive"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2b66f60368-20130326_203353
* inform{"food": "afghan"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2b66f60368-20130326_202529
* inform{"food": "italian", "pricerange": "cheap"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-2b66f60368-20130326_203610
* inform{"food": "spanish"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2b66f60368-20130326_202221
* inform{"pricerange": "moderate", "area": "north"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare{"area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2b66f60368-20130326_203705
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* correct{"food": "chinese"}
 - select
* inform{"food": "chinese"}
 - expl-conf
* affirm
 - canthelp
* inform{"area": "dontcare"}
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* confirm{"food": "chinese"}
 - canthelp
* inform{"area": "dontcare"}
 - expl-conf
* affirm
 - canthelp
* inform{"area": "dontcare"}
 - expl-conf
* negate
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2b66f60368-20130326_202811
* inform{"food": "turkish"}
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* inform{"food": "turkish"}
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2b66f60368-20130326_203018
* query{"food": "christmas", "requested_signature": "True"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british", "pricerange": "expensive"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "british", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e72dba1759-20130325_211057
* inform{"food": "world", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e72dba1759-20130326_221205
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - request_food
* inform{"pricerange": "moderate"}
 - request_food
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e72dba1759-20130326_223506
* inform{"food": "chinese", "pricerange": "cheap"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e72dba1759-20130326_215630
* inform{"food": "hungarian"}
 - request_food
* inform{"food": "hungarian"}
 - offer
* request{"requested_pricerange": "True"}
 - offer_detailed
* inform{"food": "hungarian", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"pricerange": "dontcare"}
 - reqmore
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e72dba1759-20130325_204847
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e72dba1759-20130326_222657
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e72dba1759-20130325_204725
* inform{"food": "vegetarian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e72dba1759-20130326_220053
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e72dba1759-20130326_220605
* include_filter{"pricerange": "cheap"}
 - request_area
* inform_dontcare{"pricerange": "cheap"}
 - offer_detailed
* confirm{"area": "south"}
 - offer_detailed
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e72dba1759-20130325_204601
* inform{"area": "west"}
 - request_food
* inform{"food": "thai"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A1/voip-e72dba1759-20130326_222550
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e72dba1759-20130325_210629
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e72dba1759-20130325_205739
* inform{"food": "cuban", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e72dba1759-20130326_223157
* inform{"pricerange": "cheap", "area": "west"}
 - expl-conf
* affirm
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e72dba1759-20130325_210917
* inform{"pricerange": "moderate"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S0A0/voip-e72dba1759-20130325_205315
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e72dba1759-20130325_210022
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_pricerange": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e72dba1759-20130326_220956
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - expl-conf
* include_filter{"food": "corsica"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e72dba1759-20130325_215313
* affirm
 - request_area
* inform{"food": "crossover", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - expl-conf
* affirm
 - request_pricerange
* inform_dontcare
 - select
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fe2783c40a-20130401_150540
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - select
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-fe2783c40a-20130401_145640
* inform{"pricerange": "moderate"}
 - select
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fe2783c40a-20130401_144037
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fe2783c40a-20130401_151115
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fe2783c40a-20130401_145010
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-fe2783c40a-20130401_145931
* inform{"area": "north"}
 - request_food
* inform{"food": "eritrean"}
 - request_food
* inform{"food": "eritrean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-fe2783c40a-20130401_145146
* inform{"pricerange": "cheap"}
 - request_area
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"food": "seafood"}
 - offer_detailed
* inform{"food": "seafood"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e30cb521fb-20130328_131711
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e30cb521fb-20130328_144608
* inform{"food": "cuban", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - expl-conf
* include_filter{"food": "chinese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e30cb521fb-20130328_122635
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* thankyou
 - offer_detailed
* bye
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e30cb521fb-20130328_134803
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e30cb521fb-20130328_135828
* inform{"food": "romanian", "area": "centre"}
 - request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_food": "True"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e30cb521fb-20130328_135454
* inform{"pricerange": "cheap", "area": "south"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e0035cc31b-20130323_210244
* inform{"food": "barbeque", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e0035cc31b-20130323_211513
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e0035cc31b-20130323_211354
* inform{"food": "polynesian", "area": "west"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e0035cc31b-20130326_204829
* inform{"pricerange": "moderate", "area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e0035cc31b-20130323_212516
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e0035cc31b-20130326_205511
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e0035cc31b-20130326_205626
* inform{"food": "russian"}
 - canthelp
* inform{"food": "korean"}
 - select
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e0035cc31b-20130323_212959
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e0035cc31b-20130326_203550
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e0035cc31b-20130326_205950
* inform{"food": "scottish"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e0035cc31b-20130323_211206
* inform{"food": "african", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e0035cc31b-20130326_205004
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e0035cc31b-20130323_211112
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e0035cc31b-20130326_203939
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e0035cc31b-20130323_212626
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e0035cc31b-20130323_212221
* inform_dontcare
 - request_food
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e0035cc31b-20130326_210405
* inform{"food": "irish", "pricerange": "expensive"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "italian", "pricerange": "expensive"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e0035cc31b-20130326_205255
* inform{"food": "british", "area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e0035cc31b-20130326_203710
* inform{"food": "irish", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e0035cc31b-20130326_204429
* inform{"food": "scandinavian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0a45bc863d-20130325_201403
* inform{"food": "spanish"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0a45bc863d-20130325_201117
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0a45bc863d-20130325_195848
* inform{"food": "caribbean"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0a45bc863d-20130325_202319
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0a45bc863d-20130325_201240
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0a45bc863d-20130326_205127
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - request_area
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0a45bc863d-20130326_205629
* inform{"area": "west"}
 - request_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "british"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-0a45bc863d-20130325_200201
* inform{"area": "south"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0a45bc863d-20130325_200034
* inform{"food": "english", "area": "centre"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "british"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0a45bc863d-20130325_200515
* inform{"pricerange": "moderate", "area": "north"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0a45bc863d-20130326_204718
* inform{"pricerange": "expensive"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "korean"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-0a45bc863d-20130325_202120
* inform{"food": "belgian"}
 - expl-conf
* correct{"food": "belgian"}
 - canthelp
* inform{"food": "british"}
 - request_area
* inform{"area": "centre"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-0a45bc863d-20130326_205408
* inform{"food": "european"}
 - request_food
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-0a45bc863d-20130326_210243
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-43479eb5c2-20130324_004748
* inform{"pricerange": "cheap", "area": "west"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-43479eb5c2-20130329_045902
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-43479eb5c2-20130324_003643
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-43479eb5c2-20130323_180515
* inform{"area": "south"}
 - request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "portuguese"}
 - expl-conf
* affirm
 - expl-conf
* inform{"food": "portuguese"}
 - expl-conf
* negate
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-43479eb5c2-20130323_180105
* inform{"pricerange": "expensive", "area": "south"}
 - expl-conf
* correct{"area": "south"}
 - request_food
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f113dbb0e1-20130322_233310
* inform{"area": "east"}
 - select
* inform{"area": "east"}
 - request_food
* inform{"area": "west"}
 - expl-conf
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f113dbb0e1-20130327_173541
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f113dbb0e1-20130322_233822
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f113dbb0e1-20130327_173417
* inform{"area": "west"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "british"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f113dbb0e1-20130327_173842
* inform{"pricerange": "moderate"}
 - request_food
* inform{"food": "vietnamese"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"pricerange": "cheap"}
 - request_area_detailed
* request{"requested_addr": "True"}
 - request_area
* inform{"area": "east"}
 - canthelp
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d645d56d23-20130324_000301
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d645d56d23-20130323_221635
* inform{"food": "african", "area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - reqmore
* negate
 - reqmore
* bye
 - bye

## Mar13_S1A0/voip-d645d56d23-20130324_001536
* inform{"food": "halal", "pricerange": "moderate"}
 - offer_detailed
* confirm{"food": "halal"}
 - offer_detailed
* correct{"food": "halal"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d645d56d23-20130323_222004
* inform{"food": "european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d645d56d23-20130401_204623
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d645d56d23-20130401_204424
* inform{"area": "east"}
 - request_food
* inform{"food": "world"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* query{"name": "pizza hut city centre", "requested_food": "True"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d645d56d23-20130323_223158
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* inform{"pricerange": "expensive", "area": "east"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d645d56d23-20130323_222341
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-d645d56d23-20130401_203033
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "portuguese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-d645d56d23-20130324_232209
* inform{"area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - offer_detailed
* confirm{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-d645d56d23-20130324_232416
* inform{"pricerange": "cheap", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d645d56d23-20130324_000123
* inform{"area": "dontcare"}
 - expl-conf
* inform{"food": "unusual"}
 - canthelp
* inform{"food": "spanish"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d645d56d23-20130324_000651
* inform{"pricerange": "moderate"}
 - expl-conf
* affirm
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d645d56d23-20130402_035204
* inform{"pricerange": "cheap", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-d645d56d23-20130401_203325
* inform{"food": "russian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* confirm{"food": "chinese"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - select
* inform{"food": "russian"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* inform{"pricerange": "cheap"}
 - select
* inform{"food": "chinese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03d6592b76-20130326_015131
* inform{"food": "italian", "pricerange": "cheap"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* confirm{"pricerange": "cheap"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03d6592b76-20130326_012615
* inform{"food": "steakhouse", "pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "steakhouse"}
 - expl-conf
* affirm
 - offer_detailed
* confirm{"food": "steakhouse"}
 - offer_detailed
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_detailed
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03d6592b76-20130326_012832
* inform{"area": "south"}
 - request_food
* inform{"food": "world"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03d6592b76-20130327_030334
* inform{"food": "japanese", "area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - reqmore
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03d6592b76-20130326_014023
* inform{"food": "cuban", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - confirm-domain
* affirm
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03d6592b76-20130326_012940
* inform{"food": "turkish"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - expl-conf
* affirm
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03d6592b76-20130326_012529
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03d6592b76-20130327_025441
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03d6592b76-20130327_024630
* inform{"area": "east"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - request_food
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "cantonese"}
 - offer_detailed
* inform{"food": "cantonese"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03d6592b76-20130327_030034
* inform{"pricerange": "cheap"}
 - request_food
* inform{"food": "dontcare"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True", "requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-03d6592b76-20130326_013107
* inform{"food": "international", "area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03d6592b76-20130327_030602
* inform{"food": "asian oriental"}
 - request_area
* inform{"area": "dontcare"}
 - request_food
* inform{"food": "asian oriental"}
 - request_food
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* correct{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - expl-conf
* affirm
 - expl-conf
* negate
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - select
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03d6592b76-20130327_024820
* inform{"food": "thai", "pricerange": "expensive"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03d6592b76-20130326_012136
* inform{"area": "north"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03d6592b76-20130327_025219
* inform{"food": "austrian", "area": "south"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-03d6592b76-20130326_014855
* inform{"food": "halal", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_detailed
* confirm{"food": "gastropub"}
 - offer_detailed
* inform{"food": "gastropub"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-03d6592b76-20130327_030242
* inform{"pricerange": "moderate", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-03d6592b76-20130326_013208
* inform{"food": "greek", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* inform{"food": "chinese"}
 - offer_detailed
* confirm{"food": "chinese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ad40cf5489-20130325_180702
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - confirm-domain
* include_filter{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ad40cf5489-20130327_192610
* inform{"food": "scottish", "pricerange": "moderate"}
 - canthelp
* inform{"food": "british", "pricerange": "moderate"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ad40cf5489-20130325_180305
* inform{"food": "corsica", "area": "centre"}
 - canthelp
* inform{"food": "international", "area": "centre"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ad40cf5489-20130325_175953
* inform{"food": "seafood", "area": "centre"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ad40cf5489-20130327_193841
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* reqalts
 - confirm-domain
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ad40cf5489-20130327_192458
* inform{"food": "caribbean", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ad40cf5489-20130327_192300
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ad40cf5489-20130327_194457
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ad40cf5489-20130327_194224
* inform{"food": "australian", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - request_pricerange
* inform_dontcare
 - expl-conf
* inform{"food": "chinese"}
 - expl-conf
* inform{"food": "chinese"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ad40cf5489-20130325_180552
* inform{"pricerange": "expensive", "area": "north"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ad40cf5489-20130327_191905
* inform{"pricerange": "moderate", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ad40cf5489-20130327_192405
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ad40cf5489-20130325_181942
* inform{"food": "gastropub", "pricerange": "cheap"}
 - request_food
* inform{"food": "gastropub"}
 - request_food
* inform{"food": "gastropub"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ad40cf5489-20130325_181004
* inform{"food": "welsh", "pricerange": "cheap"}
 - expl-conf
* include_filter{"pricerange": "cheap"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "mediterranean", "pricerange": "cheap"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ad40cf5489-20130325_175502
* inform{"food": "catalan", "pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish", "pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ad40cf5489-20130327_191318
* inform{"food": "jamaican", "area": "west"}
 - request_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "vietnamese", "area": "west"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* negate
 - offer_detailed
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - expl-conf
* affirm
 - expl-conf
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ad40cf5489-20130327_194114
* inform{"pricerange": "cheap", "area": "north"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-ad40cf5489-20130327_191638
* inform{"food": "seafood", "area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-ad40cf5489-20130327_192155
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ad40cf5489-20130325_180434
* inform{"food": "vietnamese", "area": "north"}
 - canthelp
* inform{"area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ad40cf5489-20130325_175141
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "modern european"}
 - confirm-domain
* inform{"food": "modern european"}
 - request_area
* inform{"area": "dontcare"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-ad40cf5489-20130325_181825
* inform{"pricerange": "moderate", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-ad40cf5489-20130325_182117
* inform{"food": "creative", "area": "east"}
 - canthelp
* inform{"food": "indian", "area": "east"}
 - canthelp
* inform{"food": "indian", "area": "east"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_191629
* inform{"food": "kosher", "area": "north"}
 - canthelp
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_190757
* inform{"food": "kosher", "pricerange": "expensive"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_190456
* inform{"pricerange": "expensive"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_193033
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_190613
* inform{"food": "world", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_191755
* inform{"food": "mexican", "pricerange": "expensive"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_192646
* inform{"pricerange": "moderate", "area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_191205
* inform{"pricerange": "cheap", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_190045
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_area": "True"}
 - offer
* request{"requested_area": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_185424
* inform{"food": "asian oriental", "area": "centre"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_185133
* inform{"area": "south"}
 - request_food
* inform{"food": "turkish"}
 - offer_detailed
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_191934
* inform{"pricerange": "expensive", "area": "east"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_165410
* inform{"food": "indian"}
 - request_area
* inform{"area": "west"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f22c2bf9c7-20130328_122513
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f22c2bf9c7-20130326_192953
* inform{"food": "vietnamese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f22c2bf9c7-20130326_020833
* inform{"area": "south"}
 - request_food
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "irish"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f22c2bf9c7-20130326_193723
* inform{"food": "german"}
 - request_area
* inform{"area": "east"}
 - request_area
* inform{"area": "east"}
 - request_food
* inform{"food": "german"}
 - canthelp
* inform{"food": "gastropub"}
 - expl-conf
* affirm
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - offer
* bye
 - bye

## Mar13_S1A0/voip-f22c2bf9c7-20130326_202745
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "turkish"}
 - request_area
* inform{"area": "east"}
 - canthelp
* inform{"area": "north"}
 - canthelp
* inform{"area": "north"}
 - expl-conf
* negate
 - expl-conf
* affirm
 - canthelp
* bye
 - bye

## Mar13_S0A0/voip-f22c2bf9c7-20130326_203001
* inform{"food": "portuguese"}
 - request_food
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f22c2bf9c7-20130328_120523
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f22c2bf9c7-20130328_114452
* inform{"food": "swedish"}
 - request_area
* inform{"area": "centre"}
 - request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_115849
* inform{"food": "turkish"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* inform{"area": "south"}
 - request_area
* bye
 - bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_121753
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - request_area
* inform{"area": "north"}
 - select
* inform{"area": "north"}
 - select
* inform{"area": "north"}
 - select
* inform{"area": "north"}
 - select
* inform{"pricerange": "moderate"}
 - select
* inform{"pricerange": "moderate"}
 - select
* inform{"area": "north"}
 - offer_detailed
* inform{"area": "north"}
 - offer
* inform{"area": "north"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f22c2bf9c7-20130326_203410
* inform{"area": "west"}
 - expl-conf
* affirm
 - offer_detailed
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "british"}
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f22c2bf9c7-20130328_121125
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "indian"}
 - request_area_detailed
* inform{"area": "centre"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f22c2bf9c7-20130326_020431
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_115128
* inform{"food": "japanese"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer
* request{"requested_pricerange": "True"}
 - canthelp
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f22c2bf9c7-20130326_193956
* inform{"food": "scandinavian"}
 - request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f22c2bf9c7-20130328_113750
* inform{"food": "gastropub"}
 - request_pricerange
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-f22c2bf9c7-20130328_114939
* inform{"pricerange": "cheap"}
 - offer
* inform{"area": "south"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f22c2bf9c7-20130328_120123
* inform{"food": "international"}
 - request_area
* inform{"area": "centre"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - bye

## Mar13_S0A1/voip-f22c2bf9c7-20130326_203814
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - offer_detailed
* request{"requested_pricerange": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* inform_dontcare
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-f22c2bf9c7-20130328_113940
* inform{"area": "south"}
 - request_food
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-f22c2bf9c7-20130328_120730
* inform{"food": "unusual"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - request_area
* inform{"area": "centre"}
 - request_food
* inform{"food": "unusual"}
 - canthelp
* inform{"area": "north"}
 - canthelp
* inform{"area": "south"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"area": "centre"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* bye
 - bye

## Mar13_S0A1/voip-e99e4f4538-20130328_195304
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e99e4f4538-20130328_202105
* inform{"food": "african", "area": "centre"}
 - request_food
* inform{"food": "african"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e99e4f4538-20130328_200547
* inform{"food": "portuguese"}
 - request_area
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e99e4f4538-20130327_152308
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130328_201948
* inform{"area": "west"}
 - request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e99e4f4538-20130327_154223
* inform{"area": "west"}
 - request_area
* inform{"area": "west"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e99e4f4538-20130327_145422
* inform{"pricerange": "cheap", "area": "north"}
 - request_area
* inform{"area": "north"}
 - offer_detailed
* reqalts
 - confirm-domain
* reqalts
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130327_152525
* inform{"pricerange": "cheap"}
 - request_area
* inform{"area": "east"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e99e4f4538-20130327_145848
* inform{"pricerange": "expensive"}
 - request_food
* inform{"food": "mediterranean"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130328_195927
* inform{"area": "west"}
 - request_food
* inform{"food": "indian"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130328_201531
* inform{"pricerange": "moderate", "area": "south"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130327_140746
* inform{"food": "mexican"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* thankyou
 - offer
* bye
 - bye

## Mar13_S1A0/voip-e99e4f4538-20130328_195729
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "international"}
 - expl-conf
* negate
 - canthelp
* negate
 - canthelp
* inform{"food": "international"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e99e4f4538-20130328_200259
* inform{"food": "jamaican"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "jamaican"}
 - offer
* inform{"food": "jamaican"}
 - offer
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130328_203355
* inform_dontcare
 - request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "mediterranean"}
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130327_153656
* inform{"food": "catalan"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "catalan"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* reqalts
 - expl-conf
* affirm
 - expl-conf
* negate
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e99e4f4538-20130327_141042
* inform{"area": "north"}
 - request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "italian"}
 - confirm-domain
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e99e4f4538-20130328_201813
* inform{"pricerange": "cheap"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e99e4f4538-20130327_150414
* inform{"food": "french"}
 - request_area
* inform_dontcare
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "french"}
 - offer_detailed
* inform{"pricerange": "expensive"}
 - offer_detailed
* affirm
 - offer
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer
* request{"requested_phone": "True"}
 - canthelp
* query{"name": "restaurant two two", "requested_phone": "True"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-e99e4f4538-20130327_150148
* inform{"area": "north"}
 - request_food
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-e99e4f4538-20130328_201635
* inform{"pricerange": "cheap"}
 - offer_detailed
* inform{"area": "west"}
 - offer
* confirm{"pricerange": "cheap"}
 - offer_detailed
* confirm{"area": "west"}
 - offer_detailed
* inform{"area": "west"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e99e4f4538-20130327_141718
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "modern european"}
 - request_area
* inform_dontcare
 - request_pricerange
* inform{"pricerange": "expensive"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e99e4f4538-20130328_200645
* inform{"pricerange": "cheap", "area": "west"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-e99e4f4538-20130327_154024
* inform{"area": "north"}
 - confirm-domain
* request{"requested_area": "True"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* inform{"food": "indian"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130327_144810
* inform{"area": "south"}
 - request_food
* inform{"pricerange": "moderate"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-e99e4f4538-20130327_150005
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-6d6587c57d-20130328_142518
* inform{"pricerange": "moderate", "area": "north"}
 - request_food
* inform{"food": "dontcare"}
 - expl-conf
* affirm
 - offer_detailed
* reqalts
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-6d6587c57d-20130328_142302
* inform{"food": "irish", "area": "centre"}
 - confirm-domain
* affirm
 - request_pricerange
* inform{"pricerange": "dontcare"}
 - offer_detailed
* inform{"food": "irish"}
 - canthelp
* inform{"food": "north american"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-6d6587c57d-20130328_143700
* inform{"area": "east"}
 - request_food
* inform{"food": "corsica"}
 - request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* bye
 - bye

## Mar13_S0A0/voip-6d6587c57d-20130328_143034
* inform{"pricerange": "expensive", "area": "south"}
 - request_food
* inform{"food": "dontcare"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-263ab0e49f-20130326_104818
* inform{"pricerange": "moderate", "area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - canthelp
* correct{"pricerange": "moderate"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-263ab0e49f-20130326_104535
* include_filter{"food": "portuguese"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-263ab0e49f-20130326_104358
* request{"requested_area": "True", "requested_postcode": "True", "requested_addr": "True"}
 - request_area
* inform{"area": "south"}
 - request_food
* inform_dontcare
 - request_pricerange
* include_filter{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_addr": "True", "requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-263ab0e49f-20130326_110450
* inform{"food": "polynesian", "area": "south"}
 - canthelp
* inform{"food": "italian"}
 - offer_detailed
* request{"requested_phone": "True", "requested_postcode": "True"}
 - offer_detailed
* request{"requested_postcode": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-263ab0e49f-20130326_105455
* include_filter{"pricerange": "expensive", "area": "east"}
 - request_food
* inform{"food": "dontcare"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_food": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-263ab0e49f-20130326_105158
* include_filter{"food": "hungarian", "area": "south"}
 - request_pricerange
* inform_dontcare
 - request_food
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "modern european"}
 - offer_detailed
* request{"requested_addr": "True", "requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a617b6827c-20130323_170328
* inform_dontcare
 - request_food
* inform{"food": "corsica"}
 - request_food
* inform{"food": "corsica"}
 - request_food
* inform{"food": "gastropub"}
 - request_pricerange
* inform_dontcare
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A1/voip-a617b6827c-20130323_170210
* inform{"pricerange": "moderate"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "chinese"}
 - offer_detailed
* inform{"pricerange": "moderate"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A1/voip-a617b6827c-20130323_165831
* inform{"food": "british"}
 - request_area
* inform{"area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_detailed
* request{"requested_addr": "True"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S0A0/voip-a617b6827c-20130323_170929
* inform{"pricerange": "expensive", "area": "east"}
 - request_food
* inform_dontcare
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* confirm{"pricerange": "expensive"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-a617b6827c-20130323_171108
* inform{"food": "french"}
 - request_area
* inform_dontcare
 - request_food
* inform{"food": "french"}
 - offer_detailed
* reqalts
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

## Mar13_S1A0/voip-80451eaa72-20130401_191337
* inform{"food": "german", "area": "north"}
 - expl-conf
* affirm
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french", "area": "north"}
 - select
* inform{"food": "french"}
 - offer_detailed
* request{"requested_phone": "True"}
 - offer_detailed
* bye
 - bye

