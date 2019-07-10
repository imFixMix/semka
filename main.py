import seko
import re
import speech_recognition as sr
import win32com.client as wincl
import time
speak = wincl.Dispatch("SAPI.SpVoice")
voices = speak.GetVoices();
speak.Voice = voices.Item(2);
mode=0
preveus=""
t=1
ask=""
def playFile(sound,reps=1):
    import pyglet
    from pyglet.media import Player
  
    player = Player()
    song = pyglet.media.load(sound,streaming=False)
    for i in range(reps):
        player.queue(song)
  
    player.play()
    def callback(dt):
        pyglet.app.exit()
  
    pyglet.clock.schedule_once(callback,song.duration*reps)
    pyglet.app.run()
def say(frase):
	print(frase)
	speak.Speak(frase)
say("Семён готов беседовать")
while 1:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		playFile("start.wav")
		print("Слушаю")
		r.non_speaking_duration = 0.3
		r.pause_threshold = 0.4
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
		playFile("stop.wav")
		print("Распознование")
	try:
		ask = r.recognize_google(audio, language="ru-RU").lower()
		print("=> " + ask)
	except sr.UnknownValueError:
		say("Говорите погромче")
		ask="";
		t=0;
	if mode == 1:
		if "нет" in ask.lower():
			mode=0
			say("Отмененно :-) О чём поговорим?")
		else:
			f = open('in.bd','a', encoding="UTF-8")
			f.write(re.sub("[.,?!]", "", preveus.lower())+'\n')
			f.close()
			f = open('out.bd','a', encoding="UTF-8")
			f.write(ask+'\n')
			f.close()
			say("Так и запишем: " + ask)
			mode=0
	else:
		request = ask.lower()
		answer = seko.seko(request)
		u=1
		if answer == "":
			answer = seko.sys(request)				
			if answer == "" and t == 1:
				answer =  "Внимание! Это новая фраза. Вы уверенны?"
				mode=1
				preveus=ask
		say(answer);
		t=1;