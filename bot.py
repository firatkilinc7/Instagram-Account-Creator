from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pyperclip, time, sys
print("*--**--**--* |-Revised by HekiR-| *--**--**--*")
total_acc = int(input("How much you want to create acc: "))
password = input("Create pass for acc: ")
engine = webdriver.Chrome()
engine.get("https://smailpro.com/advanced")
time.sleep(3)

all_iframes = engine.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    print("Ad Found, Ads Blocking...\n")
    engine.execute_script("""
        var deleteAds = document.getElementsByClassName('adsbygoogle-noablate');   
        for(var i = 0; i < deleteAds.length; i++){
            deleteAds[i].style.display = "none";
            }
    """)

time.sleep(1)
for i in range(1,total_acc + 1):
    print("Creating", str(i+1) + ". acc")
    engine.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[1]/div[3]/div[2]/div[1]/input").click();#click "Generate temporary email"
    time.sleep(0.5)
    engine.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[1]/div[3]/div[2]/div[2]/div/ul[2]/li/div/div").click();#click "random@storegmail.com"
    time.sleep(0.5)
    engine.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[1]/div[2]/div[1]/button[2]").click();#click green button
    time.sleep(5)
    engine.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[2]/div[1]/div[1]/button").click();#click for copy mail
    time.sleep(0.5)
    mail = pyperclip.paste()
    fullname = "Anastasia Lukalias"
    username = mail.rpartition('@')[0]
    chrome = webdriver.Chrome()
    chrome.get("https://www.instagram.com/accounts/emailsignup/")
    time.sleep(3)
    try:
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[3]/div/label/input").send_keys(mail)
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[4]/div/label/input").send_keys(fullname)
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[5]/div/label/input").send_keys(username)
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[6]/div/label/input").send_keys(password)
        time.sleep(2)
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button").click()#click register
        time.sleep(2)
    except:
        print("Error, restart...")
        chrome.close()
        chrome.quit()
        continue

    birthday_xpath = "/html/body/div[1]/section/main/div/div/div[1]/div/span"
    try:
        chrome.find_element_by_xpath(birthday_xpath)
    except NoSuchElementException:
        break
    else:
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]").click()#click choose years
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[28]").click()#click year '1994'
        time.sleep(1)
        chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[28]").click()#click next in year page

    time.sleep(2)
    time.sleep(2)
    mailContent = ""
    def WaitingMail():
        global mailContent
        print("Waiting For Mail...")
        try:
            chrome.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[2]/div[2]/div[1]/button").click()
            time.sleep(2)
            mailContent = engine.find_elements_by_xpath("/html/body/div[3]/main/div[2]/div[2]/div[2]/div[2]/div/div[1]/span")[0]
        except:
            WaitingMail()
    WaitingMail()

    if str(mailContent.text).endswith("is your Instagram code"):
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input").send_keys(
            str(mailContent.text)[0:6])
        time.sleep(2)
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button").click()
        time.sleep(2)
        print(username + ":" + password + "\n")
        engine.refresh()
        time.sleep(2)
        open("acc.txt", "a").write(username + ":" + password + "\n")
        chrome.close()
        chrome.quit()
print("Accounts created and saved acc.txt")
engine.close()
engine.quit()
sys.exit()

