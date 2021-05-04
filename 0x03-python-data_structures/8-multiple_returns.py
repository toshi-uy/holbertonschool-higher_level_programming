#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first = sentence[0]
        return length, first
    else:
        length = 0
        first = None
        return length, first
