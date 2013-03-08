from pymongo import MongoClient

connection = MongoClient()
db = connection.imagequick_dev
events = db.events.find()
voices = db.voices.find()

voicelist = []

for voice in voices:
	voicelist.append(voice['name'])

voice_play = dict.fromkeys(voicelist,0)
voice_buy = dict.fromkeys(voicelist,0)

templatelist = []
for template in db.templates.find():
	templatelist.append(template['name'])

template_play = dict.fromkeys(templatelist,0)
template_buy = dict.fromkeys(templatelist,0)

def zerotoone(l):
	keyl = []
	valuel = []
	for key,value in l.iteritems():
		keyl.append(key)
		if value==0:
			valuel.append(1)
		else:
			valuel.append(value)
	return dict(zip(keyl,valuel))

for template in db.templates.find():
	for event in db.events.find():
		if event['template']==template['name']:
			if event['event'] == 'play':
				template_play[template['name']] += 1
			elif event['event'] == 'purchase':
				template_buy[template['name']] += 1
			else:
				pass

for voice in db.voices.find():
	
	for event in db.events.find():
		for e_voice in event['voices']:
			if e_voice == voice['name']:
				if(event['event']=='play'):			
					voice_play[voice['name']] += 1
				elif(event['event']=='purchase'):
					voice_buy[voice['name']] += 1
				else:
					pass
formatlist = []
for format in db.formats.find():
	formatlist.append(format['name'])

format_play = dict.fromkeys(formatlist,0)
format_buy = dict.fromkeys(formatlist,0)
for format in db.formats.find():
	for event in db.events.find():
		if format['name'] == event['format']:
			if event['event']=='play':
				format_play[format['name']] +=1
			elif event['event']=='purchase':
				format_buy[format['name']] +=1
			else:
				pass

voice_play = zerotoone(voice_play)
ratio = {k: float(voice_buy[k])/voice_play[k] for k in voice_buy}	

template_play = zerotoone(template_play)
template_ratio = {k: float(template_buy[k])/template_play[k] for k in template_buy}	

format_play = zerotoone(format_play)
format_ratio = {k: float(format_buy[k])/format_play[k] for k in format_buy}	



