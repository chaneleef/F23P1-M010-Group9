import pandas as pd

# opens the Excel file and reads it into two lists, bins and chars
wb = pd.read_excel('F23P1-M010-Group9.xlsx', dtype=str)
bins = list(wb["Bin"])
chars = list(wb["Char"])
# fixes the "\\n"
chars[13] = "\n"


# Task 2
# Reads a string and returns the binary value and new string that has that character removed


def Task2(p1: str) -> tuple:
    # Gets the first 8 characters and sees if they're in the character list
    # the reason is one of our items is "Syracuse"
    if len(p1) >= 8:
        # sets s1 as the first 8 letters of p1
        s1 = p1[0:8]
        # goes through every item in chars and checks to see if equal
        for i in range(len(chars)):
            if chars[i] == s1:
                # sets the rest of s1 to every character after this string
                p1 = p1[8:]
                # fetches the binary value
                bin_val = bins[i]
                # returns the binary value and rest of the string
                return bin_val, p1

    # Gets the first 3 characters and sees if they're in the character list
    if len(p1) >= 3:
        # sets s1 as the first 3 letters of p1
        s1 = p1[0:3]
        # goes through every item in chars and checks to see if equal
        for i in range(len(chars)):
            if chars[i] == s1:
                # sets the rest of s1 to every character after this string
                p1 = p1[3:]
                # fetches the binary value
                bin_val = bins[i]
                # returns the binary value and rest of the string
                return bin_val, p1

    # Gets the first 2 characters and sees if they're in the character list
    if len(p1) >= 2:
        # sets s1 as the first 2 letters of p1
        s1 = p1[0:2]
        # goes through every item in chars and checks to see if equal
        for i in range(len(chars)):
            if chars[i] == s1:
                # sets the rest of s1 to every character after this string
                p1 = p1[2:]
                # fetches the binary value
                bin_val = bins[i]
                # returns the binary value and rest of the string
                return bin_val, p1

    # Checks for one character
    if len(p1) >= 1:
        # goes through every item in chars and checks to see if equal
        for i in range(len(chars)):
            if chars[i] == p1[0]:
                if len(p1) > 1:
                    # sets the rest of s1 to every character after this string
                    p1 = p1[1:]
                else:
                    p1 = ""
                # fetches the binary value
                bin_val = bins[i]
                # returns the binary value and rest of the string
                return bin_val, p1

    # returns an empty string if given an empty string
    return "", ""


# Task 6
# Returns true if both text files are equal

def check_if_equal (p1: str) -> bool:
    # defaults p2 to TextOutput.txt
    p2 = "TextOutput.txt"

    # for p1, opens and reads p1 into a string
    f = open(p1)
    s1 = f.read()

    # for p2, opens and reads p1 into a string
    g = open(p2)
    s2 = g.read()

    # closes both files - at the end
    f.close()
    g.close()

    # returns True if equal and False otherwise
    return s1 == s2

