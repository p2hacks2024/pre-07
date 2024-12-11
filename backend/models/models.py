from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    ideas = relationship('Ideas', back_populates='user')

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.email})"
    
class Ideas(Base):
    __tablename__ = 'ideas'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String)
    user = relationship('User', back_populates='ideas')
    user_id = Column(Integer, ForeignKey('users.id'))
    fork = Column(Integer, ForeignKey('ideas.id'), default=None)
    tags = relationship('Tags', back_populates='idea')
    
    def __repr__(self):
        return f"{self.id}: {self.title} ({self.description})"

class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    tag = Column(String(255))
    idea = relationship('Ideas', back_populates='tags')
    idea_id = Column(Integer, ForeignKey('ideas.id'))
    
    def __repr__(self):
        return f"{self.id}: {self.tag}"
    
class Goods(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) 
    idea_id = Column(Integer, ForeignKey('ideas.id'))