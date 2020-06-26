import os, re, time, datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

formats = ['.mkv','.avi', '.mp4']
res = ['480p', '480P', '720p', '720P', '1080p', '1080P']
separators = ['.', ';', '-', '_', '+']

#square brackets and its contents
criteria_1 = "\[[ a-zA-Z0-9]*\]"

#normal brackets and its contents
criteria_2 = "\([ a-zA-Z0-9]*\)"

#curly brackets and its contents
criteria_3 = "\{[ a-zA-Z0-9]*\}"

#year
criteria_4 = "[0-9]{4}"
p = re.compile(criteria_4)


def format(base_string):
	for var in formats:
		if (re.search(var, base_string, re.IGNORECASE)):
			return base_string.replace(var, '')
	return base_string

def resolution(base_string):
	for var in res:
		if (re.search(var, base_string, re.IGNORECASE)):
			return base_string.replace(var, '')
	return base_string

def separator(base_string):
	for var in separators:
			base_string = base_string.replace(var, ' ')
	return base_string

def regex(base_string):
	output = re.sub(criteria_1, '', base_string)
	output = re.sub(criteria_2, '', output)
	output = re.sub(' +', ' ',output)
	position = []
	if len(re.findall(criteria_4, output)) > 0:
		for m in p.finditer(output):
				num = output[m.start():m.end()]
				if (output.find(num)>0):
					if (int(num)<datetime.datetime.now().year):
						position.append(output.find(num))					
	blacklist = open("blacklist.txt", "r")
	for line in blacklist:
			if (re.search(line.strip(), output, re.IGNORECASE)):
				position.append(output.lower().find(line.lower().strip()))
	blacklist.close()
	if len(position) > 0:
		output = output[0:min(position)]
	return output

def modify(base_string):
	output = regex(separator(resolution(format(base_string))))
	return output

files=os.listdir('.')
f = open("files.txt", "r")
clean = open("clean.txt","w")
for line in f:
			refinedtxt = modify(line.strip())
#			print(line.strip() + ' => ' + bcolors.FAIL + refinedtxt + bcolors.ENDC)
			clean.write(refinedtxt.strip() + '\n')
f.close()