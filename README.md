[![Python application test with Github Actions](https://github.com/nogibjj/Project-3-WM/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/nogibjj/Project-3-WM/actions/workflows/main.yml)

# Project-3-WM

## Introduction

Hi! Welcome to my 3rd Project for Data Engineering Class.

In this project, we will be focusing on SQL query to answer some lingering questions from a dataset.

## Demo Video
Here's a link to my [demo video.](https://youtu.be/6FkeP3xBnkQ)

## Flow Diagram
<img src=https://user-images.githubusercontent.com/104295829/200189520-0666812e-6ca6-4dd5-985d-4f233d3b6835.png width=75% height=75%>

## Dataset
Here's the link to [Kaggle Spotify Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) that I'm using. This dataset consist of 20 variables, with the primary variable of interests are:
- Popularity (0 - 100 scale, based on song)
- Artists
- Track Name
- Album Name
- Song Duration (miliseconds)
- Danceability (0 - 1 scale,  the higher means song is a dance song with high tempo, rythm, beat strength)
- Liveness (0 - 1 scale, the higher means song is recorded live)

## Try it yourself!

Be bold, duplicate this repo, try these code yourself!

I use Python Fire to make all functions accessible in the command line interface! Simply type `python filename.py command line`; for example: `python spotify_quest.py top_10_songs`

Here's some preliminary questions that I made to start the engine:

1. I love to dance!! I need to know the top and bottom 10 songs in the chart and their danceability score!
> For top and bottom chart, call the function `top_10_songs` and `bottom_10_songs`
> For their respective danceability score, call the function `dance_score_top_songs` and `dance_score_bottom_songs`

2. Our time in this world is limited. I want to know the average time I need to allocate to listen to the top and bottom songs in the chart?
> Call the function `avg_length_top_songs` and `avg_length_bottom_songs`

3. I hate covid-19!! I want to hear live songs so I feel like I'm in a concert, tell me the top live songs!!
> Call the function `top_10_live_songs`

4. Okay, enough with the live music, I need the songs with STUDIO quality!
> Call the function `top_10_studio_songs`

5. I need a whole album to accompany me making stats HW tonight, any suggestions?
> Call the function `top_10_albums`

6. I just started listening to Linkin Park again after 10 years (RIP Chester), do you know what their top songs are?
> Call the function `my_fav_band "Linkin Park`  -- This one is interactive, put any band name!!

7. Is there any other band that has "Faint" in their song title?
> Call the function `my_fav_song_distinct "Faint"` -- This one also interactive, play with it how you want!

8. Okay I only need to know what is the popularity score of "Somewhere I Belong"!
> Call the function `my_fav_song_all "Somewhere I Belong"` -- This one also interactive, play with it how you want!

Thanks for stopping by!
