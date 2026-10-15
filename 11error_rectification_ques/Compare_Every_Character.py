#Q.Compare every character with every other character and label Same/Different.
string = input("Enter a string: ")
for i in string:    # Outer loop: selects one character at a time from the string
     for j in string:   # Inner loop: compares the selected character with every character
                        # in the string, starting from the first character each time
                        # Checks whether both characters are equal
        if i == j:
            print(i, j, "Same")  # Prints Same if both characters match
        else:
            print(i, j, "Different")  # Prints Different if they don't match
# After the inner loop finishes all comparisons,
# the outer loop selects the next character
# The process repeats until every character has been selected