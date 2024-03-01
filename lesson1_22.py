melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}

for word in melt.keys():
    for char in range(len(word)):
        if (word[char]=="O" and char!=0):
            print(melt[word], end=' ')