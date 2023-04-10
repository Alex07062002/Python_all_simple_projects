import re
from bs4 import BeautifulSoup

def delete_tags_with_bs4(input_string):# пакет html встроен в bs
    soup = BeautifulSoup(input_string, "html.parser")
    text = soup.get_text(' ')
    return text


def delete_tags_with_bs4_2(input_string):# пакет lxml скачивается отдельно
    soup = BeautifulSoup(input_string, "lxml")
    text = soup.get_text(' ')
    return text


def delete_tags_with_bs4_3(input_string):# пакет xml встроен в lxml (работает неадекватно с 2 примером)
    soup = BeautifulSoup(input_string, "xml")
    text = soup.get_text(' ')
    return text


def delete_html_tags(input_string): #удаление c помощью регулярного выражения описать всё практически невозможно...
    delete = re.compile('<[A-Za-z/]{1}[0-9A-Za-z=:/" ]{1,}>')# регулярные отношения (недопустимы знаки препинания, кроме /) !!! <a href...
    clear_text = re.sub(delete,' ',input_string)
    return ' '.join(clear_text.split())




if __name__ == '__main__':
#doc = '<html><head><title>Моя страница</title><head><h1>Привет, Я Колян!<BR />Закурить есть?</h1></head></body>'
    doc = '<html><head><title>12+25<75>15</title><head><h1>'
    #doc = '<html><head><title>12+25<x y>15</title><head><h1>'
    print(delete_tags_with_bs4(doc))
    #print(delete_html_tags(doc))
    #print(delete_tags_with_bs4_2(doc))

