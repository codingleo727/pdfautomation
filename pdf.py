import fitz
import os

# Merges selected PDF files and saves the merged PDF.
# Parameter:
#         filelist: (List[String]) List containing the paths of uploaded files
#         master: (tk Widget) The parent widget
# Returns:
#         None
def mergePDF(filelist, master):
    doc = fitz.open()
    for filename in filelist:
        doc.insert_file(filename)

    os.system("download.bat")
    with open("downloads_folder.txt", "r") as file:
        downloads_folder = file.readline().strip()

    if os.path.exists(downloads_folder):
        output_dest = os.path.join(downloads_folder, "Merged.pdf")

    doc.save(output_dest)
    doc.close()

    clear_all(filelist, master)

# Clears all uploaded files and their associated widgets.
# Parameter:
#         filelist: (List[String]) List containing the paths of uploaded files
#         master: (tk Widget) The parent widget
# Returns:
#         None
def clear_all(filelist, master):
    filelist.clear()
    for widget in master.winfo_children():
          widget.destroy()