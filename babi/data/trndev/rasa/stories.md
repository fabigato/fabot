## Mar13_S0A1/voip-b772dbf437-20130402_143019
* inform{"food": "swedish", "pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* reqalts
 - utter_anything_else
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-b772dbf437-20130402_142118
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "catalan"}
 - utter_request_food
* inform{"food": "catalan"}
 - utter_request_food
* inform{"food": "italian"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-b772dbf437-20130402_141805
* inform{"area": "dontcare"}
 - confirm_summary
* inform{"pricerange": "dontcare"}
 - utter_request_area
* inform{"food": "world"}
 - canthelp
* inform{"food": "mediterranean"}
 - utter_select_food
* inform{"food": "mediterranean"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-b772dbf437-20130402_141105
* inform{"area": "west"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-b772dbf437-20130402_142550
* inform{"area": "east"}
 - utter_request_food
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-b772dbf437-20130402_141548
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "spanish"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-ec87351630-20130328_162752
* inform{"food": "mexican", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* thankyou
 - utter_anything_else
* negate
 - utter_anything_else
* negate
 - utter_bye

## Mar13_S1A0/voip-ec87351630-20130328_162916
* inform{"food": "lebanese", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-14cb91bc48-20130327_202138
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-14cb91bc48-20130328_162839
* inform{"pricerange": "expensive"}
 - utter_request_area
* negate
 - confirm_area
* inform{"food": "portuguese"}
 - utter_request_food
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "mediterranean"}
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-14cb91bc48-20130328_163311
* inform{"food": "korean"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-14cb91bc48-20130328_194336
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-14cb91bc48-20130327_190340
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"food": "japanese"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-14cb91bc48-20130328_163437
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "indian"}
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-14cb91bc48-20130328_161626
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "thai"}
 - utter_select_price
* inform{"area": "west"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - utter_anything_else
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-14cb91bc48-20130328_163139
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-14cb91bc48-20130328_165532
* inform{"food": "venetian"}
 - utter_select_price
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-14cb91bc48-20130327_204058
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-4c0d36762a-20130328_213330
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-4c0d36762a-20130328_204534
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4c0d36762a-20130328_210737
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "greek"}
 - utter_request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-4c0d36762a-20130328_202045
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-4c0d36762a-20130328_212300
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "polish"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-4c0d36762a-20130328_204720
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-4c0d36762a-20130328_205236
* inform{"food": "indonesian", "pricerange": "expensive"}
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform_dontcare
 - confirm_food
* negate
 - confirm_summary
* inform_dontcare
 - canthelp
* inform{"food": "british"}
 - confirm_food
* affirm
 - confirm_summary
* affirm
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4c0d36762a-20130328_212449
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-4c0d36762a-20130328_204956
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-4c0d36762a-20130328_203937
* inform{"pricerange": "cheap", "area": "west"}
 - confirm_summary
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e2a895cfe5-20130327_020622
* inform{"area": "east"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-e2a895cfe5-20130325_233852
* inform{"area": "south"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e2a895cfe5-20130325_231121
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "world"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e2a895cfe5-20130327_021102
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e2a895cfe5-20130326_232941
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-e2a895cfe5-20130326_233604
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e2a895cfe5-20130325_234115
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e2a895cfe5-20130326_233655
* inform{"area": "dontcare"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "jamaican"}
 - utter_request_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-e2a895cfe5-20130326_233829
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "indian"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-e2a895cfe5-20130325_230900
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "spanish"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-e2a895cfe5-20130325_230741
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "hungarian"}
 - confirm_food
* correct{"food": "hungarian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* confirm{"food": "hungarian"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-e2a895cfe5-20130327_021619
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e2a895cfe5-20130326_232742
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"area": "west", "address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e2a895cfe5-20130325_232606
* inform{"food": "kosher", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e2a895cfe5-20130325_233234
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "north american"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-fce37b0ccb-20130328_151459
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* inform{"area": "north"}
 - offer_restaurant
* inform{"area": "north"}
 - offer_restaurant
* reqalts
 - futile_offer_restaurant
* reqalts
 - futile_offer_restaurant
* reqalts
 - futile_offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-fce37b0ccb-20130328_145245
* inform{"food": "persian"}
 - utter_request_food
* inform{"food": "persian"}
 - futile_offer_restaurant
* confirm{"area": "north"}
 - utter_offer_area
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_offer_area
* bye
 - utter_offer_area
* bye
 - utter_bye

## Mar13_S1A0/voip-fce37b0ccb-20130328_145831
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "east"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-fce37b0ccb-20130328_143529
* inform{"area": "north"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-fce37b0ccb-20130328_145418
* include_filter{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-fce37b0ccb-20130328_145014
* inform{"food": "basque"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - confirm_food
* affirm
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-fce37b0ccb-20130328_144400
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "spanish"}
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-fce37b0ccb-20130328_144745
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-8991b7bff6-20130401_180409
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "south"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-8991b7bff6-20130401_174504
* inform{"area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-8991b7bff6-20130327_192101
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-8991b7bff6-20130401_175934
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-8991b7bff6-20130401_174957
* inform{"pricerange": "cheap"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - offer_pricerange
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-8991b7bff6-20130326_232407
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-8991b7bff6-20130326_231508
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-8991b7bff6-20130401_161851
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-8991b7bff6-20130326_230316
* inform_dontcare
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "korean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-8991b7bff6-20130401_174811
* inform_dontcare
 - utter_request_food
* inform{"food": "canapes"}
 - utter_request_food
* inform{"food": "turkish"}
 - utter_request_food
* inform{"food": "turkish"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-8991b7bff6-20130401_160325
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-8991b7bff6-20130326_230200
* inform{"food": "european"}
 - confirm_food
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-8991b7bff6-20130401_163110
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-ef9aa63b85-20130329_131927
* inform{"pricerange": "cheap", "area": "south"}
 - confirm_summary
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-ef9aa63b85-20130328_223357
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "unusual"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_food
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-ef9aa63b85-20130329_132421
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-ef9aa63b85-20130329_125741
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-ef9aa63b85-20130328_190444
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ef9aa63b85-20130329_130049
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ef9aa63b85-20130328_210319
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-ef9aa63b85-20130329_131544
* inform_dontcare
 - utter_request_food
* inform{"food": "eritrean"}
 - utter_select_food
* negate
 - utter_select_food
* inform{"food": "eritrean"}
 - utter_select_food
* deny{"food": "vietnamese"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - utter_anything_else
* inform{"food": "french"}
 - utter_anything_else
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - utter_bye

## Mar13_S0A1/voip-ef9aa63b85-20130328_184027
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "italian"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-ef9aa63b85-20130328_211048
* inform_dontcare
 - utter_request_food
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "asian oriental"}
 - confirm_food
* affirm
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-ef9aa63b85-20130329_131415
* inform{"food": "hungarian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "turkish"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-22a181cad5-20130326_023529
* inform{"food": "lebanese", "area": "centre"}
 - confirm_area
* inform{"food": "lebanese"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "lebanese"}
 - utter_request_food
* inform{"food": "lebanese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-22a181cad5-20130326_022324
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_184430
* inform{"food": "english"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-3cf7bd870d-20130327_180414
* inform{"food": "indonesian", "pricerange": "cheap"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-3cf7bd870d-20130328_212502
* inform{"area": "centre"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "kosher"}
 - utter_request_food
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_174017
* inform{"area": "north"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3cf7bd870d-20130328_211947
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-3cf7bd870d-20130328_212749
* inform{"food": "malaysian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* correct{"food": "british"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-3cf7bd870d-20130328_150815
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_183049
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "french", "pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-3cf7bd870d-20130327_175817
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3cf7bd870d-20130327_175213
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-3cf7bd870d-20130327_174155
* inform{"food": "tuscan", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_pricerange
* inform{"food": "gastropub"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-3cf7bd870d-20130327_180852
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3cf7bd870d-20130327_181243
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-3cf7bd870d-20130328_212136
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3cf7bd870d-20130327_184051
* inform{"food": "crossover", "area": "west"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3cf7bd870d-20130327_174526
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"area": "west"}
 - offer_restaurant
* correct{"area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-4f069a4136-20130402_032014
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-4f069a4136-20130327_205937
* inform{"food": "vietnamese", "pricerange": "cheap"}
 - offer_pricerange
* inform{"food": "vietnamese"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* inform_dontcare
 - utter_anything_else
* inform{"pricerange": "moderate"}
 - utter_anything_else
* inform_dontcare
 - utter_anything_else
* request{"pricerange": "_REQUESTED_"}
 - utter_anything_else
* inform{"pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-4f069a4136-20130402_031309
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-4f069a4136-20130327_205819
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-4f069a4136-20130327_204405
* inform{"food": "afghan"}
 - confirm_food
* inform{"pricerange": "expensive"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "korean"}
 - confirm_food
* negate
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-4f069a4136-20130327_211252
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-4f069a4136-20130402_030948
* inform{"food": "portuguese"}
 - offer_restaurant
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-4f069a4136-20130327_210318
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* confirm{"area": "centre"}
 - offer_restaurant
* inform{"food": "british"}
 - offer_restaurant
* confirm{"area": "centre"}
 - offer_restaurant
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-4f069a4136-20130402_032750
* inform{"food": "international"}
 - utter_request_area
* inform{"area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4f069a4136-20130402_031636
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "danish"}
 - canthelp
* correct{"food": "danish"}
 - utter_select_food
* inform{"food": "danish"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - confirm_area
* affirm
 - confirm_food
* affirm
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-4f069a4136-20130327_204947
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4f069a4136-20130402_030550
* inform{"food": "thai"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "thai"}
 - confirm_food
* inform_dontcare
 - utter_select_price
* inform{"food": "thai"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* negate
 - offer_restaurant
* confirm{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-4f069a4136-20130327_205654
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-4f069a4136-20130402_033307
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "turkish"}
 - utter_select_food
* inform{"food": "turkish"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* affirm
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-4f069a4136-20130327_204639
* inform{"food": "scandinavian"}
 - utter_request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4f069a4136-20130402_034737
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4f069a4136-20130402_032149
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* inform{"food": "swiss"}
 - confirm_area
* inform{"food": "swiss"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - confirm_summary
* negate
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4f069a4136-20130327_205501
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-fdf8b50918-20130326_051637
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-fdf8b50918-20130329_014245
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-fdf8b50918-20130327_024718
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-fdf8b50918-20130329_013736
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-fdf8b50918-20130327_024110
* inform{"food": "european", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-fdf8b50918-20130329_042606
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-fdf8b50918-20130329_035324
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-fdf8b50918-20130326_050512
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-fdf8b50918-20130329_014041
* inform{"food": "bistro", "pricerange": "moderate"}
 - utter_request_food
* inform{"food": "bistro"}
 - utter_request_food
* inform{"food": "bistro"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-fdf8b50918-20130326_051438
* inform{"food": "indian", "area": "east"}
 - canthelp
* inform{"food": "indian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-fdf8b50918-20130327_024909
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "jamaican"}
 - offer_restaurant
* inform{"food": "jamaican"}
 - offer_pricerange
* confirm{"food": "jamaican"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-fdf8b50918-20130327_023811
* inform{"food": "jamaican", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* bye
 - utter_bye

## Mar13_S1A1/voip-fdf8b50918-20130329_013925
* inform{"food": "spanish"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-fdf8b50918-20130326_051921
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-fdf8b50918-20130326_052504
* inform{"food": "italian", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-fdf8b50918-20130326_052355
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-fdf8b50918-20130329_042348
* inform{"food": "european", "pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-fdf8b50918-20130327_024453
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-249d0f617b-20130328_161219
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-249d0f617b-20130326_005503
* inform{"pricerange": "moderate"}
 - utter_select_price
* affirm
 - utter_select_price
* inform{"pricerange": "moderate"}
 - confirm_summary
* affirm
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-249d0f617b-20130326_010500
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "british"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-249d0f617b-20130328_161812
* inform{"area": "west"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-9819537952-20130328_232353
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "singaporean"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-9819537952-20130327_022757
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* thankyou
 - futile_offer_restaurant
* bye
 - offer_restaurant
* bye
 - offer_restaurant
* bye
 - no_more_options
* thankyou
 - offer_restaurant
* thankyou
 - futile_offer_restaurant
* bye
 - no_more_options
* bye
 - utter_bye

## Mar13_S0A1/voip-9819537952-20130328_230928
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-9819537952-20130328_231209
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-9819537952-20130327_023104
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare
 - utter_offer_area
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-9819537952-20130328_235404
* request{"pricerange": "_REQUESTED_"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "dontcare"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-9819537952-20130327_024815
* inform{"food": "lebanese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-9819537952-20130327_023856
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-9819537952-20130327_021901
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "british"}
 - confirm_food
* affirm
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-9819537952-20130328_235607
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-9819537952-20130328_234847
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "dontcare"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-9f447ce48e-20130328_115123
* inform_dontcare
 - confirm_area
* affirm
 - canthelp
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-05e7a5440b-20130328_214746
* inform{"food": "italian", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-05e7a5440b-20130328_211013
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-05e7a5440b-20130328_220724
* inform_dontcare
 - utter_request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "european"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-05e7a5440b-20130328_215502
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-05e7a5440b-20130328_213943
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-05e7a5440b-20130328_220901
* inform{"food": "vegetarian"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-05e7a5440b-20130328_213636
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-05e7a5440b-20130328_211620
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - no_more_options
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-05e7a5440b-20130328_211413
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-05e7a5440b-20130328_215138
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-05e7a5440b-20130328_222114
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-05e7a5440b-20130328_211839
* inform{"food": "cuban", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-05e7a5440b-20130328_212037
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-583e7cede5-20130323_060529
* inform{"food": "polish", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-583e7cede5-20130324_060002
* inform{"food": "italian", "area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-583e7cede5-20130324_063315
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-583e7cede5-20130324_055306
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-583e7cede5-20130323_052525
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-583e7cede5-20130323_143756
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_restaurant
* inform{"food": "north american"}
 - futile_offer_restaurant
* inform{"food": "north american"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-583e7cede5-20130324_060901
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - utter_select_area
* inform_dontcare
 - utter_request_food
* inform{"food": "turkish"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-583e7cede5-20130323_061037
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - confirm_food
* affirm
 - utter_request_area
* inform_dontcare
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - utter_bye

## Mar13_S1A1/voip-583e7cede5-20130324_062107
* inform{"food": "european", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-583e7cede5-20130323_062756
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-583e7cede5-20130324_060405
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-583e7cede5-20130323_055421
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-583e7cede5-20130324_063452
* inform{"food": "turkish", "pricerange": "expensive"}
 - utter_request_food
* inform{"food": "turkish"}
 - offer_pricerange
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-583e7cede5-20130323_060100
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-583e7cede5-20130323_051824
* inform{"food": "seafood", "pricerange": "expensive"}
 - offer_restaurant
* confirm{"name": "_REQUESTED_"}
 - offer_restaurant
* confirm{"name": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-583e7cede5-20130323_054735
* inform{"area": "centre"}
 - utter_request_area
* inform{"area": "centre"}
 - utter_select_price
* inform{"food": "english", "area": "centre"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-583e7cede5-20130324_061500
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-583e7cede5-20130324_062248
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-583e7cede5-20130324_063717
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - utter_offer_area
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-869dd52548-20130401_183901
* inform{"food": "hungarian", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-869dd52548-20130401_175459
* inform{"food": "catalan", "area": "east"}
 - utter_request_food
* inform{"food": "catalan"}
 - utter_request_food
* inform{"food": "catalan"}
 - utter_request_food
* inform{"food": "catalan"}
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-869dd52548-20130401_184505
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-869dd52548-20130401_175746
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-869dd52548-20130326_000755
* inform{"food": "moroccan", "pricerange": "moderate"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-869dd52548-20130401_180217
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-869dd52548-20130401_184747
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-869dd52548-20130401_180331
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-869dd52548-20130401_184008
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-869dd52548-20130326_000655
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-869dd52548-20130401_184240
* inform_dontcare
 - utter_request_food
* inform{"food": "portuguese"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - no_more_options
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* inform{"food": "portuguese", "pricerange": "dontcare"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* reqalts
 - no_more_options
* bye
 - utter_bye

## Mar13_S0A1/voip-869dd52548-20130326_001137
* inform{"food": "asian oriental", "area": "south"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - utter_offer_area
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-869dd52548-20130401_175624
* inform{"food": "spanish", "pricerange": "expensive"}
 - offer_pricerange
* inform{"food": "modern european"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-869dd52548-20130326_000910
* inform{"food": "african", "pricerange": "dontcare"}
 - confirm_food
* include_filter{"food": "african"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-869dd52548-20130401_184559
* inform{"food": "japanese", "area": "centre"}
 - utter_request_food
* inform{"food": "cantonese"}
 - utter_request_food
* inform{"food": "cantonese"}
 - utter_request_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-869dd52548-20130401_175253
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-a7ddefaeb3-20130327_174327
* inform{"area": "centre"}
 - utter_request_area
* inform{"food": "modern european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-a7ddefaeb3-20130327_174908
* inform{"food": "barbeque", "pricerange": "cheap"}
 - utter_request_food
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-a7ddefaeb3-20130328_172838
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_select_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - utter_request_food
* inform_dontcare
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-a7ddefaeb3-20130328_172708
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-a7ddefaeb3-20130328_173142
* affirm
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - utter_select_price
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-8d5173f3a6-20130324_183442
* inform{"food": "fusion"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-8d5173f3a6-20130324_185406
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-8d5173f3a6-20130323_012203
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "international"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-8d5173f3a6-20130323_011736
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-8d5173f3a6-20130324_183623
* bye
 - utter_request_area
* inform{"area": "west"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-8d5173f3a6-20130323_012048
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-8d5173f3a6-20130323_015026
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-8d5173f3a6-20130324_190545
* inform{"food": "mexican", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-8d5173f3a6-20130324_190350
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-8d5173f3a6-20130324_184915
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-8d5173f3a6-20130323_011549
* inform{"pricerange": "cheap"}
 - utter_request_area
* request{"area": "_REQUESTED_"}
 - utter_request_food
* inform_dontcare
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-8d5173f3a6-20130323_013323
* inform{"food": "seafood", "pricerange": "expensive"}
 - utter_request_food
* inform{"food": "seafood"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-8d5173f3a6-20130324_184603
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-8d5173f3a6-20130323_015902
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "british"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-8d5173f3a6-20130324_185203
* inform{"area": "east"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-8d5173f3a6-20130323_013205
* inform{"food": "greek", "area": "south"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-8d5173f3a6-20130323_015159
* request{"pricerange": "_REQUESTED_"}
 - utter_select_price
* inform_dontcare
 - offer_pricerange
* inform{"area": "east"}
 - offer_restaurant
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-8d5173f3a6-20130324_190231
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-8d5173f3a6-20130324_183949
* inform{"food": "creative"}
 - canthelp
* inform{"food": "north american"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-8d5173f3a6-20130324_184438
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "indian"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-58047f5227-20130327_032952
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-58047f5227-20130327_034311
* inform{"food": "seafood"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "seafood"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-58047f5227-20130326_032713
* inform{"food": "swedish", "area": "dontcare"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "north american"}
 - canthelp
* inform{"food": "north american"}
 - confirm_area
* affirm
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-58047f5227-20130326_031756
* inform{"pricerange": "cheap", "area": "north"}
 - confirm_summary
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-58047f5227-20130326_030552
* inform{"food": "danish", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-58047f5227-20130326_031502
* inform{"food": "australian", "area": "west"}
 - utter_request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-58047f5227-20130327_032049
* inform{"food": "venetian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "turkish"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-58047f5227-20130327_033611
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-58047f5227-20130326_032849
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-58047f5227-20130327_032257
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-58047f5227-20130326_032210
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-58047f5227-20130327_033352
* inform{"food": "european", "pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-58047f5227-20130327_034209
* inform{"food": "mexican"}
 - utter_request_food
* inform{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-58047f5227-20130327_032835
* inform{"food": "unusual", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-58047f5227-20130326_030421
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-58047f5227-20130327_004644
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-58047f5227-20130327_033220
* inform{"food": "russian", "area": "dontcare"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "russian"}
 - canthelp
* inform{"food": "north american"}
 - confirm_area
* affirm
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-58047f5227-20130326_030155
* inform{"food": "traditional", "area": "centre"}
 - utter_request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-58047f5227-20130327_032739
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-da4a08ad84-20130328_154258
* inform{"food": "korean", "pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-da4a08ad84-20130328_160004
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"postcode": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-da4a08ad84-20130328_154358
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-da4a08ad84-20130328_155250
* inform{"food": "traditional", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-da4a08ad84-20130328_155023
* inform{"food": "turkish", "pricerange": "moderate"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-da4a08ad84-20130328_155120
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-da4a08ad84-20130328_160315
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_area
* affirm
 - offer_pricerange
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-14f776f781-20130328_140514
* inform{"food": "vietnamese", "area": "north"}
 - utter_request_food
* inform{"food": "vietnamese"}
 - canthelp
* inform{"area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - no_more_options
* thankyou
 - offer_restaurant
* bye
 - confirm_food
* bye
 - utter_bye

## Mar13_S0A1/voip-14f776f781-20130328_141638
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_pricerange
* inform{"food": "north american"}
 - confirm_food
* affirm
 - offer_restaurant
* inform{"food": "north american"}
 - offer_pricerange
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-14f776f781-20130328_115724
* inform{"food": "polish"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-14f776f781-20130329_033249
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-14f776f781-20130328_123358
* inform{"food": "australian", "area": "east"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* inform{"food": "australian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-14f776f781-20130328_151904
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-14f776f781-20130328_121622
* inform{"food": "vegetarian", "pricerange": "expensive"}
 - utter_select_price
* thankyou
 - canthelp
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* inform{"food": "asian oriental", "pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-14f776f781-20130328_142356
* inform{"food": "basque", "pricerange": "expensive"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "korean"}
 - offer_pricerange
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-14f776f781-20130328_123813
* inform{"food": "creative", "pricerange": "moderate"}
 - offer_pricerange
* inform{"food": "british"}
 - offer_pricerange
* inform{"food": "creative"}
 - offer_pricerange
* inform{"food": "creative"}
 - canthelp
* inform{"food": "british"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-1b51204ef5-20130401_173145
* inform{"food": "indian"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "indian"}
 - offer_restaurant
* reqalts
 - no_more_options
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-1b51204ef5-20130401_172934
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "centre"}
 - confirm_food
* include_filter{"food": "italian"}
 - offer_restaurant
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - utter_anything_else
* bye
 - utter_bye

## Mar13_S1A0/voip-1b51204ef5-20130401_145241
* inform{"food": "steakhouse"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "turkish"}
 - confirm_food
* inform{"food": "turkish"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-1b51204ef5-20130401_150524
* inform{"food": "unusual"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-1b51204ef5-20130401_145742
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "international"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-1b51204ef5-20130401_145115
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-fd0c0fb514-20130328_114840
* negate
 - confirm_summary
* inform_dontcare
 - confirm_summary
* inform_dontcare
 - utter_request_area
* inform{"area": "west"}
 - confirm_summary
* inform_dontcare
 - utter_request_food
* inform{"food": "italian"}
 - offer_restaurant
* inform_dontcare
 - futile_offer_restaurant
* inform_dontcare
 - futile_offer_restaurant
* inform{"food": "polynesian"}
 - futile_offer_restaurant
* inform_dontcare
 - futile_offer_restaurant
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* confirm{"food": "italian"}
 - offer_restaurant
* inform{"food": "italian"}
 - confirm_summary
* inform_dontcare
 - confirm_summary
* inform{"pricerange": "expensive"}
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - canthelp
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-fd0c0fb514-20130328_114152
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-fd0c0fb514-20130328_114024
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-e3b4879e0d-20130327_030628
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-e3b4879e0d-20130327_181026
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "french", "area": "centre"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e3b4879e0d-20130327_182147
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-e3b4879e0d-20130326_024455
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e3b4879e0d-20130326_021022
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e3b4879e0d-20130326_024336
* inform{"area": "centre"}
 - utter_select_price
* inform{"food": "english"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e3b4879e0d-20130326_020631
* inform{"food": "english", "area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "english"}
 - utter_request_food
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_anything_else
* bye
 - utter_anything_else
* bye
 - utter_anything_else
* negate
 - utter_anything_else
* bye
 - utter_anything_else
* inform_dontcare
 - offer_restaurant
* bye
 - utter_anything_else
* bye
 - utter_bye

## Mar13_S1A0/voip-e3b4879e0d-20130327_181509
* inform{"food": "european", "area": "centre"}
 - utter_request_food
* inform{"food": "european"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-e3b4879e0d-20130326_215515
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e3b4879e0d-20130326_022732
* inform{"food": "lebanese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - no_more_options
* bye
 - utter_bye

## Mar13_S0A0/voip-e3b4879e0d-20130327_030803
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - offer_restaurant
* bye
 - offer_restaurant
* bye
 - canthelp
* bye
 - utter_bye

## Mar13_S1A1/voip-e3b4879e0d-20130327_181715
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e3b4879e0d-20130326_023327
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-560cbd32a5-20130401_144308
* inform{"food": "afghan"}
 - utter_request_food
* inform{"food": "afghan"}
 - utter_request_food
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform_dontcare
 - confirm_area
* negate
 - confirm_food
* affirm
 - canthelp
* inform{"food": "vietnamese", "area": "dontcare"}
 - offer_restaurant
* confirm{"pricerange": "cheap"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-560cbd32a5-20130401_143827
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - utter_bye

## Mar13_S1A0/voip-62cc0cc55d-20130323_155832
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-62cc0cc55d-20130328_143213
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-62cc0cc55d-20130323_155313
* inform{"food": "world", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-62cc0cc55d-20130328_141332
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "vietnamese"}
 - offer_pricerange
* reqalts
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-62cc0cc55d-20130323_155046
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"name": "da vinci pizzeria", "address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-62cc0cc55d-20130328_140957
* inform{"food": "polynesian", "area": "dontcare"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* reqalts
 - canthelp
* inform{"food": "modern european"}
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-62cc0cc55d-20130323_160732
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "indian", "pricerange": "cheap"}
 - confirm_ask_area
* inform{"area": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* inform{"food": "indian"}
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-62cc0cc55d-20130323_160541
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "portuguese"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-62cc0cc55d-20130323_161217
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "international"}
 - canthelp
* inform{"area": "centre"}
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"name": "bloomsbury restaurant", "phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-62cc0cc55d-20130328_143025
* inform_dontcare
 - offer_pricerange
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "italian", "area": "west"}
 - canthelp
* inform{"food": "italian", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-ab4f1dbb59-20130325_214245
* inform{"food": "cuban", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-ab4f1dbb59-20130328_180542
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ab4f1dbb59-20130325_214609
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-ab4f1dbb59-20130325_214838
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-ab4f1dbb59-20130325_214441
* inform{"food": "kosher", "area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-158a881c88-20130328_152500
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-158a881c88-20130328_153956
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-158a881c88-20130328_151638
* inform{"pricerange": "expensive", "area": "east"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-158a881c88-20130328_150912
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-158a881c88-20130328_151847
* inform{"food": "lebanese"}
 - utter_request_area
* inform_dontcare
 - utter_offer_area
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-158a881c88-20130328_151021
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-39a25ab2f8-20130326_122045
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-39a25ab2f8-20130326_120526
* inform{"food": "european"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-39a25ab2f8-20130328_131901
* inform{"area": "west"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-39a25ab2f8-20130326_131509
* inform{"pricerange": "cheap", "area": "west"}
 - confirm_area
* affirm
 - confirm_summary
* affirm
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_request_food
* bye
 - utter_bye

## Mar13_S1A1/voip-30772678da-20130328_193916
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-30772678da-20130328_192354
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-30772678da-20130328_192819
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "english"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-30772678da-20130328_200455
* inform{"food": "portuguese", "pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-30772678da-20130328_200202
* inform{"food": "world"}
 - canthelp
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-30772678da-20130328_195730
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-30772678da-20130328_193458
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-d76f6e4f82-20130327_195041
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-d76f6e4f82-20130327_193430
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "spanish"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-d76f6e4f82-20130327_201839
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-d76f6e4f82-20130327_184807
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-d76f6e4f82-20130327_184557
* inform{"food": "creative"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-d76f6e4f82-20130327_185043
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-d76f6e4f82-20130327_185328
* inform{"pricerange": "expensive"}
 - utter_select_price
* inform_dontcare
 - futile_offer_restaurant
* thankyou
 - futile_offer_restaurant
* inform_dontcare
 - futile_offer_restaurant
* confirm{"area": "east"}
 - utter_offer_area
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-d76f6e4f82-20130327_194817
* inform{"pricerange": "expensive"}
 - utter_request_area
* request{"area": "_REQUESTED_"}
 - confirm_food
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-d76f6e4f82-20130327_190022
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-d76f6e4f82-20130327_193247
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-21ec2b7850-20130327_043931
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-21ec2b7850-20130327_033947
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-21ec2b7850-20130327_034759
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-21ec2b7850-20130326_021426
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-21ec2b7850-20130327_044255
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-21ec2b7850-20130327_040209
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-21ec2b7850-20130327_040416
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-21ec2b7850-20130326_114409
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-21ec2b7850-20130327_042044
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "chinese"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-21ec2b7850-20130325_143118
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-21ec2b7850-20130326_021614
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_postcode
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_pricerange
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-21ec2b7850-20130327_040626
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-21ec2b7850-20130325_132551
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - confirm_summary
* negate
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-21ec2b7850-20130326_024646
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - futile_offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-21ec2b7850-20130325_145025
* inform{"food": "hungarian"}
 - offer_restaurant
* inform{"food": "hungarian"}
 - offer_restaurant
* negate
 - futile_offer_restaurant
* inform{"area": "south"}
 - futile_offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* inform{"food": "hungarian"}
 - offer_restaurant
* inform{"food": "modern european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-21ec2b7850-20130326_025529
* inform{"food": "german"}
 - utter_request_area
* inform_dontcare
 - utter_offer_area
* inform{"food": "german"}
 - canthelp
* inform{"food": "european", "pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-21ec2b7850-20130325_154906
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"area": "north"}
 - utter_select_area
* inform{"area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-21ec2b7850-20130326_025736
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "spanish"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-21ec2b7850-20130326_022849
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"food": "gastropub"}
 - futile_offer_restaurant
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-21ec2b7850-20130327_045035
* inform{"area": "east"}
 - offer_restaurant
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-21ec2b7850-20130327_044903
* inform{"food": "persian"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-21ec2b7850-20130325_162417
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-b27a230d2e-20130323_050439
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130329_032627
* inform{"food": "cantonese", "area": "south"}
 - utter_request_food
* inform{"food": "cantonese"}
 - canthelp
* affirm
 - utter_select_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-b27a230d2e-20130323_042544
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "seafood"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-b27a230d2e-20130323_053403
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-b27a230d2e-20130329_035828
* inform{"area": "south"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "kosher"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-b27a230d2e-20130329_031831
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-b27a230d2e-20130323_053029
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "italian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* inform{"food": "italian"}
 - utter_offer_area
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-b27a230d2e-20130329_034847
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-b27a230d2e-20130323_043046
* inform{"area": "centre"}
 - utter_select_price
* inform_dontcare
 - offer_pricerange
* inform_dontcare
 - futile_offer_restaurant
* inform_dontcare
 - futile_offer_restaurant
* inform{"area": "centre"}
 - utter_offer_area
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130323_050944
* inform{"food": "unusual", "pricerange": "moderate"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130329_031627
* inform{"food": "danish"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130323_041953
* inform{"food": "german", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - confirm_food
* inform{"food": "asian oriental"}
 - confirm_summary
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_pricerange
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - offer_pricerange
* inform_dontcare
 - futile_offer_restaurant
* inform_dontcare
 - futile_offer_restaurant
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-b27a230d2e-20130329_040014
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130329_043420
* inform{"food": "indian", "area": "east"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "indian", "area": "east"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130329_035413
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* inform{"name": "chiquito restaurant bar"}
 - offer_restaurant
* inform{"pricerange": "expensive", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-b27a230d2e-20130329_031256
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130323_050830
* inform{"food": "seafood", "pricerange": "expensive"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-b27a230d2e-20130329_033804
* inform{"food": "chinese", "pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b27a230d2e-20130323_045538
* inform{"pricerange": "expensive"}
 - offer_pricerange
* confirm{"food": "seafood"}
 - offer_pricerange
* inform{"food": "seafood"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - utter_anything_else
* request{"area": "_REQUESTED_"}
 - utter_anything_else
* request{"area": "_REQUESTED_"}
 - utter_anything_else
* inform{"food": "seafood", "pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-b27a230d2e-20130329_030940
* inform{"food": "vietnamese", "pricerange": "moderate"}
 - offer_pricerange
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "indian"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-b27a230d2e-20130329_031422
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "european"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-b27a230d2e-20130329_030324
* inform{"food": "christmas", "pricerange": "cheap"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "christmas"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* inform{"food": "christmas"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-b27a230d2e-20130323_050551
* inform{"food": "korean", "area": "north"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-2d2d103292-20130326_041300
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-2d2d103292-20130329_041636
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-2d2d103292-20130326_041008
* inform{"food": "indonesian"}
 - canthelp
* inform{"food": "thai"}
 - confirm_food
* affirm
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2d2d103292-20130326_041541
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "basque"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2d2d103292-20130329_041521
* inform{"food": "russian", "area": "centre"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-2d2d103292-20130326_042921
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2d2d103292-20130326_041959
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_restaurant
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-2d2d103292-20130326_041815
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-2d2d103292-20130326_043748
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "spanish"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-2d2d103292-20130326_044020
* inform_dontcare
 - offer_pricerange
* inform{"area": "centre"}
 - offer_restaurant
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-2d2d103292-20130329_041255
* inform{"food": "bistro", "area": "centre"}
 - canthelp
* inform{"food": "north american"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2d2d103292-20130329_035727
* inform{"food": "world"}
 - canthelp
* inform{"food": "spanish"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-2d2d103292-20130329_040958
* inform{"food": "moroccan", "area": "centre"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "thai"}
 - confirm_area
* affirm
 - confirm_food
* correct{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - confirm_food
* affirm
 - canthelp
* inform{"pricerange": "dontcare"}
 - offer_pricerange
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai", "pricerange": "moderate"}
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-2d2d103292-20130326_043352
* inform{"food": "mediterranean"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-2d2d103292-20130329_040656
* inform{"food": "japanese", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - confirm_food
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2d2d103292-20130329_041424
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-2d2d103292-20130329_035835
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-2d2d103292-20130329_042056
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2d2d103292-20130328_195634
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-2d2d103292-20130329_041951
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-2d2d103292-20130328_195103
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-2d2d103292-20130329_035601
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-2d2d103292-20130326_040723
* inform{"area": "centre"}
 - utter_offer_area
* confirm{"food": "fusion"}
 - offer_restaurant
* inform{"food": "fusion"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-908884f5fd-20130326_224812
* inform{"food": "belgian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-908884f5fd-20130326_215916
* inform{"food": "scandinavian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "mediterranean"}
 - utter_request_area
* inform_dontcare{"pricerange": "cheap"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - confirm_area
* inform{"pricerange": "cheap"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-8586129f35-20130328_160121
* inform{"food": "romanian", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - confirm_area
* affirm
 - confirm_food
* inform{"food": "mediterranean"}
 - utter_select_food
* inform{"food": "mediterranean"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-03c59ba692-20130325_183305
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-03c59ba692-20130324_034930
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-03c59ba692-20130324_034507
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03c59ba692-20130402_054245
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-03c59ba692-20130324_034058
* inform{"food": "vegetarian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-03c59ba692-20130324_033629
* inform{"food": "afghan", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-03c59ba692-20130324_180022
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* thankyou
 - utter_bye

## Mar13_S0A1/voip-03c59ba692-20130402_060307
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-03c59ba692-20130402_053545
* inform{"food": "brazilian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03c59ba692-20130324_180433
* inform{"food": "romanian", "area": "centre"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-03c59ba692-20130402_060050
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-03c59ba692-20130324_034712
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03c59ba692-20130325_180735
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-03c59ba692-20130324_033821
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-aaa44b4121-20130326_060013
* inform{"food": "danish"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* inform{"food": "asian oriental", "pricerange": "expensive"}
 - utter_request_area
* inform{"area": "north"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-aaa44b4121-20130326_055316
* inform{"area": "north"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-aaa44b4121-20130326_055608
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-aaa44b4121-20130326_051152
* inform{"pricerange": "moderate"}
 - utter_select_area
* inform{"food": "british"}
 - utter_select_area
* inform{"food": "british"}
 - utter_select_area
* inform{"area": "north"}
 - canthelp
* inform{"area": "south"}
 - canthelp
* inform{"food": "british"}
 - confirm_summary
* affirm
 - canthelp
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-aaa44b4121-20130326_055421
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-aaa44b4121-20130327_170849
* inform{"area": "south"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-aaa44b4121-20130327_171453
* inform{"food": "korean"}
 - offer_restaurant
* inform{"area": "dontcare"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-aaa44b4121-20130327_170337
* inform{"food": "moroccan", "pricerange": "moderate"}
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "indian"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-aaa44b4121-20130326_051458
* inform{"food": "european"}
 - utter_request_area
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-aaa44b4121-20130327_171321
* inform{"pricerange": "cheap", "area": "south"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-aaa44b4121-20130327_002455
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "british"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-aaa44b4121-20130327_165758
* inform{"food": "european"}
 - futile_offer_restaurant
* negate
 - futile_offer_restaurant
* inform{"food": "european"}
 - futile_offer_restaurant
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* inform{"food": "portuguese", "area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-aaa44b4121-20130326_050817
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"area": "north"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-aaa44b4121-20130327_172530
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-aaa44b4121-20130327_170541
* inform{"food": "malaysian", "area": "centre"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-aaa44b4121-20130327_172225
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-aaa44b4121-20130327_170209
* inform{"food": "world", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_pricerange
* inform{"food": "vietnamese"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-aaa44b4121-20130327_171617
* inform{"food": "international"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-aaa44b4121-20130327_170719
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-aaa44b4121-20130326_060838
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-aaa44b4121-20130326_054647
* inform{"food": "traditional", "area": "south"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-aaa44b4121-20130327_171958
* inform{"area": "south"}
 - utter_request_food
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-affbf578cf-20130401_162946
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-affbf578cf-20130401_163655
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e61fa89add-20130327_074357
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e61fa89add-20130326_013340
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - confirm_ask_area
* inform{"food": "spanish"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e61fa89add-20130327_075222
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e61fa89add-20130326_100409
* inform{"food": "basque", "pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e61fa89add-20130327_072313
* inform{"food": "korean", "area": "north"}
 - canthelp
* inform{"food": "persian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e61fa89add-20130327_075612
* inform{"food": "tuscan", "pricerange": "expensive"}
 - canthelp
* inform{"food": "french"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e61fa89add-20130327_074017
* inform_dontcare
 - utter_request_food
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "north american"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-e61fa89add-20130326_013931
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "asian oriental"}
 - utter_select_food
* inform{"food": "asian oriental"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_select_price
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e61fa89add-20130327_080334
* inform{"food": "romanian", "area": "centre"}
 - utter_request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "british"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e61fa89add-20130326_011204
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform{"food": "chinese"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "cheap"}
 - confirm_summary
* inform{"pricerange": "cheap"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e61fa89add-20130326_100750
* inform{"food": "greek", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - confirm_food
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-e61fa89add-20130327_074526
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-e61fa89add-20130326_013737
* inform{"food": "eritrean", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-e61fa89add-20130326_100617
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e61fa89add-20130327_071630
* inform{"food": "danish", "area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-c8ec8c76dd-20130328_205311
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-c8ec8c76dd-20130328_205953
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-c8ec8c76dd-20130328_180054
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-c8ec8c76dd-20130328_175715
* inform{"food": "scottish"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "international"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-c8ec8c76dd-20130328_174742
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-c8ec8c76dd-20130328_175504
* inform{"food": "bistro", "area": "centre"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-c8ec8c76dd-20130328_210403
* inform{"food": "malaysian", "area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-c8ec8c76dd-20130328_181909
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* inform{"food": "gastropub", "area": "east"}
 - utter_select_food
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-c8ec8c76dd-20130328_205558
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-c8ec8c76dd-20130328_205041
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-5cf59cc660-20130327_144955
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-5cf59cc660-20130328_161517
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-5cf59cc660-20130328_163609
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-5cf59cc660-20130327_145314
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-5cf59cc660-20130328_143501
* inform{"food": "thai"}
 - utter_request_area
* inform_dontcare
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-5cf59cc660-20130328_164112
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-5cf59cc660-20130328_161200
* inform{"food": "cuban", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - confirm_food
* correct{"food": "spanish"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-5cf59cc660-20130328_161054
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - confirm_food
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-5cf59cc660-20130328_143758
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_pricerange
* confirm{"area": "north"}
 - futile_offer_restaurant
* confirm{"area": "north"}
 - offer_restaurant
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-5cf59cc660-20130327_144735
* inform{"food": "korean"}
 - confirm_food
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-5cf59cc660-20130328_172318
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-5cf59cc660-20130327_145222
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-5cf59cc660-20130327_144604
* inform{"food": "japanese", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-5cf59cc660-20130328_151124
* inform{"food": "chinese", "pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-5cf59cc660-20130327_143126
* inform{"food": "italian"}
 - utter_select_price
* inform_dontcare
 - offer_pricerange
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-5cf59cc660-20130328_171914
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-5cf59cc660-20130327_145740
* inform{"food": "creative"}
 - canthelp
* inform{"food": "north american"}
 - confirm_food
* inform{"food": "north american"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-5cf59cc660-20130328_145134
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-5cf59cc660-20130328_160837
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - confirm_food
* correct{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-5cf59cc660-20130327_144338
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-5cf59cc660-20130328_160946
* inform{"food": "european", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-5cf59cc660-20130327_143308
* inform{"food": "greek"}
 - canthelp
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-5cf59cc660-20130328_172556
* inform{"food": "persian", "area": "south"}
 - utter_request_food
* inform{"food": "persian"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* confirm{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-5749b16764-20130328_145900
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-5749b16764-20130328_150143
* inform{"food": "asian oriental", "area": "dontcare"}
 - canthelp
* inform{"food": "international"}
 - canthelp
* inform{"food": "international"}
 - confirm_area
* inform{"pricerange": "dontcare"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-5749b16764-20130328_151730
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-5749b16764-20130328_145608
* inform{"food": "unusual", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-5749b16764-20130328_151234
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-3b59a0391b-20130401_135225
* inform{"food": "vietnamese"}
 - futile_offer_restaurant
* inform{"food": "vietnamese"}
 - offer_restaurant
* reqalts
 - utter_anything_else
* inform{"food": "vietnamese"}
 - offer_restaurant
* reqalts
 - utter_anything_else
* inform{"food": "vietnamese"}
 - offer_restaurant
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-3b59a0391b-20130401_133524
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-3b59a0391b-20130401_133038
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - no_more_options
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-3b59a0391b-20130401_133238
* inform{"food": "chinese"}
 - utter_select_area
* inform{"area": "south"}
 - confirm_area
* negate
 - confirm_area
* correct{"area": "south"}
 - utter_request_food
* inform{"food": "chinese"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - no_more_options
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3b59a0391b-20130401_135704
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"area": "west"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3b59a0391b-20130401_132324
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* ack
 - offer_restaurant
* ack
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-3b59a0391b-20130401_134901
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3b59a0391b-20130401_134053
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-b20b6e847a-20130326_222313
* inform{"food": "gastropub", "area": "dontcare"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-b20b6e847a-20130326_222030
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b20b6e847a-20130326_222936
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-b20b6e847a-20130326_224116
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "north"}
 - confirm_food
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-b20b6e847a-20130326_222829
* inform{"food": "japanese", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-199d62165b-20130402_123401
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-199d62165b-20130402_122050
* inform{"food": "russian"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - confirm_food
* affirm
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-199d62165b-20130402_122711
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-199d62165b-20130402_123507
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-199d62165b-20130402_115733
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "turkish"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-199d62165b-20130402_120922
* inform{"food": "korean", "area": "centre"}
 - confirm_area
* include_filter{"food": "korean"}
 - confirm_summary
* inform{"food": "korean", "area": "centre"}
 - canthelp
* inform{"food": "korean", "pricerange": "dontcare", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-199d62165b-20130402_121352
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-199d62165b-20130402_120456
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-199d62165b-20130402_122354
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-199d62165b-20130402_122214
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-199d62165b-20130402_121601
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "turkish"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* thankyou
 - futile_offer_restaurant
* bye
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-199d62165b-20130402_115850
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-3860c915c2-20130328_164046
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-3860c915c2-20130328_164431
* inform{"food": "corsica", "pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_pricerange
* reqalts
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-22c938c8ba-20130325_134402
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform_dontcare
 - offer_restaurant
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* inform{"area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* negate
 - offer_restaurant
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
 - utter_bye

## Mar13_S1A0/voip-22c938c8ba-20130325_130740
* inform{"area": "south"}
 - offer_pricerange
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

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
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-22c938c8ba-20130325_130445
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "south"}
 - offer_pricerange
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* inform_dontcare
 - offer_pricerange
* inform_dontcare
 - offer_pricerange
* bye
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-22c938c8ba-20130325_134206
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-22c938c8ba-20130325_142552
* inform{"food": "afghan"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"food": "afghan"}
 - offer_pricerange
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform_dontcare
 - offer_pricerange
* inform_dontcare
 - offer_pricerange
* inform_dontcare
 - offer_pricerange
* reqalts
 - offer_pricerange
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* bye
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform{"food": "asian oriental"}
 - offer_pricerange
* bye
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - offer_pricerange
* thankyou
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-22c938c8ba-20130325_143621
* inform{"food": "european", "pricerange": "cheap"}
 - canthelp
* inform{"food": "european", "pricerange": "expensive"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* inform{"area": "north"}
 - futile_offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-22c938c8ba-20130325_125039
* inform{"food": "asian oriental"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - utter_request_food
* inform{"food": "chinese"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-22c938c8ba-20130325_130208
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-52d599db9c-20130327_175215
* thankyou
 - utter_request_area
* inform{"food": "german"}
 - canthelp
* inform{"food": "french"}
 - utter_request_area
* inform_dontcare
 - utter_select_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-52d599db9c-20130402_001953
* inform{"food": "chinese", "area": "south"}
 - utter_request_food
* inform{"food": "chinese"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-52d599db9c-20130323_054632
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-52d599db9c-20130326_214515
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-52d599db9c-20130326_213117
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-52d599db9c-20130326_214326
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "indian"}
 - confirm_food
* inform{"food": "indian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-52d599db9c-20130326_212814
* inform{"food": "japanese", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-52d599db9c-20130326_214615
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "catalan"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform{"food": "indian"}
 - utter_select_price
* affirm
 - utter_select_price
* inform{"food": "indian"}
 - utter_select_price
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-52d599db9c-20130402_001838
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-52d599db9c-20130402_002245
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-52d599db9c-20130325_135450
* inform{"food": "italian", "pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-52d599db9c-20130328_154633
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-52d599db9c-20130326_010952
* inform{"food": "mexican", "pricerange": "cheap"}
 - canthelp
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - utter_select_food
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-52d599db9c-20130323_054736
* inform{"pricerange": "moderate"}
 - utter_request_area
* request{"pricerange": "_REQUESTED_"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-52d599db9c-20130402_002522
* inform{"food": "crossover", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "crossover"}
 - utter_request_food
* inform{"food": "crossover"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-52d599db9c-20130326_212959
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-52d599db9c-20130402_000814
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-52d599db9c-20130326_011106
* inform{"food": "vietnamese", "pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_141848
* inform_dontcare
 - utter_offer_area
* inform{"food": "swedish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0fa32b1e78-20130328_234145
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_151950
* inform{"area": "south"}
 - confirm_area
* negate
 - confirm_area
* negate
 - confirm_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_140213
* inform{"area": "south"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0fa32b1e78-20130401_151332
* inform_dontcare
 - offer_pricerange
* inform{"area": "east"}
 - utter_offer_area
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_234804
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "british"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-0fa32b1e78-20130328_151140
* inform{"area": "south"}
 - utter_select_price
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_233916
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "turkish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130402_132031
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_233625
* inform{"food": "turkish"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-0fa32b1e78-20130402_142351
* inform{"food": "mexican"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_233747
* inform{"food": "portuguese"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_142234
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130402_142022
* inform{"food": "austrian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_151336
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "singaporean"}
 - offer_restaurant
* inform{"food": "north american"}
 - confirm_area
* affirm
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_235008
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "polish"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130328_153725
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0fa32b1e78-20130402_140846
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-0fa32b1e78-20130328_152808
* inform{"food": "brazilian"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "brazilian"}
 - canthelp
* inform{"food": "korean"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0fa32b1e78-20130402_140739
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "polish"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0fa32b1e78-20130402_140356
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0fa32b1e78-20130402_141117
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-09733d9e4c-20130327_123942
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-7e4cdce06a-20130323_130200
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-7e4cdce06a-20130323_131109
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-7e4cdce06a-20130323_130824
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "international"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-7e4cdce06a-20130323_130520
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-edb8609855-20130327_183456
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-edb8609855-20130327_183200
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-edb8609855-20130327_183323
* inform{"food": "danish"}
 - canthelp
* inform{"food": "chinese"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-edb8609855-20130327_183802
* inform{"area": "south"}
 - utter_select_price
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-b6618de447-20130328_152114
* inform{"pricerange": "moderate", "area": "east"}
 - confirm_area
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b6618de447-20130328_160617
* inform{"food": "vietnamese", "area": "south"}
 - canthelp
* inform{"food": "indian", "area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b6618de447-20130329_131207
* inform{"food": "jamaican", "pricerange": "cheap"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-b6618de447-20130328_160419
* inform{"food": "traditional", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - offer_pricerange
* confirm{"food": "spanish"}
 - offer_restaurant
* inform{"food": "spanish", "pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-b6618de447-20130326_211132
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-b6618de447-20130328_160315
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-b6618de447-20130326_211551
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "halal"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-b6618de447-20130328_154703
* inform{"food": "greek", "pricerange": "expensive"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform{"food": "asian oriental", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-b6618de447-20130328_160810
* inform{"food": "basque", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-b6618de447-20130328_151251
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-b6618de447-20130328_155353
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-b6618de447-20130328_151535
* include_filter{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "french", "pricerange": "expensive"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-b6618de447-20130328_154027
* inform{"food": "vietnamese", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-b6618de447-20130325_145518
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-b6618de447-20130328_152908
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-b6618de447-20130328_155531
* inform{"food": "hungarian", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "hungarian"}
 - confirm_food
* negate
 - offer_pricerange
* confirm{"food": "hungarian"}
 - offer_restaurant
* inform{"food": "hungarian", "pricerange": "expensive"}
 - offer_pricerange
* confirm{"food": "hungarian"}
 - offer_restaurant
* inform{"food": "british"}
 - futile_offer_restaurant
* inform{"pricerange": "expensive"}
 - utter_select_food
* inform{"food": "british"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b6618de447-20130328_153612
* inform{"food": "belgian", "area": "centre"}
 - canthelp
* inform{"food": "korean", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-b6618de447-20130328_153132
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-2d3d74d091-20130328_134757
* inform{"food": "belgian"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "malaysian"}
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - no_more_options
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-2d3d74d091-20130401_235307
* inform{"food": "spanish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-2d3d74d091-20130328_143735
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_offer_area
* inform{"food": "world"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-2d3d74d091-20130328_191642
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-2d3d74d091-20130328_135311
* affirm
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-2d3d74d091-20130328_135137
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "european"}
 - canthelp
* inform{"area": "centre"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-2d3d74d091-20130328_140026
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "indian"}
 - utter_request_food
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-2d3d74d091-20130401_234343
* inform_dontcare
 - utter_request_food
* inform{"food": "korean"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-2d3d74d091-20130328_153522
* inform{"area": "west"}
 - utter_select_area
* inform{"area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2d3d74d091-20130401_234151
* inform{"pricerange": "expensive"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-2d3d74d091-20130328_144241
* inform{"area": "centre"}
 - utter_request_area
* inform{"area": "centre"}
 - futile_offer_restaurant
* inform{"food": "italian"}
 - futile_offer_restaurant
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-2d3d74d091-20130325_224245
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-fe60dae302-20130328_191353
* inform{"food": "polynesian"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-fe60dae302-20130328_192329
* inform{"area": "south"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_offer_area
* inform{"pricerange": "expensive"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_postcode
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - offer_restaurant
* bye
 - offer_postcode
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
 - utter_bye

## Mar13_S1A0/voip-4c25da9a27-20130327_141855
* inform{"food": "african"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-4c25da9a27-20130327_135709
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "spanish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-4c25da9a27-20130325_184604
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "north american"}
 - confirm_area
* negate
 - confirm_area
* negate
 - confirm_area
* negate
 - confirm_food
* affirm
 - canthelp
* reqalts
 - canthelp
* inform{"food": "north american"}
 - confirm_area
* bye
 - utter_bye

## Mar13_S0A1/voip-4c25da9a27-20130325_182216
* inform{"food": "mediterranean"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4c25da9a27-20130327_140750
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-4c25da9a27-20130325_183726
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-4c25da9a27-20130325_183445
* inform{"food": "moroccan", "area": "south"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* confirm{"food": "modern european"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "european"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4c25da9a27-20130327_141034
* inform{"food": "australasian"}
 - offer_restaurant
* inform{"food": "australasian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* confirm{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4c25da9a27-20130327_140554
* inform{"pricerange": "moderate"}
 - offer_pricerange
* confirm{"food": "gastropub"}
 - offer_restaurant
* confirm{"food": "gastropub"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-4c25da9a27-20130327_140246
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* inform{"food": "korean"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-4c25da9a27-20130325_184738
* inform{"area": "dontcare"}
 - futile_offer_restaurant
* confirm{"food": "christmas"}
 - offer_restaurant
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-4c25da9a27-20130327_141556
* inform{"food": "cuban", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* confirm{"food": "chinese"}
 - confirm_food
* include_filter{"food": "chinese"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4c25da9a27-20130325_181340
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4c25da9a27-20130325_181011
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-4c25da9a27-20130327_140126
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-4c25da9a27-20130325_183247
* inform{"food": "mediterranean", "pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-4c25da9a27-20130327_140438
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-4c25da9a27-20130325_181701
* inform{"food": "polynesian", "area": "north"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-317a1436fe-20130325_171203
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-317a1436fe-20130325_172154
* inform{"food": "turkish"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "turkish"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-317a1436fe-20130325_171718
* inform{"food": "jamaican", "pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "jamaican"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* deny{"food": "chinese"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "jamaican"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"food": "jamaican"}
 - futile_offer_restaurant
* inform{"food": "italian"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - utter_bye

## Mar13_S1A1/voip-317a1436fe-20130325_171321
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "basque"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "basque"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "basque"}
 - offer_pricerange
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-317a1436fe-20130325_173537
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - utter_anything_else
* request{"address": "_REQUESTED_"}
 - utter_anything_else
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_anything_else
* negate
 - utter_anything_else
* bye
 - utter_bye

## Mar13_S0A1/voip-317a1436fe-20130325_174012
* inform{"food": "african", "pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - utter_anything_else
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-317a1436fe-20130325_171950
* inform{"food": "traditional"}
 - utter_request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-317a1436fe-20130325_173122
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"area": "south"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-88f198881b-20130326_032712
* inform{"food": "irish", "area": "centre"}
 - utter_request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-88f198881b-20130326_014111
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* inform{"area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-88f198881b-20130326_014812
* inform{"food": "steakhouse", "pricerange": "cheap"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-88f198881b-20130326_032851
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "chinese"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-0f41c16f2f-20130402_005145
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-0f41c16f2f-20130325_213659
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "mediterranean"}
 - utter_request_area
* inform{"area": "north"}
 - canthelp
* bye
 - utter_bye

## Mar13_S1A0/voip-0f41c16f2f-20130401_235338
* inform{"pricerange": "moderate", "area": "east"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0f41c16f2f-20130402_005015
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-0f41c16f2f-20130325_213819
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-0f41c16f2f-20130402_004841
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-0f41c16f2f-20130325_213951
* inform{"food": "fusion"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-0f41c16f2f-20130401_235748
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "north"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "fusion"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0f41c16f2f-20130401_235017
* inform{"food": "thai"}
 - utter_request_area
* inform{"area": "centre"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-0f41c16f2f-20130401_235542
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "german"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0f41c16f2f-20130401_235916
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "chinese"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-0f41c16f2f-20130402_000226
* inform{"pricerange": "cheap"}
 - confirm_summary
* affirm
 - utter_request_area
* inform{"area": "east"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0f41c16f2f-20130325_193614
* inform{"food": "seafood"}
 - utter_request_area
* inform{"area": "south"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-0f41c16f2f-20130402_004415
* inform{"food": "international"}
 - utter_request_area
* inform{"area": "dontcare"}
 - confirm_area
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-0f41c16f2f-20130325_193856
* inform{"food": "italian"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - canthelp
* bye
 - utter_bye

## Mar13_S0A1/voip-87de4f7a80-20130324_154621
* inform{"food": "basque", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* confirm{"food": "basque"}
 - utter_offer_area
* confirm{"food": "basque"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-87de4f7a80-20130324_154113
* inform{"food": "indian", "pricerange": "moderate"}
 - utter_request_food
* inform{"food": "indian"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - confirm_food
* affirm
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* confirm{"area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-87de4f7a80-20130324_153705
* inform{"area": "west"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-87de4f7a80-20130324_155006
* inform{"food": "korean", "area": "centre"}
 - confirm_area
* include_filter{"food": "korean"}
 - offer_restaurant
* confirm{"food": "korean"}
 - canthelp
* confirm{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-87de4f7a80-20130324_154807
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-202b6a3cc4-20130327_185502
* inform{"pricerange": "moderate"}
 - utter_request_area
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* inform{"area": "west"}
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-202b6a3cc4-20130327_185351
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-202b6a3cc4-20130327_184215
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - utter_select_food
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-202b6a3cc4-20130327_184721
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-ccf48b9a6a-20130329_042239
* inform{"area": "east"}
 - utter_select_area
* inform{"area": "east"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ccf48b9a6a-20130329_041327
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform{"food": "italian"}
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - offer_restaurant
* thankyou
 - offer_restaurant
* thankyou
 - utter_bye

## Mar13_S0A1/voip-ccf48b9a6a-20130329_053509
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-ccf48b9a6a-20130329_052518
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "north american"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-ccf48b9a6a-20130329_053241
* inform{"area": "centre"}
 - utter_request_area
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "world"}
 - canthelp
* request{"area": "_REQUESTED_"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "european"}
 - confirm_area
* affirm
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-ccf48b9a6a-20130329_053050
* inform{"food": "cantonese", "area": "west"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "italian"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-ccf48b9a6a-20130329_041830
* inform{"food": "french"}
 - utter_request_area
* inform{"area": "centre"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "french"}
 - utter_request_food
* inform{"food": "french"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-ccf48b9a6a-20130329_043420
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-15d8a89cec-20130327_021458
* inform{"food": "asian oriental", "area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - utter_offer_area
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-15d8a89cec-20130327_015041
* inform{"food": "australian", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-15d8a89cec-20130327_020255
* inform{"food": "international", "area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-15d8a89cec-20130327_020852
* inform{"food": "asian oriental"}
 - confirm_area
* affirm
 - confirm_food
* negate
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-15d8a89cec-20130327_014753
* inform{"food": "brazilian", "pricerange": "moderate"}
 - confirm_food
* affirm
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "asian oriental"}
 - utter_select_food
* bye
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-15d8a89cec-20130327_022535
* inform_dontcare
 - canthelp
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-15d8a89cec-20130327_015432
* inform{"food": "mexican"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - utter_anything_else
* request{"food": "mexican", "name": "chiquito restaurant bar", "area": "_REQUESTED_"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-15d8a89cec-20130327_020057
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - futile_offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"name": "prezzo", "address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-f1e8236264-20130323_002501
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-f1e8236264-20130323_003719
* inform{"food": "venetian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - confirm_food
* negate
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f1e8236264-20130323_003057
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-f1e8236264-20130323_002130
* inform{"food": "lebanese", "pricerange": "cheap"}
 - utter_request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-f1e8236264-20130323_004330
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-f1e8236264-20130323_002326
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-f1e8236264-20130323_004442
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f1e8236264-20130323_005548
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-f1e8236264-20130323_003523
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-7c3a08072d-20130326_005842
* inform{"food": "english"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* confirm{"area": "centre"}
 - futile_offer_restaurant
* confirm{"area": "centre"}
 - offer_restaurant
* inform{"food": "british", "area": "centre"}
 - confirm_area
* affirm
 - utter_select_price
* inform{"food": "british"}
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-7c3a08072d-20130326_005512
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-7c3a08072d-20130326_010113
* inform{"food": "gastropub"}
 - utter_request_food
* inform{"food": "gastropub"}
 - futile_offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* inform{"food": "gastropub"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-7c3a08072d-20130326_005642
* inform{"food": "afghan"}
 - canthelp
* inform{"area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-b08f15a787-20130402_072347
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare{"pricerange": "expensive"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-b08f15a787-20130402_075759
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "indian"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-b08f15a787-20130326_021953
* inform{"pricerange": "moderate", "area": "north"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b08f15a787-20130402_071415
* inform{"food": "unusual"}
 - utter_request_food
* inform{"food": "unusual"}
 - futile_offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* inform{"food": "unusual"}
 - offer_pricerange
* inform{"food": "unusual"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-b08f15a787-20130326_023412
* inform{"food": "german"}
 - canthelp
* inform{"food": "european"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-b08f15a787-20130402_074900
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-b08f15a787-20130326_023936
* inform{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-b08f15a787-20130402_075211
* inform{"food": "british"}
 - utter_select_price
* inform_dontcare{"area": "west"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-b08f15a787-20130326_021438
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-b08f15a787-20130402_074726
* inform{"food": "european"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-b08f15a787-20130402_072532
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare{"pricerange": "moderate"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-b08f15a787-20130326_022327
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b08f15a787-20130402_072705
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-b08f15a787-20130402_065804
* inform_dontcare
 - utter_offer_area
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-b08f15a787-20130402_070704
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-22756d9e8f-20130329_045435
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-22756d9e8f-20130329_044955
* inform{"food": "african", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-22756d9e8f-20130329_043954
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-22756d9e8f-20130329_045117
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-22756d9e8f-20130329_050412
* inform{"food": "swedish", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_pricerange
* confirm{"food": "korean"}
 - confirm_area
* affirm
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-22756d9e8f-20130328_170312
* inform{"food": "canapes", "pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* confirm{"food": "canapes"}
 - futile_offer_restaurant
* inform{"pricerange": "moderate"}
 - futile_offer_restaurant
* confirm{"food": "canapes"}
 - futile_offer_restaurant
* inform{"food": "indian"}
 - futile_offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* inform{"food": "indian"}
 - confirm_area
* confirm{"pricerange": "moderate"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-22756d9e8f-20130329_044234
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-22756d9e8f-20130329_050743
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-22756d9e8f-20130329_050114
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "romanian"}
 - utter_request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* confirm{"food": "thai"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-22756d9e8f-20130329_044622
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-22756d9e8f-20130329_050612
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "british"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-22756d9e8f-20130329_044511
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-22756d9e8f-20130329_043814
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "persian"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* inform{"food": "vietnamese"}
 - offer_restaurant
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0999e9bb30-20130325_124910
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform{"food": "scottish"}
 - utter_request_food
* inform{"food": "north american"}
 - confirm_food
* affirm
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-0999e9bb30-20130325_124715
* inform{"area": "dontcare"}
 - futile_offer_restaurant
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-dda7c88c6e-20130323_052950
* inform{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-dda7c88c6e-20130323_055048
* inform{"pricerange": "expensive"}
 - utter_request_food
* request{"area": "_REQUESTED_"}
 - utter_request_food
* inform{"food": "eritrean"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "expensive"}
 - offer_pricerange
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-dda7c88c6e-20130323_053057
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - no_more_options
* request{"phone": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-dda7c88c6e-20130323_053928
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-9735278861-20130401_153620
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-9735278861-20130401_160849
* inform{"food": "mexican"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-9735278861-20130401_154740
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-9735278861-20130401_161036
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-9735278861-20130401_161717
* inform{"food": "lebanese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-9735278861-20130401_151648
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "chinese"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-9735278861-20130401_161215
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-9735278861-20130401_154605
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-9735278861-20130402_140608
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-9735278861-20130401_155528
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-9735278861-20130401_154251
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - confirm_area
* affirm
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "thai"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-9735278861-20130401_152826
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - confirm_area
* affirm
 - confirm_food
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-9735278861-20130401_160600
* inform{"food": "english"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-7e22911804-20130327_200922
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

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
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-7e22911804-20130324_193050
* negate
 - utter_request_area
* inform{"food": "indonesian", "area": "north"}
 - confirm_area
* correct{"area": "north"}
 - confirm_food
* include_filter{"area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-7e22911804-20130326_142538
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* confirm{"food": "chinese"}
 - offer_restaurant
* inform{"food": "chinese"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-7e22911804-20130324_173542
* inform{"food": "greek"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-7e22911804-20130328_164203
* inform{"food": "swedish", "pricerange": "cheap"}
 - offer_pricerange
* confirm{"food": "swedish"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* confirm{"food": "asian oriental"}
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-7e22911804-20130325_202948
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-7e22911804-20130324_184843
* inform{"food": "brazilian"}
 - utter_request_area
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-7e22911804-20130328_162243
* inform{"pricerange": "cheap", "area": "south"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - utter_request_food
* thankyou
 - offer_pricerange
* inform{"area": "south"}
 - offer_restaurant
* correct{"area": "south"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-7e22911804-20130328_162140
* inform{"food": "lebanese", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-7e22911804-20130327_202516
* inform{"food": "thai", "area": "centre"}
 - utter_request_food
* inform{"food": "thai"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* negate
 - futile_offer_restaurant
* negate
 - futile_offer_restaurant
* inform{"food": "thai"}
 - utter_offer_area
* include_filter{"food": "thai"}
 - offer_restaurant
* confirm{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-7e22911804-20130328_204851
* inform{"pricerange": "cheap", "area": "east"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - futile_offer_restaurant
* confirm{"area": "east"}
 - utter_offer_area
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-7e22911804-20130328_161325
* inform{"area": "west"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - utter_select_price
* inform_dontcare
 - futile_offer_restaurant
* confirm{"area": "west"}
 - offer_restaurant
* inform{"food": "thai", "area": "west"}
 - utter_offer_area
* confirm{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-7e22911804-20130328_204150
* inform_dontcare{"food": "traditional"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french"}
 - confirm_area
* include_filter{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-7e22911804-20130328_162643
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - offer_pricerange
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-7e22911804-20130324_190421
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-7e22911804-20130325_200320
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-7e22911804-20130328_203706
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* negate
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-7e22911804-20130328_204351
* affirm
 - utter_select_price
* inform{"pricerange": "cheap", "area": "north"}
 - confirm_food
* affirm
 - offer_pricerange
* inform{"area": "north"}
 - offer_pricerange
* inform{"area": "north"}
 - offer_pricerange
* inform{"area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-876ef67873-20130402_032159
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "african"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-876ef67873-20130327_035756
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-876ef67873-20130402_030352
* inform{"area": "east"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-876ef67873-20130327_040247
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - futile_offer_restaurant
* inform{"area": "north"}
 - utter_offer_area
* reqalts
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-876ef67873-20130327_035558
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-876ef67873-20130327_035101
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "singaporean"}
 - offer_restaurant
* inform{"food": "singaporean"}
 - offer_restaurant
* inform{"food": "european"}
 - futile_offer_restaurant
* thankyou
 - no_more_options
* bye
 - utter_bye

## Mar13_S1A1/voip-876ef67873-20130402_031718
* affirm
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "danish"}
 - canthelp
* inform{"food": "mediterranean"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-876ef67873-20130402_033525
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-876ef67873-20130402_033954
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "thai"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-876ef67873-20130402_030744
* inform{"food": "world", "pricerange": "moderate"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-d225fad9df-20130328_201024
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-d225fad9df-20130328_183716
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform{"food": "italian"}
 - canthelp
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "dontcare", "pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-d225fad9df-20130328_200758
* inform{"area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-d225fad9df-20130328_205512
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "north american"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"area": "south"}
 - canthelp
* inform{"pricerange": "expensive", "area": "south"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-d225fad9df-20130328_205817
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform{"food": "spanish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-d225fad9df-20130328_175010
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-d225fad9df-20130328_201303
* inform{"food": "english", "area": "west"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-d225fad9df-20130328_183352
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-d225fad9df-20130328_175805
* inform{"food": "moroccan", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-d225fad9df-20130328_203254
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-d225fad9df-20130328_175224
* inform{"food": "german"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-31d9d1a567-20130402_042843
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-31d9d1a567-20130402_035757
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-31d9d1a567-20130402_042614
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-31d9d1a567-20130402_041025
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-31d9d1a567-20130402_035524
* inform{"food": "belgian", "area": "north"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-31d9d1a567-20130402_041209
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"area": "north"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-31d9d1a567-20130402_040402
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-31d9d1a567-20130402_035950
* inform{"food": "canapes", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-31d9d1a567-20130402_034546
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-31d9d1a567-20130402_042138
* inform{"food": "turkish", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-31d9d1a567-20130402_034915
* inform{"food": "gastropub", "pricerange": "dontcare"}
 - confirm_summary
* include_filter{"food": "gastropub"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-31d9d1a567-20130402_034022
* inform{"food": "tuscan", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian", "pricerange": "cheap"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-a31ca3e355-20130324_190654
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* affirm
 - offer_pricerange
* inform{"food": "swiss"}
 - futile_offer_restaurant
* inform{"food": "swiss"}
 - futile_offer_restaurant
* inform{"food": "british"}
 - futile_offer_restaurant
* inform{"food": "british"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-a31ca3e355-20130323_223152
* inform{"area": "centre"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - utter_anything_else
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-a31ca3e355-20130323_223338
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-a31ca3e355-20130323_222931
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* inform{"food": "scandinavian"}
 - canthelp
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - canthelp
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - canthelp
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-a31ca3e355-20130324_190831
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-a31ca3e355-20130323_223643
* inform{"food": "international"}
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

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
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - canthelp
* bye
 - utter_bye

## Mar13_S0A0/voip-3b3edac94d-20130326_004101
* inform{"food": "german", "area": "centre"}
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-3b3edac94d-20130326_003522
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-3b3edac94d-20130326_004002
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3b3edac94d-20130324_211737
* inform{"food": "caribbean", "pricerange": "cheap"}
 - offer_pricerange
* confirm{"food": "caribbean"}
 - offer_restaurant
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "indian"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-3b3edac94d-20130324_201732
* inform{"food": "french", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-3b3edac94d-20130323_203121
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-3b3edac94d-20130324_202932
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-3b3edac94d-20130323_201535
* inform{"pricerange": "moderate", "area": "north"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3b3edac94d-20130323_202936
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-3b3edac94d-20130324_210908
* inform{"food": "austrian", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-3b3edac94d-20130324_203209
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-3b3edac94d-20130324_211848
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-3b3edac94d-20130326_004204
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-3b3edac94d-20130323_202743
* inform{"food": "french"}
 - offer_restaurant
* reqalts
 - confirm_food
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-3b3edac94d-20130324_202415
* inform{"food": "jamaican", "area": "south"}
 - utter_request_food
* inform{"food": "jamaican"}
 - utter_request_food
* inform{"food": "jamaican"}
 - utter_select_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese", "area": "south"}
 - canthelp
* inform{"food": "chinese", "area": "south"}
 - utter_select_food
* correct{"food": "chinese"}
 - utter_select_food
* inform{"food": "chinese"}
 - confirm_food
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-3b3edac94d-20130324_202802
* inform{"food": "swiss", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-3b3edac94d-20130326_004303
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-3b3edac94d-20130323_203738
* inform{"food": "mediterranean", "area": "dontcare"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - utter_offer_area
* confirm{"food": "mediterranean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-a352cb5ca5-20130401_234557
* inform{"pricerange": "moderate"}
 - futile_offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-a352cb5ca5-20130401_232817
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-a352cb5ca5-20130401_234753
* inform{"area": "centre"}
 - utter_select_price
* inform{"area": "centre"}
 - utter_select_price
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-a352cb5ca5-20130401_231740
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-a352cb5ca5-20130401_234216
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "barbeque"}
 - utter_request_food
* inform{"food": "barbeque"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - confirm_summary
* affirm
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-a352cb5ca5-20130401_234944
* inform{"food": "singaporean"}
 - offer_restaurant
* inform{"food": "singaporean"}
 - offer_restaurant
* inform{"area": "south"}
 - canthelp
* inform{"food": "italian"}
 - confirm_food
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-a352cb5ca5-20130401_231236
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-8f9fb7a86b-20130328_183857
* inform{"food": "tuscan", "area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "tuscan"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - utter_offer_area
* request{"phone": "_REQUESTED_"}
 - utter_offer_area
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-8f9fb7a86b-20130328_185140
* inform{"food": "scandinavian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-8f9fb7a86b-20130328_182235
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"food": "moroccan"}
 - utter_request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-8f9fb7a86b-20130328_184241
* inform{"food": "japanese", "pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-8f9fb7a86b-20130328_184820
* inform{"food": "portuguese", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "portuguese"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-8f9fb7a86b-20130328_182710
* inform{"food": "danish", "area": "south"}
 - confirm_food
* include_filter{"area": "south"}
 - canthelp
* inform{"food": "italian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"postcode": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-8f9fb7a86b-20130328_184504
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-8f9fb7a86b-20130328_181534
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "thai"}
 - utter_select_food
* inform{"food": "thai"}
 - utter_select_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* inform{"name": "prezzo"}
 - utter_select_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "thai"}
 - confirm_food
* affirm
 - offer_restaurant
* inform{"name": "prezzo"}
 - no_more_options
* confirm{"name": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* ack
 - offer_restaurant
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-155e939ebc-20130327_203952
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-155e939ebc-20130327_204114
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-155e939ebc-20130327_202425
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-155e939ebc-20130327_203006
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "european"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-155e939ebc-20130327_203543
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-155e939ebc-20130327_211511
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-155e939ebc-20130327_203128
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-00d76b791d-20130327_011740
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-00d76b791d-20130327_005023
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "modern european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-00d76b791d-20130327_004513
* inform{"food": "creative", "pricerange": "moderate"}
 - canthelp
* inform{"food": "modern european"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-00d76b791d-20130327_012807
* inform{"food": "venetian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-00d76b791d-20130327_012331
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-00d76b791d-20130327_010416
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-00d76b791d-20130327_010906
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-00d76b791d-20130327_011609
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-00d76b791d-20130327_012711
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-00d76b791d-20130327_011116
* inform{"food": "lebanese", "area": "west"}
 - utter_request_food
* inform{"food": "lebanese"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - utter_anything_else
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-00d76b791d-20130327_003853
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-0abf414c0c-20130327_000359
* inform{"food": "gastropub"}
 - utter_request_food
* inform{"food": "gastropub"}
 - futile_offer_restaurant
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0abf414c0c-20130326_235444
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0abf414c0c-20130326_235059
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - utter_anything_else
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - utter_anything_else
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-4b7e22cc07-20130401_185110
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4b7e22cc07-20130401_185640
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "crossover"}
 - utter_request_food
* inform{"food": "crossover"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - confirm_area
* inform{"food": "modern european"}
 - utter_select_food
* inform{"food": "modern european"}
 - utter_select_food
* inform{"food": "modern european"}
 - utter_select_food
* inform{"food": "european"}
 - utter_select_food
* inform{"food": "modern european"}
 - utter_select_food
* inform{"food": "modern european"}
 - utter_select_food
* bye
 - confirm_food
* negate
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "modern european"}
 - confirm_area
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-f32f2cfdae-20130327_013132
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - confirm_food
* affirm
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f32f2cfdae-20130328_195839
* inform{"food": "eritrean", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-f32f2cfdae-20130327_013402
* inform{"food": "african"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f32f2cfdae-20130327_015652
* inform{"food": "catalan", "pricerange": "cheap"}
 - utter_request_food
* inform{"food": "catalan"}
 - utter_request_food
* inform{"food": "catalan"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-f32f2cfdae-20130328_195220
* inform{"area": "centre"}
 - utter_offer_area
* inform{"food": "romanian"}
 - utter_offer_area
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f32f2cfdae-20130327_020400
* inform{"food": "caribbean", "area": "south"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_192506
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_postcode
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f32f2cfdae-20130328_193321
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_restaurant
* inform{"food": "gastropub"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-f32f2cfdae-20130327_012823
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-f32f2cfdae-20130328_195409
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-f32f2cfdae-20130328_192703
* inform{"food": "chinese"}
 - utter_request_area
* inform{"food": "seafood"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "seafood"}
 - utter_request_food
* inform{"food": "seafood"}
 - offer_restaurant
* inform{"food": "seafood"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-f32f2cfdae-20130327_015332
* inform{"food": "polish"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-f32f2cfdae-20130328_194348
* inform{"food": "spanish", "pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-f32f2cfdae-20130328_200054
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_200431
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* inform{"food": "portuguese", "pricerange": "cheap"}
 - offer_postcode
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-f32f2cfdae-20130328_194814
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_194522
* inform{"food": "japanese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-f32f2cfdae-20130327_015213
* inform{"food": "crossover", "area": "north"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-f32f2cfdae-20130327_014628
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-f32f2cfdae-20130328_193841
* bye
 - utter_request_area
* inform{"food": "turkish"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "turkish"}
 - futile_offer_restaurant
* inform{"food": "turkish"}
 - offer_restaurant
* inform{"food": "turkish"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-f32f2cfdae-20130327_014457
* inform{"food": "english", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-f32f2cfdae-20130328_193606
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-f32f2cfdae-20130327_013713
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-381a50592b-20130326_035922
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "indian"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-381a50592b-20130326_040146
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-381a50592b-20130323_234808
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-381a50592b-20130324_000124
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - futile_offer_restaurant
* inform{"food": "british"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-381a50592b-20130324_000330
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-381a50592b-20130323_233220
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "seafood"}
 - offer_pricerange
* inform{"food": "seafood"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-381a50592b-20130326_043646
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-381a50592b-20130323_233439
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-381a50592b-20130326_040928
* inform{"food": "gastropub"}
 - utter_select_price
* inform_dontcare
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-381a50592b-20130326_040539
* inform{"food": "danish"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-381a50592b-20130326_043059
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-381a50592b-20130326_044413
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "cuban"}
 - utter_request_food
* inform{"food": "cuban"}
 - utter_request_food
* inform{"food": "cuban"}
 - utter_request_food
* inform{"food": "cuban"}
 - confirm_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-381a50592b-20130326_044146
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-381a50592b-20130326_043457
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-381a50592b-20130323_234249
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-381a50592b-20130323_235612
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-381a50592b-20130326_040051
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-381a50592b-20130323_234506
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

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
 - utter_request_area
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-381a50592b-20130326_041932
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - no_more_options
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-922209b777-20130325_160523
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-922209b777-20130325_162603
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-922209b777-20130327_004402
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-922209b777-20130325_163924
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-922209b777-20130325_162222
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-922209b777-20130325_160004
* inform{"food": "canapes", "area": "west"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-922209b777-20130327_012955
* inform{"food": "seafood", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-922209b777-20130327_013531
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-922209b777-20130327_004226
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-922209b777-20130327_011149
* inform{"food": "thai", "pricerange": "moderate"}
 - utter_select_area
* inform_dontcare
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-922209b777-20130325_160141
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-922209b777-20130325_155209
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-922209b777-20130327_011354
* inform{"area": "east"}
 - futile_offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-922209b777-20130327_005342
* inform{"area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "creative"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - utter_select_price
* inform_dontcare
 - confirm_area
* affirm
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-922209b777-20130325_161023
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-922209b777-20130327_011455
* inform{"food": "european", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-922209b777-20130325_162946
* inform{"food": "international", "pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-922209b777-20130325_162423
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-922209b777-20130327_012258
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - utter_request_area
* inform{"food": "thai"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - canthelp
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-922209b777-20130326_140616
* inform{"food": "gastropub", "pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-ccc459b689-20130327_002730
* inform{"area": "north"}
 - confirm_food
* affirm
 - futile_offer_restaurant
* inform{"area": "north"}
 - utter_offer_area
* inform{"food": "japanese", "area": "north"}
 - canthelp
* inform{"food": "indian", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-ccc459b689-20130327_004851
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-ccc459b689-20130327_004727
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-ccc459b689-20130327_004458
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* confirm{"food": "european"}
 - offer_pricerange
* confirm{"food": "european"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-ccc459b689-20130327_004041
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "modern european"}
 - confirm_area
* affirm
 - utter_select_food
* inform{"food": "modern european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-bde2721237-20130326_200257
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-bde2721237-20130325_162942
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-bde2721237-20130326_194753
* inform{"food": "moroccan"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "moroccan"}
 - utter_request_food
* inform{"food": "moroccan"}
 - utter_request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-bde2721237-20130326_194022
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "mediterranean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-bde2721237-20130326_193127
* inform{"food": "irish", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-bde2721237-20130325_164032
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-bde2721237-20130326_193025
* inform{"food": "world"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-bde2721237-20130326_192751
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-bde2721237-20130325_154829
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-bde2721237-20130326_200505
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-bde2721237-20130325_161826
* inform{"food": "french", "area": "centre"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-bde2721237-20130325_162740
* inform{"food": "belgian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - utter_request_area
* inform{"area": "north"}
 - canthelp
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-bde2721237-20130325_162622
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-bde2721237-20130325_155806
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-bde2721237-20130326_195337
* inform{"food": "gastropub"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "gastropub"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-bde2721237-20130326_193743
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"food": "english"}
 - canthelp
* inform{"food": "italian"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-bde2721237-20130326_195733
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "north"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-bde2721237-20130325_155143
* inform{"area": "south"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "mexican"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-78f497f314-20130323_184557
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-78f497f314-20130324_202309
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-78f497f314-20130323_184435
* inform{"area": "dontcare"}
 - utter_select_price
* inform_dontcare
 - utter_offer_area
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-78f497f314-20130324_201554
* inform{"food": "creative", "pricerange": "cheap"}
 - canthelp
* inform{"food": "creative"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - utter_select_food
* inform{"food": "mediterranean"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-78f497f314-20130324_201211
* inform{"food": "persian", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-78f497f314-20130324_200748
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "north american"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-78f497f314-20130324_203101
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-78f497f314-20130323_143533
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-78f497f314-20130323_184250
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-78f497f314-20130324_200619
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "vietnamese"}
 - confirm_food
* correct{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-78f497f314-20130323_184110
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-78f497f314-20130323_144139
* inform{"pricerange": "moderate"}
 - offer_pricerange
* confirm{"food": "indonesian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-78f497f314-20130323_142856
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-88b68a9a41-20130322_221424
* inform{"food": "canapes", "area": "dontcare"}
 - utter_request_food
* inform{"food": "canapes"}
 - utter_request_food
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "modern european"}
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-88b68a9a41-20130323_114000
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "turkish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-88b68a9a41-20130322_223613
* inform{"food": "australian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-88b68a9a41-20130324_002417
* inform{"food": "mediterranean", "area": "centre"}
 - canthelp
* inform{"food": "mediterranean", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-88b68a9a41-20130324_004148
* inform{"food": "cuban", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-88b68a9a41-20130324_004748
* inform{"food": "traditional", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-88b68a9a41-20130324_004031
* inform{"food": "cuban", "area": "south"}
 - utter_request_food
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-88b68a9a41-20130322_221603
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-88b68a9a41-20130322_221256
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-88b68a9a41-20130322_222845
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "modern european"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-88b68a9a41-20130324_002917
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-88b68a9a41-20130322_224608
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-88b68a9a41-20130324_003144
* inform{"food": "japanese", "area": "south"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "japanese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-88b68a9a41-20130324_002132
* inform{"food": "danish", "area": "west"}
 - canthelp
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-88b68a9a41-20130322_222725
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-88b68a9a41-20130324_004639
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-88b68a9a41-20130324_003412
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-88b68a9a41-20130324_002251
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-88b68a9a41-20130322_224115
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-88b68a9a41-20130324_003525
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "polynesian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-88b68a9a41-20130322_222344
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - utter_select_food
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-bb1fd497eb-20130325_165023
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-bb1fd497eb-20130325_131052
* inform{"food": "turkish", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_232136
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "greek"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-bb1fd497eb-20130326_230444
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-bb1fd497eb-20130325_132300
* inform{"food": "hungarian", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-bb1fd497eb-20130326_232439
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - utter_offer_area
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-bb1fd497eb-20130325_164823
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "spanish"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-bb1fd497eb-20130326_120755
* inform{"food": "vegetarian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "indian"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-bb1fd497eb-20130325_123757
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_233411
* inform{"area": "dontcare"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-bb1fd497eb-20130325_163241
* inform{"food": "malaysian", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-bb1fd497eb-20130325_164128
* inform{"food": "african"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-bb1fd497eb-20130325_163635
* inform{"food": "basque", "area": "east"}
 - utter_request_food
* inform{"food": "basque"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_223048
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-bb1fd497eb-20130326_230746
* inform{"food": "spanish", "pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish"}
 - confirm_food
* affirm
 - offer_pricerange
* inform{"food": "spanish"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - utter_bye

## Mar13_S0A0/voip-bb1fd497eb-20130326_231219
* inform{"food": "seafood"}
 - utter_request_food
* inform{"food": "seafood"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* inform{"food": "seafood"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-bb1fd497eb-20130325_164421
* inform{"food": "brazilian"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-bb1fd497eb-20130326_233115
* inform{"food": "venetian"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "venetian"}
 - utter_request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - confirm_food
* affirm
 - confirm_area
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-bb1fd497eb-20130326_231928
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "british"}
 - canthelp
* inform{"food": "indian"}
 - confirm_food
* affirm
 - utter_select_price
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-bb1fd497eb-20130326_230547
* inform{"food": "corsica", "area": "west"}
 - utter_request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai"}
 - confirm_area
* affirm
 - utter_select_food
* inform{"food": "thai"}
 - offer_restaurant
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-bb1fd497eb-20130325_163956
* inform{"food": "vietnamese"}
 - confirm_food
* affirm
 - futile_offer_restaurant
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - utter_anything_else
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-03c2655d43-20130327_194746
* inform{"food": "international", "pricerange": "moderate"}
 - offer_pricerange
* reqalts
 - confirm_food
* inform{"pricerange": "moderate"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03c2655d43-20130327_195421
* inform{"food": "basque", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - confirm_food
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03c2655d43-20130327_195546
* inform{"food": "creative", "area": "west"}
 - confirm_area
* include_filter{"food": "creative"}
 - canthelp
* inform{"food": "italian"}
 - confirm_food
* include_filter{"area": "west"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-03c2655d43-20130327_193309
* inform{"food": "persian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-03c2655d43-20130327_201323
* inform{"food": "seafood"}
 - utter_request_area
* inform_dontcare
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-03c2655d43-20130327_193528
* inform{"food": "welsh", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - confirm_food
* inform{"food": "british"}
 - utter_request_area
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-03c2655d43-20130327_194221
* inform{"food": "international", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03c2655d43-20130327_191742
* inform{"food": "european", "pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* thankyou
 - offer_pricerange
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* reqalts
 - offer_pricerange
* inform{"pricerange": "expensive"}
 - offer_pricerange
* inform{"pricerange": "expensive"}
 - offer_pricerange
* thankyou
 - offer_pricerange
* thankyou
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-03c2655d43-20130327_200522
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03c2655d43-20130327_194616
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03c2655d43-20130327_192312
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "swiss"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-03c2655d43-20130327_200023
* inform{"food": "chinese", "pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-03c2655d43-20130327_195308
* inform{"area": "north"}
 - utter_request_area
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-d0341706f2-20130329_022056
* inform{"food": "italian", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_select_price
* negate
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-d0341706f2-20130329_053021
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - futile_offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-d0341706f2-20130329_012808
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-d0341706f2-20130329_052240
* inform{"food": "afghan", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - confirm_area
* inform{"area": "east"}
 - utter_select_food
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-d0341706f2-20130329_021540
* request{"pricerange": "moderate", "area": "south", "address": "_REQUESTED_"}
 - confirm_ask_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-d0341706f2-20130329_021425
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-d0341706f2-20130329_052605
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-d0341706f2-20130329_051653
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-d0341706f2-20130329_052031
* inform{"food": "bistro", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* inform{"food": "italian"}
 - offer_restaurant
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-d0341706f2-20130329_021901
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-3b81cbb287-20130324_215534
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-3b81cbb287-20130324_015653
* inform{"food": "world"}
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-3b81cbb287-20130326_030605
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-3b81cbb287-20130326_030827
* inform{"food": "african", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-3b81cbb287-20130326_031714
* inform{"food": "world"}
 - canthelp
* inform{"food": "thai"}
 - canthelp
* inform{"food": "thai", "pricerange": "dontcare"}
 - confirm_food
* inform{"food": "thai"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-3b81cbb287-20130324_020817
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3b81cbb287-20130324_014336
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-3b81cbb287-20130324_020125
* inform{"food": "basque", "pricerange": "expensive"}
 - canthelp
* inform{"food": "korean"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-3b81cbb287-20130326_024829
* inform{"food": "thai", "area": "centre"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-3b81cbb287-20130324_014713
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "european"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-3b81cbb287-20130326_025919
* inform{"food": "malaysian", "area": "south"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* confirm{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-3b81cbb287-20130324_020944
* inform{"food": "international", "pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3b81cbb287-20130326_024219
* inform{"food": "basque", "pricerange": "moderate"}
 - canthelp
* inform{"food": "british"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3b81cbb287-20130326_025552
* inform{"food": "japanese", "pricerange": "moderate"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - offer_pricerange
* inform{"food": "european", "pricerange": "moderate"}
 - utter_select_food
* affirm
 - offer_pricerange
* inform{"food": "modern european"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "modern european"}
 - confirm_area
* confirm{"pricerange": "moderate"}
 - utter_select_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3b81cbb287-20130326_031529
* inform{"food": "danish", "area": "centre"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-3b81cbb287-20130324_022110
* inform{"food": "french"}
 - offer_restaurant
* request{"pricerange": "dontcare", "address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-3b81cbb287-20130324_021600
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-3b81cbb287-20130324_014857
* inform{"food": "traditional", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3b81cbb287-20130324_015234
* inform{"food": "scottish", "area": "west"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "scottish"}
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* confirm{"food": "indian"}
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-3be3bda933-20130326_132152
* inform{"food": "french", "pricerange": "moderate"}
 - utter_request_food
* inform{"food": "french"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - confirm_ask_area
* inform_dontcare
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-3be3bda933-20130326_125503
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-3be3bda933-20130326_131833
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - futile_offer_restaurant
* inform{"area": "west"}
 - futile_offer_restaurant
* inform{"area": "west"}
 - futile_offer_restaurant
* inform_dontcare
 - offer_restaurant
* inform{"area": "east"}
 - utter_select_area
* inform{"area": "south"}
 - utter_select_area
* inform{"area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-3be3bda933-20130327_014120
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* inform_dontcare
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* reqalts
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* inform{"area": "south"}
 - offer_restaurant
* inform{"area": "west"}
 - offer_restaurant
* inform{"area": "west"}
 - confirm_food
* inform{"area": "west"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* inform{"area": "south"}
 - futile_offer_restaurant
* inform_dontcare
 - offer_restaurant
* inform{"area": "west"}
 - offer_restaurant
* inform{"area": "west"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-3be3bda933-20130327_015627
* inform{"food": "french", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "french"}
 - canthelp
* inform{"pricerange": "expensive"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* reqalts
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-3be3bda933-20130327_014928
* inform{"food": "international", "area": "east"}
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-3be3bda933-20130326_131651
* inform{"pricerange": "cheap", "area": "north"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* thankyou
 - offer_restaurant
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-3be3bda933-20130326_125353
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130401_222446
* inform{"food": "english"}
 - canthelp
* inform{"food": "italian"}
 - utter_request_area
* inform{"area": "south"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130401_221503
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-90732b027d-20130401_215559
* inform{"food": "italian"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130401_194905
* inform{"area": "east"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130401_195256
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-90732b027d-20130327_183400
* inform{"area": "east"}
 - futile_offer_restaurant
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-90732b027d-20130401_215804
* inform{"food": "seafood"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-90732b027d-20130327_190536
* inform{"pricerange": "dontcare"}
 - offer_pricerange
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-90732b027d-20130327_174703
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "british"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-90732b027d-20130401_222250
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-90732b027d-20130327_180737
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "portuguese"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-90732b027d-20130327_181557
* inform{"food": "greek"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-90732b027d-20130327_181126
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-90732b027d-20130401_215925
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "modern european"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130327_170938
* inform{"food": "danish", "area": "west"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130401_220530
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130327_184229
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "italian"}
 - confirm_food
* negate
 - confirm_summary
* negate
 - canthelp
* inform{"food": "italian"}
 - confirm_summary
* inform{"pricerange": "dontcare"}
 - confirm_summary
* negate
 - confirm_summary
* negate
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-90732b027d-20130328_164236
* inform{"food": "tuscan"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "tuscan"}
 - canthelp
* inform{"food": "thai"}
 - confirm_area
* affirm
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-90732b027d-20130401_222034
* inform{"food": "mexican"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-90732b027d-20130327_190004
* inform{"food": "greek"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* inform{"area": "centre"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-90732b027d-20130401_195651
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-90732b027d-20130327_190315
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - futile_offer_restaurant
* inform{"pricerange": "cheap"}
 - futile_offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-90732b027d-20130401_221049
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-90732b027d-20130327_183925
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-90732b027d-20130327_173620
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "dontcare"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "asian oriental"}
 - utter_select_food
* inform{"food": "asian oriental"}
 - offer_restaurant
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-f091d0e461-20130327_210252
* inform{"area": "east"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-f091d0e461-20130327_211411
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-f091d0e461-20130327_205009
* include_filter{"food": "kosher", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-f091d0e461-20130327_210653
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f091d0e461-20130327_211146
* inform{"food": "lebanese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f091d0e461-20130327_205249
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f091d0e461-20130327_210851
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* correct{"food": "asian oriental"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-340dbb333e-20130327_011501
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-340dbb333e-20130325_230536
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-340dbb333e-20130325_231720
* inform{"food": "turkish", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-340dbb333e-20130327_004847
* inform{"pricerange": "expensive"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - futile_offer_restaurant
* inform{"area": "south"}
 - utter_offer_area
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"pricerange": "expensive"}
 - offer_pricerange
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-340dbb333e-20130325_233510
* inform{"food": "mediterranean", "pricerange": "expensive"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "mediterranean"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-340dbb333e-20130327_011550
* inform{"food": "indian", "pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-340dbb333e-20130325_231846
* inform{"pricerange": "cheap", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-340dbb333e-20130325_232333
* inform{"food": "eritrean", "area": "west"}
 - utter_request_food
* inform{"food": "eritrean"}
 - utter_request_food
* inform{"food": "italian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-340dbb333e-20130327_011403
* inform{"food": "international"}
 - utter_request_food
* inform{"food": "international"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-340dbb333e-20130325_231614
* inform{"food": "african"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "african"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-340dbb333e-20130327_012037
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-340dbb333e-20130327_004741
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "british"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-340dbb333e-20130327_011703
* inform{"food": "canapes", "area": "north"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-340dbb333e-20130325_233348
* inform{"food": "japanese", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-340dbb333e-20130325_233821
* inform{"food": "indian", "pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "indian"}
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-318851c80b-20130328_224338
* inform{"food": "basque"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "basque"}
 - canthelp
* inform{"food": "spanish"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-318851c80b-20130328_220608
* inform{"food": "greek"}
 - canthelp
* inform{"food": "korean"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-318851c80b-20130328_214947
* inform{"food": "european", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-318851c80b-20130328_214609
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-318851c80b-20130328_224511
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "canapes"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"food": "canapes"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-318851c80b-20130328_224701
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-318851c80b-20130328_214057
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-318851c80b-20130328_220743
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-318851c80b-20130328_220341
* inform{"food": "hungarian", "pricerange": "cheap"}
 - canthelp
* negate
 - canthelp
* inform{"food": "modern european"}
 - confirm_food
* inform{"food": "modern european"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-36440f7305-20130326_201757
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "asian oriental"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-36440f7305-20130327_201555
* inform{"food": "thai"}
 - utter_select_price
* inform{"area": "west"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-36440f7305-20130326_140907
* inform{"food": "tuscan"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - offer_pricerange
* inform{"pricerange": "moderate"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-36440f7305-20130327_200335
* inform{"food": "japanese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - utter_anything_else
* request{"phone": "_REQUESTED_"}
 - utter_anything_else
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_anything_else
* bye
 - utter_anything_else
* bye
 - utter_bye

## Mar13_S1A0/voip-36440f7305-20130327_200608
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-36440f7305-20130327_201745
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-36440f7305-20130327_195221
* inform{"food": "spanish", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "spanish"}
 - utter_request_food
* inform{"food": "spanish"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* thankyou
 - futile_offer_restaurant
* ack
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-36440f7305-20130326_141231
* inform{"food": "mexican"}
 - utter_request_food
* inform{"food": "mexican"}
 - offer_restaurant
* affirm
 - utter_anything_else
* request{"pricerange": "_REQUESTED_", "address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-36440f7305-20130327_194928
* inform{"area": "south"}
 - utter_request_food
* inform{"pricerange": "expensive"}
 - futile_offer_restaurant
* reqalts
 - futile_offer_restaurant
* reqalts
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-36440f7305-20130327_200102
* inform{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-36440f7305-20130326_200035
* inform{"food": "mexican"}
 - utter_request_food
* inform{"food": "mexican"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-36440f7305-20130326_142415
* inform{"food": "kosher", "area": "centre"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-a8649977cf-20130323_161909
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "british"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-a8649977cf-20130323_161257
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "italian"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-a8649977cf-20130323_155614
* inform{"food": "international", "area": "dontcare"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-a8649977cf-20130323_160436
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-a8649977cf-20130323_155424
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"area": "north"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-a8649977cf-20130323_160845
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-a8649977cf-20130323_160201
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - confirm_food
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-a8649977cf-20130323_160311
* inform{"food": "mediterranean", "pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-2f209793f4-20130326_005104
* inform{"food": "basque"}
 - canthelp
* inform{"food": "international"}
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-2f209793f4-20130326_005217
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "chinese"}
 - confirm_food
* negate
 - canthelp
* inform{"food": "chinese", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2f209793f4-20130326_004451
* inform{"food": "european", "pricerange": "dontcare"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "european"}
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2f209793f4-20130326_004858
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-2f209793f4-20130326_012033
* inform{"food": "hungarian", "pricerange": "cheap"}
 - confirm_summary
* affirm
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-2f209793f4-20130326_003256
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "south"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-f17e3b578c-20130328_174844
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "vegetarian"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f17e3b578c-20130328_173556
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-f17e3b578c-20130328_171738
* affirm
 - utter_request_area
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "british"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"pricerange": "moderate"}
 - confirm_summary
* affirm
 - canthelp
* inform{"pricerange": "moderate"}
 - confirm_area
* affirm
 - confirm_summary
* affirm
 - offer_restaurant
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* thankyou
 - futile_offer_restaurant
* ack
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-f17e3b578c-20130328_180105
* inform{"food": "cuban", "area": "dontcare"}
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-f17e3b578c-20130328_174548
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-f17e3b578c-20130328_174111
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f17e3b578c-20130328_173326
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "french"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_151857
* inform{"food": "german", "area": "north"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130328_125036
* inform{"food": "spanish", "area": "centre"}
 - utter_select_area
* inform{"area": "centre"}
 - confirm_area
* include_filter{"food": "spanish"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130329_151950
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130328_124608
* inform{"food": "spanish"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - futile_offer_restaurant
* reqalts
 - futile_offer_restaurant
* inform{"food": "spanish"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - no_more_options
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130328_125150
* inform{"food": "basque"}
 - canthelp
* inform{"food": "spanish"}
 - utter_select_food
* inform{"food": "spanish"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130328_121012
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130329_153643
* inform{"food": "lebanese", "area": "centre"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_151331
* inform{"food": "japanese", "pricerange": "cheap"}
 - canthelp
* inform{"food": "italian"}
 - offer_pricerange
* inform{"food": "italian"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130328_124458
* inform{"food": "afghan"}
 - canthelp
* inform{"food": "french"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130329_153749
* inform{"pricerange": "moderate", "area": "north"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130328_121706
* inform{"food": "african", "area": "centre"}
 - canthelp
* inform{"food": "african"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130328_120337
* inform{"food": "spanish"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* inform{"food": "spanish"}
 - offer_restaurant
* negate
 - offer_restaurant
* reqalts
 - offer_restaurant
* inform{"food": "spanish"}
 - offer_restaurant
* negate
 - offer_restaurant
* negate
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130328_124342
* inform{"food": "hungarian", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - utter_select_price
* inform_dontcare
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_124921
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "indian"}
 - confirm_food
* include_filter{"food": "indian"}
 - utter_select_price
* inform_dontcare{"area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_154425
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_123700
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_153858
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130329_152505
* inform{"food": "christmas", "area": "north"}
 - canthelp
* inform{"food": "indian"}
 - utter_request_area
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_120628
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-4a6ecc1f1c-20130329_153244
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-4a6ecc1f1c-20130328_121528
* inform{"food": "creative", "area": "south"}
 - confirm_food
* include_filter{"area": "south"}
 - canthelp
* inform{"food": "chinese", "area": "south"}
 - offer_restaurant
* inform{"food": "chinese"}
 - futile_offer_restaurant
* confirm{"food": "chinese"}
 - offer_restaurant
* inform{"food": "chinese"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-4a6ecc1f1c-20130328_120903
* inform{"food": "gastropub", "area": "east"}
 - utter_request_food
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-4a6ecc1f1c-20130329_154219
* inform{"food": "russian", "pricerange": "moderate"}
 - offer_pricerange
* inform{"food": "russian"}
 - canthelp
* inform{"food": "chinese"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0241bbae39-20130327_201053
* inform_dontcare
 - utter_request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "indian"}
 - confirm_food
* affirm
 - utter_select_price
* inform{"pricerange": "cheap"}
 - confirm_summary
* negate
 - confirm_area
* affirm
 - confirm_summary
* negate
 - offer_restaurant
* inform{"area": "south"}
 - confirm_area
* correct{"pricerange": "cheap"}
 - canthelp
* inform_dontcare
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "indian"}
 - confirm_summary
* affirm
 - canthelp
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - no_more_options
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-0241bbae39-20130327_193939
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "eritrean"}
 - canthelp
* inform{"food": "eritrean"}
 - canthelp
* inform{"food": "eritrean"}
 - offer_restaurant
* inform{"food": "asian oriental", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0241bbae39-20130327_190942
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-0241bbae39-20130327_204651
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-0241bbae39-20130327_191625
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare{"food": "vegetarian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"food": "indian", "pricerange": "cheap"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-0241bbae39-20130327_204233
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "north american"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-0241bbae39-20130327_194703
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-afd3aa91f0-20130325_225729
* inform{"area": "centre"}
 - confirm_area
* inform{"food": "kosher"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - confirm_area
* affirm
 - confirm_food
* affirm
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-afd3aa91f0-20130327_190135
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-afd3aa91f0-20130327_185906
* inform{"area": "north"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - utter_request_food
* inform{"food": "indian"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-afd3aa91f0-20130325_224112
* inform{"food": "french", "pricerange": "expensive"}
 - offer_pricerange
* reqalts
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-afd3aa91f0-20130325_230434
* inform{"pricerange": "moderate", "area": "south"}
 - confirm_food
* affirm
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-afd3aa91f0-20130325_231946
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-afd3aa91f0-20130325_224706
* inform{"food": "european", "pricerange": "expensive"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-afd3aa91f0-20130325_224842
* inform{"food": "japanese", "area": "dontcare"}
 - utter_request_food
* inform{"food": "japanese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-afd3aa91f0-20130325_223728
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "irish"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-afd3aa91f0-20130325_225303
* inform{"food": "french", "area": "south"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"food": "indian", "area": "south"}
 - canthelp
* inform{"food": "indian", "area": "south"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-afd3aa91f0-20130327_190234
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-afd3aa91f0-20130326_015648
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "international"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-afd3aa91f0-20130325_224235
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-afd3aa91f0-20130326_015124
* inform{"food": "japanese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-afd3aa91f0-20130327_211102
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-cfd5fa34d9-20130402_073524
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-cfd5fa34d9-20130402_073021
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-cfd5fa34d9-20130402_073351
* inform{"pricerange": "cheap", "area": "west"}
 - confirm_summary
* include_filter{"area": "west"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-cfd5fa34d9-20130402_072808
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "seafood"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-cfd5fa34d9-20130402_074254
* inform{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-d6f8c4271e-20130326_221007
* inform{"food": "scottish"}
 - canthelp
* inform{"food": "scottish"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-d6f8c4271e-20130326_220359
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"food": "mexican"}
 - canthelp
* inform{"food": "international"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130402_080841
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "hungarian"}
 - offer_pricerange
* inform{"food": "european"}
 - canthelp
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-50af5438f1-20130402_085506
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"food": "european"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-50af5438f1-20130402_084641
* inform{"pricerange": "expensive"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - futile_offer_restaurant
* inform{"food": "irish"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130327_034500
* inform{"food": "world"}
 - canthelp
* inform{"food": "modern european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130402_085256
* inform{"pricerange": "moderate"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-50af5438f1-20130402_085647
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "italian"}
 - confirm_area
* affirm
 - offer_pricerange
* inform{"food": "italian"}
 - offer_pricerange
* inform{"food": "italian"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "italian"}
 - offer_pricerange
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-50af5438f1-20130402_090250
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130402_081930
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130402_082750
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-50af5438f1-20130402_084400
* inform{"food": "gastropub"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "gastropub"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-50af5438f1-20130402_081345
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_select_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "basque"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-50af5438f1-20130327_032137
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130327_043337
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-50af5438f1-20130402_081208
* inform{"food": "thai"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130327_032335
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "singaporean"}
 - canthelp
* inform{"food": "indian"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-50af5438f1-20130402_085904
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "chinese"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-50af5438f1-20130327_041542
* inform_dontcare
 - utter_offer_area
* inform{"food": "traditional"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-50af5438f1-20130327_041921
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - confirm_food
* inform{"food": "italian"}
 - offer_pricerange
* inform{"food": "italian"}
 - offer_pricerange
* reqalts
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-50af5438f1-20130327_031854
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "spanish"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-eaef6f434c-20130323_025453
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "modern european"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-eaef6f434c-20130323_030832
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* inform{"food": "italian", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-eaef6f434c-20130323_025316
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-eaef6f434c-20130323_031257
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-eaef6f434c-20130323_031356
* request{"pricerange": "_REQUESTED_"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-eaef6f434c-20130323_025154
* inform_dontcare
 - utter_request_food
* inform{"food": "asian oriental", "pricerange": "cheap"}
 - confirm_summary
* affirm
 - utter_request_food
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-eaef6f434c-20130323_024502
* inform{"food": "world"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-eaef6f434c-20130323_025614
* include_filter{"food": "steakhouse", "area": "north"}
 - canthelp
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "chinese", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-eaef6f434c-20130323_025908
* include_filter{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "belgian"}
 - canthelp
* inform{"food": "asian oriental", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e8997b10da-20130329_011058
* include_filter{"food": "french"}
 - utter_request_area
* inform{"area": "centre"}
 - confirm_area
* include_filter{"food": "french"}
 - confirm_area
* affirm
 - offer_restaurant
* ack
 - no_more_options
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* ack
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* ack
 - no_more_options
* ack
 - confirm_area
* request{"address": "_REQUESTED_"}
 - offer_address
* ack
 - futile_offer_restaurant
* thankyou
 - utter_bye

## Mar13_S0A0/voip-e8997b10da-20130327_193112
* include_filter{"food": "vegetarian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* confirm{"food": "british"}
 - confirm_food
* include_filter{"food": "british"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* ack
 - utter_anything_else
* bye
 - utter_bye

## Mar13_S1A0/voip-e8997b10da-20130329_001748
* include_filter{"food": "chinese", "area": "east"}
 - utter_request_food
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e8997b10da-20130401_152342
* include_filter{"food": "korean", "pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e8997b10da-20130401_152530
* include_filter{"food": "malaysian"}
 - canthelp
* inform{"food": "french"}
 - confirm_food
* include_filter{"pricerange": "dontcare"}
 - utter_select_price
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* ack
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e8997b10da-20130329_011626
* include_filter{"area": "north"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e8997b10da-20130401_151850
* include_filter{"food": "lebanese", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_anything_else
* negate
 - utter_bye

## Mar13_S1A1/voip-e8997b10da-20130327_194306
* include_filter{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e8997b10da-20130329_010926
* include_filter{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e8997b10da-20130329_001948
* include_filter{"food": "italian", "pricerange": "expensive"}
 - utter_request_area
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e8997b10da-20130329_000534
* include_filter{"pricerange": "cheap"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* ack
 - no_more_options
* bye
 - utter_bye

## Mar13_S1A1/voip-e8997b10da-20130327_200112
* inform{"food": "scottish"}
 - canthelp
* inform{"food": "british"}
 - confirm_food
* correct{"food": "british"}
 - utter_request_area
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e8997b10da-20130329_012511
* inform{"food": "african"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e8997b10da-20130329_010205
* include_filter{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e8997b10da-20130329_000658
* affirm
 - utter_request_area
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e8997b10da-20130327_194901
* include_filter{"food": "brazilian", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* ack
 - offer_pricerange
* inform{"food": "gastropub", "pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e8997b10da-20130327_195713
* include_filter{"food": "turkish", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_postcode
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e8997b10da-20130327_193641
* include_filter{"pricerange": "expensive", "area": "east"}
 - confirm_food
* include_filter{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare{"pricerange": "expensive"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* ack
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-e8997b10da-20130329_012334
* include_filter{"food": "turkish"}
 - offer_restaurant
* inform{"food": "turkish", "pricerange": "cheap"}
 - confirm_food
* affirm
 - offer_restaurant
* inform{"food": "turkish", "pricerange": "cheap"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e8997b10da-20130401_152228
* include_filter{"pricerange": "cheap", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - confirm_area
* include_filter{"pricerange": "cheap"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e8997b10da-20130329_012706
* include_filter{"food": "danish"}
 - utter_request_area
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "danish"}
 - canthelp
* inform{"food": "international"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - confirm_area
* affirm
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-e8997b10da-20130401_152019
* include_filter{"food": "persian"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* include_filter{"food": "persian"}
 - utter_request_food
* inform{"food": "persian"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - canthelp
* inform{"food": "portuguese"}
 - confirm_area
* affirm
 - confirm_food
* correct{"food": "portuguese"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* include_filter{"food": "portuguese"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-31de0daa7b-20130402_133530
* inform{"food": "creative"}
 - canthelp
* inform{"food": "modern european"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_pricerange
* inform{"area": "south"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

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
 - confirm_food
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - utter_request_area
* inform{"pricerange": "expensive"}
 - offer_restaurant
* negate
 - canthelp
* inform{"food": "european"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-31de0daa7b-20130401_205355
* inform{"food": "kosher", "pricerange": "moderate"}
 - utter_request_area
* inform{"food": "kosher", "pricerange": "moderate"}
 - utter_request_area
* inform{"area": "north"}
 - utter_select_area
* inform{"area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform{"food": "kosher"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-31de0daa7b-20130401_204415
* inform{"food": "creative"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "creative"}
 - offer_restaurant
* inform{"food": "international"}
 - canthelp
* inform{"food": "creative"}
 - canthelp
* inform{"area": "centre"}
 - confirm_area
* correct{"area": "centre"}
 - confirm_area
* negate
 - canthelp
* inform{"area": "centre"}
 - confirm_food
* affirm
 - canthelp
* bye
 - utter_bye

## Mar13_S0A1/voip-31de0daa7b-20130401_220541
* inform{"food": "kosher", "area": "dontcare"}
 - utter_request_food
* inform{"food": "kosher"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-31de0daa7b-20130401_220728
* inform{"pricerange": "moderate", "area": "south"}
 - confirm_summary
* affirm
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - futile_offer_restaurant
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-31de0daa7b-20130401_205633
* inform{"food": "international", "area": "south"}
 - confirm_area
* affirm
 - canthelp
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-31de0daa7b-20130401_221101
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"postcode": "_REQUESTED_"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-31de0daa7b-20130402_133047
* inform{"food": "seafood", "pricerange": "moderate"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "chinese"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-31de0daa7b-20130401_203534
* include_filter{"pricerange": "cheap"}
 - offer_pricerange
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-52eb280e7b-20130325_130820
* inform{"food": "christmas", "area": "west"}
 - utter_request_food
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-52eb280e7b-20130326_212826
* inform{"food": "british"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-52eb280e7b-20130325_124240
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* confirm{"pricerange": "expensive"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-52eb280e7b-20130326_215158
* inform{"food": "korean"}
 - utter_request_food
* inform{"food": "korean"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-52eb280e7b-20130326_211923
* inform{"food": "international"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-52eb280e7b-20130326_212733
* inform{"food": "italian", "pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-52eb280e7b-20130325_131334
* inform{"food": "turkish", "pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-52eb280e7b-20130325_125522
* inform{"area": "north"}
 - utter_request_food
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-52eb280e7b-20130326_213528
* inform{"food": "thai"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-52eb280e7b-20130326_213227
* inform{"food": "japanese"}
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-52eb280e7b-20130325_130645
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-52eb280e7b-20130325_125355
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-52eb280e7b-20130325_132224
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-52eb280e7b-20130325_123856
* inform{"food": "korean", "pricerange": "expensive"}
 - offer_pricerange
* inform{"food": "creative"}
 - canthelp
* inform{"food": "italian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-52eb280e7b-20130326_214342
* inform{"food": "portuguese"}
 - confirm_food
* inform{"food": "portuguese", "pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-52eb280e7b-20130325_130950
* inform{"food": "polynesian", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-52eb280e7b-20130326_215044
* inform{"food": "international"}
 - utter_request_area
* inform{"area": "centre"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-52eb280e7b-20130325_125157
* inform{"food": "cantonese"}
 - offer_restaurant
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "thai"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* inform{"food": "thai"}
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-2c217000af-20130328_224808
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-2c217000af-20130328_223711
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-2c217000af-20130328_224934
* inform{"food": "singaporean", "area": "north"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-2c217000af-20130325_221252
* inform{"food": "british", "area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-2c217000af-20130325_222647
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2c217000af-20130328_224449
* inform{"food": "lebanese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - no_more_options
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-2c217000af-20130325_221701
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "french", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-2c217000af-20130325_222430
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2c217000af-20130325_221525
* inform{"food": "traditional", "pricerange": "expensive"}
 - canthelp
* inform{"pricerange": "expensive"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-2c217000af-20130328_224206
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e9b53d6ace-20130324_223617
* inform{"area": "north"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "european"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_190230
* inform{"food": "jamaican", "area": "north"}
 - offer_restaurant
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* inform{"food": "chinese"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e9b53d6ace-20130324_221046
* inform{"food": "hungarian", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e9b53d6ace-20130324_222525
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e9b53d6ace-20130401_190004
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "european"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e9b53d6ace-20130324_222855
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e9b53d6ace-20130401_210057
* inform{"area": "south"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_202424
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_202659
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_184931
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e9b53d6ace-20130324_221924
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_212753
* inform{"food": "caribbean", "area": "centre"}
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_204254
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e9b53d6ace-20130401_201306
* inform{"food": "australian", "area": "east"}
 - utter_request_food
* inform{"food": "australian"}
 - utter_request_food
* inform{"food": "australian"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_200405
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "chinese"}
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A1/voip-e9b53d6ace-20130324_220844
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130324_222746
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130401_194326
* inform{"food": "welsh", "area": "dontcare"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e9b53d6ace-20130324_223300
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e9b53d6ace-20130324_222642
* inform{"food": "korean", "area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e9b53d6ace-20130324_220734
* inform{"food": "turkish"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_190135
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e9b53d6ace-20130324_221520
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "halal"}
 - canthelp
* inform{"food": "spanish"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e9b53d6ace-20130401_205843
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f4026333dc-20130327_175843
* inform{"food": "portuguese", "pricerange": "expensive"}
 - canthelp
* inform{"food": "british"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-f4026333dc-20130327_180235
* inform{"food": "asian oriental"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-2b66f60368-20130326_203353
* inform{"food": "afghan"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"food": "modern european"}
 - canthelp
* inform{"food": "modern european"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-2b66f60368-20130326_202529
* inform{"food": "italian", "pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-2b66f60368-20130326_203610
* inform{"food": "spanish"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2b66f60368-20130326_202221
* inform{"pricerange": "moderate", "area": "north"}
 - confirm_summary
* affirm
 - utter_request_food
* inform_dontcare{"area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-2b66f60368-20130326_203705
* inform{"food": "fusion", "pricerange": "moderate"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - confirm_food
* correct{"food": "chinese"}
 - utter_select_food
* inform{"food": "chinese"}
 - confirm_summary
* affirm
 - canthelp
* inform{"area": "dontcare"}
 - confirm_area
* negate
 - confirm_food
* affirm
 - canthelp
* confirm{"food": "chinese"}
 - canthelp
* inform{"area": "dontcare"}
 - confirm_summary
* affirm
 - canthelp
* inform{"area": "dontcare"}
 - confirm_area
* negate
 - confirm_food
* negate
 - confirm_summary
* affirm
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"area": "dontcare"}
 - canthelp
* inform{"area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2b66f60368-20130326_202811
* inform{"food": "turkish"}
 - offer_restaurant
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* inform{"food": "turkish"}
 - offer_restaurant
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-2b66f60368-20130326_203018
* request{"food": "christmas", "signature": "_REQUESTED_"}
 - canthelp
* inform{"food": "british"}
 - canthelp
* inform{"food": "british", "pricerange": "expensive"}
 - confirm_food
* negate
 - canthelp
* inform{"food": "british", "pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e72dba1759-20130325_211057
* inform{"food": "world", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e72dba1759-20130326_221205
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - utter_request_food
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e72dba1759-20130326_223506
* inform{"food": "chinese", "pricerange": "cheap"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e72dba1759-20130326_215630
* inform{"food": "hungarian"}
 - utter_request_food
* inform{"food": "hungarian"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* inform{"food": "hungarian", "pricerange": "dontcare"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_pricerange
* inform{"pricerange": "dontcare"}
 - utter_anything_else
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e72dba1759-20130325_204847
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e72dba1759-20130326_222657
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "food": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-e72dba1759-20130325_204725
* inform{"food": "vegetarian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "korean"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_address
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-e72dba1759-20130326_220053
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "mediterranean"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-e72dba1759-20130326_220605
* include_filter{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare{"pricerange": "cheap"}
 - offer_pricerange
* confirm{"area": "south"}
 - offer_restaurant
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e72dba1759-20130325_204601
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "thai"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-e72dba1759-20130326_222550
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e72dba1759-20130325_210629
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e72dba1759-20130325_205739
* inform{"food": "cuban", "pricerange": "moderate"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e72dba1759-20130326_223157
* inform{"pricerange": "cheap", "area": "west"}
 - confirm_area
* affirm
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-e72dba1759-20130325_210917
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_area
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S0A0/voip-e72dba1759-20130325_205315
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-e72dba1759-20130325_210022
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "pricerange": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-e72dba1759-20130326_220956
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - confirm_area
* include_filter{"food": "corsica"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "indian"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e72dba1759-20130325_215313
* affirm
 - utter_request_area
* inform{"food": "crossover", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - confirm_food
* affirm
 - utter_select_price
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-fe2783c40a-20130401_150540
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_select_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-fe2783c40a-20130401_145640
* inform{"pricerange": "moderate"}
 - utter_select_area
* inform{"pricerange": "moderate"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-fe2783c40a-20130401_144037
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-fe2783c40a-20130401_151115
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "moderate", "area": "west"}
 - offer_pricerange
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-fe2783c40a-20130401_145010
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-fe2783c40a-20130401_145931
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "eritrean"}
 - utter_request_food
* inform{"food": "eritrean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-fe2783c40a-20130401_145146
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"food": "seafood"}
 - offer_pricerange
* inform{"food": "seafood"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e30cb521fb-20130328_131711
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e30cb521fb-20130328_144608
* inform{"food": "cuban", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - confirm_summary
* include_filter{"food": "chinese"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e30cb521fb-20130328_122635
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* thankyou
 - offer_restaurant
* bye
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-e30cb521fb-20130328_134803
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-e30cb521fb-20130328_135828
* inform{"food": "romanian", "area": "centre"}
 - utter_request_food
* inform{"food": "romanian"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - utter_select_price
* inform_dontcare
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e30cb521fb-20130328_135454
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e0035cc31b-20130323_210244
* inform{"food": "barbeque", "area": "east"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e0035cc31b-20130323_211513
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e0035cc31b-20130323_211354
* inform{"food": "polynesian", "area": "west"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e0035cc31b-20130326_204829
* inform{"pricerange": "moderate", "area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e0035cc31b-20130323_212516
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A1/voip-e0035cc31b-20130326_205511
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e0035cc31b-20130326_205626
* inform{"food": "russian"}
 - canthelp
* inform{"food": "korean"}
 - utter_select_food
* inform{"food": "korean"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-e0035cc31b-20130323_212959
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-e0035cc31b-20130326_203550
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e0035cc31b-20130326_205950
* inform{"food": "scottish"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e0035cc31b-20130323_211206
* inform{"food": "african", "pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e0035cc31b-20130326_205004
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-e0035cc31b-20130323_211112
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e0035cc31b-20130326_203939
* inform{"food": "barbeque"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* inform{"food": "vietnamese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e0035cc31b-20130323_212626
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e0035cc31b-20130323_212221
* inform_dontcare
 - utter_request_food
* inform{"food": "gastropub"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e0035cc31b-20130326_210405
* inform{"food": "irish", "pricerange": "expensive"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "italian", "pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-e0035cc31b-20130326_205255
* inform{"food": "british", "area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e0035cc31b-20130326_203710
* inform{"food": "irish", "pricerange": "expensive"}
 - canthelp
* inform{"food": "italian"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e0035cc31b-20130326_204429
* inform{"food": "scandinavian", "pricerange": "expensive"}
 - canthelp
* inform{"food": "turkish"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-0a45bc863d-20130325_201403
* inform{"food": "spanish"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-0a45bc863d-20130325_201117
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0a45bc863d-20130325_195848
* inform{"food": "caribbean"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-0a45bc863d-20130325_202319
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "mediterranean"}
 - canthelp
* inform{"pricerange": "cheap"}
 - canthelp
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-0a45bc863d-20130325_201240
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-0a45bc863d-20130326_205127
* inform{"pricerange": "moderate"}
 - confirm_summary
* affirm
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0a45bc863d-20130326_205629
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "british"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-0a45bc863d-20130325_200201
* inform{"area": "south"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-0a45bc863d-20130325_200034
* inform{"food": "english", "area": "centre"}
 - confirm_area
* affirm
 - canthelp
* inform{"food": "british"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-0a45bc863d-20130325_200515
* inform{"pricerange": "moderate", "area": "north"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-0a45bc863d-20130326_204718
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "malaysian"}
 - canthelp
* inform{"food": "korean"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-0a45bc863d-20130325_202120
* inform{"food": "belgian"}
 - confirm_food
* correct{"food": "belgian"}
 - canthelp
* inform{"food": "british"}
 - utter_request_area
* inform{"area": "centre"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-0a45bc863d-20130326_205408
* inform{"food": "european"}
 - utter_request_food
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-0a45bc863d-20130326_210243
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-43479eb5c2-20130324_004748
* inform{"pricerange": "cheap", "area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-43479eb5c2-20130329_045902
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-43479eb5c2-20130324_003643
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-43479eb5c2-20130323_180515
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "portuguese"}
 - confirm_area
* affirm
 - confirm_food
* inform{"food": "portuguese"}
 - confirm_summary
* negate
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-43479eb5c2-20130323_180105
* inform{"pricerange": "expensive", "area": "south"}
 - confirm_area
* correct{"area": "south"}
 - utter_request_food
* inform{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-f113dbb0e1-20130322_233310
* inform{"area": "east"}
 - utter_select_area
* inform{"area": "east"}
 - utter_request_food
* inform{"area": "west"}
 - confirm_food
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f113dbb0e1-20130327_173541
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "austrian"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-f113dbb0e1-20130322_233822
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-f113dbb0e1-20130327_173417
* inform{"area": "west"}
 - utter_select_price
* inform_dontcare
 - utter_offer_area
* inform{"food": "british"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f113dbb0e1-20130327_173842
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform{"food": "vietnamese"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"pricerange": "dontcare"}
 - canthelp
* inform{"pricerange": "cheap"}
 - confirm_ask_area
* request{"address": "_REQUESTED_"}
 - utter_request_area
* inform{"area": "east"}
 - canthelp
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-d645d56d23-20130324_000301
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-d645d56d23-20130323_221635
* inform{"food": "african", "area": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_anything_else
* negate
 - utter_anything_else
* bye
 - utter_bye

## Mar13_S1A0/voip-d645d56d23-20130324_001536
* inform{"food": "halal", "pricerange": "moderate"}
 - offer_pricerange
* confirm{"food": "halal"}
 - offer_restaurant
* correct{"food": "halal"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-d645d56d23-20130323_222004
* inform{"food": "european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "area": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-d645d56d23-20130401_204623
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-d645d56d23-20130401_204424
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "world"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"name": "pizza hut city centre", "food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-d645d56d23-20130323_223158
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* inform{"pricerange": "expensive", "area": "east"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-d645d56d23-20130323_222341
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-d645d56d23-20130401_203033
* inform{"food": "swedish"}
 - canthelp
* inform{"food": "portuguese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-d645d56d23-20130324_232209
* inform{"area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - offer_restaurant
* confirm{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-d645d56d23-20130324_232416
* inform{"pricerange": "cheap", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-d645d56d23-20130324_000123
* inform{"area": "dontcare"}
 - confirm_area
* inform{"food": "unusual"}
 - canthelp
* inform{"food": "spanish"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A1/voip-d645d56d23-20130324_000651
* inform{"pricerange": "moderate"}
 - confirm_summary
* affirm
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-d645d56d23-20130402_035204
* inform{"pricerange": "cheap", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-d645d56d23-20130401_203325
* inform{"food": "russian", "pricerange": "cheap"}
 - canthelp
* inform{"food": "chinese"}
 - offer_pricerange
* confirm{"food": "chinese"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - utter_select_food
* inform{"food": "russian"}
 - offer_pricerange
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"pricerange": "cheap"}
 - utter_select_food
* inform{"food": "chinese"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03d6592b76-20130326_015131
* inform{"food": "italian", "pricerange": "cheap"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* confirm{"pricerange": "cheap"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-03d6592b76-20130326_012615
* inform{"food": "steakhouse", "pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "steakhouse"}
 - confirm_area
* affirm
 - offer_pricerange
* confirm{"food": "steakhouse"}
 - offer_restaurant
* inform{"food": "steakhouse"}
 - canthelp
* inform{"food": "vietnamese"}
 - offer_pricerange
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03d6592b76-20130326_012832
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "world"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-03d6592b76-20130327_030334
* inform{"food": "japanese", "area": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - utter_anything_else
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-03d6592b76-20130326_014023
* inform{"food": "cuban", "area": "west"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03d6592b76-20130326_012940
* inform{"food": "turkish"}
 - utter_request_area
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - confirm_area
* affirm
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-03d6592b76-20130326_012529
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-03d6592b76-20130327_025441
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03d6592b76-20130327_024630
* inform{"area": "east"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - utter_request_food
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "cantonese"}
 - canthelp
* inform{"food": "cantonese"}
 - offer_restaurant
* inform{"food": "cantonese"}
 - offer_restaurant
* inform{"food": "chinese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03d6592b76-20130327_030034
* inform{"pricerange": "cheap"}
 - utter_request_food
* inform{"food": "dontcare"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "address": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-03d6592b76-20130326_013107
* inform{"food": "international", "area": "north"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-03d6592b76-20130327_030602
* inform{"food": "asian oriental"}
 - utter_request_area
* inform{"area": "dontcare"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - utter_request_food
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - confirm_food
* correct{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - confirm_area
* affirm
 - confirm_food
* negate
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - utter_select_price
* inform_dontcare
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-03d6592b76-20130327_024820
* inform{"food": "thai", "pricerange": "expensive"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-03d6592b76-20130326_012136
* inform{"area": "north"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03d6592b76-20130327_025219
* inform{"food": "austrian", "area": "south"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-03d6592b76-20130326_014855
* inform{"food": "halal", "pricerange": "moderate"}
 - canthelp
* inform{"food": "gastropub"}
 - offer_pricerange
* confirm{"food": "gastropub"}
 - offer_restaurant
* inform{"food": "gastropub"}
 - offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-03d6592b76-20130327_030242
* inform{"pricerange": "moderate", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-03d6592b76-20130326_013208
* inform{"food": "greek", "area": "east"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* inform{"food": "chinese"}
 - offer_restaurant
* confirm{"food": "chinese"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ad40cf5489-20130325_180702
* inform{"food": "mexican"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - confirm_food
* include_filter{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-ad40cf5489-20130327_192610
* inform{"food": "scottish", "pricerange": "moderate"}
 - canthelp
* inform{"food": "british", "pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-ad40cf5489-20130325_180305
* inform{"food": "corsica", "area": "centre"}
 - canthelp
* inform{"food": "international", "area": "centre"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-ad40cf5489-20130325_175953
* inform{"food": "seafood", "area": "centre"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A0/voip-ad40cf5489-20130327_193841
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* reqalts
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-ad40cf5489-20130327_192458
* inform{"food": "caribbean", "area": "west"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-ad40cf5489-20130327_192300
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ad40cf5489-20130327_194457
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-ad40cf5489-20130327_194224
* inform{"food": "australian", "area": "south"}
 - canthelp
* inform{"food": "chinese"}
 - canthelp
* inform{"food": "chinese"}
 - utter_select_price
* inform_dontcare
 - confirm_summary
* inform{"food": "chinese"}
 - confirm_summary
* inform{"food": "chinese"}
 - confirm_summary
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-ad40cf5489-20130325_180552
* inform{"pricerange": "expensive", "area": "north"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-ad40cf5489-20130327_191905
* inform{"pricerange": "moderate", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-ad40cf5489-20130327_192405
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ad40cf5489-20130325_181942
* inform{"food": "gastropub", "pricerange": "cheap"}
 - utter_request_food
* inform{"food": "gastropub"}
 - utter_request_food
* inform{"food": "gastropub"}
 - canthelp
* inform{"pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-ad40cf5489-20130325_181004
* inform{"food": "welsh", "pricerange": "cheap"}
 - confirm_food
* include_filter{"pricerange": "cheap"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "mediterranean", "pricerange": "cheap"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-ad40cf5489-20130325_175502
* inform{"food": "catalan", "pricerange": "moderate"}
 - canthelp
* inform{"pricerange": "moderate"}
 - canthelp
* inform{"food": "spanish", "pricerange": "moderate"}
 - offer_pricerange
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-ad40cf5489-20130327_191318
* inform{"food": "jamaican", "area": "west"}
 - utter_request_food
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "vietnamese", "area": "west"}
 - canthelp
* inform{"food": "vietnamese"}
 - canthelp
* negate
 - offer_restaurant
* inform{"food": "vietnamese"}
 - no_more_options
* inform{"food": "vietnamese"}
 - confirm_area
* affirm
 - confirm_food
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-ad40cf5489-20130327_194114
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-ad40cf5489-20130327_191638
* inform{"food": "seafood", "area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-ad40cf5489-20130327_192155
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-ad40cf5489-20130325_180434
* inform{"food": "vietnamese", "area": "north"}
 - canthelp
* inform{"area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-ad40cf5489-20130325_175141
* inform{"food": "welsh"}
 - canthelp
* inform{"food": "modern european"}
 - confirm_food
* inform{"food": "modern european"}
 - utter_request_area
* inform{"area": "dontcare"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-ad40cf5489-20130325_181825
* inform{"pricerange": "moderate", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-ad40cf5489-20130325_182117
* inform{"food": "creative", "area": "east"}
 - canthelp
* inform{"food": "indian", "area": "east"}
 - canthelp
* inform{"food": "indian", "area": "east"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_191629
* inform{"food": "kosher", "area": "north"}
 - canthelp
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_190757
* inform{"food": "kosher", "pricerange": "expensive"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_190456
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_193033
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_190613
* inform{"food": "world", "pricerange": "expensive"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_pricerange
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_191755
* inform{"food": "mexican", "pricerange": "expensive"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_192646
* inform{"pricerange": "moderate", "area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_191205
* inform{"pricerange": "cheap", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"food": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_190045
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"area": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"area": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-2f4c700ae3-20130401_185424
* inform{"food": "asian oriental", "area": "centre"}
 - canthelp
* inform{"food": "european"}
 - canthelp
* inform{"food": "european"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-2f4c700ae3-20130401_185133
* inform{"area": "south"}
 - utter_request_food
* inform{"food": "turkish"}
 - offer_restaurant
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S1A0/voip-2f4c700ae3-20130401_191934
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_165410
* inform{"food": "indian"}
 - utter_request_area
* inform{"area": "west"}
 - confirm_area
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-f22c2bf9c7-20130328_122513
* inform{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-f22c2bf9c7-20130326_192953
* inform{"food": "vietnamese"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f22c2bf9c7-20130326_020833
* inform{"area": "south"}
 - utter_request_food
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
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-f22c2bf9c7-20130326_193723
* inform{"food": "german"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_area
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "german"}
 - canthelp
* inform{"food": "gastropub"}
 - confirm_food
* affirm
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-f22c2bf9c7-20130326_202745
* inform{"food": "bistro"}
 - canthelp
* inform{"food": "turkish"}
 - utter_request_area
* inform{"area": "east"}
 - canthelp
* inform{"area": "north"}
 - canthelp
* inform{"area": "north"}
 - confirm_area
* negate
 - confirm_food
* affirm
 - canthelp
* bye
 - utter_bye

## Mar13_S0A0/voip-f22c2bf9c7-20130326_203001
* inform{"food": "portuguese"}
 - utter_request_food
* inform{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-f22c2bf9c7-20130328_120523
* inform{"food": "mexican"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-f22c2bf9c7-20130328_114452
* inform{"food": "swedish"}
 - utter_request_area
* inform{"area": "centre"}
 - utter_request_food
* inform{"food": "swedish"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_115849
* inform{"food": "turkish"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_area
* bye
 - utter_bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_121753
* inform{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - utter_select_area
* inform{"area": "north"}
 - utter_select_area
* inform{"area": "north"}
 - utter_select_area
* inform{"area": "north"}
 - utter_select_area
* inform{"pricerange": "moderate"}
 - utter_select_area
* inform{"pricerange": "moderate"}
 - utter_select_area
* inform{"area": "north"}
 - offer_pricerange
* inform{"area": "north"}
 - futile_offer_restaurant
* inform{"area": "north"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-f22c2bf9c7-20130326_203410
* inform{"area": "west"}
 - confirm_area
* affirm
 - offer_restaurant
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "british"}
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f22c2bf9c7-20130328_121125
* inform{"food": "christmas"}
 - canthelp
* inform{"food": "indian"}
 - confirm_ask_area
* inform{"area": "centre"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* inform{"area": "west"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-f22c2bf9c7-20130326_020431
* inform{"food": "spanish"}
 - canthelp
* inform{"food": "spanish"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-f22c2bf9c7-20130328_115128
* inform{"food": "japanese"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - no_more_options
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* bye
 - utter_bye

## Mar13_S0A0/voip-f22c2bf9c7-20130326_193956
* inform{"food": "scandinavian"}
 - utter_request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - canthelp
* inform{"food": "asian oriental"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-f22c2bf9c7-20130328_113750
* inform{"food": "gastropub"}
 - utter_select_price
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "south"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-f22c2bf9c7-20130328_114939
* inform{"pricerange": "cheap"}
 - futile_offer_restaurant
* inform{"area": "south"}
 - utter_offer_area
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A1/voip-f22c2bf9c7-20130328_120123
* inform{"food": "international"}
 - utter_request_area
* inform{"area": "centre"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - utter_bye

## Mar13_S0A1/voip-f22c2bf9c7-20130326_203814
* inform{"food": "turkish"}
 - canthelp
* inform{"food": "turkish"}
 - offer_restaurant
* request{"pricerange": "_REQUESTED_"}
 - offer_pricerange
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* inform_dontcare
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A1/voip-f22c2bf9c7-20130328_113940
* inform{"area": "south"}
 - utter_request_food
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-f22c2bf9c7-20130328_120730
* inform{"food": "unusual"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - utter_request_area
* inform{"area": "centre"}
 - utter_request_food
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
 - utter_bye

## Mar13_S0A1/voip-e99e4f4538-20130328_195304
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e99e4f4538-20130328_202105
* inform{"food": "african", "area": "centre"}
 - utter_request_food
* inform{"food": "african"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e99e4f4538-20130328_200547
* inform{"food": "portuguese"}
 - utter_request_area
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e99e4f4538-20130327_152308
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130328_201948
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e99e4f4538-20130327_154223
* inform{"area": "west"}
 - utter_request_area
* inform{"area": "west"}
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-e99e4f4538-20130327_145422
* inform{"pricerange": "cheap", "area": "north"}
 - utter_request_area
* inform{"area": "north"}
 - offer_restaurant
* reqalts
 - confirm_food
* reqalts
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130327_152525
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform{"area": "east"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-e99e4f4538-20130327_145848
* inform{"pricerange": "expensive"}
 - utter_request_food
* inform{"food": "mediterranean"}
 - offer_pricerange
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130328_195927
* inform{"area": "west"}
 - utter_request_food
* inform{"food": "indian"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130328_201531
* inform{"pricerange": "moderate", "area": "south"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130327_140746
* inform{"food": "mexican"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* thankyou
 - futile_offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-e99e4f4538-20130328_195729
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "international"}
 - confirm_food
* negate
 - canthelp
* negate
 - canthelp
* inform{"food": "international"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-e99e4f4538-20130328_200259
* inform{"food": "jamaican"}
 - utter_select_price
* inform_dontcare
 - offer_pricerange
* inform{"food": "jamaican"}
 - futile_offer_restaurant
* inform{"food": "jamaican"}
 - futile_offer_restaurant
* inform{"food": "jamaican"}
 - canthelp
* inform{"food": "portuguese"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130328_203355
* inform_dontcare
 - utter_request_food
* inform{"food": "venetian"}
 - canthelp
* inform{"food": "mediterranean"}
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130327_153656
* inform{"food": "catalan"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "catalan"}
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* reqalts
 - confirm_area
* affirm
 - confirm_food
* negate
 - canthelp
* inform{"food": "gastropub"}
 - canthelp
* inform{"food": "gastropub"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-e99e4f4538-20130327_141042
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "scandinavian"}
 - canthelp
* inform{"food": "italian"}
 - confirm_food
* inform{"food": "italian"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e99e4f4538-20130328_201813
* inform{"pricerange": "cheap"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "moroccan"}
 - canthelp
* inform{"food": "indian"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A0/voip-e99e4f4538-20130327_150414
* inform{"food": "french"}
 - utter_request_area
* inform_dontcare
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "french"}
 - offer_restaurant
* inform{"pricerange": "expensive"}
 - offer_restaurant
* affirm
 - futile_offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - futile_offer_restaurant
* request{"phone": "_REQUESTED_"}
 - no_more_options
* request{"name": "restaurant two two", "phone": "_REQUESTED_"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S0A0/voip-e99e4f4538-20130327_150148
* inform{"area": "north"}
 - utter_request_food
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-e99e4f4538-20130328_201635
* inform{"pricerange": "cheap"}
 - offer_pricerange
* inform{"area": "west"}
 - futile_offer_restaurant
* confirm{"pricerange": "cheap"}
 - offer_pricerange
* confirm{"area": "west"}
 - offer_restaurant
* inform{"area": "west"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e99e4f4538-20130327_141718
* inform{"food": "cuban"}
 - canthelp
* inform{"food": "modern european"}
 - utter_request_area
* inform_dontcare
 - utter_select_price
* inform{"pricerange": "expensive"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e99e4f4538-20130328_200645
* inform{"pricerange": "cheap", "area": "west"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A1/voip-e99e4f4538-20130327_154024
* inform{"area": "north"}
 - confirm_food
* request{"area": "_REQUESTED_"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* inform{"food": "indian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130327_144810
* inform{"area": "south"}
 - utter_request_food
* inform{"pricerange": "moderate"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-e99e4f4538-20130327_150005
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-6d6587c57d-20130328_142518
* inform{"pricerange": "moderate", "area": "north"}
 - utter_request_food
* inform{"food": "dontcare"}
 - confirm_food
* affirm
 - offer_restaurant
* reqalts
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-6d6587c57d-20130328_142302
* inform{"food": "irish", "area": "centre"}
 - confirm_food
* affirm
 - utter_select_price
* inform{"pricerange": "dontcare"}
 - offer_restaurant
* inform{"food": "irish"}
 - canthelp
* inform{"food": "north american"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-6d6587c57d-20130328_143700
* inform{"area": "east"}
 - utter_request_food
* inform{"food": "corsica"}
 - utter_request_food
* inform{"food": "corsica"}
 - canthelp
* inform{"food": "indian"}
 - canthelp
* bye
 - utter_bye

## Mar13_S0A0/voip-6d6587c57d-20130328_143034
* inform{"pricerange": "expensive", "area": "south"}
 - utter_request_food
* inform{"food": "dontcare"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-263ab0e49f-20130326_104818
* inform{"pricerange": "moderate", "area": "east"}
 - utter_request_food
* inform{"food": "dontcare"}
 - canthelp
* correct{"pricerange": "moderate"}
 - canthelp
* inform{"area": "east"}
 - canthelp
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-263ab0e49f-20130326_104535
* include_filter{"food": "portuguese"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-263ab0e49f-20130326_104358
* request{"area": "_REQUESTED_", "postcode": "_REQUESTED_", "address": "_REQUESTED_"}
 - utter_request_area
* inform{"area": "south"}
 - utter_request_food
* inform_dontcare
 - utter_select_price
* include_filter{"pricerange": "moderate"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-263ab0e49f-20130326_110450
* inform{"food": "polynesian", "area": "south"}
 - canthelp
* inform{"food": "italian"}
 - offer_restaurant
* request{"phone": "_REQUESTED_", "postcode": "_REQUESTED_"}
 - offer_phone
* request{"postcode": "_REQUESTED_"}
 - offer_postcode
* bye
 - utter_bye

## Mar13_S1A0/voip-263ab0e49f-20130326_105455
* include_filter{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform{"food": "dontcare"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"food": "_REQUESTED_"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S0A1/voip-263ab0e49f-20130326_105158
* include_filter{"food": "hungarian", "area": "south"}
 - utter_select_price
* inform_dontcare
 - utter_request_food
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "hungarian"}
 - canthelp
* inform{"food": "modern european"}
 - offer_restaurant
* request{"address": "_REQUESTED_", "phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-a617b6827c-20130323_170328
* inform_dontcare
 - utter_request_food
* inform{"food": "corsica"}
 - utter_request_food
* inform{"food": "corsica"}
 - utter_request_food
* inform{"food": "gastropub"}
 - utter_select_price
* inform_dontcare
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_postcode
* request{"phone": "_REQUESTED_"}
 - offer_phone
* request{"address": "_REQUESTED_"}
 - offer_address
* bye
 - utter_bye

## Mar13_S0A1/voip-a617b6827c-20130323_170210
* inform{"pricerange": "moderate"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "caribbean"}
 - canthelp
* inform{"food": "chinese"}
 - offer_restaurant
* inform{"pricerange": "moderate"}
 - offer_pricerange
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A1/voip-a617b6827c-20130323_165831
* inform{"food": "british"}
 - utter_request_area
* inform{"area": "south"}
 - canthelp
* inform{"area": "centre"}
 - offer_restaurant
* request{"address": "_REQUESTED_"}
 - offer_address
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S0A0/voip-a617b6827c-20130323_170929
* inform{"pricerange": "expensive", "area": "east"}
 - utter_request_food
* inform_dontcare
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* confirm{"pricerange": "expensive"}
 - offer_restaurant
* bye
 - utter_bye

## Mar13_S1A0/voip-a617b6827c-20130323_171108
* inform{"food": "french"}
 - utter_request_area
* inform_dontcare
 - utter_request_food
* inform{"food": "french"}
 - offer_restaurant
* reqalts
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

## Mar13_S1A0/voip-80451eaa72-20130401_191337
* inform{"food": "german", "area": "north"}
 - confirm_food
* affirm
 - canthelp
* inform{"food": "french"}
 - canthelp
* inform{"food": "french", "area": "north"}
 - utter_select_food
* inform{"food": "french"}
 - offer_restaurant
* request{"phone": "_REQUESTED_"}
 - offer_phone
* bye
 - utter_bye

