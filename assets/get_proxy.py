from selenium import webdriver
from selenium.webdriver.common.by import By
import linecache, time

def getProxy(line_proxy):
    print("Do you have proxys in ./assets/proxys/proxy.txt ?")
    haveProxy = int(input("\n1-> YES\n2-> NO\n"))

    if(haveProxy == 2):
        
        proxyEngine = webdriver.Chrome()
        proxyEngine.get("https://spys.one/en/https-ssl-proxy/")
        time.sleep(999999)
        proxyEngine.find_element(By.XPATH, value="/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/font/select[1]").click()
        proxyEngine.find_element(By.XPATH, value="/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/font/select[1]/option[2]").click()
        
        proxyEngine.execute_script("""
                var deleteAds = document.getElementsByClassName('adsbygoogle-noablate');   
                for(var i = 0; i < deleteAds.length; i++){
                        deleteAds[i].style.display = "none";
                    }
            """)
        
        for i in range(3, 202):
            try:
                temp = "tr[" + str(i) + "]"
                proxyXpath = "/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[3]/td[1]/font"
                replacedXpath = proxyXpath.replace("tr[3]", temp)
                proxys = proxyEngine.find_element(By.XPATH, value=replacedXpath).text
                open("./assets/proxys/proxy.txt", "a").write(proxys + "\n")
                
            except:
                break
        
        print(str(i-3) + " proxy saved in ./assets/proxys/proxy.txt")
    
    proxy = linecache.getline('./assets/proxys/proxy.txt', line_proxy)
    return proxy