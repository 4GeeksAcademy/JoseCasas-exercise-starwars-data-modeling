import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)
    first_name = Column(String, unique=False, nullable=False)
    last_name = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number =Column(String, unique=False, nullable=True)
    gender = Column(String, unique=False, nullable=False)

    favorites = relationship('favorites', back_populates='user')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    specie = Column(String, unique=False, nullable=False)
    height = Column(String, unique=False, nullable=False)
    mass = Column(String, unique=False, nullable=False)

    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    climate = Column(String, unique=False, nullable=False)
    population = Column(String, unique=False, nullable=False)
    size = Column(String, unique=False, nullable=False)

    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    life_span = Column(String, unique=False, nullable=False)
    planet = Column(String, unique=False, nullable=False)
    skin_color = Column(String, unique=False, nullable=False)

    # user_id = Column(Integer, ForeignKey('user.id'))


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    species_id = Column(Integer, ForeignKey('species.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)
    characters = relationship(Characters)
    species = relationship(Species)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')