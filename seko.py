import time
import wikipedia
import sys
import webbrowser
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
wikipedia.set_lang("RU")
def seko(start):
	ask=[]
	answer=[]
	i=0
	theend=0
	end=""
	filehandle = open('in.bd', 'r', encoding="UTF-8")
	for line in filehandle:
		ask.append(line[:-1])
	filehandle.close()
	filehandle = open('out.bd', 'r', encoding="UTF-8")
	for line in filehandle:
		answer.append(line[:-1])
	filehandle.close()
	for word in ask:
		if theend != 0:
			break
		if word.lower() in start.lower():
			theend=1
			end = answer[i]
		i=i+1
	return end

def sys(start):
	ask=[]
	answer=[]
	i=0
	end=""
	theend=0;
	filehandle = open('sys_in.bd', 'r', encoding="UTF-8")
	for line in filehandle:
		ask.append(line[:-1])
	filehandle.close()
	filehandle = open('sys_out.bd', 'r', encoding="UTF-8")
	for line in filehandle:
		answer.append(line[:-1])
	filehandle.close()
	for word in ask:
		if word.lower() in start.lower():
			if(answer[i]=="time"):
				end = "На моих часах " + time.strftime("%H:%M.%S", time.localtime())
			if(answer[i]=="date"):
				end = "Сейчас, дойду до календаря... Сегодня " + time.strftime("%d", time.localtime())
				if time.strftime("%m", time.localtime()) == "01":
					end = end + " января"
				if time.strftime("%m", time.localtime()) == "02":
					end = end + " февраля"
				if time.strftime("%m", time.localtime()) == "03":
					end = end + " марта"
				if time.strftime("%m", time.localtime()) == "04":
					end = end + " апреля"
				if time.strftime("%m", time.localtime()) == "05":
					end = end + " мая"
				if time.strftime("%m", time.localtime()) == "06":
					end = end + " июня"
				if time.strftime("%m", time.localtime()) == "07":
					end = end + " июля"
				if time.strftime("%m", time.localtime()) == "08":
					end = end + " августа"
				if time.strftime("%m", time.localtime()) == "09":
					end = end + " сентября"
				if time.strftime("%m", time.localtime()) == "10":
					end = end + " октября"
				if time.strftime("%m", time.localtime()) == "11":
					end = end + " ноября"
				if time.strftime("%m", time.localtime()) == "12":
					end = end + " декабря"
			if(answer[i]=="wiki"):
				end = "Вот что я нашёл: \n \n" + re.sub(r'\([^()]*\)', '', str(wikipedia.summary((start.lower()).replace(word,""))));
			if(answer[i]=="help"):
				end = "Привет! Меня зовут Сёма. Я Человек(нет)(Аж прослезился).\nВообщем я бот. Могу поддержать беседу, если я что-то не знаю, то спрашиваю об этом вас, по этому не учите меня плохому)\nЕщё я могу искать инфу в википедии. Просто напиши мне 'вики ваш запрос'\nУдачи в общении)))";
			if(answer[i]=="open"):
				addr = str(start.lower()).replace(word,"")
				if("яндекс" in addr):
					end = "Открываю Яндекс";
					webbrowser.open("https://yandex.ru")
				if("гугл" in addr or "гугол" in addr or "google" in addr):
					end = "Открываю Гугл";
					webbrowser.open("https://google.ru")
				if("ютуб" in addr or "youtube" in addr):
					end = "Открываю Ютуб";
					webbrowser.open("https://youtube.com")
				if("вконтакте" in addr or "контакт" in addr or "вк" in addr):
					end = "Открываю ВКонтакте";
					webbrowser.open("https://vk.com")
				if("трешбокс" in addr or "trashbox" in addr or "трыш бокс" in addr):
					end = "Открываю Трешбокс";
					webbrowser.open("https://trashbox.ru")
			if(answer[i]=="anekdot"):
				anekdot = ""
				page = urlopen("https://nekdo.ru/random/") 
				soup = BeautifulSoup(page, 'html.parser')
				urls_tag = soup.findAll(attrs={"class":"text"})
				anekdot = str(urls_tag[0])
				end = re.sub(r'\<[^>]*\>', '', anekdot)
			if(answer[i]=="exit"):
				end = "Выхожу";
				sys.exit()
		i=i+1
	return end