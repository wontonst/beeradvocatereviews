# Beeradvocatereviews

Beeradvocatereviews is a module that lets you export a user's reviews
from Beer Advocate.

Usage is very simple. To install:

```
pip install beeradvocatereviews
```

To run

```
beeradvocatereviews MyUsername NumberOfReviewsIHave
```

e.g.

```
beeradvocatereviews TheHefe 231
```

The output is in JSON, and is an array of objects, e.g.

```
[
   {
         "comment":"look: 3 | smell: 3.75 | taste: 4.25 | feel: 4 |  overall: 4\n/5 rDev +1%",
		 "rating":"3.98",
		 "style":"Hefeweizen",
		 "name":"Hefeweizen",
		 "url":"/beer/profile/26607/101363/?ba=TheHefe#review",
		 "abv":"4.70",
		 "date":"11-27-2016",
		 "brewery":"Occidental Brewing Co."
   }
]
```
