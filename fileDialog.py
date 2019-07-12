# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:29:49 2019

@author: Renato
"""

from tkinter import filedialog
from tkinter import *
import logging

class fileDialog:
    dialog = Tk()
    logging.basicConfig(filename = 'fileDialog.log', format='%(asctime)s - %(message)s', level=logging.DEBUG)
    path = ''
    
    def __init__(self, fileType, fileExtension):
        self.fileType = fileType
        self.fileExtension = fileExtension
    def openFile(self):
        try:
            fileDialog.dialog.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = ((""+self.fileType +"","*"+self.fileExtension+""),("All files","*.*")))
            fileDialog.path = fileDialog.dialog.filename
            logging.info(f'{fileDialog.path} succeded.')
            fileDialog.dialog.destroy()
        except Exception:
            logging.exception("Exception ocurred", exc_info=True)
