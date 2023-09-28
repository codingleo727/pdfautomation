import tkinter.filedialog as tkf

def uploadFile(filelist, ui, style):
   pathTuple = tkf.askopenfilenames(title = "Select a file", filetypes = [("PDF Files", "*.pdf")])
   pathList = list(pathTuple)
   for path in pathList:
      filelist.append(path)
      ui.fileDisplay(path, style)

def removeFile(filelist, pdfname, pairList, ui):
   for path in filelist:
      if pdfname in path:
         index = filelist.index(path)
         break
   filelist.pop(index)
   removeWidget(pairList, index, ui)

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