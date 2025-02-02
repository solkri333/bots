from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.common.action_chains import ActionChains # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time
import logging
logging.basicConfig(
    filename='app.log',      # Name of the log file
    level=logging.DEBUG,     # Minimum level of messages to capture (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format with timestamp, level, and message
)
import random


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/133.0.6943.33 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/133.0.6943.33 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (X11; Linux i686; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/134.0 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Android 15; Mobile; rv:134.0) Gecko/134.0 Firefox/134.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/131.0.2903.86",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/131.0.2903.86",
    "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36 EdgA/131.0.2903.87",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36 EdgA/131.0.2903.87",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36 EdgA/131.0.2903.87",
    "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36 EdgA/131.0.2903.87",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/131.2903.92 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/116.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/116.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/116.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/116.0.0.0",
    "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36 OPR/76.2.4027.73374",
    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36 OPR/76.2.4027.73374",
    "Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 Mobile Safari/537.36 OPR/76.2.4027.73374",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/24.12.0.1846 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/24.12.0.1846 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 YaBrowser/25.2.1.527 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 YaBrowser/25.2.1.527 Mobile/15E148 Safari/605.1",
    "Mozilla/5.0 (Linux; arm_64; Android 15; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.164 YaBrowser/24.12.5.28 Mobile Safari/537.36"
]

def click(driver):
    try:
        # Get the browser window size (width and height)
        window_width = driver.execute_script("return window.innerWidth")
        window_height = driver.execute_script("return window.innerHeight")

        # Calculate the center of the window
        center_x = window_width / 2
        center_y = window_height / 2

        driver.execute_script(f"document.elementFromPoint({center_x}, {center_y}).click();")
    except Exception as e:
        logging.error(f"{str(e)} Cannot click")
def tab(driver):
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[0])
    # current_url = driver.current_url
    # print("The current URL is:", current_url)

def arrange(driver):
    click(driver)
    tab(driver)

def close(driver):
    window_handles = driver.window_handles
    # Loop through all window handles and close all except the first one
    for handle in window_handles[1:]:  # Start from index 1 to exclude the first tab
        driver.switch_to.window(handle)  # Switch to the tab
        time.sleep(1)
        driver.close()  # Close the tab
    arrange(driver)

