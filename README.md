# SmartSpot
Generating a smart playlist based on favourite taste with great transitions between songs

## Abstract

Pyro from Serato is known for its ability to be an automatic DJ for parties whereas Pyro automatically fades from song to song. Pyro is no longer supported by Spotify since May 7th 2020, hence a possible challenge could be to replicate, if not even improve the application's abilities with additional features in future iterations. Smartspot shall offer these capabilites together with Spotify again. 

## Basic Idea

Use different data sets from kaggle and train a network with multiple attributes/features to create a playlist for a great party/event.

### Two subproblems of creating a playlist

1. Creating a playlist (define an optimal playlist given a huge library)
2. Reorder a given tracklist (take a sample set of songs and choose the optimal order)

### How do you know that a song can be transitioned to another one?

According to different sources, Serato Pyro uses following effects for transitions:

1. Pitch in Time (Adjustment of BPM such that they match in pitch)
2. Blending/crossfading similar BPMs
3. 

### Pyro scores

Pyro has a scoring system whereas two songs seem to transition well if their scores are similar or identical. 



## Literature 

#### Spotify API

https://developer.spotify.com/documentation/web-api/

#### Spotify iOS SDK

https://developer.spotify.com/documentation/ios/

#### Paper on mathematical interpretation

https://ejhumphrey.com/assets/pdf/bittner2017automatic.pdf

This paper introduces three important features that need to be included into such a model:

- Acoustic vectors: Train a convolutional neural network (CNN with 16 nodes) to reproduce filtering vectors in R^2048 where the acoustic vectors should match in eudlidian space close to each other
- Key and mode: Information about key
- Tempo

### Pacemaker - A company with patents in mixing music in an app

https://patentimages.storage.googleapis.com/0a/a4/3e/eaa8a77991ef6a/US10078488.pdf
