from analysis import *
from pandas import Series, DataFrame
import pandas as pd

index = get_template_list()
index = list(set(index))

t_play = []
t_buy = []
for template in index:
	buy = 0
	play = 0
	for event in db.events.find({'template':template}):
		if event['event'] == 'play':
			play +=1
		elif event['event'] == 'purchase':
			buy +=1
	t_play.append(play)
	t_buy.append(buy)
