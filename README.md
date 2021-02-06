# Flask React Template App

![React CI](https://github.com/jj-style/FlaskReactTemplateApp/workflows/React%20CI/badge.svg)
![Flask CI](https://github.com/jj-style/FlaskReactTemplateApp/workflows/Flask%20CI/badge.svg)

Simple flask and react apps useful for starting a web project.  
  
Flask configured with a few `flask-restful` Resources and blueprints, easy to add more.  
Login managed with flask-login using jwt tokens between client and server.  
Posts resource configured as facade with an in memory and sqlalchemy implementation which can be selected via an environment variable.  
React has auth provider and login page which uses the JWT token in all requests.  

# Running
## Docker
Both apps come with a docker file which can be built and run. For example:
```
docker build . -t flaskapp:latest
docker run -p 80:8080 flaskapp:latest
```

Can also use docker-compose, once built both images run `docker-compose up`.

## Manually
In flask directory:  
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python run.py # or flask run
```
  
In react directory:  
```
npm install
npm run
```
