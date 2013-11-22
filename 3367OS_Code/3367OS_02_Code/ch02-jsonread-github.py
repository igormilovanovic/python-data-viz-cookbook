import requests

url = 'https://github.com/timeline.json'

r = requests.get(url)
json_obj = r.json()

repos = set() # we want just unique urls
for entry in json_obj:
    try:
        repos.add(entry['repository']['url'])
    except KeyError as e:
        print "No key %s. Skipping..." % (e)

from pprint import pprint 
pprint(repos)
