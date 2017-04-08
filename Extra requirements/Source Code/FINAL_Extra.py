import operator
FF = open("Final_Extra_Req_OP.txt",'w')
op = dict()
with open('Extra_OP.txt') as f:
    lines = f.read().splitlines()
    res = len(lines)
    for i in lines:
    	r = i.split('\t')
    	op[r[0]] = int(r[1])
    #print(lines)
FF.write("Top 10 Best times to tweet\n")
sorted_x = sorted(op.items(), key=operator.itemgetter(1), reverse = True)
fin = sorted_x[:10]
for each in fin:
	print(each[0])
	FF.write(each[0] + '\n')