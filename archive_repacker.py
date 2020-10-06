import os
import zipfile
import shutil

data_path = 'C:\\Users\\UnSi\\Downloads\\zip_repacker\\data'
input_path = 'C:\\Users\\UnSi\\Downloads\\zip_repacker\\in'
output_path = 'C:\\Users\\UnSi\\Downloads\\zip_repacker\\out'


def unpack(archive_name):
    with zipfile.ZipFile(os.path.join(input_path, f'{archive_name}.zip')) as archive:
        archive.extractall(data_path)


def pack(new_archive_name):
    # create archive
    with zipfile.ZipFile(os.path.join(output_path, f'{new_archive_name}.zip'), "w") as archive:
        # pack_logic (all files in data_folder will be packed in archive)
        for folder, sub_folders, files in os.walk(data_path):
            for file in files:
                archive.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), data_path),
                              compress_type=zipfile.ZIP_DEFLATED)

    # remove folder after packing
    shutil.rmtree(data_path)


if __name__ == '__main__':
    pack('test')
    # unpack('unsi')
    pass


