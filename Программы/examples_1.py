#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Python #6. Examples. Using apostrophes:")
s1 = 'spam"s'
s2 = "spam's"
print("Single apostrophes : ", s1, ". Double apostrophes : ",
      s2, "\n", r"\nAnd using 'r' we are able\n to show raw lines.")
c1 = '''It's a very, very, very, very,
    very, very, very, very,
    very, very, big amount of text.'''
c2 = "It's a very, very, very, very,\nvery, very, very, very,\nvery, very, big amount of text."
print("String operators:\nNext example is using lines with three apostrophes:",
      c1, "\n", r"And putting \n right in the variable: ", c2)
s = 'py'
t = 'th'
u = 'on'
print("That is an example of summarising variables:",
      s + t + u + u + t + s, ". Interesting," + " right?")
print("Why don't we repeat it several times?", (s + t + u) * 5)
print("In next example, we are checking, whether there is or there is no such a word:")
s = "Python"
print("Is Java in s?", s in "Java",
      ". Well then, is it in Python fixer?", s in "Python fixer")
print("If it's needed to know symbol's id, then ord can be used: o =",
      ord('o'), "and © =", ord('©'))
print("Turning number back into the symbol can be done with chr(): 112 =",
      chr(112), "170 =", chr(170))
print("Length of line can be counted with len(): ",
      len("Length of line can be counted with len(): "))
print("Changing element's type to string can be done with str():",
      str(123 + 31), "and", str("something"))
something = "Long-Long_long"
print(
    "If symbol of line is needed, than [index] can help:", something[12], "or", something[-len(
        something)],
    "\nBut if several symbols are needed, than:", something[4:8], "or", something[:8], "and", something[8:])
