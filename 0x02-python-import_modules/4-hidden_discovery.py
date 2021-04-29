#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    a = dir(hidden_4)
    for i in range(len(a)):
        if a[i][:2] != "__":
            print(a[i])
