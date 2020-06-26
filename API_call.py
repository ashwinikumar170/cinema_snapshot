import urllib2
import json
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

apikey = 'ed70b3a0'
f = open("clean.txt", "r")
for line in f:
	arg=line.strip().replace(' ', '+')
	try:
		apiurl = 'http://www.omdbapi.com/?t=' + arg + '?&apikey=' + apikey
		r = requests.get(apiurl)
		stg = r.text
		json_data = json.loads(stg)
		imdbRating = float(json_data['imdbRating'])
		metaScore = int(json_data['Metascore'])
		print(line.strip()+ ' : ' + bcolors.OKGREEN + json_data['imdbRating'] + bcolors.ENDC + " : "+ bcolors.HEADER + json_data['Metascore'] + bcolors.ENDC)
	except KeyError:
		print(line.strip()+ ' : ' + 'Not Found')
	except ValueError:
		print(line.strip() + ' : ' + "ValueError")
f.close()


