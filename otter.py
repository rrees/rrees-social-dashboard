from google.appengine.api import urlfetch
from google.appengine.api import memcache
from urllib import quote, urlencode

import logging
import json

def most_shared(site):
	url = "http://otter.topsy.com/search.json?q=site:%s&apikey=7DBBA309BA054A498F741E3C781A7D1F&window=d&perpage=100" % site

	sharing_data = memcache.get(site)

	if sharing_data: return json.loads(sharing_data)

	result = urlfetch.fetch(url, deadline = 30)

	if result.status_code == 200:
		data = json.loads(result.content)
		sharing_data = data.get("response", {}).get("list", [])
		memcache.set(json.dumps(sharing_data), 30)
		return sharing_data

	return None