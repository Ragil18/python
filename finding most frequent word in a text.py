def main():
filename=raw_input("enter the file").strip()
infile=dopen(filename,"r")
wordcounts={}
for line in infile:
processLine(line.lower(),wordcounts)
pairs=list(wordcounts.items())
items=[[x,y] for (y,x) in pairs]
items.sort()
for i in range(len(items)-1,len(items)-11,-1):
print(items[i][1]+"\t"+str(items[i][0]))
def processLine(line,wordcounts):
line=replacePunctuations(line)
words=line.split()
for word in words:
if word in wordcounts:
wordcounts[word]+=1
else:
wordcounts[word]=1
def replacePunctuations(line):
for ch in line:
if ch in "~@#$%^&*()_-+=<>?/.,:;!{}[]''":
line=line.replace(ch," ")
return line
main()
