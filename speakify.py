
# Created by inc0gnit0

# Please copy this code without my permission


# MODULES #

try:

	import speech_recognition as sr

	import os

	import random

	import time

except ImportError:

	print("  You did not follow the instructions")

	print("\n")

	print("  I will do them for you...")

	time.sleep(3)

	os.system("chmod +x * && sudo ./install.sh")



# COLORS #

red = "\u001b[31;1m"

reset = "\u001b[0;1m"

green = "\u001b[32;1m"

cyan = "\u001b[36;1m"

yellow = "\u001b[33;1m"

magenta = "\u001b[35;1m"

blue = "\u001b[34;1m"

white = "\u001b[37;1m"

list = ["\u001b[31;1m", "\u001b[32;1m", "\u001b[36;1m", "\u001b[33;1m", "\u001b[35;1m", "\u001b[34;1m", "\u001b[37;1m"] # List of colors to chose from #



# BANNER #

def banner():

	print("\n")
	print(random.choice(list) + "                                https://github.com/iinc0gnit0/speakify")
	print("\n")
	time.sleep(0.1)
	print(random.choice(list) + "                                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                88888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888            888888888                    8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "          88                    888888                    88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                               88   888                        88   88   888")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88888888  888888  88  8 88  888888  88888888 88 888888 88  8 88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 8        88 8  88 88    88 88    88 88   88   88 8  88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 88    88 888  888 88    88 88    88 88   88   888   88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88  888888   888888   8888888 88    88 88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                             888")
	time.sleep(0.1)
	print(random.choice(list) + "                                         888888" + red + "                                v1.2")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Created by: inc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     GitHub: iinc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Email: iinc0gnit0@pm.me")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Instagram: i.nc0gnit0")
	time.sleep(0.1)
	print("\033[0m")


# SPEAKIFY #

def speak():

	r = sr.Recognizer()

	print("\n")

	print(random.choice(list) + "  This only supports .wav format if you need to convert")

	print("\n")

	print(random.choice(list) + "  Go to \"https://github.com/iinc0gnit0/loader\" to convert")

	print("\n")

	def output():

		path = input(random.choice(list) + "  Enter full path of the file(ex: /home/inc0gnit0/example.wav): ")

		print("\n")

		print(random.choice(list) + "=============================================================================================\033[0m")

		print("\n")

		with sr.AudioFile(path) as source:

			audio = r.record(source)

			print(r.recognize_google(audio))

		print("\n")

		print(random.choice(list) + "=============================================================================================")

	output()



# MAIN #

def main():

	os.system("clear")

	for x in range(5): # Loading Effect #

		print(random.choice(list) + "|")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "/")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "-")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "\\")

		time.sleep(0.1)

		os.system("clear")

	print(random.choice(list) + "  speakify is starting")

	time.sleep(3)



	os.system("clear") # Clear the terminal #


	banner()
	speak()



# START #

try:

	if __name__ == "__main__":

		main()

except KeyboardInterrupt: # Catch KeyboardInterruption errors #

	print("\n")

	print("  KeyboardInterrupt detected, Exiting...")

	print("\n")

	print(random.choice(list) + "  Have a nice day!! \033[0m")

	print("\n")

	time.sleep(3)

	os.system("clear")

	exit(1)