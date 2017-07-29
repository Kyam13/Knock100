#00
print("00\n")
word1 = "stressed"
print(word1[::-1])

#01
print("01\n")
word2="パタトクカシーー"
word=word2[::2]
print(word)

#02
print("02\n")
taxi="タクシー"
for i in range(len(word)):
    print(word[i]+taxi[i],end='')
    if i == len(word)-1:
        print('\n')

#03
print("03\n")
cell="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
w=[word for word in cell.split(" ")]
print(w)

#04
print("04\n")
import string
cell="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
for word in string.punctuation:
    if word == '.':
        cells=cell.split(word)
ans_word={}
cnt=1
chars=[]
identification=[1, 5,6, 7, 8,9, 15, 16, 19]
for word in cells:
    for char in word.split(" "):
        if char != "":
            chars.append(char)
for char in chars:
    if cnt in identification:
        ans_word[cnt]=char[0:1]
    else:
        ans_word[cnt]=char[0:2]
    cnt+=1
print(ans_word,cnt)

#05
print("05\n")
import ngram
def n_gram(cell):
    bi_gram=[]
    index = ngram.NGram(N=2)
    for term in index.ngrams(index.pad(cell)):
        bi_gram.append(term)
    return set(bi_gram)

print(n_gram("I am an NLPer"))

#06
print("06\n")
X=n_gram('paraparaparadise')
Y=n_gram("paragraph")
print("X&Y",X&Y,"X|Y,",X|Y,"X-Y",X-Y)

# 07
print("07\n")
def stringtime(x,y,z):
    return "{0}時の{1}は{2}".format(x,y,z)
print(stringtime(12,"気温",22.4))

# 08
print("08\n")
def cipher(text):
    nocnt=[]
    newword=[]
    newstr=""
    for i,char in enumerate(text):
        if char!=" ":
            if char in string.ascii_lowercase:
                newword.append(chr(219-ord(char)))
            else:
                newword.append(char)
        else:
            nocnt.append(i)
    cnt=0
    for j in range(len(newword)+len(nocnt)):
        if j in nocnt:
            newstr+=" "
        else:
            newstr+=newword[cnt]
            cnt+=1

    return str(newstr)

print(cipher("I An Am Emtrmvvi."))

# 09
print("09\n")
text="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(text)
import random
cell =[word for word in text.split(" ")]
randomcell=cell[1:len(cell)-1]
newrandomcell=""
for i in range(len(cell)):
    if i==0 or i==len(cell)-1:
        newrandomcell+=cell[i]
    else:
        newrandomcell+=" "+random.choice(randomcell)

print(newrandomcell)
