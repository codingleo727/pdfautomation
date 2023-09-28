import tkinter.filedialog as tkf

# Allows user to upload files and displays them on the UI.
# Parameter:
#         filelist: (List[String]) List containing the paths of uploaded files
#         ui: (self) The main UI class instance
#         style: (tk.Style) The styling function for tkinter
# Returns:
#         None
def uploadFile(filelist, ui, style):
   pathTuple = tkf.askopenfilenames(title = "Select a file", filetypes = [("PDF Files", "*.pdf")])
   pathList = list(pathTuple)
   for path in pathList:
      filelist.append(path)
      ui.fileDisplay(path, style)

# Removes a file from the filelist and UI.
# Parameter:
#         filelist: (List[String]) List containing the paths of uploaded files
#         pdfname: (String) The name of the PDF to be removed
#         pairList: (Tuple[tk Widget, tk Widget]) List of label-button pairs
#         ui: (self) The main UI class instance
# Returns:
#         None
def removeFile(filelist, pdfname, pairList, ui):
   for path in filelist:
      if pdfname in path:
         index = filelist.index(path)
         break
   filelist.pop(index)
   removeWidget(pairList, index, ui)

# Removes the label and button widgets associated with a file.
# Parameter:
#         pairList: (Tuple[tk Widget, tk Widget]) List of label-button pairs
#         index: (int) Index of the file to be removed
#         ui: (self) The main UI class instance
# Returns:
#         None
def removeWidget(pairList, index, ui):
   label, button = pairList.pop(index)
   label.destroy()
   button.destroy()
   for i in range(index, len(pairList)):
      label, button = pairList[i]
      label.grid(row = i)
      button.grid(row = i)
      button["command"] = lambda filename = ui.fileList[i]: removeFile(ui.fileList, filename, ui.label_button_pairs, ui)
      ui.onCanvasConfigure(None)