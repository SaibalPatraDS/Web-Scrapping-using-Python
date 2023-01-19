import selenium
from selenium import webdriver
from selenium.driver.common.keys import Keys
from selenium.driver.common.by import By

PATH = 'path_of_webdriver'

driver = webdriver.Edge(PATH) #for ms edge
driver = webdriver.Chrome(PATH) #for chrome user
