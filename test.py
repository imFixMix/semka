import seko
import re
mode=0
preveus=""
print("СёмаКолБот готов беседовать")
while 1:
	ask = input("=->")
	if mode == 1:
		if "морской огурец" in ask.lower():
			mode=0
			print("Отмененно :-) О чём поговорим?")
		else:
			f = open('in.bd','a', encoding="UTF-8")
			f.write(re.sub("[.,?!]", "", preveus.lower())+'\n')
			f.close()
			f = open('out.bd','a', encoding="UTF-8")
			f.write(ask+'\n')
			f.close()
			print("Так и запишем: " + ask)
			mode=0
	else:
		request = ask.lower()
		answer = seko.seko(request)
		u=1
		if answer == "":
			while True:
				try:
					if u == 1:
						u=0
						answer = seko.sys(request)
						break
				except Exception as ex:
					answer = "Ой, ошибочка вышла..."		
			if answer == "":
				answer =  "Внимание! Это новая фраза. Если вы уверены, то напишите ответ. Если нет, то напишите 'морской огурец'."
				mode=1
				preveus=ask
		print(answer);