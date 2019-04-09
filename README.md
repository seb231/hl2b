# hl2b

##  Project Goal

The project aims to build an app that can ultimately recommend games to a user based on a game they like, or even their own catalogue, based on data recovered from the website [howlongtobeat.com](www.howlongtobeat.com).

So as not to cause issues for the website and creator, [Everdread](https://howlongtobeat.com/user.php?n=Everdred), my short term plan is to create my own database of games, collected from the website. Ideally I'd build a small program which can do this periodically so as to collect new game information and details such as typical play times, when they are updated. This database will also be comparatively small, when compared to the amount of data available on the actual HowLongToBeat website, for ease of storage and for rapid development of apps that can query the database.

I will not be attempting to access user data but rater information which is freely available on the website, although a potential long term goal is to host an app, which can recommend games to a user based on the users history, such as games played, type of games and playtimes.

Currently I am planning on developing all of this open source, at least initially, and code in Python, just simply for the ease of collecting data from webpages and the availability of data science tools. Also it means potentially other are more likely to get involved, due to Python being so widely adopted (unlike my previous project in Clojure, see below).

This project is a follow up to my original aim of building an app to recommend video games through the, now essentially defunct, Steam API, details of which can be found [here](https://github.com/seb231/steamie.window).

## Tasks
1. ~~Find *all* titles~~
2. ~~What data can be collected from a title~~
3. Create database of titles with useful data from _2_ (How big will this be? Where will it be stored? Locally?)
4. Create some summary stats and plots
5. Create program for updating or rebuilding the database from the website - PRIORITISE THIS and push to AWS
6. Search database with a title (i.e. not an ID number) ([this](https://www.somebits.com/~nelson/pandas-multiindex-slice-demo.html) may help)
7. Do some title cluster analysis
8. Long term goal 1: Predict a games playtime based on some useful variables (genre, dev, publisher
9. Long term goal 2: Would it be possible to input a username and generate a short list of recommended games based on a user's library and their playtimes?
