from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import threading
import uvicorn
import time

def run_app():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)

def test_ui_chat():
    thread = threading.Thread(target=run_app, daemon=True)
    thread.start()
    time.sleep(3)

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://127.0.0.1:8000")

    input_box = driver.find_element(By.ID, "message")
    input_box.send_keys("What is devops?")

    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    assert "DevOps" in driver.page_source or "devops" in driver.page_source.lower()
    driver.quit()