# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:04:15 2019

@author: Renato
"""
import psycopg2
import logging

class postgresConnection:
    connection = ''
    logging.basicConfig(filename = 'postgresConnection.log', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
    
    def connect(self):
        try:
            postgresConnection.connection = psycopg2.connect("dbname="+self.dbname+" user="+self.user+" password="+self.password+" host="+self.host+" port="+self.port)
            print('Connection Established.')
            logging.info(f'Connection Established.')
        except Exception:
            logging.exception("Exception ocurred", exc_info=True)
