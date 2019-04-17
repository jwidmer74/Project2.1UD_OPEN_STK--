import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Zoo(Base):
    __tablename__ = 'zoo'

    id = Column(Integer, primary_key=True)
    zoo_name = Column(String(250), nullable=False)
    contact = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'zoo_name': self.zoo_name,
            'id': self.id,
            'contact': self.contact,
        }


class RescueAnimals(Base):
    __tablename__ = 'animal'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    species = Column(String(20))
    diet = Column(String(250))
    zoo_id = Column(Integer, ForeignKey('zoo.id'))
    zoo = relationship(Zoo)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'species': self.species,
            'diet': self.diet,
        }


engine = create_engine('sqlite:///jwrescueanimals.db')


Base.metadata.create_all(engine)
