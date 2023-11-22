from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import ui_functions as fc

load_dotenv()
# DOCUMENTAÇÃO SELENIUM
# https://selenium-python.readthedocs.io/

# ROOT_FOLDER = Path(__file__).parent
# CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'

# r'user-data-dir=C:\\Users\\joaov\\AppData\\
# Local\\Google\\Chrome\\User Data\\Default')


class Disparo:

    def make_chrome_browser(self, *options: str) -> webdriver.Chrome:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = '/opt/google/chrome/chrome'
        chrome_options.page_load_strategy = 'eager'
        if options is not None:
            for option in options:
                chrome_options.add_argument(option)

        # chrome_options.add_argument(option)
        chrome_service = Service(ChromeDriverManager().install())

        browser = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options,
        )

        return browser

    def select_element(self, browser: webdriver.Chrome, x_path: str):
        elemento = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, x_path))
        )
        return elemento

    def disparar(self, lista_disparo: list, callbakc=None):

        mensagens = []
        options = ['--disable-gpu', '--no-sandbox',]  # noqa F841
        browser = self.make_chrome_browser()
        browser.get('https://web.whatsapp.com/')
        while len(browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[4]/header')) < 1:  # noqa E501
            sleep(1)
        try:
            for infos in lista_disparo:
                sleep(5)
                url = 'https://web.whatsapp.com/send/?phone=' + \
                    fc.format_phone_url(infos['WhatsApp'])

                browser.get(url)
                while len(browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[4]/header')) < 1:  # noqa E501
                    sleep(1)
                sleep(2)

                try:
                    if len(browser.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button')) < 1:  # noqa E501
                        while len(browser.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) == 1:  # noqa E501
                            print('carregando mensagem!')
                            sleep(1)
                        clique1 = self.select_element(
                            browser, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'  # NOQA E501
                        )
                        texto = infos['Texto'].replace('\n', '')
                        clique1.send_keys(str(texto))

                        clique1.send_keys(Keys.ENTER)
                        mensagens.append({
                            'Nome Cliente': infos["Nome"],
                            'Whatsapp': infos["WhatsApp"],
                            'Status': 'Mensagem Entregue!',
                        })
                        sleep(5)
                    else:
                        button = self.select_element(
                            browser=browser,
                            x_path='//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button/div'  # noqa E501
                        )
                        button.click()
                        mensagens.append({
                            'Nome Cliente': infos["Nome"],
                            'Whatsapp': infos["WhatsApp"],
                            'Status': 'Número Inválido!',
                        })
                        continue

                except Exception as e:
                    print(e)
                    mensagens.append({
                        'Nome Cliente': infos["Nome"],
                        'Whatsapp': infos["WhatsApp"],
                        'Status': 'Erro ao entreguar Mensagem!',
                    })
                    sleep(5)
                if callbakc:
                    callbakc()

        except Exception as e:
            browser.quit()
            print('Você não conectou seu whatsapp web: ', e)
            mensagens.append({
                'Nome Cliente': 'Você não conectou seu whatsapp web'
            })

        browser.quit()
        return {'mensagens': mensagens, 'success': True}


# if __name__ == '__main__':
#     disparo = Disparo()
#     # browser = disparo.make_chrome_browser()
#     # browser.get('https://web.whatsapp.com/')
#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.binary_location = '/opt/google/chrome/chrome'
#     # chrome_options.add_argument('--headless')
#     chrome_options.page_load_strategy = 'normal'
#     chrome_service = Service(ChromeDriverManager().install())

#     browser = webdriver.Chrome(
#         service=chrome_service,
#         options=chrome_options,
#     )
#     browser.get("https://www.selenium.dev/selenium/web/web-form.html")
