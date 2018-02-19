import csv

def match (lis,name):
	for t in range (len(lis)):
		alen1=len(name[0])
		blen1=len(lis[t][0])
		alen2=len(name[1])
		blen2=len(lis[t][1])
		if alen1>blen1:
			longer1=name[0]
			shorter1=lis[t][0]
		else:
			shorter1=name[0]
			longer1=lis[t][0]
		if alen2>blen2:
			longer2=name[1]
			shorter2=lis[t][1]
		else:
			shorter2=name[1]
			longer2=lis[t][1]

		llis1=longer1.split(" ")
		slis1=shorter1.split(" ")
		llis2=longer2.split(" ")
		slis2=shorter2.split(" ")
		k=0
		z=0
		for i in range(len(llis1)):
			if llis1[i]==slis1[k] or llis1[i][0]==slis1[k]:
				k+=1
			if k==len(slis1):
				for j in range(len(llis2)):
					if llis2[j]==slis2[z] or llis2[j][0]==slis2[z]:
						z+=1
					if z==len(slis2):
						break
				break
		if (k==len(slis1) and z==len(slis2)):
			return 0
	return 1
	#if matches to anyone return 0 else 1



words=[]
with open('Deduplication Problem - Sample Dataset.csv','rU') as f:
	reader = csv.reader(f)
	words=list(reader)
	words=words[1:]
mdict={}
fdict={}
for i in range(len(words)):
	if words[i][2]=='M':
		if words[i][1] in mdict:
			if match(mdict[words[i][1]],[words[i][3],words[i][0]]):
				mdict[words[i][1]].append([words[i][3],words[i][0]])
		else:
			mdict[words[i][1]]=[[words[i][3],words[i][0]]]
	else:
		if words[i][1] in fdict:
			if match(fdict[words[i][1]],[words[i][3],words[i][0]]):
				fdict[words[i][1]].append([words[i][3],words[i][0]])
		else:
			fdict[words[i][1]]=[[words[i][3],words[i][0]]]
print "ln,dob,gn,fn"


for i in fdict:
	#print fdict[i]
	for j in range (len(fdict[i])):
		print fdict[i][j][1],",",i,",F",",",fdict[i][j][0]
for i in mdict:
	#print fdict[i]
	for j in range (len(mdict[i])):
		print mdict[i][j][1],",",i,",M",",",mdict[i][j][0]