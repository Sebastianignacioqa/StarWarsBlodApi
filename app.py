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
        user = User.query.all()
        user = list(map(lambda user: user.serialize(), user))
        if user is not None:
            return jsonify(user)
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

@app.route("/user/favorite", methods=["POST", "GET"])
def favorite():
    if request.method == "GET":
        favorite = Favorite.query.get(1)
        if favorite is not None:   
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

@app.route("/favorite/planets/<int:planet_id>", methods=["POST"])
def addplanetid(planet_id):
    if request.method == "POST":
        
        favorite = Favorite()
        favorite.user_id = request.json.get("user_id")
        favorite.fav_planet_id = request.json.get("planet_id")

        db.session.add(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 200

@app.route("/favorite/characters/<int:character_id>", methods=["POST"])
def addcharacterid(character_id):
    if request.method == "POST":
        
        favorite = Favorite()
        favorite.user_id = request.json.get("user_id")
        favorite.fav_character_id = request.json.get("character_id")

        db.session.add(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 200

@app.route("/favorite/vehicles/<int:vehicle_id>", methods=["POST"])
def addvehicleid(vehicle_id):
    if request.method == "POST":
        
        favorite = Favorite()
        favorite.user_id = request.json.get("user_id")
        favorite.fav_vehicle_id = request.json.get("vehicle_id")

        db.session.add(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 200

@app.route("/favorite/vehicles/<int:vehicle_id>", methods=["DELETE"])
def deletevehicleid(vehicle_id):
    if request.method == "DELETE":
        
        favorite = Favorite.query.get(vehicle_id)

        db.session.delete(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 200

@app.route("/favorite/characters/<int:character_id>", methods=["DELETE"])
def deletecharacters(character_id):
    if request.method == "DELETE":
        
        favorite = Favorite.query.all()
        favorite.fav_character_id = request.json.get("character_id")
        favorite.user_id = request.json.get("user_id")

        db.session.delete(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 200

@app.route("/favorite/planets/<int:planet_id>", methods=["DELETE"])
def deleteplanets(planet_id):
    if request.method == "DELETE":
        
        favorite = Favorite.query.filter_by(user_id = 1).first()
        favorite.fav_planet_id = request.json.get("planet_id")

        db.session.delete(favorite)
        db.session.commit()
        return jsonify(favorite.serialize()), 200

@app.route("/planets", methods=["POST", "GET"])
def planets():
    if request.method == "GET":
        planets = Planets.query.all()
        planets = list(map(lambda planets: planets.serialize(), planets))
        if planets is not None:
            return jsonify(planets)
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


@app.route("/addplanets", methods=["POST"])
def addplanets(): 
    planets_list = request.json.get("planets_list")  
    for planets in planets_list:
        new_planets = Planets()
        new_planets.name= planets["name"]
        new_planets.climate = planets["climate"]
        new_planets.terrain = planets["terrain"]
        new_planets.population = planets["population"]
        new_planets.diameter = planets["diameter"]
        new_planets.rotation_period = planets["rotation_period"]
        new_planets.orbital_period = planets["orbital_period"]
        new_planets.surface_water = planets["surface_water"]
        new_planets.residents = planets["residents"]

        db.session.add(new_planets)
        db.session.commit()

    return jsonify("Done"), 200


@app.route("/planets/<int:planet_id>", methods=["GET","POST"])
def planet(planet_id):
    if request.method == "GET":
        if planet_id is not None:
            planets = Planets.query.get(planet_id)
            return jsonify(planets.serialize()), 200
        else:
            return jsonify('Missing id parameter in route'), 404
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


@app.route("/characters", methods=["POST", "GET"])
def characters():
    if request.method == "GET":
        characters = Characters.query.all()
        characters = list(map(lambda characters: characters.serialize(), characters))
        if planets is not None:
            return jsonify(characters)
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


@app.route("/characters/<int:character_id>", methods=["GET","POST"])
def character(character_id):
    if request.method == "GET":
        if character_id is not None:
            characters = Characters.query.get(character_id)
            return jsonify(characters.serialize()), 200
        else:
            return jsonify('Missing id parameter in route'), 404
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
        vehicles = Vehicles.query.all()
        vehicles = list(map(lambda vehicles: vehicles.serialize(), vehicles))
        if vehicles is not None:
            return jsonify(vehicles)
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


@app.route("/addvehicles", methods=["POST"])
def addvehicles(): 
    vehicles_list = request.json.get("vehicles_list")  
    for vehicles in vehicles_list:
        new_vehicles = Vehicles()
        new_vehicles.name= vehicles["name"]
        new_vehicles.model = vehicles["model"]
        new_vehicles.manufacturer = vehicles["manufacturer"]
        new_vehicles.cost_in_credits = vehicles["cost_in_credits"]
        new_vehicles.crew = vehicles["crew"]
        new_vehicles.passengers = vehicles["passengers"]
        new_vehicles.cargo_capacity = vehicles["cargo_capacity"]
        new_vehicles.vehicle_class = vehicles["vehicle_class"]
        #new_vehicles.pilots = vehicles["pilots"]

        db.session.add(new_vehicles)
        db.session.commit()
        
    return jsonify("Done"), 200


@app.route("/vehicles/<int:vehicle_id>", methods=["GET","POST"])
def vehicle(vehicle_id):
    if request.method == "GET":
        if vehicle_id is not None:
            vehicles = Vehicles.query.get(vehicle_id)
            return jsonify(vehicles.serialize()), 200
        else:
            return jsonify('Missing id parameter in route'), 404
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