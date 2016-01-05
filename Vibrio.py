import utils
f = open('Vibrio_cholerae.txt',"r")
dna = f.read()
f.close()
pattern = 'CTTGATCAT'
pos = utils.patternMatchPos(pattern,dna)
f = open('Vibrio_pos.txt',"w+")

for item in pos:
    print(item,end = ' ', file = f)
f.close()
