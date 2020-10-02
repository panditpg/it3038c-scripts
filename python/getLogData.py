import os

filename = "C:/it3038c-scripts\testing\testfile"

with open(filename) as f:
    lines = set(f.read().splitlines())
    for l in lines:
        if "Prayag" in l:
            print(l) 