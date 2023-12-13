import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

from spire.presentation import *
from spire.presentation.common import *


def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)


def convert_pptx_to_pdf():
    files = filedialog.askopenfilenames(filetypes=[("PowerPoint files", "*.pptx")])
    temp_files = []

    for file in files:
        temp_pdf_path = os.path.basename(file) + "_temp.pdf"
        print(os.path.realpath(file))
        presentation = Presentation()
        presentation.LoadFromFile(os.path.realpath(file), FileFormat.Pptx2019)
        presentation.SaveToFile(temp_pdf_path, FileFormat.PDF)
        presentation.Dispose()
        temp_files.append(temp_pdf_path)

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    merge_pdfs(temp_files, save_path)

    # Delete temporary files
    for temp_file in temp_files:
        os.remove(temp_file)

root = tk.Tk()
root.title("PPTX to PDF Converter")
root.geometry("300x150")

button = tk.Button(root, text="Select PPTX Files", command=convert_pptx_to_pdf)
button.pack(expand=True)

root.mainloop()
