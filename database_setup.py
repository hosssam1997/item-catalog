import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine



Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="category")

    @property
    def serialize(self): 
        """Return object data in easily serializeable format"""
        return {

            'name': self.name,
            'id': self.id
        }

class CategoryItem(Base):
    __tablename__ = 'category_item'

    name = Column(String(80), nullable = False)
    description = Column(String(250))
    id = Column(Integer, primary_key = True)
    date = Column(DateTime, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, backref=backref('CategoryItem', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="CategoryItem")
    

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name'          : self.name,
            'id'            : self.id,
            'description'   : self.description,
            'picture'       : self.picture,
            'category'      : self.category.name
        }

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)
