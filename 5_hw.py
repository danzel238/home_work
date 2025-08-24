from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def website_test():
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        

        elements = [
            ("username", By.ID, "user-name"),
            ("password", By.ID, "password"),
            ("submit button", By.ID, "login-button")
        ]
        
        all_found = True
        for name, by, value in elements:
            try:
                element = driver.find_element(by, value)
                print(f"✓ {name} найден")
            except:
                print(f"✗ {name} не найден")
                all_found = False
        
        if all_found:
            print("Все элементы найдены!")
        else:
            print("Не все элементы найдены")
            
        time.sleep(2)
        
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    website_test()
