#Проверка
# «Создание заказа на доставку с оплатой через Kaspi
# для авторизированного пользователя с выбором ранее добавленного адреса»

import json
import os
import time

import allure
from playwright.sync_api import sync_playwright




@allure.step("paracetamol")
def test_paracetomol():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["iPhone X"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/")
        with open("storage_load5.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                for (const key in data) {
                    localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        page.reload()
        page.locator("input").click()
        page.locator("input").fill("Парацетамол")
        page.wait_for_timeout(4000)
        sel=page.get_by_text("Парацетамол таблетки 500 мг №10").first
        sel.click()
        local_storage = page.evaluate('''() => {
            let data = {};
            for (let i = 0; i < localStorage.length; i++) {
                let key = localStorage.key(i);
                data[key] = localStorage.getItem(key);
            }
               return data;
            }''')
        with open("storage_load1.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        page.wait_for_timeout(2000)

@allure.step("click_paracetamol")
def test_click_paracetamol():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["iPhone X"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/products/paracetamol-0-5-10--3c20eebe-3ee1-4d9e-bd34-0ba2afd85286")
        with open("storage_load1.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                for (const key in data) {
                    localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        page.reload()
        page.get_by_text("В корзину").click()
        page.get_by_text("Моя корзина").click()
        local_storage = page.evaluate('''() => {
                    let data = {};
                    for (let i = 0; i < localStorage.length; i++) {
                        let key = localStorage.key(i);
                        data[key] = localStorage.getItem(key);
                    }
                       return data;
                    }''')
        with open("storage_load2.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)

@allure.step("cart")
def test_naiti_apteka():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["iPhone X"], permissions=["geolocation"],
                                      geolocation={"latitude": 37.7749, "longitude": -122.4194},
                                      locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/cart")
        with open("storage_load2.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                for (const key in data) {
                    localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        page.reload()
        page.get_by_text("Найти в аптеках").click()
        local_storage = page.evaluate('''() => {
                            let data = {};
                            for (let i = 0; i < localStorage.length; i++) {
                                let key = localStorage.key(i);
                                data[key] = localStorage.getItem(key);
                            }
                               return data;
                            }''')
        with open("storage_load3.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)

@allure.step("ofo_form")
def test_ofo_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["iPhone X"], permissions=["geolocation"],
                                      geolocation={"latitude": 37.7749, "longitude": -122.4194},
                                      locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/pharmacies")
        with open("storage_load3.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                       for (const key in data) {
                           localStorage.setItem(key, data[key]);
                           }
                       }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(6000)
        page.get_by_role("button",name="Перейти к оформлению 110₸").click()
        local_storage = page.evaluate('''() => {
                                    let data = {};
                                    for (let i = 0; i < localStorage.length; i++) {
                                        let key = localStorage.key(i);
                                        data[key] = localStorage.getItem(key);
                                    }
                                       return data;
                                    }''')
        with open("storage_load4.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
time.sleep(3)
@allure.step("dos")
def test_dos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.wait_for_timeout(3000)
        page.goto("https://dev.daribar.kz/checkout")
        with open("storage_load4.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                for (const key in data) {
                    localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(2000)
        sel = page.get_by_role("button", name="Доставка")
        if sel:
            sel.click()
        else:
            print("ERROR:test_dos")
        page.wait_for_timeout(3000)
        page.get_by_text("Алматы улица Гоголя,20").click()
        local_storage = page.evaluate('''() => {
                                                        let data = {};
                                                        for (let i = 0; i < localStorage.length; i++) {
                                                            let key = localStorage.key(i);
                                                            data[key] = localStorage.getItem(key);
                                                        }
                                                        return data;
                                                    }''')
        with open("storage_load6.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        page.wait_for_timeout(2000)

