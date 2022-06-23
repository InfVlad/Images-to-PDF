import os
from PIL import Image
root = "D:\Weeb Shit\lector mo descargas\Release\Descargas"
manga = "Kaiju"

os.chdir(root)
# for file in os.listdir():
#     if "Kaiju" in file:
#         print(file)
folders = [f"./{folder}/" for folder in os.listdir() if manga in folder]
file_list = []
for folder in folders:
    pdf_name= f'{folder[2:29].replace("   ","  ")}.pdf'
    images = [ Image.open(f'{folder}/{file}') for file in os.listdir(folder)]
    pdf_path = f"{root}\PDF/{pdf_name}"
    images[0].save(pdf_path,"PDF",resolution=100.0,save_all=True, append_images=images[1:])
    print(pdf_name)
print("Easy")
# print(file_list)


# images = [ Image.open('D:\Weeb Shit\lector mo descargas\Release\Descargas\Kaiju No. 8   Capítulo 38.00  KamiSubs/'+ f)
#            for file in ["001.jpg","002.jpg","003.jpg"]]
# pdf_path = "D:\Weeb Shit\lector mo descargas\Release\Descargas\Kaiju No. 8   Capítulo 38.00  KamiSubs\Kaiju8-C38.pdf"
#
# images[0].save(pdf_path,"PDF",resolution=100.0, save_all=True, append_images=images[1:])
# print("queso")