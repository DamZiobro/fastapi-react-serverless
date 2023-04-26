## FastAPI + React + Serverless

Template Full Stack serverless application composed of:
* **RESTful API** build based on [FastAPI](https://fastapi.tiangolo.com/) framework
* **Frontend UI** build based on [React](https://react.dev/) and [Next.js](https://nextjs.org/) framework with [Typescript](https://www.typescriptlang.org/) template
* **automatic deployment** scripts based on [Serverless framework](https://www.serverless.com/) and deploying both UI and RESTful API to [Google Could Run](https://cloud.google.com/run) cloud service

### Getting started - run locally

1. Make sure that all project dependencies are installed by running:
```
make deps
```
2. Fill your .env config files based on .env.example examples:
```
cd todo-frontend/.env.example todo-frontend/.env
```
**Edit the `todo-frontend/.env` file manually** and fill all the required vars.

3. Run both API and Frontend locally: 
```
make run
```
4. Make sure both API and UI are up-and running opening those URLs in your browser
[Rest API - http://localhost:8000](http://localhost:8000)
[Frontend UI - http://localhost:3000](http://localhost:3000)

### Deploy to Google Cloud Run

In order to deploy project to [Google Cloud Run](https://cloud.google.com/run) service please use this command:
```
make deploy
```


### Cleaning project

To clean the project, remove all dependencies and start from scratch you can
use command:
```
make clean
```
