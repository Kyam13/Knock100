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

#15
print("10\n")
#16
print("10\n")
#17
print("10\n")
#18
print("18\n")
#19
print("19\n")