def clickbot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Optional: Remove if you want the UI to appear
    # chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    # chrome_options.add_argument('referer=https://www.example.com')
    # chrome_options.add_argument('origin=https://www.example.com')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("accept-language=en-US,en;q=0.9")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ["enable-automation", 'enable-logging'])
    # chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument("--window-size=1366,768")
    chrome_options.add_argument("--lang=en-US,en;q=0.9")
    chrome_options.add_argument("--disable-notifications")
    # chrome_options.add_argument(f"--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    # chrome_options.add_argument(f"--lang={random_language}")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('prefs', {
        'profile.default_content_setting_values.notifications': 2
    })
    user_agent=random.choice(user_agents)
    chrome_options.add_argument(f"--user-agent={user_agent}")
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.set_page_load_timeout(20)
        for i in range(8):
            logging.info("Entered loop")
            # time.sleep(5)
            # Navigate to the page
            if(i==0): 
                try: 
                    driver.get(url) 
                except: 
                    logging.info("timeout")
            else: 
                # if(random.randint(0,50)<=5): continue
                close(driver)
                try:
                    driver.refresh()
                except: logging.info("timeout") 

            # Wait for the iframe to load
            driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to be ready

            # Get all iframe elements on the page
            logging.info("Here")
            iframe_elements = driver.find_elements(By.TAG_NAME, 'iframe')
            iframe_elements.reverse()
            logging.info(len(iframe_elements))
            # Scroll to the bottom of the page (similar to Playwright's scrollTo)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

            # Loop through each iframe and interact with the div inside
            arrange(driver)
            # browser_logs = driver.get_log('browser')
            # logging.info(f"Browser logs: {browser_logs}")
            # html_source = driver.page_source
            # print(html_source)
            for iframe_element in iframe_elements:
                arrange(driver)
                time.sleep(5)
                try:
                    if random.randint(1,10)<10:
                        try:
                            native_ad_div = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.ID, "native-ad-container"))
                            )

                            # Click the div
                            native_ad_div.click()
                            logging.debug("Clicked the div with id 'native-ad-container'.")

                            tab(driver)

                            # Wait for the second <a> element (the one you want to click) to be clickable
                            # Modify this to the appropriate selector for the <a> element you want to click
                            WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.TAG_NAME, "a"))
                                )
                            links = driver.find_elements(By.TAG_NAME, "a")
                            
                            for link in links:
                                link.click()
                            logging.debug("Clicked the second <a> link.")
                        except:
                            logging.debug("Ad not clickable")
                    time.sleep(2)
                    arrange(driver)
                    if random.randint(1,10)<8: continue
                    # Switch to the iframe
                    driver.switch_to.frame(iframe_element)

                    # Wait for the div to be available inside the iframe
                    driver.implicitly_wait(5)  # Implicit wait to wait for the div to appear

                    # Find the first div inside the iframe and click it
                    div = driver.find_element(By.TAG_NAME, 'div')
                    location = div.location  # Returns {'x': x_position, 'y': y_position}
                    size = div.size  # Returns {'width': width, 'height': height}
                    center_x = location['x'] + size['width'] / 2
                    center_y = location['y'] + size['height'] / 2
                    try:
                        driver.execute_script(f"document.elementFromPoint({center_x}, {center_y}).click();")
                    except:
                        logging.error("Error while trying to click at center")
                    try:
                        action = ActionChains(driver)
                        action.move_to_element_with_offset(div, size['width'] / 2, size['height'] / 2).click().perform()
                    except:
                        logging.error("Error while using Actionchain to click at the center")
                    div.click()

                    logging.info('Clicked the div inside the iframe!')
                except Exception as e:
                    try:
                        action=ActionChains(driver)
                        action.move_by_offset(1980 / 2, 720 / 2).click().perform()
                    except:
                        logging.error("Error")
                    logging.error(f'Error: {str(e)}. Div not found in this iframe, moving to the next one...')
                finally:
                    driver.switch_to.default_content()  # Switch back to the main page before moving to the next iframe
                    tab(driver)

    finally:
        # Close the browser after operations
        time.sleep(2)  # Pause for a few seconds before closing to observe the actions
        driver.quit()

def main():
    # Set up the webdriver (make sure you have the correct driver installed for your browser, e.g., chromedriver)
    # chrome_options = Options()
    # user_agent=random.choice(user_agents)
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument(f"--user-agent={user_agent}")
    # chrome_options.add_argument('--log-level=3')
    # chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument('--disable-extensions')
    # chrome_options.add_experimental_option('prefs', {
    #         'profile.default_content_setting_values.notifications': 2
    #     })
    # chrome_options.add_argument("--window-size=1366,768")
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    # chrome_options.add_argument("--no-sandbox")  # Disables the sandbox for testing in a docker container
    # chrome_options.add_argument("--disable-dev-shm-usage")  # To handle shared memory issues in Docker
    # # chrome_options.add_argument("--start-maximized")  # Start the browser maximized
    # chrome_options.add_experimental_option('excludeSwitches', ["enable-automation", 'enable-logging'])
    # chrome_options.add_argument("--disable-gpu")
    
    

    for i in range(random.randint(4,8)):
        try:
            clickbot("https://formula1-8d16.onrender.com")
        except Exception as e:
            logging.error("clickbot " + e)
        try:    
            clickbot("https://formula01.onrender.com")
        except Exception as e:
            logging.error("clickbot " + e)
        try:    
            clickbot("https://formula02.onrender.com")
        except Exception as e:
            logging.error("clickbot " + e)
        try:
            clickbot("https://formula03.onrender.com")
        except Exception as e:
            logging.error("clickbot " + e)
        try:
            clickbot("https://formula04.onrender.com")
        except Exception as e:
            logging.error("clickbot " + e)
        

    time.sleep(100)

if __name__ == '__main__':
    logging.info("Something bro")
    main()
