from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from datetime import datetime
import uuid


TWITTER_USERNAME = "your_TWITTER_USERNAME"
TWITTER_PASSWORD = "yoUR_TWITTER_PASSWORD"
TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
CHROME_DRIVER_PATH = r"C:\Program Files\ChromeDriver\chromedriver.exe" # Replace with the path to your ChromeDriver executable

MONGO_URI = "mongodb+srv://ashish:78747874a@cluster0.oskyg.mongodb.net/"

def get_trending_topics():
    options = webdriver.ChromeOptions()
    service = Service(CHROME_DRIVER_PATH)



    driver = None

    try:
       
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://x.com/i/flow/login")

        
        username_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_input.send_keys(TWITTER_USERNAME)
        username_input.send_keys(Keys.RETURN)

       
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            email_input.send_keys(TWITTER_EMAIL)
            email_input.send_keys(Keys.RETURN)
        except Exception:
            pass  

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.RETURN)

       
        div_indices = [3, 4, 5, 6]
        xpaths = [
            f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/section/div/div/div[{i}]/div/div/div/div/div/div[1]/span"
            for i in div_indices
        ]

       
        trends = []
        for xpath in xpaths:
            try:
                trend_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                trends.append(trend_element.text.strip())
            except Exception as e:
                print(f"Error extracting trend for XPath {xpath}: {e}")
                trends.append("")  
        print(f"Extracted trends: {trends}")

       
        driver.get("https://api.ipify.org?format=text")
        ip_address = driver.find_element(By.TAG_NAME, "body").text

        unique_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        client = MongoClient(MONGO_URI)
        db = client["x_trends"]
        collection = db["trending_topics"]

        document = {
            "unique_id": unique_id,
            "trend1": trends[0] if len(trends) > 0 else "",
            "trend2": trends[1] if len(trends) > 1 else "",
            "trend3": trends[2] if len(trends) > 2 else "",
            "trend4": trends[3] if len(trends) > 3 else "",
            "date_time": timestamp,
            "ip_address": ip_address
        }

        inserted_id = collection.insert_one(document).inserted_id
        document["_id"] = str(inserted_id)

        return document

    except Exception as e:
        return {"error": str(e)}

    finally:
        if driver:
            driver.quit()
            

if __name__ == "__main__":
    print(get_trending_topics())
