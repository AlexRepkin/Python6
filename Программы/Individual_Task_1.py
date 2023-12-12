#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


if __name__ == '__main__':
    words = input("Good day! Please, enter your sentence.")
    # There are two variants - checking five letters and using a counter.
    start_time = time.time()
    contains = False
    for i in range(0, len(words)-4):
        if words[i] == words[i+1] == words[i+2] == words[i+3] == words[i+4]:
            print("Yes, there are 5 symbols '", words[i], "'.")
            contains = True
            break
    first_variant_time = time.time() - start_time
    start_time = time.time()
    count = 1
    symbol = words[0]
    for i in words[1:]:
        if i == symbol:
            count += 1
            if count == 5:
                print("Yes, there are 5 symbols '", i, "'.")
                contains = True
                break
        else:
            count = 1
            symbol = i
    if not contains:
        print("Sorry, there are no 5 equal symbols.")
    second_variant_time = time.time() - start_time
    print("First variant took ", first_variant_time,
          " and Second variant took ", second_variant_time)
