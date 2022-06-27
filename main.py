import os

from PIL import Image
from PyPDF2 import PdfMerger

root = "D:\Downloads"
manga = "some_manga_title"
pdf_to_join_folder = "D:\Downloads\PDF"
os.chdir(root)
#-------------join pictures in to a pdf---------
folders = [f"./{folder}/" for folder in os.listdir() if manga in folder]
file_list = []
for folder in folders:
    pdf_name = f'{folder[2:67].replace("   ", "  ")}.pdf'
    images = [Image.open(f'{folder}/{file}') for file in os.listdir(folder)]
    pdf_path = f"{root}\PDF/{pdf_name}"
    images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    print(pdf_name)
print("Easy")
# --------------pdf join----------------
os.chdir(pdf_to_join_folder)
pdf_list = [file for file in os.listdir() if manga in file]
merger = PdfMerger()
counter = 1
volume = 1
for pdf in pdf_list:
    merger.append(pdf)
    counter+=1
    if counter % 10 == 0 or counter ==len(pdf_list): #merges 10 pdf files into 1
        merger.write(f"{manga} Vol {volume}.pdf")
        volume +=1
        merger.close()
        merger = PdfMerger()

merger.close()
