# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:44:16 2019

@author: Renato
"""

import xlrd
import logging

class excelClass:
    book = ''
    sheet = 0
    logging.basicConfig(filename = 'excelCLass.log', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    
    def __init__(self, filename, sheetNumber):
        self.filename = filename
        self.sheetNumber = sheetNumber
    
    def excelCrawl(self):
        try:
            excelClass.book = xlrd.open_workbook(self.filename)
            excelClass.sheet = excelClass.book.sheet_by_index(self.sheetNumber)
            logging.info(f'{self.filename} opened  on sheet {excelClass.sheet.name}.')
        except Exception:
            logging.exception("Exception ocurred", exc_info = True)