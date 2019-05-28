import sys

def usage():
        print('Usage: python3 urlhex.py "<script>alert(888)</script>"')
        sys.exit (1)

if len (sys.argv) != 2 :
        usage()

text = sys.argv[1]

utf = text.encode('utf-8')
s=utf.hex()

hexArray=[]
count=0
first=0
next=first+2
max=len(s)/2
while count < max:
	next=first+2
	hexArray.append("&#x" + s[first:next] + ";")
	count = count+1
	first=first+2

for i in range (int(max)):
	print(hexArray[i], end ="")

print("")
