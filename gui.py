import tkinter as tk
from tkinter import ttk
import re
import pdf
import fileoptions as fo

class ProgramUI:

    fileList = []
    label_button_pairs = []

    # Sets the title and initializes the frames for the tkinter window.
    # Parameter:
    #         master: (tk Widget) The parent widget
    # Returns:
    #         None
    def __init__(self, master):
       master.title("Leo's PDF Merger")
       self.frameSetup(master)

    # Configures the main frames for the UI.
    # Parameter:
    #         master: (tk Widget) The parent widget
    # Returns:
    #         None
    def frameSetup(self, master):
       style = ttk.Style()
       master.minsize(600, 350)
       master.resizable(False, False)
       self.introCreate(master)
       self.displayFunctionality(master, style)
       self.functionality(master, style)

    # Creates the introduction section of the UI.
    # Parameter:
    #         master: (tk Widget) The parent widget
    # Returns:
    #         None
    def introCreate(self, master):
       self.introFrame = ttk.Frame(master, relief = "solid", height = 100, width = 100)
       self.introFrame.pack()
       title = "Please upload the pdfs for merging"
       self.intro = ttk.Label(self.introFrame, text = title, font = 100)
       self.intro.pack(fill = "both", expand = True)

    # Sets up the buttons for the main functionality.
    # Parameter:
    #         master: (tk Widget) The parent widget
    #         style: (tk.Style) The styling function for tkinter
    # Returns:
    #         None
    def functionality(self, master, style):
       self.buttonFrame = ttk.Frame(master, height = 100, width = 100)
       self.buttonFrame.pack(side = "left", expand = 1, pady = 20)
       self.uploadFunctionality(self.buttonFrame, style)
       self.mergeFunctionality(self.buttonFrame)

    # Creates the upload button.
    # Parameter:
    #         master: (tk Widget) The parent widget
    #         style: (tk.Style) The styling function for tkinter
    # Returns:
    #         None
    def uploadFunctionality(self, master, style):
       self.uploadButton = ttk.Button(master, command = lambda: fo.uploadFile(self.fileList, self, style), text = "Upload")
       self.uploadButton.grid(row = 2, column = 1)

    # Creates the merge button.
    # Parameter:
    #         master: (tk Widget) The parent widget
    # Returns:
    #         None
    def mergeFunctionality(self, master):
       self.mergeButton = ttk.Button(master, command = lambda: pdf.mergePDF(self.fileList, self.displayFrame), text = "Merge")
       self.mergeButton.grid(row = 2, column = 2)

    # Sets up the display functionality.
    # Parameter:
    #         master: (tk Widget) The parent widget
    #         style: (tk.Style) The styling function for tkinter
    # Returns:
    #         None
    def displayFunctionality(self, master, style):
       self.containerFrame = ttk.Frame(master)
       self.containerFrame.pack(fill = "both", expand = True, padx = 20)

       self.displayCanvas = tk.Canvas(self.containerFrame, bg = "white", width = 300, height = 200)
       self.displayScrollBar = tk.Scrollbar(self.containerFrame, orient = "vertical", command = self.displayCanvas.yview)
       self.displayCanvas.configure(yscrollcommand = self.displayScrollBar.set)

       style.configure("Display.TFrame", background = "white")
       self.displayFrame = ttk.Frame(self.displayCanvas, style = "Display.TFrame")
       self.displayCanvas.create_window(250, 0, window = self.displayFrame, anchor = "n")

       self.displayCanvas.bind("<Configure>", self.onCanvasConfigure)
       self.displayCanvas.bind("<MouseWheel>", self._on_mousewheel)

       self.displayCanvas.pack(side = "left", fill = "both", expand = True, padx = 20)
       self.displayScrollBar.pack(side = "right", fill = "y")

    # Updates and displays the uploaded filenames.
    # Parameter:
    #         filename: (String) The name of the uploaded file
    #         style: (tk.Style) The styling function for tkinter
    # Returns:
    #         None
    def fileDisplay(self, filename, style):
       pdfname = re.search("[^\/]*$", filename).group()
       self.createLabelButtonPair(self.displayFrame, pdfname, style)

       self.displayFrame.update_idletasks()
       self.displayCanvas.configure(scrollregion = self.displayCanvas.bbox("all"))

    # Creates label and button pairs for each uploaded file.
    # Parameter:
    #         master: (tk Widget) The parent widget
    #         pdfname: (String) The name of the uploaded PDF
    #         style: (tk.Style) The styling function for tkinter
    # Returns:
    #         None
    def createLabelButtonPair(self, master, pdfname, style):
       style.configure("PDF.TLabel", background = "white")
       self.row_number = len(self.label_button_pairs)
       self.fileLabel = ttk.Label(master, text = pdfname, style = "PDF.TLabel")
       self.fileLabel.grid(row = self.row_number, column = 0, padx = 5, pady = 5, sticky = "w")
       self.removeButton = ttk.Button(master, command = lambda: fo.removeFile(self.fileList, pdfname,
       self.label_button_pairs, self), text = "Remove")
       self.removeButton.grid(row = self.row_number, column = 1, padx = 5, pady = 5)
       self.label_button_pairs.append((self.fileLabel, self.removeButton))

    # Adjusts the canvas configuration upon resizing.
    # Parameter:
    #         event: (tk Event) The event that triggers this method
    # Returns:
    #         None
    def onCanvasConfigure(self, event):
       self.displayCanvas.configure(scrollregion = self.displayCanvas.bbox("all"))

    # Handles mouse wheel scrolling for the canvas.
    # Parameter:
    #         event: (tk Event) The event that triggers this method
    # Returns:
    #         None
    def _on_mousewheel(self, event):
       if self.displayCanvas.bbox("all")[3] > self.displayCanvas.winfo_height():
        self.displayCanvas.yview_scroll(-1 * (event.delta//120), "units")