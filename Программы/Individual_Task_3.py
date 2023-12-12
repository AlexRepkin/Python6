#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    words = input("Good day! Please, enter your text.\n")
    for i in words:
        if not (58 > ord(i) > 47):
            print("Sorry, but text can't be transformed into Integer type.")
            exit(1)
    print("Sure, that text can be transformed into Integer type.")
