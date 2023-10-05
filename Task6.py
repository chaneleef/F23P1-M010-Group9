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

