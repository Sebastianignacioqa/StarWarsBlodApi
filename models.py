from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id= db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id

    def serialize(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'email': self.email 
        }

    def serialize_just_username(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'email': self.email 
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #fav_planet_id = db.Column(db.Integer, db.ForeignKey('planets.planet_id'))
    #planets = db.relationship('Planets')
    #fav_character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'))
    #characters = db.relationship('Characters')
    #fav_vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.vehicle_id'))
    #vehicles = db.relationship('Vehicles')

class Planets(db.Model):
    __tablename__ = 'planets'
    planet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    climate = db.Column(db.String(200))
    terrain = db.Column(db.String(200))
    population = db.Column(db.Integer)
    diameter= db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    surface_water = db.Column(db.Integer)
    residents = db.Column(db.String(200))
    #characters = db.relationship('Characters')

    def __repr__(self):
        return "<Planets %r>" % self.planet_id

    def serialize(self):
        return {
            'planet_id': self.planet_id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
            'diameter': self.diameter, 
            'rotation_period': self.rotation_period, 
            'orbital_period': self.orbital_period, 
            'surface_water': self.surface_water,
            'residents': self.residents
        }

    def serialize_just_username(self):
        return {
            'planet_id': self.planet_id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
            'diameter': self.diameter, 
            'rotation_period': self.rotation_period, 
            'orbital_period': self.orbital_period, 
            'surface_water': self.surface_water,
            'residents': self.residents
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    character_id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(200))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(200))
    skin_color = db.Column(db.String(200))
    eye_color = db.Column(db.String(200))
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(200))
    homeworld = db.Column(db.String(200))
    #planets = db.relationship('Planets')
    #vehicles = db.Column(db.String(200))
    #vehicles = db.relationship('Vehicles')

    def __repr__(self):
        return "<Characters %r>" % self.character_id

    def serialize(self):
        return {
            'character_id': self.character_id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color, 
            'eye_color': self.eye_color, 
            'birth_year': self.birth_year, 
            'gender': self.gender,
            'homeworld': self.homeworld
            #'vehicles': self.vehicles
        }

    def serialize_just_username(self):
        return {
            'character_id': self.character_id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color, 
            'eye_color': self.eye_color, 
            'birth_year': self.birth_year, 
            'gender': self.gender,
            'homeworld': self.homeworld
            #'vehicles': self.vehicles
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    vehicle_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    model = db.Column(db.String(200))
    manufacturer = db.Column(db.String(200))
    cost_in_credits = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    vehicle_class = db.Column(db.String(200))
    pilots = db.Column(db.String(200))
    #characters = db.relationship('Characters')

    def __repr__(self):
        return "<Vehicles %r>" % self.vehicle_id

    def serialize(self):
        return {
            'vehicle_id': self.vehicle_id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'crew': self.crew, 
            'passengers': self.passengers, 
            'cargo_capacity': self.cargo_capacity, 
            'vehicle_class': self.vehicle_class,
            'pilots ': self.pilots 
        }

    def serialize_just_username(self):
        return {
            'vehicle_id': self.vehicle_id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'crew': self.crew, 
            'passengers': self.passengers, 
            'cargo_capacity': self.cargo_capacity, 
            'vehicle_class': self.vehicle_class,
            'pilots ': self.pilots
        }


