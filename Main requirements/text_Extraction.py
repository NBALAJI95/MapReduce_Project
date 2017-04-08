import re
f = open('STEP_OP.json')
wf= open('text_ip.txt', 'w')
while True:
	ind = 0
	original_data = f.readline()
	j=1
	if len(original_data) <= 1:
		continue
	else:
		a = original_data.split(',')
		try:
			aa = a[3]
		except IndexError:
			print(a)
		n = aa.index(':')
		print('\n'+aa[n+2:-2])
		
		wf.write(aa[n+2:-2]+'\n')

f.close()
wf.close()