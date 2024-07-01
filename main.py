import time

## - pip install --upgrade webdriver_manager (update the webdriver manager)

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get('https://www.facebook.com/')
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
# driver.find_element(By.NAME,"firstname").send_keys('sachin kumar')
# driver.find_element(By.NAME,"lastname").send_keys('chejara')
# driver.find_element(By.NAME,"reg_email__").send_keys('skc@223424')
# driver.find_element(By.NAME,"reg_passwd__").send_keys(3243443534534)
# d=Select(driver.find_element(By.ID,"day"))
# d.select_by_value('4')
# m=Select(driver.find_element(By.ID,"month"))
# m.select_by_visible_text('Aug')
# y=Select(driver.find_element(By.ID,"year"))
# y.select_by_index(6)
# driver.find_element(By.XPATH,"//input[@value='2']").click()
# driver.find_element(By.XPATH,"(//button[text()='Sign Up'])[1]").click()
# time.sleep(3)


# driver.get('https://sourcebuddy.stage02.obdemo.com/')
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.find_element(By.XPATH, "//*[text()='Register']").click()
#
# driver.find_element(By.NAME, "name").send_keys('rakesh')
# driver.find_element(By.NAME, "email").send_keys('Rakesh01234@yopmail.com')
# driver.find_element(By.NAME, "phone_number").send_keys(9876543210)
# driver.find_element(By.NAME, "password").send_keys('Bb@12345')
# driver.find_element(By.NAME, "confirm_password").send_keys('Bb@12345')
# button = driver.find_element(By.XPATH, "//*[text()='Sign Up']")
# driver.execute_script("arguments[0].click();", button)

# driver.get("https://yopmail.com/")
# driver.refresh()
# driver.implicitly_wait(10)
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@placeholder='Enter your inbox here']").send_keys("Rakesh01234")
# driver.find_element(By.XPATH, "//*[@id='refreshbut']/button").click()
# driver.switch_to.frame( 'ifmail')
# time.sleep(2)
# driver.find_element(By.XPATH,"//div//a[@href = 'https://sourcebuddy.stage02.obdemo.com/verify-email/verify/V25XOXViSGUzTjlodlhlMjlXQjU3cFVhWmRTeWdtQmEwSGFSaERkNlhERVgyN01HVERIdFR1clBQOXlmOGVLbg==']").click()
# time.sleep(5)
# driver.get_screenshot_as_file('Screenshot1.png')


# driver.get("https://sourcebuddy.stage02.obdemo.com/login")
# driver.find_element(By.NAME,'email').send_keys("Rakesh01234@yopmail.com")
# driver.find_element(By.NAME,'password').send_keys("Bb@12345")
# driver.find_element(By.XPATH,"//button[text()='Login']").click()
# time.sleep(5)

# driver.get("https://sourcebuddy.stage02.obdemo.com/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.find_element(By.XPATH,"//*[text()='Login Now']").click()
# driver.find_element(By.XPATH,"//*[text()='Forgot Password']").click()
# driver.find_element(By.NAME,"email").send_keys("sourcebuddy@yopmail.com")
# driver.find_element(By.XPATH,"//*[text()='Submit']").click()
# time.sleep(3)
# driver.get_screenshot_as_file('screenshots.png')

# driver.get("https://yopmail.com/")
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "//input[@placeholder='Enter your inbox here']").send_keys("biboqe@yopmail.com")
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='refreshbut']/button").click()
# driver.switch_to.frame('ifmail')
# A = ActionChains(driver)
# A.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
#
# # driver.find_element(By.XPATH, "(//tbody//a)[2]").click()
# time.sleep(3)

# driver.find_element(By.NAME, "password").send_keys("System@12345")
# driver.find_element(By.NAME, "confirm_password").send_keys("System@12345")
# driver.find_element(By.XPATH, "//*[text()='Reset Password']")
# time.sleep(3)

