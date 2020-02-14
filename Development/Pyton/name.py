#!/usr/bin/env python
# -*- Codeing: utf-8 -*-

name = raw_input("Hallo! Wie heisst du? ")
name_with_borders =  "= {0} =".format(name)
line = "-" * len(name_with_borders)

print(line)
print(name_with_borders)
print(line)
