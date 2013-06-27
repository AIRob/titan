#!/usr/local/bin/python2.7
#coding:utf-8

import os
from datetime import datetime
from models import db

class Repos(db.Model):
    __tablename__ = 'repos'
    __table_args__ = (db.UniqueConstraint('path', 'oid', name='uix_path_oid'), )
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.CHAR(30), nullable=False)
    oid = db.Column(db.Integer, nullable=False, index=True)
    tid = db.Column(db.Integer, nullable=False, index=True, default=0)
    uid = db.Column(db.Integer, nullable=False, index=True)
    summary = db.Column(db.String(200))
    commiters = db.Column(db.Integer, nullable=False, default=0)
    watchers = db.Column(db.Integer, nullable=False, default=0)
    path = db.Column(db.String(150), nullable=False)
    parent = db.Column(db.Integer, nullable=False, default=0)
    forks = db.Column(db.Integer, nullable=False, default=0)
    create = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, path, oid, uid, tid=0, summary='', parent=0, commiters=0, watchers=0):
        self.name = name
        self.path = path
        self.oid = oid
        self.uid = uid
        self.tid = tid
        self.commiters = commiters
        self.watchers = watchers
        self.summary = summary
        self.parent = parent

    def get_real_path(self):
        return  os.path.join(
                        str(self.oid), \
                        str(self.tid) if self.tid else '', \
                        '%d.git' % self.id,
                    )

    def set_args(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
        db.session.add(self)
        db.session.commit()

class Commiters(db.Model):
    __tablename__ = 'commiters'
    __table_args__ = (db.UniqueConstraint('uid', 'rid', name='uix_uid_rid'), )
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, nullable=False)
    rid = db.Column(db.Integer, nullable=False, index=True)

    def __init__(self, uid, rid):
        self.uid = uid
        self.rid = rid

class Watchers(db.Model):
    __tablename__ = 'Watchers'
    __table_args__ = (db.UniqueConstraint('uid', 'rid', name='uix_uid_rid'), )
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, nullable=False)
    rid = db.Column(db.Integer, nullable=False, index=True)

    def __init__(self, uid, rid):
        self.uid = uid
        self.rid = rid

