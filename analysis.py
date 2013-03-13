from pymongo import MongoClient

connection = MongoClient()
db = connection.imagequick_dev

def zerotoone(l):
	keyl = []
	valuel = []
	for key,value in l.iteritems():
		keyl.append(key)
		if value==0:
			valuel.append(1)
		if value==0.0:
			valuel.append(1)
		else:
			valuel.append(value)
	return dict(zip(keyl,valuel))

def get_voice_list():
	voicelist = []
	for voice in db.voices.find():
		voicelist.append(voice['name'])
	return voicelist

def get_template_list():
	templatelist = []
	for template in db.templates.find():
		templatelist.append(template['name'])
	return templatelist

def get_producer_list():
	producer_list = []
	for template in db.templates.find():
		producer_list.append(template['producer'])
	return list(set(producer_list))

def get_format_list():
	formatlist = []
	for format in db.formats.find():
		formatlist.append(format['name'])
	return formatlist

def analyse_templates():
	template_play = dict.fromkeys(get_template_list(),0)
	template_buy = dict.fromkeys(get_template_list(),0)
	for template in db.templates.find():
		play = 0
		buy = 0
		for event in db.events.find({'template':template['name']}):
			if event['event'] == 'play':
				play += 1
			elif event['event'] == 'purchase':
				buy += 1
			else:
				pass
		template_play[template['name']] = play
		template_buy[template['name']] = buy
	return template_play,template_buy

def analyse_voices():
	voice_play = dict.fromkeys(get_voice_list(),0)
	voice_buy = dict.fromkeys(get_voice_list(),0)
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
	return voice_play,voice_buy

def analyse_formats():
	format_play = dict.fromkeys(get_format_list(),0)
	format_buy = dict.fromkeys(get_format_list(),0)
	for format in db.formats.find():
		for event in db.events.find():
			if format['name'] == event['format']:
				if event['event']=='play':
					format_play[format['name']] +=1
				elif event['event']=='purchase':
					format_buy[format['name']] +=1
				else:
					pass
	return format_play,format_buy

def get_ratio(l1,l2):
	l1 = zerotoone(l1)
	print l1,l2
	ratio = {k: float(l2[k])/float(l1[k]) for k in l2}	
	return ratio

def stripzeros(p,b):
	for key,value in p.items():
		if value == 0:
			del p[key]
			del b[key]

def pretty_print(analyse_function):
	f_play,f_buy = analyse_function()
	print f_play,f_buy
	#p,b = stripzeros(f_play, f_buy)
	items = get_ratio(f_play,f_buy)
	return items

def analyse_voice(voice):
	play = 0
	buy = 0
	for event in db.events.find({'voices':voice}):
		for e_voice in event['voices']:
			if e_voice == voice:
				if event['event'] == 'play':
					play +=1
				elif event['event'] == 'purchase':
					buy +=1
				else:
					pass

	return play,buy

def analyse_template(template):
	play = 0
	buy = 0
	for event in db.events.find({'template':template}):
		if event['event'] == 'play':
			play +=1
		elif event['event'] == 'purchase':
			buy +=1
		else:
			pass

	return play,buy


