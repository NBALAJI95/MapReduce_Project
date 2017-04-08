f = open('fetched_tweets_output1.json')
ff = open('STEP_OP.json','a')
while True:
	a = f.readline()
	print(a)
	if a == '\n' or len(a)<60:
		continue
	else:
		ff.write(a.lower())
f.close()
ff.close()