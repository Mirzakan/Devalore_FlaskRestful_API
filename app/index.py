from flask_swagger import swagger
from flask import make_response, jsonify, redirect
import json
import flask
from flask_swagger_ui import get_swaggerui_blueprint

app = flask.Flask(__name__)
app.config["DEBUG"] = True

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app': "Devalore Assignment Restfull API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

@app.route("/")
def spec():
    return redirect("http://localhost:5000/swagger", code=302)

@app.route('/users', methods=['GET'])
def getUsers():
    data = getData()
    for key in data:
        data[key].pop('id')     
    return data

@app.route('/user/<username>', methods=['GET'])
def getUser(username):
    data = getData()
    for key in data:
        if key == username:
            return {key : data[key]}
    response = make_response('The page named %s does not exist.' \
                             % username, 404)
    return response

def getData():
    with open('db/users.json') as json_file:
        data = json.load(json_file)  
    return data


# make docker container visible
app.run(host='0.0.0.0', port=5000)
























