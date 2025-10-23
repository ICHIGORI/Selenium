import os


BASE_PATH, this_file = os.path.split(os.path.abspath(__file__))
CHROMEDRIVER_PATH = os.path.join(BASE_PATH, "driver", "chromedriver.exe")
CONFIG_PATH = os.path.join(BASE_PATH, "utils", "CONFIG")

if __name__ == "__main__":
    print(BASE_PATH, this_file)
