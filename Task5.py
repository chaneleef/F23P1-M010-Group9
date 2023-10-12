# function that decodes bin to char

#defaults param to BinOutput.txt
def decode(sn="BinOutput.txt")
    f = open(fn, "r")
    s = f.read()
    f.close()
    i = s.index(".")
    s = s[i+1:]
    charStr = ""
    while (s!=""):
        binVal, s = getFirstBin(s)
        charStr = charStr + getChar(binVal)

    f = open("TextOutput.txt","w+")
    f.write(charStr)
    f.close