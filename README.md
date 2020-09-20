# Climate-karaoke

A karaoke web app which generates alternative lyrics for popular songs to address topics such as climate and environment. 

This project was created during HackZurich 2020. See the decription on [devpost](https://devpost.com/software/climate-karaoke).

## Getting started 

First, get the backend running:
```
cd climate-karaoke

# using virtualenv is optional, but nice
python -m venv .venv
pip install -r requirements.txt

# on ubuntu:
source .venv/bin/activate
# on widnows:
./.venv/Scripts/activate

# run backend
python ./application.py
```

Then, run frontend:
```
cd client
yarn build
yarn start
```

## How does it all work?

The project consists primarily of two parts:

 - **environmental lyrics generaion** - we fetch Genius API to get get the original lyrics, and then run our NLP magic on top of it to alter them based on climate and environment-related data that we managed to obtain and bring awereness to the world,
 - **playing music** - we take Youtube videos (with Youtube API) and feed them to Spleeter - a fantastic tool from Deezer that allows splitting a vocal track from the rest of the audio. This way you can focus only on the newly generated environment-aware lyrics!
 
 
