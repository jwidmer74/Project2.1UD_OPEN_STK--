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
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Animal(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    species = Column(String(250))
    species = Column(String(500))
    diet = Column(String(250))
    zoo_id = Column(Integer, ForeignKey('zoo.id'))
    zoo = relationship(Zoo)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'species': self.species,
            'id': self.id,
            'species': self.species,
            'diet': self.diet,
        }


engine = create_engine('sqlite:///Zoomenu.db')


Base.metadata.create_all(engine)
