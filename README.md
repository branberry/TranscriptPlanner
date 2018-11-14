# Welcome to the Transcript Planner!

-------------------------------------------------------------
## The Tech stack

For the Front-end, we are using VueJS with a custom template from Creative Tim.  The source can be found [here.](https://www.creative-tim.com/product/vue-black-dashboard?affiliate_id=104113&ref=madewithvuejs.com#)
For the Back-end, we are using a simple Python Flask app!

## Setup

### Flask App (Back-end)
For the Flask app, you will want to have Python installed, and you will need to run the following commands:
```pip install -U Flask```
```pip install -U flask-cors```
To run the flask app on Windows, type the following commands if you are using PowerShell within the repository:

```$env:FLASK_APP = "transcriptPlanner"```
```$env:FLASK_ENV = "development"```
```flask run```

If you are using the Command Prompt, you will want to type the following commands within the repository:
```set FLASK_APP=transcriptPlanner```
```set FLASK_ENV=development```
```flask run```

For Mac/Linux:
```export FLASK_APP=transcriptPlanner```
```export FLASK_ENV=development```
```flask run```

### Vue App (Front-end)

For flask you will need [NodeJS](https://nodejs.org/en/) and  the [Yarn Package Manager](https://yarnpkg.com/en/).

After these have been installed, CD into the vue-black-dashboard-master directory and run the following command to install the dependencies:
```yarn```

If you are on Mac/Linux you might need to run ```sudo``` with the previous command:

```sudo yarn```

After this has completed, you can type the following command within the vue-black-dashboard-master directory to spin up a front-end web server:

```yarn run dev```

or 

```sudo yarn run dev```

if on Mac/Linux.