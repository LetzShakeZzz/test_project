from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    info = file.namelist()
    print(len(info))
