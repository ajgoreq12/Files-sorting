import os 
import shutil

sorter = os.listdir('Sorter')
for file in sorter:
    file_name, file_extension = os.path.splitext(file)

    if file_extension == ".png" or file_extension == ".jpg":
        print(f"{file_name} is image with {file_extension} extension")
        src_path = os.path.join('Sorter', file)
        dst_path = os.path.join('Images', file)
        shutil.move(src_path, dst_path)