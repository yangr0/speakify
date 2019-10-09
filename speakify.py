import speech_recognition as sr

import pyaudio

import random



rec = sr.Recognizer()

with sr.Microphone() as mic:

	print(random.choice(list) + "  Start Speaking: ")

	audio = rec.listen(mic)


	try:

		text = rec.recognize_google(audio)

		print("{}".format(text))

	except:

		print(random.choice(list) + "  Sorry we didn't hear anything, please speak louder or move closer to the microphone")