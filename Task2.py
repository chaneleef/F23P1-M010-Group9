import pandas as pd

wb = pd.read_excel('Project1.xlsx', dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])
chars[13] = "\n"

# Task 2


def returnBinary(p1: str) -> tuple:
    # Gets the first 8 characters and sees if they're in the character list
    # the reason is one of our items is "Syracuse"
    if len(p1) >= 8:
        s1 = p1[0:8]
        for i in range(len(chars)):
            if chars[i] == s1:
                p1 = p1[8:]
                binVal = bins[i]
                return binVal, p1
    # Gets the first 4 characters and sees if they're in the character list
    elif len(p1) >= 4:
        s1 = p1[0:4]
        for i in range(len(chars)):
            if chars[i] == s1:
                p1 = p1[4:]
                binVal = bins[i]
                return binVal, p1
    # Gets the first 3 characters and sees if they're in the character list
    elif len(p1) >= 3:
        s1 = p1[0:3]
        for i in range(len(chars)):
            if chars[i] == s1:
                p1 = p1[3:]
                binVal = bins[i]
                return binVal, p1
    # Gets the first 2 characters and sees if they're in the character list
    elif len(p1) >= 2:
        s1 = p1[0:2]
        for i in range(len(chars)):
            if chars[i] == s1:
                p1 = p1[2:]
                binVal = bins[i]
                return binVal, p1
    # Checks for one character
    elif len(p1) >= 1:
        s1 = p1[0:1]
        for i in range(len(chars)):
            if chars[i] == s1:
                p1 = p1[1:]
                binVal = bins[i]
                return binVal, p1
    # returns an empty string if given an empty string
    elif len(p1) == 0:
        return ""
