#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Wed Nov 28 12:33:08 2018

@author: jordansauchuk
'''

from PIL import Image
import pytesseract

demo = Image.open("example_two.png")


text = pytesseract.image_to_string(demo, lang = 'eng')

print(text)