# driver.get("https://sourcebuddy.stage02.obdemo.com/")
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "//*[text()='Login Now']").click()
# driver.find_element(By.NAME, 'email').clear()
# driver.find_element(By.NAME, 'email').send_keys("owebest1@Yopmail.com")
# driver.find_element(By.NAME, 'password').clear()
# driver.find_element(By.NAME, 'password').send_keys("System@123")
# driver.find_element(By.XPATH, "//button[@id='submitButtonClick']").click()
# time.sleep(5)
# # driver.find_element(By.XPATH,"(//div[@id='sideMenu']//a)[5]").click()
# element = driver.find_element(By.XPATH,"(//div[@id='sideMenu']//a)[5]")
# driver.execute_script("arguments[0].click();", element)
# time.sleep(5)
# driver.get('https://sourcebuddy.stage02.obdemo.com/')
# element = driver.find_element(By.LINK_TEXT, 'Help Center')
# driver.execute_script("arguments[0].click();", element)
# driver.find_element(By.LINK_TEXT,'Home').click()
# time.sleep(3)

##---save screen_shot---> {{driver.save_screenshot(".\\Screenshot"+"test_xyz.png")}} ( ".\\ " -> present current project directory)


# driver.get('https://sourcebuddy.stage02.obdemo.com/adminpnlx')
# driver.implicitly_wait(20)
# driver.find_element(By.XPATH, "//input[@name='email']").send_keys('panel@mailinator.com')
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys('THV82FTG@123')
# driver.find_element(By.XPATH, "//input[@value='Login']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "(//*[text()='Users Management'])[1]").click()
# driver.find_element(By.XPATH, "//*[text()='Customers']").click()
# driver.find_element(By.XPATH, "//a[@class='btn btn-primary dropdown-toggle mr-2']").click()
# driver.find_element(By.XPATH, "//input[@name='email']").send_keys('mepexali@Yopmail.com')
# driver.find_element(By.XPATH, "//button[@id='kt_search']").click()
# driver.find_element(By.XPATH, "//a[@data-original-title='View']").click()
# time.sleep(2)

# driver.find_element(By.XPATH, "(//a[@data-original-title='View'])[1]").click()
# time.sleep(3)

# driver.find_element(By.XPATH, "//*[@class='btn btn-primary dropdown-toggle mr-2']").click()

# A = Select(driver.find_element(By.XPATH, "//select[@name='per_page']"))
# A.select_by_value('100')
# Users = driver.find_elements(By.XPATH, "//table[@id='taskTable']//tbody/tr")
# for User in Users:
#     if User.text == 'rakesh':
#         driver.find_element(By.XPATH, "//a[@data-original-title='View']").click()
# time.sleep(3)





# Users = driver.find_elements(By.XPATH, "//table[@id='taskTable']//tbody/tr/td")
# Newlist = []
# for user in Users:
#     name = user.text
#     Newlist.append(name)
# new = Newlist.index("Sujata")
# details = Newlist[new: new + 5]
# print(details)
# driver.find_element(By.XPATH, "(//a[@data-original-title='View'])").click()
# time.sleep(3)


# driver.get('https://sourcebuddy.stage02.obdemo.com/')
# driver.implicitly_wait(10)
# driver.maximize_window()
# element = driver.find_element(By.LINK_TEXT, "Frequently asked questions")
# driver.execute_script("arguments[0].click();", element)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0,0)")
# time.sleep(2)
# Faqs = driver.find_elements(By.XPATH, "//section[@class='section_padding faq_wrapper']//h2")

# for faq in Faqs:
#     if faq.text == 'Where can I subscribe to your newsletter?':
#         faq.click()

# time.sleep(2)
# Ans = driver.find_elements(By.XPATH, "//div[starts-with(@id,'collapseOne')]")
# for ans in Ans:
#     if ans.text == 'From the footer section on home page':
#         print(ans.text)

# driver.get('https://sourcebuddy.stage02.obdemo.com/adminpnlx')
# driver.find_element(By.XPATH, "//input[@name='email']").send_keys('panel@mailinator.com')
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys('THV82FTG@123')
# driver.find_element(By.XPATH, "//input[@value='Login']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "(//*[text()='System Management'])[1]").click()
# driver.find_element(By.XPATH, '''//span[text()="Faq's"]''').click()
# driver.find_element(By.XPATH, "(//*[text()='Users Management'])[1]").click()
# driver.find_element(By.XPATH, "//*[text()='Customers']").click()

