def add(x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    x = input("Num 1 : ")
    y = input("Num 2 : ")
    z = add(x, y)
    print(z)

# There is an error in the funciton, input will return the string and it will not
# add, and the output will throw an error. We write the pdb command in command
# line to debug it. "python -m pdb debugging.py" and then write "help" to see the
# full list of pdb commands. 