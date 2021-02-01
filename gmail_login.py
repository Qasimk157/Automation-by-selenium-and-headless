from selenium import webdriver
import time

class Myjobi():
    def __init__(self):
        print("helllo assin")
        browser = webdriver.Chrome()
        browser.get(("https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2F%3F_encoding%3DUTF8%26ref_%3Dnav_em_hd_re_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&ref_%3Dnav_em_hd_clc_signin"))
        # time.sleep(3)
        # browser.refresh()
        browser.find_element_by_xpath("//*[@id='ap_email']").send_keys("qasim@gmail.com")
        browser.find_element_by_id("continue").click()
        time.sleep(5)
        # browser.refresh()
        browser.find_element_by_name("password").send_keys("Official1998")
        time.sleep(1)
        browser.find_element_by_id("auth-signin-button").click()
        time.sleep(1)
        browser.refresh()



# browser = webdriver.Chrome()
# browser.get(("https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2F%3F_encoding%3DUTF8%26ref_%3Dnav_em_hd_re_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&ref_%3Dnav_em_hd_clc_signin"))
# press = input("press q")
# # if press == 'q':
# time.sleep(3)
# browser.refresh()
# browser.find_element_by_xpath("//*[@id='ap_email']").send_keys("mannanmaan1425@gmail.com")
# browser.find_element_by_id("continue").click()
# time.sleep(5)
# # browser.refresh()
# browser.find_element_by_name("password").send_keys("Official1998")
# time.sleep(1)
# browser.find_element_by_id("auth-signin-button").click()
# time.sleep(1)
# browser.refresh()
#
#
#
#
#
# browser.get(('https://www.amazon.fr/gp/product/B0001IWKG8'))
# try :
#
#     accept_cookies = browser.find_element_by_id("sp-cc-accept")
#     accept_cookies.click()
#     time.sleep(5)
#     browser.refresh()
#     cartbutton = browser.find_element_by_id("add-to-cart-button")
#     cartbutton.click()
#     time.sleep(3)
# except:
#     cartbutton = browser.find_element_by_id("add-to-cart-button")
#     cartbutton.click()
#     time.sleep(3)
# browser.find_element_by_xpath("//*[@id='hlb-ptc-btn-native']").click()
#
#
#
# time.sleep(5)
# browser.refresh()
# placeorder = browser.find_element_by_id("hlb-ptc-btn")
# placeorder.click()
