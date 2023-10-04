import pandas as pd


# opens the Excel file and reads it into two lists, bins and chars
wb = pd.read_excel('F23P1-M010-Group9.xlsx', dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])
# fixes the "\\n"
chars[13] = "\n"

# Task 2
# Reads a string and returns the binary value and new string that has that character removed


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

    # Gets the first 3 characters and sees if they're in the character list
    if len(p1) >= 3:
        s1 = p1[0:3]
        for i in range(len(chars)):
            if chars[i] == s1:
                p1 = p1[3:]
                binVal = bins[i]
                return binVal, p1

    # Gets the first 2 characters and sees if they're in the character list
    if len(p1) >= 2:
        s1 = p1[0:2]
        for i in range(len(chars)):
            if chars[i] == s1:
                p1 = p1[2:]
                binVal = bins[i]
                return binVal, p1

    # Checks for one character
    if len(p1) >= 1:
        for i in range(len(chars)):
            if chars[i] == p1[0]:
                if len(p1) > 1:
                    p1 = p1[1:]
                else:
                    p1 = ""
                binVal = bins[i]
                return binVal, p1

    # returns an empty string if given an empty string
    return "",""