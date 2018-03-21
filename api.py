# APi Key
key = 'AIzaSyDqkKco0uBl6vfxrb0vDkAvgP7N5CzjrsM' 

url = 'https://maps.googleapis.com/maps/api/distancematrix/json' 

# open pool for making requests
http = urllib3.PoolManager()

# set the dest as the current warehouse
params = {        
	'origins': sources,
	'destinations': f'{api_sink}',
	'key': key,
	'units': units}

# send a request to maps api
r = http.request('GET', url, params)

# convert to json
data = json.loads(r.data.decode('utf-8'))
