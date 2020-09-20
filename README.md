# Climate-karaoke

A karaoke web app which generates alternative lyrics for popular songs to address topics such as climate and environment. 

This project was created during HackZurich 2020. See the decription on [devpost](https://devpost.com/software/climate-karaoke).

## Start development environment

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


