import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileReader, PdfMerger

def merge_pdfs(paths, output):
    merger = PdfMerger()
    for path in paths:
        merger.append(path)
    merger.write(output)
    merger.close()

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_file:
            merge_pdfs(file_paths, output_file)
            messagebox.showinfo("Success", "PDFs merged successfully!")
        else:
            messagebox.showinfo("Cancelled", "Save operation cancelled")
    else:
        messagebox.showinfo("Cancelled", "File selection cancelled")

# Set up the tkinter GUI
root = tk.Tk()
root.title("PDF Merger")
root.geometry("300x150")

select_button = tk.Button(root, text="Select PDFs and Merge", command=select_files)
select_button.pack(expand=True)

root.mainloop()
