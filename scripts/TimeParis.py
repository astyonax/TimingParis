import sys
sys.path.append('../')
import googlemaps
# import citymapper
mykey=open('gmaps.key').read().strip() # not shared on GitHub
myCMkey = open('citymapper.key').read().strip()
#https://developers.google.com/maps/documentation/directions/
# https://github.com/googlemaps/google-maps-services-python
import lib
reload(lib)
# reload(citymapper)


# In[2]:

import functools

class directions(object):

    """
        This class exposes a call method that calls googlemaps.directions
        Additionally, it counts the number of times it's called

        TODO: memoize with dict & singleton
    """
    def __init__(self,key,load_cache=True):
        self.gmaps = googlemaps.Client(key=key)
        self.calls = 0
        self.memo  = {}
        self.miss  = 0
        self.hit   = 0
        self.locked= False
        self.__limit = 2500
        if load_cache:
            try:
                self._load()
            except:
                pass
    def __call__(self,*args,**kwargs):
        key = str(args)+str(kwargs)

        if key not in self.memo :
            if self.calls>(self.__limit-2):
                # the free api has a hard limit to 'limit' query/day
                print 'you reached the maximum nr of calls for today'
                raise StopIteration
            try:
                self.memo[key]=self.gmaps.directions(*args,**kwargs)
            except googlemaps.exceptions.Timeout:
                raise StopIteration
            self.calls +=1
            self.miss   = self.calls
        else:
            self.hit   += 1
        return self.memo[key]

    def _save(self):
        import cPickle
        with open('data/.directions_cache.pkl','wb') as fout:
            cPickle.dump(self.memo,fout)

    def _load(self):
        import cPickle
        with open('data/.directions_cache.pkl','rb') as fout:
            self.memo = cPickle.load(fout)

GMapDirections = directions(mykey,load_cache=True)
# CMtime         =citymapper.citymapper(myCMkey)
len(GMapDirections.memo.keys())


# In[3]:

import numpy as np

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


# In[4]:

import json
import numpy as np
# import seaborn as sns
# sns.set_context('paper')
import pandas as pd
# import matplotlib as mpl
from string import atof
# from ipyleaflet import (
#     Map,
#     Marker,
#     TileLayer, ImageOverlay,
#     Polyline, Polygon, Rectangle, Circle, CircleMarker,
#     GeoJSON,
#     DrawControl
# )


# In[5]:

import pandas as pd
import cPickle as pkl

fdin = 'sample_points/inside.pkl'
with open(fdin,'rb') as fin:
    points_inside = pkl.load(fin)

fdout = 'sample_points//outside.pkl'
with open(fdout,'rb') as fout:
    points_outside = pkl.load(fout)


# In[6]:

print len(points_inside)
print len(points_outside)
# points_inside == points_outside


# In[7]:

from string import atof
import time

def get_travel_times(p1,p2,departure=None,modes=None,filter_distance=False):
    # compute the 'big-circle' distance
    la1,lo1 = p1
    la2,lo2 = p2
    havsine_d= haversine(la1,lo1,la2,lo2)*1000#distance in meters (but low prec)

    if not modes:
         modes = ['transit','bicycling','driving']#,'walking']
#     if modes[0]!='transit':
#         raise NotImplementedError('Habemus a problem with Google server response if 1st request is not for transit')

    results = []
    for idx,mode in enumerate(modes):

        if departure and mode=='transit':
            direction = GMapDirections(p1,p2,region='fr',mode=mode,departure_time=departure)
        else:
            direction = GMapDirections(p1,p2,region='fr',mode=mode)

#               Save these results in separate list and make key to avoid duplicates
#         print ('legs: {0:d}'.format(len(direction[0]['legs'])))
#         print ('directions: {0:d}'.format(len(direction)))
        polyline = direction[0][u'overview_polyline'][u'points']
        legs = direction[0]['legs'][0]
        steps = legs['steps']

        # get infos from google directions results
        distance = atof(legs['distance']['value']) #distance in meters
        try:
            duration = atof(legs['duration_in_traffic']['value']) # distance in second
            print 'duration_in_traffic','no'
        except KeyError:
            duration = atof(legs['duration']['value']) # distance in second

#         # assign the shortest distance between two points
#         # to be the walking distance
#         if mode == 'walking':
#             shortest_path_distance = distance

        report = []

        # be sure these diretion require the requested travel mode
        steps_travel_mode = [step['travel_mode'].lower().strip() for step in steps]
        record = {'mode':mode,'distance':distance,'duration':duration,'p1':p1,'p2':p2,
                  'haversine_distance':havsine_d,'walk_distance':None,'kind':'full',
                  'departure':departure,'polyline':polyline}
        if mode in steps_travel_mode:
            report += [record,]
        else:
            if mode == 'transit':
                break

        # retrieve transit with citymapper
