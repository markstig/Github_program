# Here we use chrome, not using Firefox, this didn't follow the lession strictly, may case some problems. But we just practice the commands here.

# pip install selenium
# python3 -m pip install selenium

from selenium import webdriver

browser = webdriver.Chrome('/users/markli/Downloads/chromedriver')  # download the chromedriver, and here we need tha path

browser.get('https://www.baidu.com')

selector = browser.find_element_by_css_selector('#kw')

selector.send_keys('Markli')
selector.submit() # use the submit, there is not need to click

# Manage the brower itself
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()


# copy  the  text from the website
browser.get('https://automatetheboringstuff.com')
targettext = browser.find_element_by_css_selector('p:nth-child(6)')
targetall = browser.find_element_by_css_selector('html')  # contain the entire webpage
print(targettext.text)
print(targetall.text)

browser.quit()

