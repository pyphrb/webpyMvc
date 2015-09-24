#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
import web
'''
database config

    Database class

        mysql
        sqlite
        postgre
        oracle
'''

class Database(object):

    def __init__(self, DBN, USER, PWD, DBNAME):
        self.dbn = DBN;
        self.user = USER;
        self.pwd = PWD;
        self.dbname = DBNAME;
        self.dbconnet = None;

    def mysqlConnect(self):
        try:
            self.dbconnet = web.database(dbn=self.dbn, user=self.user, pw=self.pwd, db=self.dbname)
            return self.dbconnet

        except Exception as e:
            print e
