import string
mydict = {}
with open("dictionarytext.txt", "r") as f:
    lines = f.readlines()
for i in lines:
    words = i.split()
    for j in words:
        word = j.strip()
        word = word.translate(str.maketrans(" ", " ", string.punctuation))
        if word.lower() not in mydict.keys():
            mydict[word.lower()] = 1
        else:
            mydict[word.lower()] += 1
print(mydict.get('project'))