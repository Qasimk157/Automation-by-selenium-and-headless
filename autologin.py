import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager



# =================if we want to go headlessly==================================================
# =================if we want to go headlessly==================================================
# =================if we want to go headlessly==================================================
# =================if we want to go headlessly==================================================
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# browser = webdriver.Chrome('chromedriver', options=option)
#



 # to open beoswe link



# =================if we want to go with browser==================================================
# =================if we want to go with browser==================================================
# =================if we want to go with browser==================================================
# =================if we want to go with browser==================================================


browser = webdriver.Chrome()






browser.get(('https://www.amazon.fr/gp/product/B07TGQ194S'))
try:
    cookiesbutton = browser.find_element_by_id('a-autoid-0')
    cookiesbutton.click()
    print("cookies")
    try:
        print("entered in the first try class")
        cartbutton = browser.find_element_by_id('add-to-cart-button')
        cartbutton.click()
        print("cart")
        # time.sleep(5)
        # browser.refresh
        time.sleep(5)
        searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
        searchbutton.click()
        usernameStr = 'autobuy44@gmail.com'
        passwordStr = '12345678'
        username = browser.find_element_by_id('ap_email')
        username.send_keys(usernameStr)
        nextButton = browser.find_element_by_id('continue')
        nextButton.click()
        password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ap_password')))
        password.send_keys(passwordStr)
        signInButton = browser.find_element_by_id('auth-signin-button')
        signInButton.click()
        print("sleep")
        fullname = "s"
        firstname = browser.find_element_by_id('address-ui-widgets-enterAddressFullName')
        firstname.send_keys(fullname)
        adress = "Capitaine Jean Luc PICARD"
        adress1 = browser.find_element_by_id('address-ui-widgets-enterAddressLine1')
        adress1.send_keys(adress)
        adress2 = "52 RUE DES FLEURS"
        adress3 = browser.find_element_by_id('address-ui-widgets-enterAddressLine2')
        adress3.send_keys(adress2)
        city = "LIBOURNE"
        cityy = browser.find_element_by_id('address-ui-widgets-enterAddressCity')
        cityy.send_keys(city)
        state = "FRANCE"
        region = browser.find_element_by_id('address-ui-widgets-enterAddressStateOrRegion')
        region.send_keys(state)
        postal = "33500"
        code = browser.find_element_by_id('address-ui-widgets-enterAddressPostalCode')
        code.send_keys(postal)
        NUm = "330768990886"
        Phone = browser.find_element_by_id('address-ui-widgets-enterAddressPhoneNumber')
        Phone.send_keys(NUm)
        instruction = "Capitaine Jean Luc PICARD 52 RUE DES FLEURS"
        adresss = browser.find_element_by_id('address-ui-widgets-addr-details-address-instructions')
        adresss.send_keys(instruction)
        codenum = "33500"
        num = browser.find_element_by_id('address-ui-widgets-addr-details-gate-code')
        num.send_keys(codenum)
        chekbox = browser.find_element_by_id('address-ui-widgets-use-as-my-default')
        chekbox.click()
        print("chekbox")
        addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
        addadress.click()
        print("addadress button")
        time.sleep(5)
        browser.refresh
        addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
        addadress.click()
        print("addadress button")
        adress = browser.find_element_by_xpath("//*[@id='address-book-entry-0']/div[2]/span/a")
        adress.click()
        print("adress enter click")
        liversion = browser.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[1]/div[2]/div/span[1]")
        liversion.click()
        print("liversink ")
    except:
        browser.find_element_by_xpath("//*[@id='wishListMainButton-announce']").click()
        # searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
        # searchbutton.click()
        usernameStr = 'autobuy44@gmail.com'
        passwordStr = '12345678'
        username = browser.find_element_by_id('ap_email')
        username.send_keys(usernameStr)
        nextButton = browser.find_element_by_id('continue')
        nextButton.click()
        password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ap_password')))
        password.send_keys(passwordStr)
        signInButton = browser.find_element_by_id('auth-signin-button')
        signInButton.click()

        print("sleep")
        button = browser.find_element_by_id('add-to-cart-button')
        button.click()
        print("cart")
        # time.sleep(5)
        # browser.refresh
        time.sleep(5)
        searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
        searchbutton.click()
        # fullname = "s"
        # firstname = browser.find_element_by_id('address-ui-widgets-enterAddressFullName')
        # firstname.send_keys(fullname)
        adress = "Capitaine Jean Luc PICARD"
        adress1 = browser.find_element_by_id('address-ui-widgets-enterAddressLine1')
        adress1.send_keys(adress)
        adress2 = "52 RUE DES FLEURS"
        adress3 = browser.find_element_by_id('address-ui-widgets-enterAddressLine2')
        adress3.send_keys(adress2)
        city = "LIBOURNE"
        cityy = browser.find_element_by_id('address-ui-widgets-enterAddressCity')
        cityy.send_keys(city)
        state = "FRANCE"
        region = browser.find_element_by_id('address-ui-widgets-enterAddressStateOrRegion')
        region.send_keys(state)
        postal = "33500"
        code = browser.find_element_by_id('address-ui-widgets-enterAddressPostalCode')
        code.send_keys(postal)
        NUm = "330768990886"
        Phone = browser.find_element_by_id('address-ui-widgets-enterAddressPhoneNumber')
        Phone.send_keys(NUm)
        instruction = "Capitaine Jean Luc PICARD 52 RUE DES FLEURS"
        adresss = browser.find_element_by_id('address-ui-widgets-addr-details-address-instructions')
        adresss.send_keys(instruction)
        codenum = "33500"
        num = browser.find_element_by_id('address-ui-widgets-addr-details-gate-code')
        num.send_keys(codenum)
        chekbox = browser.find_element_by_id('address-ui-widgets-use-as-my-default')
        chekbox.click()
        print("chekbox")
        addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
        addadress.click()
        print("addadress button")
        time.sleep(5)
        browser.refresh
        addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
        addadress.click()
        print("addadress button")
        adress = browser.find_element_by_xpath("//*[@id='address-book-entry-0']/div[2]/span/a")
        adress.click()
        print("adress enter click")
        liversion = browser.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[1]/div[2]/div/span[1]")
        liversion.click()
        print("liversink ")

