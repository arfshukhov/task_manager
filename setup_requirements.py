import os

requirements = ["peewee", "PySide6"]


cur_dir = os.getcwd()


if __name__ == "__main__":
    os.system("python -m ensurepip")
    os.system("python.exe -m pip install --upgrade pip")
    for i in requirements:
        os.system(f"python.exe -m pip install {i}")