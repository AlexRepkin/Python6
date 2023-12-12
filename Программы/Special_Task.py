#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


if __name__ == '__main__':
    first_sentence = input("Good day, please, enter first sentence:\n")
    second_sentence = input("Great, now we need second sentence:\n")
    print("\nVery well, there is a list of words, that are mentioned only once in each sentence:\n")
    # В связи с тем, что split принимает только один разделитель, использована функция re.split, принимающая сразу
    # несколько разделителей. \s не считает место между двумя исключённых символов за отдельное слово.
    # Заключение в [] работает в качестве списка разграничивающих символов.
    first_words = re.split(r"[-;,.\s]\s*", first_sentence)
    second_words = re.split(r"[-;,?!.\s]\s*", second_sentence)
    for i in first_words:
        if 0 < first_words.count(i) < 2 and 0 < second_words.count(i) < 2:
            print(i)
