import os
import pyttsx3

print("Good Afternoon!!")
pyttsx3.speak("Good Afternoon!!")

while True:
	p=input("Tell us which application you want to launch:")

	if (("run" in p) or ("open" in p))  and ("chrome" in p):
		os.system('chrome')
	elif (("run" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
		os.system('notepad')
	elif ("run" in p) and ("player" in p) and ("media" in p):
		os.system('wmplayer')
	elif (("open" in p) or ("launch" in p)) and (("calc" in p) or("calculator" in p)):
		os.system('calc')
	elif (("run" in p) or ("open" in p)) and (("settings" in p) or("setting" in p)):
		os.system('start ms-settings:')
	elif (("run" in p) or ("open" in p)) and (("vs code" in p) or("visual studio" in p)):
		os.system('code')
	elif ("exit" in p) or("quit" in p):
		break
	else:
		print("Doesn't Support")
