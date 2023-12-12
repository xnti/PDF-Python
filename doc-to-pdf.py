import os
import tkinter as tk
from tkinter import filedialog, messagebox
import docx
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io

def docx_to_pdf(docx_path, pdf_path):
    doc = docx.Document(docx_path)
    packet = io.BytesIO()
    c = canvas.Canvas(packet)

    for i, p in enumerate(doc.paragraphs):
        c.drawString(72, 800 - 15 * i, p.text)
    c.save()

    packet.seek(0)
    with open(pdf_path, 'wb') as f:
        f.write(packet.getvalue())

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def convert_docs_to_pdf():
    files = filedialog.askopenfilenames(filetypes=[("Word files", "*.docx")])
    temp_files = []

    for file in files:
        temp_pdf_path = os.path.basename(file) + "_temp.pdf"
        docx_to_pdf(file, temp_pdf_path)
        temp_files.append(temp_pdf_path)

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if save_path:
            merge_pdfs(temp_files, save_path)
            for temp_file in temp_files:
                os.remove(temp_file)
            messagebox.showinfo("Success", "PDF created successfully!")
    else:
        messagebox.showinfo("Cancelled", "Save operation cancelled")
    

root = tk.Tk()
root.title("DOCX to PDF Converter")
root.geometry("300x150")

button = tk.Button(root, text="Select DOCX Files", command=convert_docs_to_pdf)
button.pack(expand=True)

root.mainloop()
