
from lib2to3.pgen2 import driver
from time import process_time_ns

from selenium import webdriver

if __name__ == "__main__" :
    driver = webdriver.Chrome('./chromedriver')
    print("snapbot")