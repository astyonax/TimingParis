#!/bin/env python2.7

# Author: G. Saggiorato
# Date: 1.2.2017
# This scripts takes directions with google maps api
# given a set of random departures and destinations
# TODO: finish writing this

import sys
sys.path.append('../')
import googlemaps
mykey=open('../gmaps.key').read().strip()
#https://developers.google.com/maps/documentation/directions/
# https://github.com/googlemaps/google-maps-services-python
import lib # my libraries
import json
import numpy as np
import pandas as pd
from string import atof
import pandas as pd
import cPickle as pkl
import numpy as np
from string import atof
import time
from concurrent import futures
from functools import partial
import os
from tqdm import tnrange, tqdm_notebook,tqdm
import traceback
import functools

class directions(object):

    """
        This class exposes a call method that calls googlemaps.directions
        Additionally, it counts the number of times it's called
        and caches the requests, to avoid useless calls to the API
    """
    def __init__(self,key,load_cache=False):
        self.gmaps = googlemaps.Client(key=key)
        self.calls = 0
        self.memo  = {}
        self.miss  = 0
        self.hit   = 0
        self.locked= False
        # Maximum number of calls to Google Maps API
        # for a free account
        self.__limit = 2500

        if load_cache:
            try:
                self._load()
            except:
                pass

    def __call__(self,*args,**kwargs):
        key = str(args)+str(kwargs)

        # poor-man memoizing
        if key not in self.memo:
            if self.calls>(self.__limit):
                # the free api has a hard limit of 2500 queries/day
                print 'you reached the maximum nr of calls for today'
                # returns a good kind of errors
                # because I expect to be calling this in a loop-like context
                raise StopIteration

            try:
                self.memo[key] = self.gmaps.directions(*args,**kwargs)
            except googlemaps.exceptions.Timeout:
                raise StopIteration

            self.calls +=1
            self.miss = self.calls
        else:
            self.hit += 1
        return self.memo[key]

    def _save(self):
        with open('../data/.directions_cache.pkl','wb') as fout:
            pkl.dump(self.memo,fout)

    def _load(self):
        with open('../data/.directions_cache.pkl','rb') as fout:
            self.memo = pkl.load(fout)


# Do not load the cache


def haversine(la1,lo1,la2,lo2):
    """
        haversine function (https://en.wikipedia.org/wiki/Haversine_formula)
        for the distance between two points on a sphere of radius R
        earth radius approximated to 6371 Km, accuracy of 0.5% (wikipedia)

        IN: la1, lo1 : latitude and longitude of 1st point  -> float
            la2, lo2 : same for 2nd point                   -> float

        OUT: distance in km -> float
    """
    EARTH_RADIUS = 6371 #Km
    C = np.cos
    S = np.sin
    lo1,la1,lo2,la2 = map(np.radians,(lo1,la1,lo2,la2))
    dlat = la2-la1
    dlon = lo2-lo1
    h2   = (S(dlat/2.)**2.+C(la1)*C(la2)*S(dlon/2.)**2.)**.5
    # returns in km
    return 2.*EARTH_RADIUS*np.arcsin(h2)

# Random points are precomputed (in the SampleParis.ipynb)
fdin = '../sample_points/inside.pkl'
with open(fdin,'rb') as fin:
    points_inside = pkl.load(fin)

fdout = '../sample_points//outside.pkl'
with open(fdout,'rb') as fout:
    points_outside = pkl.load(fout)

