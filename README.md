# lunchbreak
Screensaver fed by documents from MongoDB Atlas displayed with d3.js as Sankey diagram

# background

Revamped version of an earlier screensaver idea fed with live data.

# uses

MongoDB Atlas, Atlas Appservices, Appservices endpoints, functions and hosting, mongoimport. Bit of python and an html file with d3.js.

MongoDB Database tools (could switch to using Python and MongoDB Python client only but like the high throughput & mass import options in `mongoimport`).

```
exec bash
exec zsh
```

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/emilzegers/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
brew tap mongodb/brew
brew install mongodb-database-tools
```

# create data

Assumes you have a MongoDB cluster up and running in Atlas Data Services, a M0 is sufficient.

Export the Atlas Cluster uri to `mongodb_uri` like below on MacOS/*ix, use `SET` and %variable notation on Windows.

`export mongodb_uri=mongodb+srv://user:passyourcluster.at.mongodb.net/customerX`

Run the Python script as long as you want (break with ˆC) to create data and pipe it through `mongoimport` into the database in Atlas.

`python3 nodeslinksgenerator.py | mongoimport --uri $mongodb_uri --drop --collection funnel`

NOTE: I'm dropping the collection when (re)generating data, you can remove `--drop` from the command if you want to keep the data (but hey, it is random data anyway, so why bother). 

# Atlas App Services

In Atlas App Services, create a new app with your name of choice, I'm going for `SankeySaver`.

## create endpoint and function

In the newly created app, create an HTTPS Endpoint. Endpoint must have a route, pick somethign you like, I use `/saveme`.

Default HTTP Method is `POST`, change to `GET`. Make sure to switch the toggle for `Respond With Result` as it is off by default.

Copy the url into the your local `index.html` as the link you find in this repo will not keep on running forever.

In the HTTPS Endpoint page, create a function with [ + New Functiom ] and add the code from `findOne.js` with `findOne` as the name of the function.

Use the `Service Name` you find under `Linked Data Sources` as the `context.services.get` parameter.

Default function Authentication is `Application Authentication`, cahnge to `System`.

If you created an HTTP Endpoint for the first time in the previous step, you now have created a function directly as part of that, otherwise select the function.

## hosting file

NOTE: Hosting is no longer available with the free M0 tier, so go for a paid version like an M2 or use another (free) place where you can host static files.

To use hosting on Atlas, in the app, enable Hosting and delete the existing `index.html` (or rename to keep it), and upload your edited `index.html`, check you added your own HTTPS Endpoint first.

Or just test with a local webserver first (to avoid CORS issues with mixed content):

```
python -m SimpleHTTPServer 9000
```

or 

```
python3 -m http.server 9000
```

Open http://localhost:9000/

# relax

Open the uploaded html file in your browser and relax.

You can find an example (that might or might not be working) at https://stitch-statichosting-prod.s3.amazonaws.com/6318868fcb1c9f1272f639e3/index.html

![lb](https://user-images.githubusercontent.com/2260360/189126305-2073c8e9-640e-42df-ad8e-d1aa74a22eb8.png)

# remarks

The background color of the page is MongoDB green.
