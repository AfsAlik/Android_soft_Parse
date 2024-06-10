    # Конфиг предустановок разрешения окна интерфейса 
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.graphics import *
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
from datetime import datetime

from bs4 import BeautifulSoup as BS
from prettytable import PrettyTable

import smtplib
from email.mime.text import MIMEText
from kivy.clock import Clock

import requests
import bs4
import xlsxwriter

    # Начало кода взаимодействия приложения с классами
data = dict()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

    # Очистка остаточных данных в файлах пользователя для избежания конфликтов в выводе информации
with open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt', 'r+') as f:
    f.truncate(0)

with open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt', 'r+') as f:
    f.truncate(0)

with open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\Vivod.txt', 'r+') as f:
    f.truncate(0)

class Nastroiki(Screen):
    def switch(self, switchObject, switchValue):
        if (switchValue):
            f = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "w", encoding="utf-8")
            f.write("1")
            f.close()
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        else:
            f = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "w", encoding="utf-8")
            f.write("0")
            f.close()
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)


class Istor(Screen):
    def on_enter(self, **kwargs):
        d = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\URLadresa.txt', "r", encoding='utf-8')
        self.ids.url.text = d.read()
        d.close()
        f = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)

class Parsing(Screen):
    def on_enter(self, **kawrgs):
        f = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)
    
    def sohrURL(self):
        f = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\URLadresa.txt', "a", encoding='utf-8')
        f.write(self.ids.tx1.text + "\n")
        f.close()

    def bar2(self):
        self.bar = Clock.schedule_interval(self.bar1, 0.005)
        Clock.schedule_once(self.stop_interval, 1.637)

    def val2(self, value):
        match value:
            case "Файл":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val2.txt", "w", encoding='utf-8')
                f.write("0")
                f.close()
            case "На экран":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val2.txt", "w", encoding='utf-8')
                f.write("1")
                f.close()
   
    def val1(self, value):
        match value:
            case "Телефоны":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Телефоны")
                f.close()
            case "Часы и смарт браслеты":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Часы и смарт браслеты")
                f.close()
            case "Планшеты":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Планшеты")
                f.close()
            case "Ноутбуки и ПК":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Ноутбуки и ПК")
                f.close()
            case "Техника Dyson":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Техника Dyson")
                f.close()
            case "Мониторы":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Мониторы")
                f.close()
            case "Аксессуары":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Аксессуары")
                f.close()
            case "Товары для дома":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Товары для дома")
                f.close()
            case "Транспорт":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Транспорт")
                f.close()
            case "Фото и видео":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Фото и видео")
                f.close()
            case "Телевизоры":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Телевизоры")
                f.close()
            case "Приставки":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Приставки")
                f.close()
            case "Шлемы виртуальной реальности":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Шлемы виртуальной реальности")
                f.close()
            case "Квадрокоптеры":
                f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "w", encoding='utf-8')
                f.write("Квадрокоптеры")
                f.close()
        
    def stop_interval(self, *args):
        self.bar.cancel()
    
    def bar1(self, *args):
        current = self.ids.bar.value
        if current == 1:
            current = 0
            self.main()
        current += .01
        self.ids.bar.value = current



    def parse_file(self, html, Razdel_tov):
    
        # Обновленный парсинг с выводом данных в таблицу excel         
        main_url = 'https://trade59.ru/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        Received_parsing = [['Наименование','Цена','Ссылка','Картинка']]

        def get_soup(url):
            res = requests.get(url, headers)
            return bs4.BeautifulSoup(res.text, 'html.parser')

        categories_page = get_soup(main_url+'catalog.html?cid=7')
        categories = categories_page.findAll('a', class_='cat_item_color')
        for cat in categories:
            subcategories_page = get_soup(main_url+cat['href'])
            subcategories = subcategories_page.findAll('a',class_ ='cat_item_color')
            for subcat in subcategories:
                iphones_page = get_soup(main_url+subcat['href'])
                iphones = iphones_page.findAll('div', class_= 'items-list')
                for iphone in iphones:
                    title = iphone.find('a')['title'].strip()
                    price = iphone.find('div', class_='price').find(text=True).strip()
                    url = iphone.find('a')['href'].strip()
                    img = iphone.find('div',class_='image')['style'].split('url(')[1].split(')')[0].replace('/tn/','/source/')
                    Received_parsing.append([title, price, main_url+url, main_url+img])

        with xlsxwriter.Workbook(Razdel_tov +'.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, info in enumerate(Received_parsing):
                worksheet.write_row(row_num, 0, info)
        successfully_parse_file()

        # Обновленный парсинг с выводом данных в текстовик а после в окно вывода информации в самом приложении  
    def parse(self, html):
            main_url = 'https://trade59.ru/'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
            Received_parsing = [['Наименование','Цена']]

            def get_soup(url):
                res = requests.get(url, headers)
                return bs4.BeautifulSoup(res.text, 'html.parser')

            categories_page = get_soup(main_url+'catalog.html?cid=7')
            categories = categories_page.findAll('a', class_='cat_item_color')
            for cat in categories:
                subcategories_page = get_soup(main_url+cat['href'])
                subcategories = subcategories_page.findAll('a',class_ ='cat_item_color')
                for subcat in subcategories:
                    iphones_page = get_soup(main_url+subcat['href'])
                    iphones = iphones_page.findAll('div', class_= 'items-list')
                    for iphone in iphones:
                        title = iphone.find('a')['title'].strip()
                        price = iphone.find('div', class_='price').find(text=True).strip()
                        Received_parsing.append([title, price])

            # Определяем шапку и данные.
            self.th = ['Полученная информация']
            self.td = Received_parsing

            self.columns = len(self.th)  # Подсчитаем кол-во столбцов на будущее.

            self.table = PrettyTable(self.th)  # Определяем таблицу.

            # Cкопируем список td, на случай если он будет использоваться в коде дальше.
            # td_data = td[:]
            # Входим в цикл который заполняет нашу таблицу.
                # Цикл будет выполняться до тех пор пока у нас не кончатся данные
                # для заполнения строк таблицы (список td_data).

            while self.td:
                    # Используя срез добавляем первые пять элементов в строку.
                    # (columns = 5).
                self.table.add_row(self.td[:self.columns])
                    # Используя срез переопределяем td_data так, чтобы он
                    # больше не содержал первых 5 элементов.
                self.td = self.td[self.columns:]

                # Открываем файл для записи
            with open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\Vivod.txt', "a", encoding="utf-8") as fp:
                # создаем строку для записи в файл
                self.table = self.table.get_string()
                # пишем данные
                fp.write(self.table)
                # дописываем символ начала строки 
                fp.write('\n')
                fp.close()

            d = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\Vivod.txt', "r", encoding='utf-8')
            s = d.read()
            self.ids['VivodPars'].text = s
            d.close()

            successfully_parse()    

        # Проверка переменных на выбранный способ вывода и обращение к определенному методу 
    def main(self):
        f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val2.txt", "r", encoding='utf-8')
        Type_viv = f.read()
        f.close()
        f = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val1.txt", "r", encoding='utf-8')
        Razdel_tov = f.read()
        f.close()
        if (Type_viv == '0' and self.ids.tx1.text == 'https://trade59.ru/'):
            url = self.ids.tx1.text
            self.parse_file(url, Razdel_tov)
        else:
            pass

        if (Type_viv == '1' and self.ids.tx1.text == 'https://trade59.ru/'):
            url = self.ids.tx1.text
            self.parse(url)
        else:
            pass

        # Отправка уведомлений на адрес электронной почты пользователя 
class Rassilka(Screen):
    def on_enter(self, **kawrgs):
        f = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)
  
    def on_save(self, instance, value, date_range):
        self.ids['date_label'].text = f'c {str(date_range[0])} по {str(date_range[-1])}'

    def on_cancel(self, instance, value):
        self.ids['date_label'].text = "Вы не выбрали дату!"

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def get_time(self, instance, time):
        self.ids['time_label'].text = str(time)

    def on_cancel2(self, instance, time):
        self.ids['time_label'].text = "Вы не выбрали время!"

    def show_time_picker(self):
        default_time = datetime.strptime("12:00:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel2, time=self.get_time)
        time_dialog.open()

    # Вход в почтовый ящик приложения для отправки уведомления
    def send_email(self):
        try:
            email = 'AnyFind@yandex.ru'
            password = 'PrilANYFIND'

            server = smtplib.SMTP('smtp.yandex.ru', 587)
            server.ehlo()
            server.starttls()
            server.login(email, password)

            dest_email = self.ids['rassil_poluch'].text
            email_text = self.ids['rassil'].text

            msg = MIMEText(email_text)
            msg["Subject"] = "Приложение - парсер AnyFind"
            
            server.set_debuglevel(1)
            server.sendmail(email, dest_email, msg.as_string())
            server.quit()

            return MailSend()
        except Exception:
            return MailSendInv()
        
    # Создания нового аккаунта пользователя
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def on_enter(self, **kwargs):
        d = open("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\URLadresa.txt", "w", encoding="utf-8")
        d.write("")
        d.close()

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"
    
    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = name
        f = open('C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\val3.txt', "r", encoding='utf-8')
        a = f.read()
        f.close()
        if a == "1":
            with self.canvas.before:
                Rectangle(source = "Img\\bg.png", size = self.size)
        elif a == "0":
            with self.canvas.before:
                Rectangle(source = "Img\\Main_theme.jpg", size = self.size)

class WindowManager(ScreenManager):
    pass

    # Обработка возможных ошибок и вовод окна взаимодействия с пользователем
def parse_error():                    
    pop = Popup(title='Ошибка',
        content=Label(text='Выберите способ вывода!'),
        size_hint=(None, None), size=(300, 200))
    pop.open()

def successfully_parse():                    
    pop = Popup(title='Готово!',
        content=Label(text='Информация выведена на экран'),
        size_hint=(None, None), size=(300, 200))
    pop.open()

def successfully_parse_file():
    pop = Popup(title='Готово!',
        content=Label(text='Информация выведена в файл'),
        size_hint=(None, None), size=(300, 200))
    pop.open()

def invalidLogin():
    pop = Popup(title='Такого аккаунта нет',
        content=Label(text='Пожалуйста, проверьте данные'),
        size_hint=(None, None), size=(300, 200))
    pop.open()


def invalidForm():
    pop = Popup(title='Ошибка',
        content=Label(text='   Пожалуйста, заполните все поля\nили проверьте корректность формы'),
        size_hint=(None, None), size=(300, 200))

    pop.open()
    
def invalidSerc():
    pop = Popup(title='Ошибка',
        content=Label(text=' Введите коректный адресс\nТакой адресс не доступен'),
        size_hint=(None, None), size=(300, 200))

    pop.open()

def MailSend():
    pop = Popup(title='Уведомление',
        content=Label(text='Уведомление успешно отправлено!'),
        size_hint=(None, None), size=(300, 200))
    pop.open()

def MailSendInv():
    pop = Popup(title='Ошибка отправки уведомления',
        content=Label(text='Проверьте правильность почты'),
        size_hint=(None, None), size=(300, 200))
    pop.open()

class MyMainApp(MDApp):
    
    def build(self):
        self.title = 'Приложение "AnyFind"'
        return sm
    
# Билд интерфейса пользователя через библиотеку kivi и kiviMD
kv = Builder.load_file("my.kv")
sm = WindowManager()
db = DataBase("C:\\Users\\nikit\\Desktop\\Parseeer\\UserRegistration_Kivy-main\\users.txt")
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),Nastroiki(name="nast"),Rassilka(name="rass"),Parsing(name="pars"),Istor(name="ist")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

if __name__ == "__main__":
    MyMainApp().run()