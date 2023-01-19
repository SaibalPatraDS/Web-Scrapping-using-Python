## import packages first and make sure to write the PATH of webdriver correctly

## create an instance of driver
driver = webdriver.Edge(PATH) ## am using Edge, chnage as per needed

# driver.get("Enter url of website")
driver.get("https://www.kaggle.com/")

## a pop up of kaggle website will open up

'''One can login into his/her website or can continue without login unless he/she wants to download data from website'''

print(driver.title) # print driver title to make sure code is runninh perfect

## accessing of kaggle website

search_box = driver.get_element(By.XPATH, '//*[@id="site-container"]/div/div[3]/div[2]/div[1]/div/input').click()

search_box = driver.find_element(By.XPATH, '//*[@id="site-container"]/div/div[5]/div[1]/div/div[1]/form/input')

search_string = input() ## enter whatever you want

driver.find_element(By.XPATH, '//*[@id="site-container"]/div/div[5]/div[1]/div/div[2]/button[1]').click() #.click() to access the search item

'''to search something else after one search, run the below code'''

## if we want to delete previous and search something new
search_box = driver.find_element(By.XPATH, '//*[@id="site-container"]/div/div[5]/div[1]/div/div[2]/button[2]').click() 
## exit the current page and return to home page

## again go through same process of searching
search_box = driver.find_element(By.XPATH, '//*[@id="site-container"]/div/div[3]/div[2]/div[1]/div/input').click()

search_box = driver.find_element(By.XPATH, '//*[@id="site-container"]/div/div[5]/div[1]/div/div[1]/form/input')

search_string_new = input()
search_box.send_keys(search_string_new)
driver.find_element(By.XPATH, '//*[@id="site-container"]/div/div[5]/div[1]/div/div[2]/button[1]').click()

