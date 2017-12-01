# IPython log file

import dill
get_ipython().system(u'l')
get_ipython().system(u'ls')
import pandas
get_ipython().magic(u'logstart')
table_pbike = pandas.read_pickle('table_pbike.pkl')
table_stations = pandas.read_pickle('table_stations.pkl')
data = dill.load(open('top10s.dill','rb'))
data.keys()
stat2park = data['stat2park']
park2stat = data['park2stat']
stat2park[0]
table_stations[table_stations.id==286845307]
table_stations[table_stations.id==286845307.0]
park2stat
park2stat[0]
table_stations[table_stations.id==250656805.0]
def getstat(idx):
    return table_stations[table_stations.id==idx]
def getpark(idx):
    return table_pbike[table_pbike.id==idx]
for row_stat in park2stat[:3]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        plt.scatter(stat.lat,stat.lon,s=10,c='b')
        plt.plot([stat.lat,park.lat],[stat.lat,park.lat],'r-o')
        
for row_stat in park2stat[:3]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        plt.scatter(stat.lat,stat.lon,s=10,c='b')
        plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        plt.scatter(stat.lat,stat.lon,s=10,c='b')
        plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        plt.scatter(stat.lat,stat.lon,s=10,c='b')
        plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        plt.scatter(stat.lat,stat.lon,s=10,c='b')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        print stat
        plt.scatter(stat.lat,stat.lon,s=10,c='b')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.long,s=20,c='r')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=20,c='r')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=50*d,c='r')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=50/d,c='r')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        print park
        print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=10/d,c='r')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=10/d,c='r')
        x = [stat.lat,park.lat]
        y = [stat.lon,park.long]
        plt.plot(x,y,'k')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=10/d,c='r')
        x = [stat.lat,park.lat]
        y = [stat.lon,park.lon]
        plt.plot(x,y,'k')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        plt.plot(x,y,'k')
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:1]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        plt.scatter(stat.lat,stat.lon,s=30,c='b')
        plt.scatter(park.lat,park.lon,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
from mpl_toolkits.basemap import Basemap
map = Basemap(projection='ortho',resolution='l')
map = Basemap(projection='ortho',resolution='l',lat_0=48.864716, lon_0=2.349014)
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        map.scatter(stat.lat,stat.lon,s=30,c='b')
        map.scatter(park.lat,park.lon,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        map.scatter(stat.lat*R,stat.lon*R,s=30,c='b')
        map.scatter(park.lat*R,park.lon*R,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        map.scatter(stat.lon*R,stat.lat*R,s=30,c='b')
        map.scatter(park.lon*R,park.lat*R,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon*R,stat.lat*R,s=30,c='b')
        map.scatter(park.lon*R,park.lat*R,s=10/d,c='r')
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        #R=1
        map.scatter(stat.lon*R,stat.lat*R,s=30,c='b',latlon=1)
        map.scatter(park.lon*R,park.lat*R,s=10/d,c='r',latlon=1)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon*R,stat.lat*R,s=30,c='b',latlon=1)
        map.scatter(park.lon*R,park.lat*R,s=10/d,c='r',latlon=1)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:10]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10/d,c='r',latlon=1)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat[:100]:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10/d,c='r',latlon=1)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=-1)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=1)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=1)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=2)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:1]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=1)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=2)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        #plt.plot(x,y,'k',zorder=-1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:1]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=2)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=3)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        plt.plot(x,y,'k',zorder=1)
        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:1]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=2)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=3)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        map.plot(x,y,'k',zorder=1)
        

        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:1]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=2)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=3)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        map.plot(x,y,'k',zorder=1)
        

        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:1]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=2)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=3)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        map.plot(x,y,'k',zorder=1,latlon=1)
        

        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    for pbike in row_stat[:1]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=2)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c='r',latlon=1,lw=0,zorder=3)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        map.plot(y,x,'k',zorder=1,latlon=1)
        

        #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
for row_stat in park2stat:
    c=(i for i in 'rgk')
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=2)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c=c.next(),latlon=1,lw=0,zorder=3)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        map.plot(y,x,'k',zorder=1,latlon=1)
               #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
        
for row_stat in park2stat:
    c=(i for i in 'rgk')
    for pbike in row_stat[:3]:
        d,(idstat,idpark)=pbike
        stat=getstat(idstat)
        park=getpark(idpark)
        #print park
        #print stat
        R=180./np.pi
        R=1
        cr=c.next()
        map.scatter(stat.lon.values*R,stat.lat.values*R,s=30,c='b',latlon=1,lw=0,zorder=2)
        map.scatter(park.lon.values*R,park.lat.values*R,s=10,c=cr,latlon=1,lw=0,zorder=3)
        x = [stat.lat.values,park.lat.values]
        y = [stat.lon.values,park.lon.values]
        map.plot(y,x,cr,zorder=1,latlon=1)
               #plt.plot([stat.lat,park.lat],[stat.lon,park.lon],'r-o')
        
        
