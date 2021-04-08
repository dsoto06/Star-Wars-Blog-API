"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Characters, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# -----------------------------------------------------------------------------
@app.route('/users', methods=['GET'])
def getUser():

    user_query = Users.query.all()
    all_users = list(map(lambda x: x.serialize(), user_query))

    return jsonify(all_users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def getUsersId(user_id):

    user = Users.query.get(user_id)
    if user is None:
        raise APIException('User does not exist', status_code=405)
    result = user.serialize()
    return jsonify(result), 200

# -----------------------------------------------------------------------------

@app.route('/characters', methods=['GET'])
def getCharacters():

    characters_query = Characters.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters_query))

    return jsonify(all_characters), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def getCharactersId(character_id):

    character = Characters.query.get(character_id)
    if character is None:
        raise APIException('Character does not exist', status_code=405)
    result = character.serialize()
    return jsonify(result), 200

# -----------------------------------------------------------------------------

@app.route('/planets', methods=['GET'])
def getPlanets():

    planets_query = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets_query))

    return jsonify(all_planets), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def getPlanetsId(planet_id):

    planet = Planets.query.get(planet_id)
    if planet is None:
        raise APIException('Planet does not exist', status_code=405)
    result = planet.serialize()
    return jsonify(result), 200

# -----------------------------------------------------------------------------

@app.route('/favorites', methods=['GET'])
def getFavorites():

    favorites_query = Favorites.query.all()
    all_favorites = list(map(lambda x: x.serialize(), favorites_query))

    return jsonify(all_favorites), 200
































# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
