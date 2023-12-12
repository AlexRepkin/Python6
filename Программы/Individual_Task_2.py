#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    words = input(
        "Good day! Please, enter your text (Rememer, that only first sentence will be analised).\n")
    count = 0
    for i in words:
        if i != "." and i != "!" and i != "?" and i != ";":
            if i == "и":
                count += 1
        else:
            break
    if count == 0:
        print("Sorry, there were no 'и' in the first sentence.")
    else:
        print("In first sentence, there are", count, "symbols 'и'.")