GMapDirections = directions(mykey,load_cache=False)
def get_travel_times(p1,p2,departure=None,modes=None,filter_distance=False):
    """
        Compute the travel time between points `p1=[latitude, longitude]` and `p2`
        departing at time `departure` with `modes = [list of google maps api compatible modes]`.

        Modes can contain: ['transit','bicycling','driving','walking']

        Returns a list of dictionaries. Each dictionary corresponds to the full
        path or legs (that is subpaths.)

        For full paths the dict is:
        `{'mode':mode,'distance':distance,'duration':duration,'p1':p1,'p2':p2,
                  'haversine_distance':havsine_d,'walk_distance':None,'kind':'full',
                  'departure':departure,'polyline':polyline}`

        For legs the dict is:
        `{'mode':_mode,'distance':_distance,'duration':_duration,'p1':_p1,'p2':_p2,
                     'haversine_distance':_havsine_d,'walk_distance':None,'kind':_kind,
                     'departure':departure,'polyline':None}`
    """
    # compute the 'big-circle' distance
    la1,lo1 = p1
    la2,lo2 = p2
    havsine_d= haversine(la1,lo1,la2,lo2)*1000 #distance in meters (but low prec)

    if not modes:
         modes = ['transit','bicycling','driving']

    results = []
    for idx,mode in enumerate(modes):

        if departure and mode=='transit':
            direction = GMapDirections(p1,p2,region='fr',mode=mode,departure_time=departure)
        else:
            direction = GMapDirections(p1,p2,region='fr',mode=mode)

        polyline = direction[0][u'overview_polyline'][u'points']
        legs = direction[0]['legs'][0]
        steps = legs['steps']

        # get infos from google directions results
        distance = atof(legs['distance']['value']) #distance in meters
        try:
            duration = atof(legs['duration_in_traffic']['value']) # duration in second
            print 'duration_in_traffic','no'
        except KeyError:
            duration = atof(legs['duration']['value']) # duration in second


        report = []
        record = {'mode':mode,'distance':distance,'duration':duration,'p1':p1,'p2':p2,
                  'haversine_distance':havsine_d,'walk_distance':None,'kind':'full',
                  'departure':departure,'polyline':polyline}

        # make sure these direction require the requested travel mode
        # 1. list all travel modes in steps 2. append record if travel mode appears in at least one step step
        steps_travel_mode = [step['travel_mode'].lower().strip() for step in steps]
        if mode in steps_travel_mode:
            report += [record,]
        else:
            # TODO: why this?
            if mode == 'transit':
                break

        # now parse each steps and fill the dictionary
        for step in steps:
            try:
                _mode      = step[u'travel_mode'].lower().strip()
                _distance  = step[u'distance'][u'value']
                try:
                    _duration = atof(step[u'duration_in_traffic']['value']) # duration in second
                except KeyError:
                    _duration = atof(step[u'duration']['value']) # duration in second
                _kind      = 'step'
                _la1,_lo1  = step[u'start_location'][u'lat'],step[u'start_location'][u'lng']
                _p1        = np.asarray([_la1,_lo1])
                _la2,_lo2  = step[u'end_location'][u'lat'],step[u'end_location'][u'lng']
                _p2        = np.asarray([_la2,_lo2])
                _havsine_d = haversine(_la1,_lo1,_la2,_lo2)*1000.

                report  += [{'mode':_mode,'distance':_distance,'duration':_duration,'p1':_p1,'p2':_p2,
                             'haversine_distance':_havsine_d,'walk_distance':None,'kind':_kind,
                             'departure':departure,'polyline':None},]
            except:
                pass

        if report:
            results.extend( report )

    return results

# compute datetime object of next wednesday at 8am
# depart = lib.nextdayat(lib.days.wednesday,8,)

