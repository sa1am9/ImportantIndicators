from django.views import View
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


class BaseView(View):
    def get(self, *args):
        # делаем запрос по ссылке
        r = requests.get('https://bank.gov.ua/')
        # забираем html и конвертируем с BeautifulSoup для того что бы можно было парсить
        soup = BeautifulSoup(r.text)
        # ищем div c классом widget with-footer widget-macrovalues (это див с данными которые нам нужны
        if soup.find_all("div", {"class": "widget with-footer widget-macrovalues"}):
            # если нашли - конвертируем строку html в http responce
            return HttpResponse(soup.find_all("div", {"class": "widget with-footer widget-macrovalues"})[0])
        else:
            # иначе возвращаем просто сообщение что не нашли такой класс
            return HttpResponse('Not found')
