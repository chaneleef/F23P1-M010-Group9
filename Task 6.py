import pandas as pd

wb = pd.read_excel('Project1.xlsx', dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])
chars[13] = "\n"


def check_if_identical(p1: str, p2: str) -> bool:
    # defaults p2 to TextOutput.txt
    p2 = "TextOutput.txt"

    # for p1, opens and reads p1 into a string and prints it
    f = open(p1)
    s1 = f.read()
    print(s1)

    # for p2, opens and reads p1 into a string and prints it
    g = open(p2)
    s2 = g.read()
    print(s2)

    # checks if the two strings/files are different
    same = True
    i = 0
    while same:
        if s1[i] == s2[i]:
            print("Still same")
        else:
            same = False
        i += 1

    # closes both files - at the end
    f.close()
    g.close()

    if same == True:
        return True
    else:
        return False

