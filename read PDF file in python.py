# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 07:16:03 2023

@author: jignesh
"""

import PyPDF2
# 
FILE_PATH = 'D:/Python Folder 2024/Python Training/Python material/Master Python Pandas_ Part 1.pdf'

with open(FILE_PATH, mode='rb') as f:

    reader = PyPDF2.PdfReader(f)

    page = reader.pages[5]

    print(page.extract_text())
    
    
    
