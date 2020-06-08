from selenium import webdriver
import sched, time

s = sched.scheduler(time.time, time.sleep)
link = 'http://superakki.deer.is/'

def superaki():
    s.enter(100, 1, superaki)
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        number_of_email = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[31]/td[2]')
        number_of_email = number_of_email.text
        number_two = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[28]/td[2]')
        number_two = number_two.text
        time.sleep(1)
        if number_of_email == '0':
            f = 0
        if number_of_email != '0':
            print('Пора закупить почты')
        if number_two == '0':
            f = 0
        if number_two != '0':
            print('Можно закупаться')
    finally:
        time.sleep(1)
        browser.quit()

superaki()
s.run()