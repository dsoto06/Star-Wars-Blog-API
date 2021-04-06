from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=True, nullable=False)
    skin_color = db.Column(db.String(250), unique=True, nullable=False)
    eye_color = db.Column(db.String(250), unique=True, nullable=False)
    birth_year = db.Column(db.Integer, unique=False, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)
    gravity = db.Column(db.Integer, unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    climate = db.Column(db.String(250), unique=True, nullable=False)
    terrain = db.Column(db.String(250), unique=True, nullable=False)
    surface_water = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    id = db.Column(db.Integer, primary_key=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    planets = db.relationship('Planets')
    users = db.relationship('Users')
    characters = db.relationship('Planets')

    def __repr__(self):
        return '<Favorites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "planets_id": self.planets_id,
            "character_id": self.character_id,
            "users_id": self.users_id,
           
            # do not serialize the password, its a security breach
        }
