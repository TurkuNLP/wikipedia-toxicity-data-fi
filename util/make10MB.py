import sys
import re
import json
import itertools

def unescape(s):
    return(s)

part=0
f=open(f"out/part-{part:02d}.txt","wt")

preamble= """North Korea has released photographs which it said were taken from its most powerful missile launch in five years.

The unusual pictures taken from space show parts of the Korean peninsula and surrounding areas.

Pyongyang confirmed on Monday it had tested a Hwasong-12 intermediate range ballistic missile (IRBM).

At its full power it can travel thousands of miles, putting areas like US territory Guam within striking distance.

The latest test has raised alarm again among the international community.

Pyongyang has conducted a record number of seven missile launches in the past month alone - an intense flurry of activity that has been strongly condemned by the US, South Korea, Japan, and other nations.


"""

print(preamble,file=f)
length=0
for line in itertools.islice(sys.stdin,1,None):
    line=line.rstrip("\n")
    cols=line.split("\t")
    if cols[0]=="section":
        continue
    id=f"i-{cols[0]}-{cols[1]}"
    print(id,file=f)
    print(file=f)
    length+=len(id)+1
    txt=json.loads(cols[-1])
    txt=unescape(txt)
    print(txt,file=f)
    print(file=f)
    print(file=f)
    length+=len(txt)+3
    if length>(900000):
      f.close()
      part+=1
      f=open(f"out/part-{part:02d}.txt","wt")
      length=0
      print(preamble,file=f)
f.close()
  
    
