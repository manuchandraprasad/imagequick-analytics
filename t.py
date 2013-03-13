from sc import *
data = []
for voice in voices:
	v_chart = []
	for format in formats:
		play = 0.0
		buy = 0.0
		for event in db.events.find({'format':format,'voices':voice}):
			if event['event'] == 'play':
				play += 1
			elif event['event'] == 'purchase':
				buy +=1
		v_chart.append(play)
		v_chart.append(buy)
	data.append(v_chart)


