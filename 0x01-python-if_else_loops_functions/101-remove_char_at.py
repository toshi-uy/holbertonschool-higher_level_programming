#/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if n >= 0:
            new = str[:n] + str[n + 1 :]
            return new
        else:
            return str
