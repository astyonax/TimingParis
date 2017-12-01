#! /bin/env python2.7
# AUTHOR: Guglielmo Saggiorato <astyonax@gmail.com>
# DATE: July-November 2017
# LICENSE: GPLv3

import overpy
import dill

api = overpy.Overpass()

#query OSM for all subway entrances in Paris
stations = api.query("""area[name="Paris"];
node
  [railway=subway_entrance]
  (area);
out body;""")

#query OSM for all bike parks in Paris
bike_parks = api.query("""area[name="Paris"];
node
  [amenity=bicycle_parking]
  (area);
out body;""")

# save with dill
with open('data/data.pkl','wb') as fout:
    dill.dump({'stations':stations.nodes,'bike_parks':bike_parks.nodes},fout)
