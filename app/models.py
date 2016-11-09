# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:47:42 2016

@author: dfoley
"""

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key  =True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index =True, unique = True)
    
    # tells python how to print objects of this class
    def __repr__(self):
        return '<User %r>' % (self.nickname)