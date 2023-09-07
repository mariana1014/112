import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Mueve todas las imagenes de la carpeta descargas a otra carpeta.
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path1 = from_dir + '/' + file_name                       # Ejemplo path1 : Descargas/ImageName1.jpg        
        path2 = to_dir + '/' + "Document_Files"                     # Ejemplo path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Ejemplo path3 : D:/My Files/Image_Files/ImageName1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Verifica si la ruta carpeta/Directorio existe antes de moverla
        # De lo contrario, haz una NUEVA carpeta/Directorio luego muevela
        
        if os.path.exists(path2):
          print("Moviendo " + file_name + ".....")

          # Mueve de path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moviendo " + file_name + ".....")
          shutil.move(path1, path3)

        
