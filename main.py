import os 
import shutil

sorter = os.listdir('Sorter')
for file in sorter:
    file_name, file_extension = os.path.splitext(file)

    if file_extension == ".png" or file_extension == ".jpg" or file_extension == ".webp" or file_extension == ".gif":
        print(f"{file_name} is image with {file_extension} extension")
        src_path = os.path.join('Sorter', file)
        dst_path = os.path.join('Images', file)
        shutil.move(src_path, dst_path)

    elif file_extension == ".mp4":
        print(f"{file_name} is video with {file_extension} extension")
        src_path = os.path.join('Sorter', file)
        dst_path = os.path.join('Videos', file)
        shutil.move(src_path, dst_path)

    elif file_extension == ".exe":
        print(f"{file_name} is program with {file_extension} extension")
        src_path = os.path.join('Sorter', file)
        dst_path = os.path.join('Programs', file)
        shutil.move(src_path, dst_path)

    else:
        src_path = os.path.join('Sorter', file)
        dst_path = os.path.join('Other', file)
        shutil.move(src_path, dst_path)