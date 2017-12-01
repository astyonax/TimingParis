#! /bin/env python2.7
# AUTHOR: Guglielmo Saggiorato <astyonax@gmail.com>
# DATE: July-November 2017
# LICENSE: GPLv3

# import overpy
import dill
import pandas as pd
import numpy as np

# load the result of the queries -- data updated: july '17
data = dill.load(open('data.pkl','rb'))
stations=data['stations']
Pbike = data['bike_parks']

# convert to pandas
table_pbike    = [[j.id,float(j.lat),float(j.lon),j.tags] for j in Pbike]
table_stations = [[j.id,float(j.lat),float(j.lon),j.tags] for j in stations]

table_pbike = pd.DataFrame(table_pbike,columns=['id','lat','lon','tags'])
table_stations = pd.DataFrame(table_stations,columns=['id','lat','lon','tags'])

# save again, you never know
table_pbike.to_pickle('data/table_pbike.pkl')
table_stations.to_pickle('data/table_stations.pkl')

# accelerated haversine distance
from numba import jit
@jit('f8(f8,f8,f8,f8)')
def haversine(la1,lo1,la2,lo2):
    """
        haversine function (https://en.wikipedia.org/wiki/Haversine_formula)
        for the distance between two points on a sphere of radius R
        earth radius approximated to 6371 Km, accuracy of 0.5% (wikipedia)
    """
    EARTH_RADIUS = 6371 #Km
    C = np.cos
    S = np.sin
    lo1,la1,lo2,la2 = map(np.radians,(lo1,la1,lo2,la2))
    dlat = la2-la1
    dlon = lo2-lo1
    h2   = (S(dlat/2.)**2.+C(la1)*C(la2)*S(dlon/2.)**2.)**.5
    return 2.*EARTH_RADIUS*np.arcsin(h2)

# -------------------------------------------------------------------
# This looks complex, take it easy:
# I want a function to be applied to each of the previously created
# pandas tables (table_pbike,table_stations) as 
# `df.apply(func,axis=1)`, remember that func will receive the record
# as first and only argument. As in a cartesian product, this 
# function then measures the distance (with haversine) between the 
# record in df wrt each record in the other table and returns the 10
# nearest distances, and row ids. Hence func is a function factory
# which takes the other table as argument, and returns a function
# to be applied by pandas. I hope it's clear enough to read the code
# It's fast enough, that I don't need more clever solutions.
def makedistfunc(ref):
    def distancestation2parkings(row):
        distances = [[haversine(row.lat,row.lon,j.lat,j.lon),map(int,(row.id,j.id))] for j in ref.itertuples()]
        distances = sorted(distances,key=lambda x:x[0])
        top10 = distances[:10]
        return top10
    return distancestation2parkings
# do it
top10stat2bike = table_pbike.apply(makedistfunc(table_stations),axis=1)
top10 = table_stations.apply(makedistfunc(table_pbike),axis=1)
# we save of course
with open('data/top10s.dill','wb') as fout:
    dill.dump({'stat2park':top10stat2bike,'park2stat':top10},fout)
# -------------------------------------------------------------------