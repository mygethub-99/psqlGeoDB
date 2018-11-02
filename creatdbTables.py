# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:50:38 2018

@author: ow4253
"""
import psycopg2

connection = psycopg2.connect(database="geoowen1",user="postgres", password="amanda12")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS SiteLocation")
cursor.execute("DROP TABLE IF EXISTS SiteGeo")
cursor.execute("DROP TABLE IF EXISTS SiteFreq")
cursor.execute("DROP TABLE IF EXISTS speclandscape")
connection.commit()       
cursor.execute("CREATE TABLE SiteLocation (id SERIAL PRIMARY KEY, FA INTEGER,\
                                           STATE CHAR(2) , COUNTYSTATE VARCHAR,\
                                           FIPS INTEGER, outline GEOGRAPHY)")
cursor.execute("CREATE TABLE SiteGeo (FA INTEGER PRIMARY KEY, outline GEOGRAPHY )")
cursor.execute("CREATE TABLE SiteFreq (ID SERIAL PRIMARY KEY, FA INTEGER, f700 \
                                       VARCHAR, F1900 VARCHAR, FAWS VARCHAR, \
                                       f850 VARCHAR, outline GEOGRAPHY)")

cursor.execute("CREATE TABLE speclandscape (id serial primary key, fips integer,\
                                            f1900 varchar, f850 varchar, \
                                            f700 varchar, faws varchar, \
                                            outline GEOGRAPHY)")
connection.commit()
connection.close()