def run_many_extend_no_fail(f,x,max_workers=10,tqdm=False,quiet=False,total=None):
    """

        Execute function f on x  as map(f,x), asynchronously with futures.ThreadPoolExecutor.
        As the name says, this function runs f(x) for each x, does not stops even on
        failure for some x.

        f is expected to return a list to extend the results list

        Note: If total is not given, lenght of x is computed as len(x)
        If max_workers == 1, truly serial execution is done (and job scheduled)
        The flag tqdm determines wetether using tqdm to show progress. Works only in multi-threading

    """
    out = []
    jobs = []

    # compute the number of items
    if not total:
        total = len(x)

    # optimize number of workers to the minimum necessary/requested
    max_workers = min(max_workers,total)

    if max_workers>1:
        # we have chose the parallel branch
        with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # a good description is in the book
            # ??? don't remember the name now :/ but it's pink and thick
            print 'appending jobs'
            for ix in x:
                job = executor.submit(f,*ix)
                jobs.append(job)

            # an iterator serving completed jobs
            asc_jobs = futures.as_completed(jobs)

            #just wrapping with a progress bar
            if tqdm:
                asc_jobs = tqdm_notebook(asc_jobs,total=total)

            print 'executing jobs'
            # actually they already started, so we iterate on the completed jobs
            for job in asc_jobs:
                try:
                    records = job.result()
                    # StopIteration is (in this context) used to indicate that
                    # we can't call anymore GMaps API
                except StopIteration as msg:
                    print msg
                    # cancel all other jobs, then break
                    print 'StopIteration raised. cancelling..', job
                    for j in jobs:
                        # we don't care if we can cancel, won't affect the loop
                        if not j.done(): j.cancel()
                    break
                except Exception:
                    if not quiet:
                        print traceback.format_exc()
#                         raise
                else:
                    out.extend(records)
    else:
        for i in tqdm_notebook(x):
            try:
                records = f(*i)
            except StopIteration as msg:
                print msg
                break
            except Exception:
                if not quiet:
                    print traceback.format_exc()
            else:
                out.extend(records)

    return out


#
# import time
# def crashme(a,b,c):
#     if a>.9:
#         raise IndexError
#     if a==.1:
#         raise StopIteration
#     time.sleep(10)
#     return [[a,b,c],]
#
# x=[[1,1,1],[.5,.5,.5],[.2,.2,.2],[.2,.2,.2],[.2,.2,.2],[.1,.1,.1]]*15
# run_many_extend_no_fail(crashme,x,tqdm=True,total=2)

class NN_pair_from(object):
    def __init__(self,X,Y=False,howmany=False):
        self.X = X
        try:
            len(Y)
        except AttributeError:
            self.Y=X
        else:
            self.Y=Y

        self.N = X.shape[0]
        self.count = 0
        self.howmany=howmany

    def next(self):
        while True and (not self.howmany or self.howmany>self.count):
            i,j = np.random.choice(self.N, 2, replace=False)
            self.count+=1
            yield self.X[i],self.Y[j]

    def __iter__(self):
        return self.next()
    def __len__(self):
        return self.howmany

from time import strftime,gmtime

def get_data(X,Y,name,N):
    """

        get the travel times using the previous machinery
        saves the records on a daily files to
        avoid accidental corruption of the entire dataset

    """
    print 'running:', name
    depart = lib.nextdayat(lib.days.monday,8,)
    now = strftime("%Y-%m-%d-%H-%M-%S", gmtime())

    points = NN_pair_from(X,Y,N)

    fnout = 'data/{:s}_{:s}.pdpkl'.format(name,now)
    latest = 'data/{:s}_latest'.format(name)

    try:
        with open(latest,'rb') as fin:
            data_out=pkl.load(fin)
    except IOError:
        data_out = []
    print 'records so far:',len(data_out)


    try:
        func = partial(get_travel_times,departure=depart)
        data_out.extend(run_many_extend_no_fail(func,points,total=len(points),max_workers=2,quiet=True,tqdm=True))
    finally:
        GMapDirections._save()
        df = pd.DataFrame(data_out)
        df.to_pickle(fnout)
        print u' Done :)'
    return df

#-------------------------------------------------------------------------------
# DO THE JOB here

# define the sampling point of origin and destination of the trips
# and so the tests that we wnt to do

bigparis = np.r_[points_inside,points_outside]
tests=[{'name':'inside','X':points_inside,'Y':points_inside},
       {'name':'outin' ,'X':points_outside,'Y':points_inside},
       {'name':'bigpar','X':bigparis,'Y':bigparis}]

# do the tests
# and save the results
for ix in range(len(tests)):
    df = get_data(N=2500/3/len(tests),**tests[ix])
