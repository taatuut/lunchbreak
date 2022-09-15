# lunchbreak
Screensaver fed by documents from MongoDB Atlas displayed with d3.js as Sankey diagram

# background

Revamped version of an earlier screensaver idea fed with live data.

# uses

MongoDB Atlas, Atlas Appservices, Appservices endpoints, functions and hosting, mongoimport. Bit of python and an html file with d3.js.

# create data

Assumes you have a MongoDB Atlas cluster up and running, a M0 is sufficient.

Export the Atlas Cluster uri to `mongodb_uri` like below on MacOS/*ix, use `SET` and %variable notation on Windows.

`export mongodb_uri=mongodb+srv://user:passyourcluster.at.mongodb.net/customerX`

Run the Python script as long as you want to create data and pipe it through `mongoimport` into the database in Atlas.

NOTE: I'm dropping the collection when (re)generating data, you can remove `--drop` from the command if you want to keep the data (but hey, it is random data anyway, so why bother). 

`python3 nodeslinksgenerator.py | mongoimport --uri $mongodb_uri --drop --collection funnel`

# Atlas App Services

In Atlas, create a new app with your name of choice.

## endpoint

In the newly created Atlas App Services app, create an HTTPS Endpoint. Copy this url into the `index.html` as the link you find there will not keep on runnign forever.

## function

In the App Services app, create a function and add the code from `findOne.js`. If you created an HTTP Endpoint for the first time in the previous step, you probably created a function directly as part of that.

## hosting file

In the app, enable Hosting and delete the existing `index.html` (or rename to keep it), and upload `index.html`, make sure you added your own HTTPS Endpoint first.

# relax

Open the uploaded html file in your browser and relax.

You can find an example (that might or might not be working) at https://stitch-statichosting-prod.s3.amazonaws.com/6318868fcb1c9f1272f639e3/index.html

![lb](https://user-images.githubusercontent.com/2260360/189126305-2073c8e9-640e-42df-ad8e-d1aa74a22eb8.png)

# remarks

The background color of the page is MongoDB green.
