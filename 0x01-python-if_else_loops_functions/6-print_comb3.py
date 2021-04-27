#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x < y:
            print("{:d}{:d}".format(x, y), end="")
            if x < 8:
                print(",", end=" ")
print("")
