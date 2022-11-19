import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
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

class Media(Base):
    __tablename__ = 'media'
    id = Column(Enum, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    type_media = Column(String(30), ForeignKey('post.id'))
    
    
    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(String(250), primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    

    
    def to_dict(self):
        return {}

class Like(Base):
    __tablename__ = 'like'
    id = Column(String(250), primary_key=True)
    media_id = Column(Enum, ForeignKey('media.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    

    
    def to_dict(self):
        return {}

class Report(Base):
    __tablename__ = 'report'
    id = Column(String(250), primary_key=True)
    reported_text = Column(String(250), ForeignKey('comment.comment_text'))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    

    
    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    media_id = Column(Enum, ForeignKey('media.id'))
    


    def to_dict(self):
        return {}


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(String(250), primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram_instagram.png')
