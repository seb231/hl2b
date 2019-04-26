# hl2b

##  Project Goal

The project aims to build an app that can ultimately recommend games to a user based on a game they like, or even their own catalogue, based on data recovered from the website [howlongtobeat.com](www.howlongtobeat.com).

I will not be attempting to access user data but rather information which is freely available on the website, although a potential long term goal is to host an app, which can recommend games to a user based on the users history, such as games played, type of games and playtimes.

Currently I am planning on developing all of this open source, at least initially, and code in Python, just simply for the ease of collecting data from webpages and the availability of data science tools. Also it means potentially others are more able to get involved, due to Python being so widely adopted (unlike my previous project in Clojure, see below).

This project is a follow up to my original aim of building an app to recommend video games through the, now essentially defunct, Steam API, details of which can be found [here](https://github.com/seb231/steamie.window).

## Tasks
1. ~~Find *all* titles~~
2. ~~What data can be collected from a title~~
3. ~~Create database of titles with useful data from _2_~~
4. Create some summary stats and plots
5. Create program for updating or rebuilding the database from the website - PRIORITISE THIS and push to AWS
6. Do some title cluster analysis
7. Long term goal 1: Predict a games playtime based on some useful variables (genre, dev, publisher)
8. Long term goal 2: Would it be possible to input a username and generate a short list of recommended games based on a user's library and their playtimes?
9. Allow better rules for when a game does not have the all requested data (currently only recovers ~8k games)
10. What other useful information can be gathered?

## Requirements
- Python3

Python libs
- lxml
- requests
- bs4
- numpy
- pandas
