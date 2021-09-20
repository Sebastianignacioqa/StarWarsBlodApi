import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Planets, Characters, Vehicles, Favorite
from flask_migrate import Migrate
#from flask_script import Manager

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db") 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
#manager = Manager(app)
Migrate(app, db)
db.init_app(app)


@app.route('/')
def home():
    return jsonify('Creando Star Wars API')


@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "GET":
        user = User.query.get(1)
        if user is not None:
            return jsonify(user.serialize())
    else:
        user = User()
        user.user_name = request.json.get("user_name")
        user.first_name = request.json.get("first_name")
        user.last_name = request.json.get("last_name")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        
        db.session.add(user)
        db.session.commit()

    return jsonify(user.serialize()), 200



@app.route("/favorite", methods=["POST", "GET"])
def favorite():
    if request.method == "GET":
        favorite = Favorite.query.get(1)
        if favorite is not None:    #Lo cambié por "favorite" porque decia "planets"
            return jsonify(favorite.serialize())
    else:
        favorite = Favorite()
        favorite.user_id = request.json.get("user_id")
        favorite.fav_planet_id = request.json.get("fav_planet_id")
        favorite.fav_character_id = request.json.get("fav_character_id")
        favorite.fav_vehicle_id = request.json.get("fav_vehicle_id")

        db.session.add(favorite)
        db.session.commit()

    return jsonify(favorite.serialize()), 200


@app.route("/planets", methods=["POST", "GET"])
def planets():
    if request.method == "GET":
        planets = Planets.query.get(4)
        if planets is not None:
            return jsonify(planets.serialize_just_name())
    else:
        planets = Planets()
        planets.name = request.json.get("name")
        planets.climate = request.json.get("climate")
        planets.terrain = request.json.get("terrain")
        planets.population = request.json.get("population")
        planets.diameter = request.json.get("diameter")
        planets.rotation_period = request.json.get("rotation_period")
        planets.orbital_period = request.json.get("orbital_period")
        planets.surface_water = request.json.get("surface_water")
        planets.residents = request.json.get("residents")
        
        db.session.add(planets)
        db.session.commit()

    return jsonify(planets.serialize()), 200

@app.route("/planets/planetlist", methods=["POST", "GET"])
def planetlist():    
    if request.method == "GET":
        planetas = ["Tatooine", "Alderaan", "Yavin IV", "Hoth", "Dagobah", "Bespin"]
        return jsonify(planetas(map(planetas, planetas)))


@app.route("/characters", methods=["POST", "GET"])
def characters():
    if request.method == "GET":
        characters = Characters.query.get(1)
        if characters is not None:
            return jsonify(characters.serialize_just_name())
    else:
        characters = Characters()
        characters.name = request.json.get("name")
        characters.height = request.json.get("height")
        characters.mass = request.json.get("mass")
        characters.hair_color = request.json.get("hair_color")
        characters.skin_color = request.json.get("skin_color")
        characters.eye_color = request.json.get("eye_color")
        characters.birth_year = request.json.get("birth_year")
        characters.gender = request.json.get("gender")
        characters.homeworld = request.json.get("homeworld")
        #characters.vehicles = request.json.get("vehicles")
        
        db.session.add(characters)
        db.session.commit()

    return jsonify(characters.serialize()), 200


@app.route("/vehicles", methods=["POST", "GET"])
def vehicles():
    if request.method == "GET":
        vehicles = Vehicles.query.get(1)
        if vehicles is not None:
            return jsonify(vehicles.serialize_just_name())
    else:
        vehicles = Vehicles()
        vehicles.name = request.json.get("name")
        vehicles.model = request.json.get("model")
        vehicles.manufacturer = request.json.get("manufacturer")
        vehicles.cost_in_credits = request.json.get("cost_in_credits")
        vehicles.crew = request.json.get("crew")
        vehicles.passengers = request.json.get("passengers")
        vehicles.cargo_capacity = request.json.get("cargo_capacity")
        vehicles.vehicle_class = request.json.get("vehicle_class")
        vehicles.pilots = request.json.get("pilots")

        db.session.add(vehicles)
        db.session.commit()

    return jsonify(vehicles.serialize()), 200



if __name__ == "__main__":
    app.run(host='localhost', port=8080)