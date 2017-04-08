import re
f = open('STEP_OP.json')
wf= open('text_extra.txt', 'a')
while True:
	ind = 0
	original_data = f.readline()
	j=1
	if len(original_data) <= 1:
		continue
	else:
		a = original_data.split(',')
		try:
			aa = a[0]
			n = aa.split()
			n = n[3]
		except IndexError:
			print(a)
			continue
		print(n)
		wf.write(n+'\n')

f.close()
wf.close()