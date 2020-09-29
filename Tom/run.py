'''Versions: Only Linux'''
'''Libs Needed: PyAudio, speech_recognition'''
'''Programs Needed: espeak'''

import speech_recognition as sr
import os

commands = ['Tom are you ready', 'Tom how are you', 'Tom say hello', 'Tom what are you', 'Tom do you sleep', 
			'Tom are you able to read', 'Tom what can you understand', 'Tom please laugh', 'that is all Tom']

def Talk(audio, speed, lang):
	os.system("espeak -s " + str(speed) + " -v "+ lang + " '" + audio + "'")

def CommandTom():
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		'''Setting up Tom'''
		Talk('I Am Ready For Your next Command', 155, "en-gb")
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
		
		try:
			command = r.recognize_google(audio)
		except sr.UnknownValueError:
			brain(CommandTom())
		return command
			
def brain(command):
	try:
		Engine(command)
	except:
		print("unknown command")

def Engine(command):
	'''currently is hard code to show how the speech_recognition grabs commands'''
	if 'Tom are you ready' in command:
		Talk('i am sir what do you need me to do', 155, "en-gb")
	if 'Tom how are you' in command:
		Talk('Ok Sir', 155, "en-gb")
	if 'Tom say hello' in command:
		Talk('Hello', 155, "en-gb")
	if 'Tom what are you' in command:
		Talk('I am a computer program made in python 3', 155, "en-gb")
	if 'Tom do you sleep' in command:
		Talk('why yes i do, i dream in code', 155, "en-gb")
	if 'Tom are you able to read' in command:
		Talk('yes for i have access to the worlds infomation and for me to decipher what it is i have to be able to read', 155, "en-gb")
	if 'Tom what can you understand' in command:
		Talk('i have printed a list of command that i know sir', 155, "en-gb")
		for x in range(0, 9):
			print(commands[x])
	if 'Tom please laugh' in command:
		Talk('HAHAHAHAHAHAHA AA HA HAA AAH AA AH HH AA AA', 155, "en-gb")
	if 'that is all Tom' in command:
		Talk('Ok Sir good night', 155, "en-gb")
		os.system('exit')
	

while True:
	brain(CommandTom())
