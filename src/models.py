import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


   

class Character(Base):
    __tablename__='character'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
    age = Column(Integer,nullable=False) 
    height = Column(String(250),nullable=False)
    eye_color = Column(String(250), nullable=False)
    

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer,primary_key=True)
    name =  Column(String(250),nullable=False)
  

class User(Base):
    __tablename__= 'user'
    id = Column(Integer,primary_key=True)
    name= Column(String(250),nullable=False)
    email= Column(String(250), nullable=False)
    phone= Column(String(250),nullable=False)
    password = Column(String(250),nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    planets_id = Column(Integer, ForeignKey('planets.id')) 

class Favorites(Base):
    __tablename__='favorites'
    id = Column(Integer,primary_key=True)
    favorites_id = Column(Integer,ForeignKey('user.id'))
 
    
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
