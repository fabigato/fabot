## 0
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 1
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 2
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 3
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 4
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 5
* greet
 - greet
* inform{"price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 6
* greet
 - greet
* inform{"price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 7
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 8
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 9
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 10
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 11
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 12
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 13
* greet
 - greet
* inform{"price": "cheap", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 14
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 15
* greet
 - greet
* inform{"number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 16
* greet
 - greet
* inform{"number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 17
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 18
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 19
* greet
 - greet
* inform{"price": "moderate", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 20
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 21
* greet
 - greet
* inform{"price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 22
* greet
 - greet
* inform{"price": "expensive", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 23
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 24
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 25
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 26
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 27
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 28
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 29
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 30
* greet
 - greet
* inform{"cuisine": "french", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 31
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 32
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 33
* greet
 - greet
* inform{"number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 34
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 35
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 36
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 37
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 38
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 39
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 40
* greet
 - greet
* inform{"cuisine": "italian", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 41
* greet
 - greet
* inform{"price": "cheap", "number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 42
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 43
* greet
 - greet
* inform{"cuisine": "french", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 44
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 45
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 46
* greet
 - greet
* inform{"cuisine": "indian", "number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 47
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 48
* greet
 - greet
* inform{"cuisine": "indian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 49
* greet
 - greet
* inform{"cuisine": "french", "number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 50
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 51
* greet
 - greet
* inform{"price": "moderate", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 52
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 53
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 54
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 55
* greet
 - greet
* inform{"cuisine": "indian", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 56
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 57
* greet
 - greet
* inform{"cuisine": "french", "number": "four", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 58
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 59
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 60
* greet
 - greet
* inform{"cuisine": "spanish", "number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 61
* greet
 - greet
* inform{"number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 62
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 63
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 64
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 65
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 66
* greet
 - greet
* inform{"price": "moderate", "number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 67
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 68
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 69
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 70
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 71
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 72
* greet
 - greet
* inform{"cuisine": "french", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 73
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 74
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 75
* greet
 - greet
* inform{"cuisine": "italian", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 76
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 77
* greet
 - greet
* inform{"cuisine": "indian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 78
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 79
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 80
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 81
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 82
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 83
* greet
 - greet
* inform{"price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 84
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 85
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 86
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 87
* greet
 - greet
* inform{"cuisine": "spanish", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 88
* greet
 - greet
* inform{"price": "cheap", "number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 89
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 90
* greet
 - greet
* inform{"cuisine": "british", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 91
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 92
* greet
 - greet
* inform{"cuisine": "spanish", "number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 93
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 94
* greet
 - greet
* inform{"cuisine": "indian", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 95
* greet
 - greet
* inform{"number": "four", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 96
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 97
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 98
* greet
 - greet
* inform{"number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 99
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 100
* greet
 - greet
* inform{"price": "cheap", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 101
* greet
 - greet
* inform{"cuisine": "italian", "number": "four", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 102
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 103
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 104
* greet
 - greet
* inform{"cuisine": "british", "number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 105
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 106
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 107
* greet
 - greet
* inform{"number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 108
* greet
 - greet
* inform{"cuisine": "indian", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 109
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 110
* greet
 - greet
* inform{"cuisine": "spanish", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 111
* greet
 - greet
* inform{"cuisine": "british", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 112
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 113
* greet
 - greet
* inform{"price": "expensive", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 114
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 115
* greet
 - greet
* inform{"price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 116
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 117
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 118
* greet
 - greet
* inform{"price": "cheap", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 119
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 120
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 121
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 122
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 123
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 124
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 125
* greet
 - greet
* inform{"price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 126
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 127
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 128
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 129
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 130
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 131
* greet
 - greet
* inform{"number": "six", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 132
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 133
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 134
* greet
 - greet
* inform{"cuisine": "british", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 135
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 136
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 137
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 138
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 139
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 140
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 141
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 142
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 143
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 144
* greet
 - greet
* inform{"price": "expensive", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 145
* greet
 - greet
* inform{"cuisine": "spanish", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 146
* greet
 - greet
* inform{"cuisine": "british", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 147
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 148
* greet
 - greet
* inform{"cuisine": "french", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 149
* greet
 - greet
* inform{"cuisine": "italian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 150
* greet
 - greet
* inform{"cuisine": "indian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 151
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 152
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 153
* greet
 - greet
* inform{"number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 154
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 155
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 156
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 157
* greet
 - greet
* inform{"cuisine": "indian", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 158
* greet
 - greet
* inform{"price": "expensive", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 159
* greet
 - greet
* inform{"cuisine": "spanish", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 160
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 161
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 162
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 163
* greet
 - greet
* inform{"price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 164
* greet
 - greet
* inform{"number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 165
* greet
 - greet
* inform{"number": "two", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 166
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 167
* greet
 - greet
* inform{"price": "expensive", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 168
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 169
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 170
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 171
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 172
* greet
 - greet
* inform{"cuisine": "indian", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 173
* greet
 - greet
* inform{"price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 174
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 175
* greet
 - greet
* inform{"cuisine": "spanish", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 176
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 177
* greet
 - greet
* inform{"cuisine": "french", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 178
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 179
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 180
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 181
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 182
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 183
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 184
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 185
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 186
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 187
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 188
* greet
 - greet
* inform{"price": "expensive", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 189
* greet
 - greet
* inform{"price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 190
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 191
* greet
 - greet
* inform{"cuisine": "indian", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 192
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 193
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 194
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 195
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 196
* greet
 - greet
* inform{"number": "four", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 197
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 198
* greet
 - greet
* inform{"number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 199
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 200
* greet
 - greet
* inform{"cuisine": "french", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 201
* greet
 - greet
* inform{"number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 202
* greet
 - greet
* inform{"price": "cheap", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 203
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 204
* greet
 - greet
* inform{"price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 205
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 206
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 207
* greet
 - greet
* inform{"number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 208
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 209
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 210
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 211
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 212
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 213
* greet
 - greet
* inform{"price": "moderate", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 214
* greet
 - greet
* inform{"price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 215
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 216
* greet
 - greet
* inform{"price": "cheap", "number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 217
* greet
 - greet
* inform{"cuisine": "italian", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 218
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 219
* greet
 - greet
* inform{"price": "cheap", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 220
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 221
* greet
 - greet
* inform{"price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 222
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 223
* greet
 - greet
* inform{"cuisine": "spanish", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 224
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 225
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 226
* greet
 - greet
* inform{"cuisine": "italian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 227
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 228
* greet
 - greet
* inform{"price": "moderate", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 229
* greet
 - greet
* inform{"cuisine": "french", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 230
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 231
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 232
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 233
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 234
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 235
* greet
 - greet
* inform{"number": "four", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 236
* greet
 - greet
* inform{"number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 237
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 238
* greet
 - greet
* inform{"price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 239
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 240
* greet
 - greet
* inform{"number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 241
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 242
* greet
 - greet
* inform{"price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 243
* greet
 - greet
* inform{"cuisine": "indian", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 244
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 245
* greet
 - greet
* inform{"cuisine": "indian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 246
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 247
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 248
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 249
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 250
* greet
 - greet
* inform{"price": "cheap", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 251
* greet
 - greet
* inform{"cuisine": "british", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 252
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 253
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 254
* greet
 - greet
* inform{"cuisine": "indian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 255
* greet
 - greet
* inform{"cuisine": "indian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 256
* greet
 - greet
* inform{"number": "six", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 257
* greet
 - greet
* inform{"number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 258
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 259
* greet
 - greet
* inform{"cuisine": "british", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 260
* greet
 - greet
* inform{"cuisine": "indian", "number": "four", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 261
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 262
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 263
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 264
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 265
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 266
* greet
 - greet
* inform{"cuisine": "indian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 267
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 268
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 269
* greet
 - greet
* inform{"price": "moderate", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 270
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 271
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 272
* greet
 - greet
* inform{"price": "cheap", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 273
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 274
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 275
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 276
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 277
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 278
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 279
* greet
 - greet
* inform{"cuisine": "indian", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 280
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 281
* greet
 - greet
* inform{"number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 282
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 283
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 284
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 285
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 286
* greet
 - greet
* inform{"cuisine": "french", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 287
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 288
* greet
 - greet
* inform{"price": "moderate", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 289
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 290
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 291
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 292
* greet
 - greet
* inform{"cuisine": "spanish", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 293
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 294
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 295
* greet
 - greet
* inform{"price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 296
* greet
 - greet
* inform{"number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 297
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 298
* greet
 - greet
* inform{"number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 299
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 300
* greet
 - greet
* inform{"cuisine": "french", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 301
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 302
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 303
* greet
 - greet
* inform{"price": "cheap", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 304
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 305
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 306
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 307
* greet
 - greet
* inform{"cuisine": "italian", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 308
* greet
 - greet
* inform{"cuisine": "italian", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 309
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 310
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 311
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 312
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 313
* greet
 - greet
* inform{"cuisine": "british", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 314
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 315
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 316
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 317
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 318
* greet
 - greet
* inform{"number": "eight", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 319
* greet
 - greet
* inform{"cuisine": "french", "number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 320
* greet
 - greet
* inform{"price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 321
* greet
 - greet
* inform{"price": "expensive", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 322
* greet
 - greet
* inform{"cuisine": "italian", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 323
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 324
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 325
* greet
 - greet
* inform{"cuisine": "indian", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 326
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 327
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 328
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 329
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 330
* greet
 - greet
* inform{"cuisine": "british", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 331
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 332
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 333
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 334
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 335
* greet
 - greet
* inform{"price": "cheap", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 336
* greet
 - greet
* inform{"number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 337
* greet
 - greet
* inform{"cuisine": "british", "number": "four", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 338
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 339
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 340
* greet
 - greet
* inform{"cuisine": "indian", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 341
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 342
* greet
 - greet
* inform{"price": "expensive", "number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 343
* greet
 - greet
* inform{"price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 344
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 345
* greet
 - greet
* inform{"price": "expensive", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 346
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 347
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 348
* greet
 - greet
* inform{"price": "cheap", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 349
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 350
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 351
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 352
* greet
 - greet
* inform{"cuisine": "british", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 353
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 354
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 355
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 356
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 357
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 358
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 359
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 360
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 361
* greet
 - greet
* inform{"cuisine": "french", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 362
* greet
 - greet
* inform{"price": "moderate", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 363
* greet
 - greet
* inform{"number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 364
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 365
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 366
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 367
* greet
 - greet
* inform{"cuisine": "spanish", "number": "six", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 368
* greet
 - greet
* inform{"price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 369
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 370
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 371
* greet
 - greet
* inform{"cuisine": "indian", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 372
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 373
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 374
* greet
 - greet
* inform{"price": "expensive", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 375
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 376
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 377
* greet
 - greet
* inform{"cuisine": "british", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 378
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 379
* greet
 - greet
* inform{"price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 380
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 381
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 382
* greet
 - greet
* inform{"cuisine": "french", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 383
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 384
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 385
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 386
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 387
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 388
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 389
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 390
* greet
 - greet
* inform{"price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 391
* greet
 - greet
* inform{"price": "moderate", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 392
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 393
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 394
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 395
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 396
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 397
* greet
 - greet
* inform{"number": "eight", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 398
* greet
 - greet
* inform{"number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 399
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 400
* greet
 - greet
* inform{"price": "expensive", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 401
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 402
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 403
* greet
 - greet
* inform{"cuisine": "indian", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 404
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 405
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 406
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 407
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 408
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 409
* greet
 - greet
* inform{"number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 410
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 411
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 412
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 413
* greet
 - greet
* inform{"cuisine": "british", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 414
* greet
 - greet
* inform{"cuisine": "british", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 415
* greet
 - greet
* inform{"price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 416
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 417
* greet
 - greet
* inform{"cuisine": "british", "number": "four", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 418
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 419
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 420
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 421
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 422
* greet
 - greet
* inform{"cuisine": "italian", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 423
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 424
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 425
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 426
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 427
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 428
* greet
 - greet
* inform{"cuisine": "indian", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 429
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 430
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 431
* greet
 - greet
* inform{"price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 432
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 433
* greet
 - greet
* inform{"number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 434
* greet
 - greet
* inform{"cuisine": "italian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 435
* greet
 - greet
* inform{"cuisine": "french", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 436
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 437
* greet
 - greet
* inform{"number": "four", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 438
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 439
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 440
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 441
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 442
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 443
* greet
 - greet
* inform{"price": "moderate", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 444
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 445
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 446
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 447
* greet
 - greet
* inform{"price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 448
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 449
* greet
 - greet
* inform{"price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 450
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 451
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 452
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 453
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 454
* greet
 - greet
* inform{"cuisine": "french", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 455
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 456
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 457
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 458
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 459
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 460
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 461
* greet
 - greet
* inform{"cuisine": "italian", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 462
* greet
 - greet
* inform{"number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 463
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 464
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 465
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 466
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 467
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 468
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 469
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 470
* greet
 - greet
* inform{"cuisine": "french", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 471
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 472
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 473
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 474
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 475
* greet
 - greet
* inform{"cuisine": "british", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 476
* greet
 - greet
* inform{"cuisine": "indian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 477
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 478
* greet
 - greet
* inform{"cuisine": "indian", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 479
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 480
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 481
* greet
 - greet
* inform{"cuisine": "british", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 482
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 483
* greet
 - greet
* inform{"cuisine": "italian", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 484
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 485
* greet
 - greet
* inform{"price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 486
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 487
* greet
 - greet
* inform{"cuisine": "french", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 488
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 489
* greet
 - greet
* inform{"price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 490
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 491
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 492
* greet
 - greet
* inform{"price": "expensive", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 493
* greet
 - greet
* inform{"number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 494
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 495
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 496
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 497
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 498
* greet
 - greet
* inform{"cuisine": "british", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 499
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 500
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 501
* greet
 - greet
* inform{"price": "moderate", "number": "six", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 502
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 503
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 504
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 505
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 506
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 507
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 508
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 509
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 510
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 511
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 512
* greet
 - greet
* inform{"cuisine": "indian", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 513
* greet
 - greet
* inform{"price": "expensive", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 514
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 515
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 516
* greet
 - greet
* inform{"cuisine": "indian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 517
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 518
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 519
* greet
 - greet
* inform{"cuisine": "italian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 520
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 521
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 522
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 523
* greet
 - greet
* inform{"number": "four", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 524
* greet
 - greet
* inform{"price": "cheap", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 525
* greet
 - greet
* inform{"price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 526
* greet
 - greet
* inform{"cuisine": "spanish", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 527
* greet
 - greet
* inform{"number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 528
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 529
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 530
* greet
 - greet
* inform{"price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 531
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 532
* greet
 - greet
* inform{"cuisine": "indian", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 533
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 534
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 535
* greet
 - greet
* inform{"cuisine": "spanish", "number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 536
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 537
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 538
* greet
 - greet
* inform{"price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 539
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 540
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 541
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 542
* greet
 - greet
* inform{"cuisine": "italian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 543
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 544
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 545
* greet
 - greet
* inform{"number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 546
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 547
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 548
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 549
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 550
* greet
 - greet
* inform{"price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 551
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 552
* greet
 - greet
* inform{"number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 553
* greet
 - greet
* inform{"price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 554
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 555
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 556
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 557
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 558
* greet
 - greet
* inform{"number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 559
* greet
 - greet
* inform{"cuisine": "spanish", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 560
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 561
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 562
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 563
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 564
* greet
 - greet
* inform{"number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 565
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 566
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 567
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 568
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 569
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 570
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 571
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 572
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 573
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 574
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 575
* greet
 - greet
* inform{"price": "moderate", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 576
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 577
* greet
 - greet
* inform{"cuisine": "british", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 578
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 579
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 580
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 581
* greet
 - greet
* inform{"cuisine": "french", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 582
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 583
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 584
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 585
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 586
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 587
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 588
* greet
 - greet
* inform{"cuisine": "italian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 589
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 590
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 591
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 592
* greet
 - greet
* inform{"cuisine": "french", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 593
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 594
* greet
 - greet
* inform{"price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 595
* greet
 - greet
* inform{"cuisine": "spanish", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 596
* greet
 - greet
* inform{"cuisine": "british", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 597
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 598
* greet
 - greet
* inform{"number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 599
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 600
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 601
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 602
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 603
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 604
* greet
 - greet
* inform{"number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 605
* greet
 - greet
* inform{"price": "cheap", "number": "eight", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 606
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 607
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 608
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 609
* greet
 - greet
* inform{"cuisine": "french", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 610
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 611
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 612
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 613
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 614
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 615
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 616
* greet
 - greet
* inform{"cuisine": "italian", "number": "four", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 617
* greet
 - greet
* inform{"cuisine": "italian", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 618
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 619
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 620
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 621
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 622
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 623
* greet
 - greet
* inform{"price": "cheap", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 624
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 625
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 626
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 627
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 628
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 629
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 630
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 631
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 632
* greet
 - greet
* inform{"price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 633
* greet
 - greet
* inform{"cuisine": "french", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 634
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 635
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 636
* greet
 - greet
* inform{"cuisine": "indian", "number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 637
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 638
* greet
 - greet
* inform{"price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 639
* greet
 - greet
* inform{"cuisine": "british", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 640
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 641
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 642
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 643
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 644
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 645
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 646
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 647
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 648
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 649
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 650
* greet
 - greet
* inform{"price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 651
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 652
* greet
 - greet
* inform{"cuisine": "french", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 653
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 654
* greet
 - greet
* inform{"price": "expensive", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 655
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 656
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 657
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 658
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 659
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 660
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 661
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 662
* greet
 - greet
* inform{"cuisine": "french", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 663
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 664
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 665
* greet
 - greet
* inform{"price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 666
* greet
 - greet
* inform{"cuisine": "italian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 667
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 668
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 669
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 670
* greet
 - greet
* inform{"cuisine": "italian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 671
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 672
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 673
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 674
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 675
* greet
 - greet
* inform{"cuisine": "spanish", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 676
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 677
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 678
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 679
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 680
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 681
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 682
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 683
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 684
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 685
* greet
 - greet
* inform{"cuisine": "spanish", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 686
* greet
 - greet
* inform{"cuisine": "indian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 687
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 688
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 689
* greet
 - greet
* inform{"price": "cheap", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 690
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 691
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 692
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 693
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 694
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 695
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 696
* greet
 - greet
* inform{"cuisine": "french", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 697
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 698
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 699
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 700
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 701
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 702
* greet
 - greet
* inform{"price": "expensive", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 703
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 704
* greet
 - greet
* inform{"cuisine": "french", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 705
* greet
 - greet
* inform{"cuisine": "italian", "number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 706
* greet
 - greet
* inform{"price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 707
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 708
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 709
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 710
* greet
 - greet
* inform{"number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 711
* greet
 - greet
* inform{"price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 712
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 713
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 714
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 715
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 716
* greet
 - greet
* inform{"price": "expensive", "number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 717
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 718
* greet
 - greet
* inform{"cuisine": "indian", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 719
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 720
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 721
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 722
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 723
* greet
 - greet
* inform{"cuisine": "british", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 724
* greet
 - greet
* inform{"number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 725
* greet
 - greet
* inform{"number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 726
* greet
 - greet
* inform{"cuisine": "italian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 727
* greet
 - greet
* inform{"cuisine": "british", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 728
* greet
 - greet
* inform{"cuisine": "indian", "number": "eight", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 729
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 730
* greet
 - greet
* inform{"cuisine": "indian", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 731
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 732
* greet
 - greet
* inform{"number": "six", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 733
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 734
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 735
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 736
* greet
 - greet
* inform{"cuisine": "indian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 737
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 738
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 739
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 740
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 741
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 742
* greet
 - greet
* inform{"number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 743
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 744
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 745
* greet
 - greet
* inform{"price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 746
* greet
 - greet
* inform{"cuisine": "british", "number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 747
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 748
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 749
* greet
 - greet
* inform{"price": "expensive", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 750
* greet
 - greet
* inform{"price": "moderate", "number": "eight", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 751
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 752
* greet
 - greet
* inform{"cuisine": "spanish", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 753
* greet
 - greet
* inform{"number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 754
* greet
 - greet
* inform{"cuisine": "british", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 755
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 756
* greet
 - greet
* inform{"cuisine": "indian", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 757
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 758
* greet
 - greet
* inform{"cuisine": "italian", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 759
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 760
* greet
 - greet
* inform{"price": "moderate", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 761
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 762
* greet
 - greet
* inform{"cuisine": "italian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 763
* greet
 - greet
* inform{"number": "eight", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 764
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 765
* greet
 - greet
* inform{"cuisine": "spanish", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 766
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 767
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 768
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 769
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 770
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 771
* greet
 - greet
* inform{"cuisine": "indian", "number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 772
* greet
 - greet
* inform{"number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 773
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 774
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 775
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 776
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 777
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 778
* greet
 - greet
* inform{"cuisine": "spanish", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 779
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 780
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 781
* greet
 - greet
* inform{"price": "expensive", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 782
* greet
 - greet
* inform{"price": "moderate", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 783
* greet
 - greet
* inform{"cuisine": "british", "number": "two", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 784
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 785
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 786
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 787
* greet
 - greet
* inform{"cuisine": "italian", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 788
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 789
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 790
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 791
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 792
* greet
 - greet
* inform{"cuisine": "british", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 793
* greet
 - greet
* inform{"cuisine": "italian", "number": "six", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 794
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 795
* greet
 - greet
* inform{"cuisine": "spanish", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 796
* greet
 - greet
* inform{"cuisine": "italian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 797
* greet
 - greet
* inform{"cuisine": "british", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 798
* greet
 - greet
* inform{"price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 799
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 800
* greet
 - greet
* inform{"cuisine": "british", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 801
* greet
 - greet
* inform{"price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 802
* greet
 - greet
* inform{"cuisine": "indian", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 803
* greet
 - greet
* inform{"price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 804
* greet
 - greet
* inform{"cuisine": "italian", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 805
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 806
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 807
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 808
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 809
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 810
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 811
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 812
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 813
* greet
 - greet
* inform{"price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 814
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 815
* greet
 - greet
* inform{"price": "moderate", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 816
* greet
 - greet
* inform{"price": "cheap", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 817
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 818
* greet
 - greet
* inform{"number": "four", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 819
* greet
 - greet
* inform{"price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 820
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 821
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 822
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 823
* greet
 - greet
* inform{"price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 824
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 825
* greet
 - greet
* inform{"cuisine": "british", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 826
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 827
* greet
 - greet
* inform{"cuisine": "spanish", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 828
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 829
* greet
 - greet
* inform{"cuisine": "french", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 830
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 831
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 832
* greet
 - greet
* inform{"cuisine": "french", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 833
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 834
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 835
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 836
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 837
* greet
 - greet
* inform{"cuisine": "french", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 838
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 839
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 840
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 841
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 842
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 843
* greet
 - greet
* inform{"cuisine": "british", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 844
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 845
* greet
 - greet
* inform{"price": "cheap", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 846
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 847
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 848
* greet
 - greet
* inform{"price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 849
* greet
 - greet
* inform{"cuisine": "indian", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 850
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 851
* greet
 - greet
* inform{"price": "moderate", "number": "four", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 852
* greet
 - greet
* inform{"cuisine": "british", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 853
* greet
 - greet
* inform{"number": "four", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 854
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 855
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 856
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 857
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 858
* greet
 - greet
* inform{"price": "cheap", "number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 859
* greet
 - greet
* inform{"location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 860
* greet
 - greet
* inform{"cuisine": "indian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 861
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 862
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 863
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 864
* greet
 - greet
* inform{"cuisine": "italian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 865
* greet
 - greet
* inform{"price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 866
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 867
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 868
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 869
* greet
 - greet
* inform{"price": "expensive", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 870
* greet
 - greet
* inform{"price": "expensive", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 871
* greet
 - greet
* inform{"cuisine": "spanish", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 872
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 873
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 874
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 875
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 876
* greet
 - greet
* inform{"price": "cheap", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 877
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 878
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 879
* greet
 - greet
* inform{"cuisine": "british"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 880
* greet
 - greet
* inform{"cuisine": "italian", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 881
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 882
* greet
 - greet
* inform{"cuisine": "italian", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 883
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 884
* greet
 - greet
* inform{"price": "expensive"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 885
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 886
* greet
 - greet
* inform{"cuisine": "indian", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 887
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 888
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 889
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 890
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 891
* greet
 - greet
* inform{"cuisine": "italian", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 892
* greet
 - greet
* inform{"price": "cheap", "number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "london"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 893
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 894
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 895
* greet
 - greet
* inform{"price": "cheap", "number": "two", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 896
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 897
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 898
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 899
* greet
 - greet
* inform{"price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 900
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 901
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 902
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 903
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 904
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 905
* greet
 - greet
* inform{"cuisine": "indian"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 906
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 907
* greet
 - greet
* inform{"price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 908
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 909
* greet
 - greet
* inform{"cuisine": "indian", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 910
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 911
* greet
 - greet
* inform{"price": "expensive", "number": "four", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 912
* greet
 - greet
* inform{"price": "cheap", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 913
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 914
* greet
 - greet
* inform{"price": "expensive", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 915
* greet
 - greet
* inform{"number": "two", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 916
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 917
* greet
 - greet
* inform{"cuisine": "italian", "price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 918
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 919
* greet
 - greet
* inform{"cuisine": "british", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 920
* greet
 - greet
* inform{"cuisine": "spanish", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 921
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 922
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "location": "bombay"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 923
* greet
 - greet
* inform{"number": "four"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 924
* greet
 - greet
* inform{"price": "moderate", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 925
* greet
 - greet
* inform{"cuisine": "french", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 926
* greet
 - greet
* inform{"number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"location": "london"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 927
* greet
 - greet
* inform{"cuisine": "indian", "price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 928
* greet
 - greet
* inform{"price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"location": "paris"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 929
* greet
 - greet
* inform{"cuisine": "british", "price": "expensive", "location": "madrid"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 930
* greet
 - greet
* inform{"cuisine": "british", "price": "moderate"}
 - on_it
* silence
 - ask_location
* inform{"location": "rome"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 931
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 932
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 933
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 934
* greet
 - greet
* inform{"price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 935
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_location
* inform{"location": "rome"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 936
* greet
 - greet
* inform{"cuisine": "spanish", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "eight"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 937
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 938
* greet
 - greet
* inform{"cuisine": "italian", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 939
* greet
 - greet
* inform{"price": "moderate", "number": "two"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 940
* greet
 - greet
* inform{"cuisine": "french", "number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 941
* greet
 - greet
* inform{"cuisine": "spanish", "price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 942
* greet
 - greet
* inform{"price": "moderate", "number": "two", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 943
* greet
 - greet
* inform{"cuisine": "italian", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 944
* greet
 - greet
* inform{"location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "two"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 945
* greet
 - greet
* inform{"cuisine": "italian", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 946
* greet
 - greet
* inform{"price": "expensive", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 947
* greet
 - greet
* inform{"location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"number": "two"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 948
* greet
 - greet
* inform{"cuisine": "british", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 949
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 950
* greet
 - greet
* inform{"location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 951
* greet
 - greet
* inform{"price": "expensive", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 952
* greet
 - greet
* inform{"price": "cheap", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 953
* greet
 - greet
* inform{"price": "expensive", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "london"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 954
* greet
 - greet
* inform{"price": "cheap", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 955
* greet
 - greet
* inform{"price": "cheap", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"number": "four"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 956
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 957
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 958
* greet
 - greet
* inform{"cuisine": "french", "number": "six", "location": "madrid"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 959
* greet
 - greet
* inform{"number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 960
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "two"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "paris"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 961
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 962
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 963
* greet
 - greet
* inform{"price": "expensive", "number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"cuisine": "rome"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 964
* greet
 - greet
* inform{"cuisine": "spanish"}
 - on_it
* silence
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 965
* greet
 - greet
* inform{"number": "eight"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* inform{"location": "london"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 966
* greet
 - greet
* inform{"price": "moderate", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "italian"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "french"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 967
* greet
 - greet
* inform{"price": "expensive", "location": "london"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 968
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 969
* greet
 - greet
* inform{"cuisine": "french", "price": "expensive"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 970
* greet
 - greet
* inform{"cuisine": "italian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 971
* greet
 - greet
* inform{"cuisine": "spanish", "price": "cheap", "location": "london"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 972
* greet
 - greet
* inform{"price": "cheap", "number": "two", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 973
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "eight"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "rome"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 974
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 975
* greet
 - greet
* inform{"price": "cheap", "location": "madrid"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 976
* greet
 - greet
* inform{"number": "two", "location": "bombay"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 977
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* inform{"location": "paris"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 978
* greet
 - greet
* inform{"cuisine": "indian", "price": "moderate", "location": "rome"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 979
* greet
 - greet
* inform{"number": "six", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "french"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 980
* greet
 - greet
* inform{"cuisine": "indian", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "spanish"}
 - request_updates
* inform{"price": "cheap"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 981
* greet
 - greet
* inform{"cuisine": "spanish", "number": "four", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 982
* greet
 - greet
* inform{"cuisine": "british", "location": "paris"}
 - on_it
* silence
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 983
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "london"}
 - ask_number_of_people
* inform{"number": "four"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 984
* greet
 - greet
* inform{"cuisine": "indian", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "london"}
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 985
* greet
 - greet
* inform{"price": "expensive", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 986
* greet
 - greet
* inform{"location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_number_of_people
* inform{"number": "six"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 987
* greet
 - greet
* inform{"price": "cheap", "number": "four", "location": "paris"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 988
* greet
 - greet
* inform{"number": "six"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"cuisine": "bombay"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 989
* greet
 - greet
* inform{"cuisine": "spanish", "price": "moderate", "number": "six"}
 - on_it
* silence
 - ask_location
* inform{"location": "madrid"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 990
* greet
 - greet
* inform{"cuisine": "british", "number": "six", "location": "london"}
 - on_it
* silence
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "cheap"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 991
* greet
 - greet
* inform{"cuisine": "italian"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "madrid"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "moderate"}
 - announce_search
* silence
 - api_call
* inform{"location": "bombay"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* inform{"number": "six"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 992
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "spanish"}
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "eight"}
 - announce_search
* silence
 - api_call
* inform{"location": "madrid"}
 - request_updates
* inform{"price": "moderate"}
 - request_updates
* inform{"cuisine": "british"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 993
* greet
 - greet
* inform{"cuisine": "french"}
 - on_it
* silence
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "four"}
 - ask_price
* inform{"price": "expensive"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 994
* greet
 - greet
* inform{"cuisine": "french", "price": "cheap", "number": "four"}
 - on_it
* silence
 - ask_location
* inform{"location": "bombay"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* inform{"number": "two"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 995
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "indian"}
 - ask_location
* inform{"location": "paris"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"price": "expensive"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 996
* greet
 - greet
* inform{"price": "moderate"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"number": "six"}
 - request_updates
* inform{"cuisine": "italian"}
 - request_updates
* inform{"location": "bombay"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 997
* greet
 - greet
* inform{"price": "cheap"}
 - on_it
* silence
 - ask_cuisine
* inform{"cuisine": "british"}
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "six"}
 - announce_search
* silence
 - api_call
* inform{"location": "paris"}
 - request_updates
* inform{"price": "expensive"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

## 998
* greet
 - greet
* inform{"cuisine": "italian", "number": "eight", "location": "rome"}
 - on_it
* silence
 - ask_price
* inform{"price": "cheap"}
 - announce_search
* silence
 - api_call
* inform{"cuisine": "indian"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_phone
 - give_phone
* request_address
 - give_address
* thankyou
 - ask_anything_else
* bye
 - bye

## 999
* greet
 - greet
* inform{"cuisine": "indian", "price": "cheap"}
 - on_it
* silence
 - ask_location
* inform{"cuisine": "rome"}
 - ask_number_of_people
* inform{"number": "two"}
 - announce_search
* silence
 - api_call
* inform{"price": "moderate"}
 - request_updates
* inform{"number": "four"}
 - request_updates
* deny
 - announce_search
* silence
 - api_call
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* deny
 - announce_keep_searching
* silence
 - suggest_restaurant
* affirm
 - reserve
* request_address
 - give_address
* request_phone
 - give_phone
* thankyou
 - ask_anything_else
* bye
 - bye

