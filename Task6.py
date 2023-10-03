import pandas as pd

wb = pd.read_excel('F23P1-M010-Group9.xlsx', dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])
chars[13] = "\n"


def check_if_identical() -> bool: # or keep p1: str in ()
    # defaults p2 to TextOutput.txt
    p1 = str(input("What's the file name for p1?"))
    p2 = "TextOutput"

    # for p1, opens and reads p1 into a string
    f = open(p1)
    s1 = f.read()

    # for p2, opens and reads p1 into a string
    g = open(p2)
    s2 = g.read()

    # checks if the two strings/files are different
    same = True
    i = 0
    while True:
        if len(s1) < i or len(s2) < i:
            break
        elif s1[i] == s2[i]:
            i += 1
            continue
        else:
            same = False

    # closes both files - at the end
    f.close()
    g.close()

    if same == True:
        return True
    else:
        return False

