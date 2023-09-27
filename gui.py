import tkinter as tk
from tkinter import ttk
import re
import pdf
import fileoptions as fo

class ProgramUI:

    fileList = []
    label_button_pairs = []
    row_number = 0

    def __init__(self, master):
       master.title("Leo's PDF Merger")
       self.frameSetup(master)

    def frameSetup(self, master):
       master.geometry("800x350")
       master.minsize(800, 350)
       master.resizable(False, False)
       self.introCreate(master)
       self.displayFunctionality(master)
       self.functionality(master)
       ttk.Button(master, command = lambda: print(self.fileList), text = "Show list").pack()
       ttk.Button(master, command = lambda: print(self.label_button_pairs), text = "Show widget").pack()
       ttk.Button(master, command = lambda: print(len(self.fileList)), text = "Show list length").pack()
       ttk.Button(master, command = lambda: print(len(self.label_button_pairs) - 1), text = "Pair len").pack()

    # The UI for the program introduction
    def introCreate(self, master):
       self.introFrame = ttk.Frame(master, relief = "solid", height = 100, width = 100)
       self.introFrame.pack()
       title = "Please upload the pdfs for merging"
       self.intro = ttk.Label(self.introFrame, text = title, font = 100)
       self.intro.pack(fill = "both", expand = True)

    # The UI for the functionality
    def functionality(self, master):
       self.buttonFrame = ttk.Frame(master, relief = "ridge", height = 100, width = 100)
       self.buttonFrame.pack(side = "left", expand = 1, padx = 10, pady = 10)
       self.uploadFunctionality(self.buttonFrame)
       self.mergeFunctionality(self.buttonFrame)

    # The UI for the upload button
    def uploadFunctionality(self, master):
       self.uploadButton = ttk.Button(master, command = lambda: fo.uploadFile(self.fileList, self), text = "Upload")
       self.uploadButton.grid(row = 2, column = 1)

    # The UI for the merge button
    def mergeFunctionality(self, master):
       self.mergeButton = ttk.Button(master, command = lambda: pdf.mergePDF(self.fileList, self.displayFrame), text = "Merge")
       self.mergeButton.grid(row = 2, column = 2)

    def displayFunctionality(self, master):
       self.displayFrame = ttk.Frame(master)
       self.displayFrame.pack(padx = 20, pady = 20)

    def fileDisplay(self, filename):
       pdfname = re.search("[^\/]*$", filename).group()
       self.createLabelButtonPair(self.displayFrame, pdfname)

    def createLabelButtonPair(self, master, pdfname):
       self.row_number = len(self.label_button_pairs)
       self.fileLabel = ttk.Label(master, text = pdfname)
       self.fileLabel.grid(row = self.row_number, column = 0, padx = 5, pady = 5, sticky = "w")
       self.removeButton = ttk.Button(master, command = lambda: fo.removeFile(self.fileList, pdfname,
       self.label_button_pairs, self), text = "Remove")
       self.removeButton.grid(row = self.row_number, column = 1, padx = 5, pady = 5)
       self.label_button_pairs.append((self.fileLabel, self.removeButton))