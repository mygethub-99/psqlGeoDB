# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:45:05 2018

@author: ow4253
"""
import psycopg2
import osgeo.ogr

connection = psycopg2.connect(database="geoowen1",user="postgres", password="amanda12")
cursor = connection.cursor()
cursor.execute("DELETE FROM sitegeo")
cursor.execute("DELETE FROM sitefreq")
cursor.execute("DELETE FROM sitelocation")
cursor.execute("DELETE FROM speclandscape")

shapefile = osgeo.ogr.Open('nsbbuf.shp')
layer = shapefile.GetLayer(0)
shapefile2 = osgeo.ogr.Open("C:\\Users\ow4253\Documents\FMEData\Darren\SpectrumLandscape_GS11302012\spectrumcleanup\SpeclandAllBan.shp")
layer2 = shapefile2.GetLayer(0)
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    state = feature.GetField("State")
    fa = feature.GetField("FA_Locatio")
    countystate = feature.GetField("County_Sta")
    fips = feature.GetField("FIPS")
    f700 = feature.GetField("_700")
    f1900= feature.GetField("_1900")
    AWS = feature.GetField("AWS")
    f850 = feature.GetField("_850")
    geometry = feature.GetGeometryRef()
    wkt = geometry.ExportToWkt()
    
    cursor.execute("INSERT INTO SiteLocation(FA, STATE, COUNTYSTATE, FIPS, outline)\
                   VALUES (%s, %s, %s, %s, ST_GeogFromText(%s))", (fa, state, countystate, fips, wkt))
    cursor.execute("INSERT INTO SiteGeo (FA, outline) VALUES (%s, ST_GeogFromText(%s))", (fa, wkt))
    cursor.execute("INSERT INTO SiteFreq (FA, f700, F1900, FAWS, F850, fips, outline)\
                   VALUES (%s, %s, %s, %s, %s, %s, ST_GeogFromText(%s))", (fa, f700, f1900, AWS, f850, fips, wkt))
connection.commit()  
  
for i in range(layer2.GetFeatureCount()):
    feature = layer2.GetFeature(i)
    fips = feature.GetField("FIPS")
    f1900 = feature.GetField("_1900")
    f850 = feature.GetField("_850")
    f700 = feature.GetField("_700")
    aws = feature.GetField("aws")
    geometry = feature.GetGeometryRef()
    wkt = geometry.ExportToWkt()
    cursor.execute("INSERT INTO speclandscape (fips, f1900, f850, f700, faws, \
                                               outline) VALUES (%s, %s, %s, %s,\
                                               %s, ST_GeogFromText(%s))", \
                                               (fips, f1900, f850, f700, aws, wkt))


connection.commit()
connection.close()
