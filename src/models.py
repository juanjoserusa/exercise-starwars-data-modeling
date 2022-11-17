import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    user_name = Column(String(250))
    password = Column(String(250))
    email = Column(String(250))
    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'
    id = Column(String(250), primary_key=True)
    name = Column(String(250))
    hair_color = Column(String(250))
    gender = Column(String(250))
    
    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(String(250), primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))

    
    def to_dict(self):
        return {}

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(String(250), ForeignKey('character.id'))
    planet_id = Column((String(250)), ForeignKey('planet.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
