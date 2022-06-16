
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.request import urlopen
import urllib.request
import requests
import urllib.request
import urllib
import warnings 
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def main()
        delay = 180
        wait = 1.5
        dela = 0
        d = webdriver.Chrome()
        # passw = input(введи фразу ) 
        d.get('')
        WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, 'htmlbodydivdiv[1]divdivdiv[4]div[1]button'))).click()
        WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, 'htmlbodydivdivdivheaderdivdivnav[2]div[3]a[3]'))).click()
  

        
        login = WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, '[@id=login_login_or_email]')))
        login.send_keys('')

        password = WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, '[@id=login_password]')))
        password.send_keys('')
        
        WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, 'htmlbodydivdiv[1]divdivdiv[2]formdiv[4]button'))).click()
        
        WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, 'htmlbodydivdiv[1]divdiv[1]a'))).click()
        

        WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, 'htmlbodydivdivdivmaindivdivdiv[2]divdivdiv[3]div[1]divafooter'))).click() #model
       
        k=0
        
        site = d.current_url
        for K in range(10) 
            users = open(users.txt, w)
            i= 0
            d.get(site)
            for K in range(3) 
                
                
               
                WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, '[@id=app]divdivdivdiv[2]divdiv[2]divdiv[2]div[1]div[3]'))).click() #user list
              
                WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, '[@id=app]divdivdivdiv[2]divdiv[2]divdiv[2]div[2]div[2]div[1]')))

                html_source = d.page_source
                soup = BeautifulSoup(html_source, 'html.parser')
            
                




             
                for usertag in soup.find_all('div', {'class' 'users-list'  })
                    for goldtag in usertag.find_all('div', {'class' 'colored gold username' })
                        users.write('сайт')
                        users.write(goldtag.text)
                        users.write('n')
                        k = k+1

            

                for usertag in soup.find_all('div', {'class' 'users-list'  })
                    for greentag in usertag.find_all('div', {'class' 'colored green username' })
                        users.write('сайт')
                        users.write(greentag.text)
                        users.write('n')
                        k= k +1
                        
                     
                d.find_element_by_css_selector('#app  div  div  div  div.header-sub.view-cam-header-sub  div  nav.nav-right  div.next-model-button  span').click() #next model button 
                WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, [contains(text(), 'Похожие стримеры')])))

                if k 50
                        site = d.current_url
                        
                        break
           
            users.close()
            uniqlines = set(open('users.txt','r', encoding='utf-8').readlines())
            gotovo = open('users.txt','w', encoding='utf-8').writelines(set(uniqlines))
            users.close()



            
            k = 0
            with open(users.txt) as f
                for line in f
                    url = line.strip()  # to remove the trailing n
                    
                    d.get(url)

                   
                    try
                                    WebDriverWait(d, delay).until(EC.presence_of_element_located((By.XPATH, 'htmlbodydivdivdivmaindivdivdivdivdivdivdivdivdiv[2]div[1]')))
                                    
                                    d.find_element_by_xpath([contains(text(), 'Добавить в друзья')]).click() #add to freind

                                    
                                        
                                
                    except(NoSuchElementException, TimeoutException)
                                    pass



            users.close()  




                               
        d.get('stripchat.comfriends')
        WebDriverWait(d, 180).until(EC.presence_of_element_located((By.CSS_SELECTOR,#app  div  div  div  div.editable-list.page-block.user-friends  div.scroll-bar-container.ps  div.list-items-container)))

                                
        html_source = d.page_source

        soup = BeautifulSoup(html_source, 'html.parser')

        online = open(online.txt, w)
            
        try
            WebDriverWait(d, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR,.cookies-reminder  divnth-child(2)))).click()
        except (TimeoutException)
             pass
        for k in range(321312321)
                WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,#app  div  div  div  div.editable-list.page-block.user-friends  div.scroll-bar-container.ps  div.list-items-container  divnth-child(1)  a  span.caption  div)))


                html_source = d.page_source
                
                soup = BeautifulSoup(html_source, 'html.parser')
                for a in soup.find_all('a')
                    for span in a.find_all('span')
                        for div in span.find_all('div')
                            for span2 in div.find_all('span')
                                
                                if span2.find_all('span', {'class' 'user-status-icon online' })
                                     online.write('ссылка на сайт')
                                     online.write(a.get('href'))
                                     online.write('n')

                
                try
                    WebDriverWait(d, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,#app  div  div  div  div.pagination  a.page-button.page-button-next))).click()
                    time.sleep(1)
                except (NoSuchElementException,ElementNotInteractableException)
                     break
                     pass



    
        online.close()
        uniqlines = set(open('online.txt','r', encoding='utf-8').readlines())
        gotovo = open('online.txt','w', encoding='utf-8').writelines(set(uniqlines))
        online.close()
        with open(online.txt) as f
                 
                 for line in f
                     url = line.strip()  # to remove the trailing n
                     print(Getting %s % url)
                     d.get(url)

                            
                     try
                         WebDriverWait(d, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app  div  div  div  div  div  div.column.xs-12.s-12.m-12.l-7.xl-7.xxl-7  div  div  div.info  div.action-buttons  div  a'))).click() 
                         send = WebDriverWait(d, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, #app  div  div  div  div  div.private-messages.span-7  div  div.composer  div  div.textarea-container  div.textarea-wrapper  textarea))) 
                         send.send_keys('Захоид ко мне!!')
                         WebDriverWait(d, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, #private_messages_composer_uid_1))).click()

                                                
                                        
                     except(NoSuchElementException, TimeoutException)
                         d.refresh()
                                           


        
   
        online.close()                            


                            
                      
                    
                  
            
if __name__ == __main__
    main()
