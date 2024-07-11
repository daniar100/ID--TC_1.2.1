import time

from playwright.sync_api import sync_playwright
import os
import json
def test_export_local_storage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["iPhone X"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        while True:
            page.goto("https://dev.daribar.kz/")
            time.sleep(100)
            break
        local_storage = page.evaluate('''() => {
         let data = {};
        for (let i = 0; i < localStorage.length; i++) {
            let key = localStorage.key(i);
            data[key] = localStorage.getItem(key);
        }
           return data;
         }''')
        with open("storage_load5.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
