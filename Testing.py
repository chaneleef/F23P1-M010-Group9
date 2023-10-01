import pandas as pd
wb = pd.read_excel('File Name', dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])


''' (TO CHECK WORK)
for i in range(len(bins)):
    print(bins[i], ": ", i)
'''

#Opens and prints file
f = open('TextOutput.txt')
s1 = f.read() #reads it into a string
print(s1)

#Opens and prints Binary file
f = open('BinOutput.txt')
s2 = f.read()
print(s2)
f.close()

#checks if the two strings/files are different
same = True
i = 0
while same:
    if s1[i] == s2[i]:
        print("Still same")
    else:
        same = False
    i+=1
