#defauld setting
tempfiledata = open("hightemp.txt")
tempfile = tempfiledata.read()
tempfiledata.close()

#unix command
import subprocess

#10
print("10\n")
ana_tempfiledata = open("hightemp.txt")
ana_tempfile = ana_tempfiledata.readlines()
ana_tempfiledata.close()
subcheck=subprocess.check_output("cat hightemp.txt|wc -l",shell=True)
print(subcheck,len(ana_tempfile))

#11
print("11\n")
newtempcel=""
for char in tempfile:
    if char=='\t':
        newtempcel+=" "
    else:
        newtempcel+=char

print(newtempcel==subprocess.check_output("expand -t 1 hightemp.txt",shell=True,universal_newlines=True))
"""
#12
print("12\n")
writefile1=open("col1.txt","w")
# word=[]
for words in ana_tempfile:
    word = words.split("\t")
    writefile1.write(word[0]+"\n")
writefile1.close()
writefile2=open("col2.txt","w")
for words in ana_tempfile:
    word = words.split("\t")
    writefile2.write(word[1]+"\n")
writefile2.close()
print(subprocess.check_output("cut -f1 hightemp.txt",shell=True,universal_newlines=True)==subprocess.check_output("cut -f 1 col1.txt",shell=True,universal_newlines=True))
print(subprocess.check_output("cut -f2 hightemp.txt",shell=True,universal_newlines=True)==subprocess.check_output("cut -f 1 col2.txt",shell=True,universal_newlines=True))
#13
print("13\n")
readfile1data=open("col1.txt")
readfile1=readfile1data.readlines()
readfile1data.close()
readfile2data=open("col2.txt")
readfile2=readfile2data.readlines()
readfile2data.close()
sumfile=open("sumfile.txt","w")
print(str(readfile1[1]))
for i in range(len(readfile1)):
    word1=str(readfile1[i]).split("\n")
    word2=str(readfile2[i]).split("\n")
    sumfile.write(word1[0]+"\t"+word2[0]+"\n")
    word1=word2=[]
sumfile.close()
exaple=subprocess.check_output("paste col1.txt col2.txt",shell=True,universal_newlines=True)
readfile=open('sumfile.txt')
read=readfile.read()
print(exaple==read)
readfile.close()
#14
print("14\n")
N=int(input())
for i in range(N):
    print(ana_tempfile[i],end='')
print(subprocess.check_output("head -n10 hightemp.txt",shell=True,universal_newlines=True))
#15
print("15\n")
N=int(input())
for i in range(N)[::-1]:
    print(ana_tempfile[int(len(ana_tempfile))-i-1],end='')
print(subprocess.check_output("tail -n10 hightemp.txt",shell=True,universal_newlines=True))

#16
print("16\n")
N=len(ana_tempfile)/int(input())
newtext=[]
anstext=[]
new=""
ans=""
for i in range(len(ana_tempfile)):
    if i==23:
        newtext.append(ana_tempfile[i])
        new="".join(newtext)
        anstext=new.split('\n')
        ans=" ".join(anstext)
        print(ans,len(newtext))
        new=""
        newtext=[]
        ans=""
    elif (i+1)%(N)==0:
        new="".join(newtext)
        anstext=new.split('\n')
        ans=" ".join(anstext)
        print(ans,len(newtext))
        new=""
        newtext=[]
        ans=""
        newtext.append(ana_tempfile[i])
    else:
        newtext.append(ana_tempfile[i])
"""
#17
print("10\n")
tabarr=[]
newtab=[]
for col in ana_tempfile:
    tabarr=col.split("\t")
    newtab.append(tabarr[0])
setnewtab=set(newtab)
print(setnewtab)
#18
from collections import defaultdict,OrderedDict
print("18\n")
tabarr=[]
newtab={}
cnt=0
for col in ana_tempfile:
    cnt+=1
    tabarr=col.split("\t")
    tamprature=float(tabarr[2])
    newtab[col]=tamprature
    tamprature=0
    if cnt==23:
        newcor=OrderedDict(sorted(newtab.items(),key=lambda x:x[1],reverse=True))
        for new in newcor.keys():
            print(new,end="")
#19
print("19\n")
tabarr=[]
newtab={}
cnt=0
for col in ana_tempfile:
    cnt+=1
    tabarr=col.split("\t")
    newtab[col]=tabarr[0]
    tamprature=0
    if cnt==23:
        print(newtab)
        """
        newcor=OrderedDict(sorted(newtab.items(),key=lambda x:x[1],reverse=True))
        for new in newcor.keys():
            print(new,end="")
"""
