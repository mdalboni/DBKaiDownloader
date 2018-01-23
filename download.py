from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import traceback
from time import sleep

#Primeiro loop    
def webcrawler(url):
    try:
        browser.get(url)
        WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.ID,"google-drive-2668-0")))               
        panel = browser.find_element_by_id("google-drive-2668-0")        
        mainitems = panel.find_elements_by_css_selector('li a')
        links = []
        for key in mainitems:
            links.append(key.get_attribute("href"))
        for i in range(len(links)):
            browser.get(links[i])

            WebDriverWait(browser,40).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/div/div[3]/div[2]/div[2]/div[2]/div"))) 
            #browser.get(browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[3]/div[2]/div[2]/div[2]/div").get_attribute("href"))
            browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[3]/div[2]/div[2]/div[2]/div").click()
            print(browser.current_url)
            WebDriverWait(browser,40).until(lambda d: len(d.window_handles)==2)               
           
            browser.switch_to_window(browser.window_handles[1])
            
            WebDriverWait(browser,40).until(EC.visibility_of_element_located((By.ID,"uc-download-link")))
            browser.find_element_by_id("uc-download-link").click()
            print("Baixando")           
            browser.close()
            browser.switch_to_window(browser.window_handles[0])            
            sleep(600)



    except TimeoutException:
        print('Sem conexao de internet, site fora do ar ou problemas no carregamento')     
    except Exception as ex:
        print('Algo errado não esta certo')
        print(traceback.format_exc())
        browser.quit()

fp = webdriver.FirefoxProfile('../../../.mozilla/firefox/y38jvbwv.selenium')

browser = webdriver.Firefox(fp)

url = 'https://www.anbient.com/Tv/Dragon-Ball-Kai-2014'
webcrawler(url)

