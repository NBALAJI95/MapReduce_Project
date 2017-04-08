dups_l = 0
uniq_l = 0
with open('Duplicates.txt') as f:
    lines = f.read().splitlines()
    dups_l = len(lines)
    print('Number of Duplicate words:', dups_l)
with open('Unique.txt') as f:
    lines = f.read().splitlines()
    uniq_l = len(lines)
    print('Number of Unique words:', uniq_l)
print('Ratio of unique words to duplicates:', uniq_l/dups_l)
with open('Main_Requirements_OP.txt', 'w') as f:
	f.write('Number of duplicate words: ' + str(dups_l))
	f.write('\nNumber of unique words:' + str(uniq_l))
	f.write('\nRatio of unique words to duplicates:' + str(uniq_l/dups_l))