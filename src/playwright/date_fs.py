import os
from datetime import date

def get_file_path(filename):
    pwd = os.getcwd()

    today = date.today()

    year = str(today.year)
    month = str(today.month)
    day = str(today.day)

    dir_path = pwd + "/" + year + "/" + month + "/" + day + "/"
    print(dir_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    filename = "youtube"
    ext = ".txt"
    count = 0

    while True:
        if os.path.isfile(dir_path + filename + str(count) + ext):
            count += 1
        else:
            filename = filename + str(count)
            break

    return dir_path + filename + ext
