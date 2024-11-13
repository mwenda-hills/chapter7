import os


def run(**args):
    print("[*] In dirlister module.")  # Updated print statement for Python 3
    files = os.listdir(".")
    return str(files)
