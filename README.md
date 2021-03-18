# MicroOrchestration

## About

A Simple bot that interact with MicroController (Arduino)

## Currently Avalaile Command:

| Command  | Description          |
| -------- | -------------------- |
| turn_on  | turn on arduino LED  |
| turn_off | turn off arduino LED |
| status   | check arduino status |

## For Development Purpose

| Command | Description                           |
| ------- | ------------------------------------- |
| test    | checking of bot active or not         |
| help    | Display what function can be executed |
| load    | load cogs                             |
| unload  | unload cogs                           |
| reload  | unload and load All cogs              |

## For Future Development

## Todo

- [x] Tiddy up the Code
- [ ] Interact with MicroController (Arduino)
- [ ] Adding Temperature Record to database
- [ ] View Temperatre Record from database
- [ ] Scanning temperature
- [ ] Controlling status LED

## Requierments

- Python 3.9.1
- discord
- pymongo

## Instalation

Make sure you run this command at same folder.

```
-> Windows
pip install -r requirements.txt
python app.py

-> Linux
pip3 install -r requirements.txt
python3 app.py

```

## Docker

Make sure you run this command at same folder.

```
docker build username/name:tag .

docker run -d --env-file ./.env <DOCKER CONTAINER ID>
```