except:
    print("entered in main except")
    button = browser.find_element_by_id('add-to-cart-button')
    cartbutton.click()
    print("cart")
    # time.sleep(5)
    # browser.refresh
    time.sleep(5)
    searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
    searchbutton.click()
    usernameStr = 'autobuy44@gmail.com'
    passwordStr = '12345678'
    username = browser.find_element_by_id('ap_email')
    username.send_keys(usernameStr)
    nextButton = browser.find_element_by_id('continue')
    nextButton.click()
    password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'ap_password')))
    password.send_keys(passwordStr)
    signInButton = browser.find_element_by_id('auth-signin-button')
    signInButton.click()

    print("sleep")
    fullname = "s"
    firstname = browser.find_element_by_id('address-ui-widgets-enterAddressFullName')
    firstname.send_keys(fullname)
    adress = "Capitaine Jean Luc PICARD"
    adress1 = browser.find_element_by_id('address-ui-widgets-enterAddressLine1')
    adress1.send_keys(adress)
    adress2 = "52 RUE DES FLEURS"
    adress3 = browser.find_element_by_id('address-ui-widgets-enterAddressLine2')
    adress3.send_keys(adress2)
    city = "LIBOURNE"
    cityy = browser.find_element_by_id('address-ui-widgets-enterAddressCity')
    cityy.send_keys(city)
    state = "FRANCE"
    region = browser.find_element_by_id('address-ui-widgets-enterAddressStateOrRegion')
    region.send_keys(state)
    postal = "33500"
    code = browser.find_element_by_id('address-ui-widgets-enterAddressPostalCode')
    code.send_keys(postal)
    NUm = "330768990886"
    Phone = browser.find_element_by_id('address-ui-widgets-enterAddressPhoneNumber')
    Phone.send_keys(NUm)
    instruction = "Capitaine Jean Luc PICARD 52 RUE DES FLEURS"
    adresss = browser.find_element_by_id('address-ui-widgets-addr-details-address-instructions')
    adresss.send_keys(instruction)
    codenum = "33500"
    num = browser.find_element_by_id('address-ui-widgets-addr-details-gate-code')
    num.send_keys(codenum)
    chekbox = browser.find_element_by_id('address-ui-widgets-use-as-my-default')
    chekbox.click()
    print("chekbox")
    addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
    addadress.click()
    print("addadress button")
    time.sleep(5)
    browser.refresh
    addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
    addadress.click()
    print("addadress button")
    adress = browser.find_element_by_xpath("//*[@id='address-book-entry-0']/div[2]/span/a")
    adress.click()
    print("adress enter click")
    liversion = browser.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[1]/div[2]/div/span[1]")
    liversion.click()
    print("liversink ")




