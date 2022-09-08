# lunchbreak
Screensaver fed by documents from MongoDB Atlas displayed with d3.js as Sankey diagram

# background

Revamped version of an earier screensaver idea fed with live data.

# uses

MongoDB Atlas, Atlas Appservices, Appservices endpoints, functions and hosting, mongoimport. Bit of python and an html file with d3.js.

## endpoint

Atlas Appservices <TODO>

## function

Atlas Appservices <TODO>

## hosting file

Atlas Appservices <TODO>

# create data

Export Atlas uri to `mongodb_uri` like below on MacOS/*ix, use `SET` and %variable notation on Windows.

`export mongodb_uri=mongodb+srv://user:passyourcluster.at.mongodb.net/customerX`

Run Python script as long as you want

`python3 nodeslinksgenerator.py | mongoimport --uri $mongodb_uri --drop --collection funnel`

# relax

Add the HTTPS endpoint url to the html file, open it and relax.

Find an example at https://stitch-statichosting-prod.s3.amazonaws.com/6318868fcb1c9f1272f639e3/index.html

![lb](https://user-images.githubusercontent.com/2260360/189126305-2073c8e9-640e-42df-ad8e-d1aa74a22eb8.png)

# remarks

The background color of the page is MongoDB green.
