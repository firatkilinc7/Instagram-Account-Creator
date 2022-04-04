from cgi import test
from selenium import webdriver
import random

def userNameChanger(fullName):

    replacedName = fullName.replace(" ", ".")
    randomNumber = random.randint(10000,99999)
    finalUserName = replacedName + str(randomNumber)
    return finalUserName
