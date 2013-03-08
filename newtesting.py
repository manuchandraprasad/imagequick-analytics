
events = [1,2,3,4]
check_voice = ['a','b','c']
voices = ['a','b','c','d']

voicelist = []

for voice in voices:
	print '--------------'
	for event in events:
		for e_voice in check_voice:
			print e_voice,'-',voice
			if e_voice == voice:				
				print 'yes'
	
	