#
# class Myjobi():
#     def __init__(self):
#         print("class is initialized")
#     def amazon_job(self,ASIN,full_name,address1,address2,city,state,postal_code,phone):
#
#
#
#
# try:
#     cookiesbutton = browser.find_element_by_id('a-autoid-0')
#     cookiesbutton.click()
#     print("cookies")
#     try:
#         print("entered in the first try class")
#         cartbutton = browser.find_element_by_id('add-to-cart-button')
#         cartbutton.click()
#         print("cart")
#         # time.sleep(5)
#         # browser.refresh
#         time.sleep(5)
#         searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
#         searchbutton.click()
#         usernameStr = 'autobuy44@gmail.com'
#         passwordStr = '12345678'
#         username = browser.find_element_by_id('ap_email')
#         username.send_keys(usernameStr)
#         nextButton = browser.find_element_by_id('continue')
#         nextButton.click()
#         password = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, 'ap_password')))
#         password.send_keys(passwordStr)
#         signInButton = browser.find_element_by_id('auth-signin-button')
#         signInButton.click()
#         print("sleep")
#         fullname = "s"
#         firstname = browser.find_element_by_id('address-ui-widgets-enterAddressFullName')
#         firstname.send_keys(fullname)
#         adress = "Capitaine Jean Luc PICARD"
#         adress1 = browser.find_element_by_id('address-ui-widgets-enterAddressLine1')
#         adress1.send_keys(adress)
#         adress2 = "52 RUE DES FLEURS"
#         adress3 = browser.find_element_by_id('address-ui-widgets-enterAddressLine2')
#         adress3.send_keys(adress2)
#         city = "LIBOURNE"
#         cityy = browser.find_element_by_id('address-ui-widgets-enterAddressCity')
#         cityy.send_keys(city)
#         state = "FRANCE"
#         region = browser.find_element_by_id('address-ui-widgets-enterAddressStateOrRegion')
#         region.send_keys(state)
#         postal = "33500"
#         code = browser.find_element_by_id('address-ui-widgets-enterAddressPostalCode')
#         code.send_keys(postal)
#         NUm = "330768990886"
#         Phone = browser.find_element_by_id('address-ui-widgets-enterAddressPhoneNumber')
#         Phone.send_keys(NUm)
#         instruction = "Capitaine Jean Luc PICARD 52 RUE DES FLEURS"
#         adresss = browser.find_element_by_id('address-ui-widgets-addr-details-address-instructions')
#         adresss.send_keys(instruction)
#         codenum = "33500"
#         num = browser.find_element_by_id('address-ui-widgets-addr-details-gate-code')
#         num.send_keys(codenum)
#         chekbox = browser.find_element_by_id('address-ui-widgets-use-as-my-default')
#         chekbox.click()
#         print("chekbox")
#         addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
#         addadress.click()
#         print("addadress button")
#         time.sleep(5)
#         browser.refresh
#         addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
#         addadress.click()
#         print("addadress button")
#         adress = browser.find_element_by_xpath("//*[@id='address-book-entry-0']/div[2]/span/a")
#         adress.click()
#         print("adress enter click")
#         liversion = browser.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[1]/div[2]/div/span[1]")
#         liversion.click()
#         print("liversink ")
#     except:
#         browser.find_element_by_xpath("//*[@id='wishListMainButton-announce']").click()
#         # searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
#         # searchbutton.click()
#         usernameStr = 'autobuy44@gmail.com'
#         passwordStr = '12345678'
#         username = browser.find_element_by_id('ap_email')
#         username.send_keys(usernameStr)
#         nextButton = browser.find_element_by_id('continue')
#         nextButton.click()
#         password = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, 'ap_password')))
#         password.send_keys(passwordStr)
#         signInButton = browser.find_element_by_id('auth-signin-button')
#         signInButton.click()
#
#         print("sleep")
#         button = browser.find_element_by_id('add-to-cart-button')
#         button.click()
#         print("cart")
#         # time.sleep(5)
#         # browser.refresh
#         time.sleep(5)
#         searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
#         searchbutton.click()
#         # fullname = "s"
#         # firstname = browser.find_element_by_id('address-ui-widgets-enterAddressFullName')
#         # firstname.send_keys(fullname)
#         adress = "Capitaine Jean Luc PICARD"
#         adress1 = browser.find_element_by_id('address-ui-widgets-enterAddressLine1')
#         adress1.send_keys(adress)
#         adress2 = "52 RUE DES FLEURS"
#         adress3 = browser.find_element_by_id('address-ui-widgets-enterAddressLine2')
#         adress3.send_keys(adress2)
#         city = "LIBOURNE"
#         cityy = browser.find_element_by_id('address-ui-widgets-enterAddressCity')
#         cityy.send_keys(city)
#         state = "FRANCE"
#         region = browser.find_element_by_id('address-ui-widgets-enterAddressStateOrRegion')
#         region.send_keys(state)
#         postal = "33500"
#         code = browser.find_element_by_id('address-ui-widgets-enterAddressPostalCode')
#         code.send_keys(postal)
#         NUm = "330768990886"
#         Phone = browser.find_element_by_id('address-ui-widgets-enterAddressPhoneNumber')
#         Phone.send_keys(NUm)
#         instruction = "Capitaine Jean Luc PICARD 52 RUE DES FLEURS"
#         adresss = browser.find_element_by_id('address-ui-widgets-addr-details-address-instructions')
#         adresss.send_keys(instruction)
#         codenum = "33500"
#         num = browser.find_element_by_id('address-ui-widgets-addr-details-gate-code')
#         num.send_keys(codenum)
#         chekbox = browser.find_element_by_id('address-ui-widgets-use-as-my-default')
#         chekbox.click()
#         print("chekbox")
#         addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
#         addadress.click()
#         print("addadress button")
#         time.sleep(5)
#         browser.refresh
#         addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
#         addadress.click()
#         print("addadress button")
#         adress = browser.find_element_by_xpath("//*[@id='address-book-entry-0']/div[2]/span/a")
#         adress.click()
#         print("adress enter click")
#         liversion = browser.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[1]/div[2]/div/span[1]")
#         liversion.click()
#         print("liversink ")
#
# except:
#     print("entered in main except")
#     button = browser.find_element_by_id('add-to-cart-button')
#     cartbutton.click()
#     print("cart")
#     # time.sleep(5)
#     # browser.refresh
#     time.sleep(5)
#     searchbutton = browser.find_element_by_xpath("//*[@id='attach-sidesheet-checkout-button']/span/input")
#     searchbutton.click()
#     usernameStr = 'autobuy44@gmail.com'
#     passwordStr = '12345678'
#     username = browser.find_element_by_id('ap_email')
#     username.send_keys(usernameStr)
#     nextButton = browser.find_element_by_id('continue')
#     nextButton.click()
#     password = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.ID, 'ap_password')))
#     password.send_keys(passwordStr)
#     signInButton = browser.find_element_by_id('auth-signin-button')
#     signInButton.click()
#
#     print("sleep")
#     fullname = "s"
#     firstname = browser.find_element_by_id('address-ui-widgets-enterAddressFullName')
#     firstname.send_keys(fullname)
#     adress = "Capitaine Jean Luc PICARD"
#     adress1 = browser.find_element_by_id('address-ui-widgets-enterAddressLine1')
#     adress1.send_keys(adress)
#     adress2 = "52 RUE DES FLEURS"
#     adress3 = browser.find_element_by_id('address-ui-widgets-enterAddressLine2')
#     adress3.send_keys(adress2)
#     city = "LIBOURNE"
#     cityy = browser.find_element_by_id('address-ui-widgets-enterAddressCity')
#     cityy.send_keys(city)
#     state = "FRANCE"
#     region = browser.find_element_by_id('address-ui-widgets-enterAddressStateOrRegion')
#     region.send_keys(state)
#     postal = "33500"
#     code = browser.find_element_by_id('address-ui-widgets-enterAddressPostalCode')
#     code.send_keys(postal)
#     NUm = "330768990886"
#     Phone = browser.find_element_by_id('address-ui-widgets-enterAddressPhoneNumber')
#     Phone.send_keys(NUm)
#     instruction = "Capitaine Jean Luc PICARD 52 RUE DES FLEURS"
#     adresss = browser.find_element_by_id('address-ui-widgets-addr-details-address-instructions')
#     adresss.send_keys(instruction)
#     codenum = "33500"
#     num = browser.find_element_by_id('address-ui-widgets-addr-details-gate-code')
#     num.send_keys(codenum)
#     chekbox = browser.find_element_by_id('address-ui-widgets-use-as-my-default')
#     chekbox.click()
#     print("chekbox")
#     addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
#     addadress.click()
#     print("addadress button")
#     time.sleep(5)
#     browser.refresh
#     addadress = browser.find_element_by_id('address-ui-widgets-form-submit-button')
#     addadress.click()
#     print("addadress button")
#     adress = browser.find_element_by_xpath("//*[@id='address-book-entry-0']/div[2]/span/a")
#     adress.click()
#     print("adress enter click")
#     liversion = browser.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[1]/div[2]/div/span[1]")
#     liversion.click()
#     print("liversink ")