# User_List = []
# while True:
#  user_elements = driver.find_elements(By.XPATH, "//table[@id='taskTable']//tbody/tr")
#  # print(user_elements)
#  for user in user_elements:
#         user_email = user.find_element(By.XPATH, ".//td[2]")
#         email = user_email.text
#         User_List.append(email)
#         # print(User_List)
#         if email == 'sourcebuddy@yopmail.com':
#             view_button = user.find_element(By.XPATH, ".//a[@data-original-title = 'View']")
#             view_button.click()
#             time.sleep(2)
#             print('test case is complete')

#  next_button_element = None
#  try:
#      next_button_element = driver.find_element(By.XPATH, "(//a[@class= 'page-link'])[6]")
#  except NoSuchElementException:
#      pass
#  if next_button_element and 'sourcebuddy@yopmail.com' not in User_List:
#      next_button_element.click()
#      time.sleep(2)
#  else:
#      print('this email is not exists')
#      break


# --> for upolad any file
# driver.get('https://sourcebuddy.stage02.obdemo.com/adminpnlx')
# driver.find_element(By.XPATH, "//input[@name='email']").send_keys('panel@mailinator.com')
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys('THV82FTG@123')
# driver.find_element(By.XPATH, "//input[@value='Login']").click()
# driver.find_element(By.XPATH, "//span[text() = 'Product Management']").click()
# driver.find_element(By.XPATH, "//*[text() = 'Product']").click()
# driver.find_element(By.XPATH, "//*[text() = ' Add New  Product']").click()
# select = Select(driver.find_element(By.XPATH, "//select[@name = 'product_type_id']"))
# select.select_by_visible_text('Packaging')
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@accept='image/*']").send_keys("C://Users/pc/Desktop/sourcebuddy05-04-2023/SB Image/amino_acid-1b0e0369462e47c6aa53a45d404715ae.jpg")
# time.sleep(1)
# iframe1 = driver.find_element(By.XPATH, "(//iframe[@class='cke_wysiwyg_frame cke_reset'])[1]")
# driver.switch_to.frame(iframe1)
# time.sleep(1)
# driver.find_element(By.XPATH, "(//html[@dir='ltr']//child::body)[1]").send_keys('testing')
# # driver.switch_to.parent_frame()
# driver.switch_to.default_content()
# time.sleep(2)

# iframe2 = driver.find_element(By.XPATH, "(//iframe[@class='cke_wysiwyg_frame cke_reset'])[2]")
# driver.switch_to.frame(iframe2)
# driver.find_element(By.XPATH, "(//html[@dir='ltr']//child::body)[2]").send_keys('sdgdzdvz')

# time.sleep(2)


# ---> Date and Time formate
# now = datetime.now()
# dt_string = now.strftime("%d%m%Y%H%M%S")
# USERID = "TEST" + dt_string
# EMAIL_EXP = "Test" + dt_string + "@yopmail.com"
# print(EMAIL_EXP)
# day = now.strftime("%d")
# print(day)


# list = [1, 2, 3, 4, 5, 6, 7]
# for l in list:
#     print(l, end= " ")

# list2 = [x+5 for x in range(99)]
# print(list2)

# list = []
# for a in range(1, 10):
#     list.append(['sachin', 'kumar', 'chejara'])
# print(list)


# driver.find_element(By.XPATH, "//input[@id = 'search-bar']").send_keys('New testing product')
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[@class= 'search-btn']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//a[text()= 'Add to basket ']").click()
# time.sleep(4)
# Source_Document = driver.find_elements(By.XPATH, "//div[@class='request-docs']/div//label")
# Checkboxes = driver.find_elements(By.XPATH, "//div[@class='form-group']//input[@type='checkbox']")
# for Document in Source_Document:
#     # if Document.text == 'MSDS' or Document.text == 'Product Specification' or Document.text == 'Flow Charts':
#         Document.click()

# time.sleep(5)




# import numpy

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# A = numpy.mean(speed)
# print(A)

# B = numpy.mode(speed)
# print(B)

# C = numpy.median(speed)
# prin