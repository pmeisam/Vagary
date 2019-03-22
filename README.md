# Vagary

![](https://i.imgur.com/fHmgtx1.png)


### Introduction

Let's face it, travelling can be incredibly expensive, and it's hard to know what destinations are even available to you on your budget. Enter Vagary, a full-service travel planning app that matches you with flights and hotels based on your travel budget. Whethere you're planning a romantic getaway, a family vacation, or just need a weekend escape, Vagary is the app for you -- any budget, any time.

### Technologies Used

+ **PostgreSQL**
+ **Python**
+ **Django**
+ **Heroku**
+ **Amadeus API**
+ **IATA Codes API**


### Pitch-Deck

https://docs.google.com/presentation/d/1fX7aM9dEpv-n8vV4KU2qez4uc5lbHT2IU8ZylUF12eY/edit#slide=id.gc6f59039d_0_5

### Trello

https://trello.com/b/CRkhxSSg/vagary

### Heroku

https://vagary.herokuapp.com/

### RESTful API endpoints

GET https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=MAD

GET https://test.api.amadeus.com/v1/shopping/flight-offers?origin=NYC&destination=MAD&departureDate=2019-08-01&max=2

GET https://test.api.amadeus.com/v2/shopping/hotel-offers?cityCode=PAR&adults=1&radius=5&radiusUnit=KM&paymentPolicy=NONE&includeClosed=false&bestRateOnly=true&view=FULL&sort=PRICE

### Unsolved problems

The API will provide destinations that don't have any associated flights

The API doesn't work with all airports

### Future Enhancements

Search events and restaurants

Leave notes or messages for the trip

Add other friends to the trip

Add photos of the trip
