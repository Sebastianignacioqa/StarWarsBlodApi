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

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fav_planet_id = db.Column(db.Integer, db.ForeignKey('planets.planet_id'))
    planets = db.relationship('Planets')
    fav_character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'))
    characters = db.relationship('Characters')
    fav_vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.vehicle_id'))
    vehicles = db.relationship('Vehicles')

class Planets(Base):
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
    residents = db.Column(db.Integer, ForeignKey('characters.character_id'))
    characters = db.relationship('Characters')

class Characters(Base):
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
    homeworld = db.Column(db.Integer, db.ForeignKey('planets.planet_id'))
    planets = db.relationship('Planets')
    vehicles = db.Column(Integer, db.ForeignKey('vehicles.vehicle_id'))
    vehicles = db.relationship('Vehicles')

class Vehicles(Base):
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
    pilots = db.Column(db.Integer, db.ForeignKey('characters.character_id'))
    characters = db.relationship('Characters')

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
            'first_name': self.first_name
        }
