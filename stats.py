from pymongo import MongoClient

connection = MongoClient()
db = connection.imagequick_dev
events = db.events.find()
voices = db.voices.find()

voicelist = []

for voice in voices:
	voicelist.append(voice['name'])

counts = dict.fromkeys(voicelist,0)


for voice in db.voices.find():
	
	for event in db.events.find():
		for e_voice in event['voices']:
			if e_voice == voice['name']:				
				counts[voice['name']] += 1
	
print "---------------------------\nIQ-TALENT-ANALYSIS\n------------------------------"
for key,values in counts.iteritems():
	print key, ' -> ',values