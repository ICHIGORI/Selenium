import os


BASE_PATH, this_file = os.path.split(os.path.abspath(__file__))


if __name__ == "__main__":
    print(BASE_PATH, this_file)