#         if mode == 'transit':
#             cmq = CMtime.transit(p1,p2)
#             cm_time = cmq['travel_time_minutes']*60
#             record  = {'mode':mode,'distance':distance,'duration':cm_time,'p1':p1,'p2':p2,
#                       'haversine_distance':havsine_d,'walk_distance':shortest_path_distance,'kind':'CM','departure':departure}
#             report += [record,]

        for step in steps:
            try:
                _mode      = step[u'travel_mode'].lower().strip()
                _distance  = step[u'distance'][u'value']
                try:
                    _duration = atof(step[u'duration_in_traffic']['value']) # distance in second
                except KeyError:
                    _duration = atof(step[u'duration']['value']) # distance in second
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
#         if mode == 'transit':
#             print report
        if report:
            results.extend( report )

    return results


# In[8]:

p1,p2 = points_inside[6],points_inside[7]
depart = lib.nextdayat(lib.days.wednesday,8,)
print depart
# record = GMapDirections(p1,p2,mode='driving')
# ['transit','bicycling']
record = get_travel_times(p1,p2,modes=['driving',],filter_distance=False,departure = depart)
print GMapDirections.calls
# GMapDirections._save()
# for j in record:
#     print j
# record


# In[ ]:




# In[9]:

from concurrent import futures


# In[10]:

from tqdm import tnrange, tqdm_notebook,tqdm
tqdm_notebook = tqdm
import traceback

def run_many_extend_no_fail(f,x,max_workers=10,tqdm=False,quiet=False,total=None):
    out = []
    jobs = []


    if not total:
        total = len(x)
    max_workers = min(max_workers,total)
    if max_workers>1:
        with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            for ix in x:
                job = executor.submit(f,*ix)
                jobs.append(job)
            asc_jobs = futures.as_completed(jobs)
            if tqdm:
                asc_jobs = tqdm_notebook(asc_jobs,total=total)
            for job in asc_jobs:
                try:
                    records = job.result()
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


# In[11]:

import time
def crashme(a,b,c):
    if a>.9:
        raise IndexError
    if a==.1:
        raise StopIteration
    time.sleep(10)
    return [[a,b,c],]


x=[[1,1,1],[.5,.5,.5],[.2,.2,.2],[.2,.2,.2],[.2,.2,.2],[.1,.1,.1]]*15
# run_many_extend_no_fail(crashme,x,tqdm=True,total=2)


# In[12]:


class NN_pair_from(object):
    def __init__(self,X,Y=False,howmany=False):
        self.X = X
        if Y==False:
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


# In[13]:

from time import gmtime, strftime
from functools import partial

def get_data(X,Y,name,N):
    depart = lib.nextdayat(lib.days.monday,8,)
    now = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
    points = NN_pair_from(X,Y,N)

    fnout = 'data/{:s}_{:s}.pdpkl'.format(name,now)
    latest = 'data/{:s}_latest'.format(name)

    import cPickle
    try:
        with open(latest,'rb') as fin:
            data_out=cPickle.load(fin)
    except IOError:
        data_out = []
    print 'records so far:',len(data_out)


    try:
        func = partial(get_travel_times,departure=depart)
        data_out.extend(run_many_extend_no_fail(func,points,total=len(points),max_workers=10,quiet=True,tqdm=True))
    finally:
        GMapDirections._save()
        import pandas as pd
        import os
        df = pd.DataFrame(data_out)

        df.to_pickle(fnout)
#         latest +='.pdpkl'
#         try:
#             os.remove(latest)
#         except OSError:
#             pass
#         finally:
#             os.symlink(os.path.abspath(fnout),os.path.abspath(latest))

        print u' Done :)'
    return df


# In[ ]:

bigparis = np.r_[points_inside,points_outside]
tests=[{'name':'inside','X':points_inside,'Y':points_inside},
       {'name':'outin' ,'X':points_outside,'Y':points_inside},
       {'name':'bigpar','X':bigparis,'Y':bigparis}]

GMapDirections._save()
GMapDirections = directions(mykey,load_cache=True)
for ix in range(len(tests)):
    df = get_data(N=2500/3/len(tests),**tests[ix])
print 'total calls:',GMapDirections.calls


# In[15]:

print GMapDirections.calls
print len(df)


# In[16]:

df.groupby(('mode','kind')).count()


# In[ ]:
