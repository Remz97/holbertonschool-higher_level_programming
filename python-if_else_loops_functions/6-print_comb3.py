#!/usr/bin/python3
for num in range(0, 10):
    for num_2 in range(num+1, 10):
        if num == 8 and num_2 == 9:
            print(f"{num}{num_2}")
        else:
            print(f"{num}{num_2}, ", end="")