import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import time
import requests
import shutil
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
speak("Hello sir!")
assname =("Jarvis")
speak("I am your Assistant")
speak(assname)
speak("What should i call you sir")

def takeCommand():

	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
			print("Listening...")
			r.pause_threshold = 1
			audio = r.listen(source)
	try:
			print("Recognizing...") 
			query = r.recognize_google(audio, language ='en-in')
			print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query
query = takeCommand().lower()
	
speak("Welcome Mister")

speak(query)
columns = shutil.get_terminal_size().columns
	
print("#####################".center(columns))
print("Welcome Mr.", query.center(columns))
print("#####################".center(columns))

speak("How can i Help you, Sir")
while True:
	query = takeCommand().lower()

	if 'wikipedia' in query:
		speak('Searching Wikipedia...')
		query = query.replace("wikipedia", "")
		results = wikipedia.summary(query, sentences = 3)
		speak("According to Wikipedia")
		print(results)
		speak(results)
	elif 'who is' in query:
		speak('Searching Wikipedia...')
		query = query.replace("who is", "")
		results = wikipedia.summary(query, sentences = 3)
		speak("According to Wikipedia")
		print(results)
		speak(results)
	elif 'where is' in query:
		speak('Searching Wikipedia...')
		query = query.replace("where is", "")
		results = wikipedia.summary(query, sentences = 3)
		speak("According to Wikipedia")
		print(results)
		speak(results)
	
	elif 'what is' in query:
		speak('Searching Wikipedia...')
		query = query.replace("what is", "")
		results = wikipedia.summary(query, sentences = 3)
		speak("According to Wikipedia")
		print(results)
		speak(results)

	elif 'open youtube' in query:
		speak("Here you go to Youtube\n")
		webbrowser.open("youtube.com")

	elif 'open google' in query:
		speak("Here you go to Google\n")
		webbrowser.open("google.com")

	elif 'open stackoverflow' in query:
		speak("Here you go to Stack Over flow.Happy coding")
		webbrowser.open("stackoverflow.com") 

	elif 'play music' in query or "play song" in query:
		speak("Here you go with music")
		music_dir = "C:\\Users\vivek VANAM\Music"  #Path
		songs = os.listdir(music_dir)
		print(songs) 
		random = os.startfile(os.path.join(music_dir, songs[1]))

	elif 'the time' in query:
		strTime = datetime.datetime.now().strftime("% H:% M:% S") 
		speak(f"Sir, the time is {strTime}")

	elif 'how are you' in query:
		speak("I am fine, Thank you")
		speak("How are you, Sir")

	elif 'fine' in query or "good" in query:
		speak("It's good to know that your fine")

	elif "change my name to" in query:
		query = query.replace("change my name to", "")
		assname = query

	elif "change name" in query:
		speak("What would you like to call me, Sir ")
		assname = takeCommand()
		speak("Thanks for naming me")

	elif "what's your name" in query or "What is your name" in query:
		speak("My friends call me")
		speak(assname)
		print("My friends call me", assname)

	elif 'exit' in query:
		speak("Thanks for giving me your time")
		exit()
	elif "who made you" in query or "who created you" in query: 
		speak("I have been created by vivek.")
			
	elif 'joke' in query:
		speak(pyjokes.get_joke())
		print(pyjokes.get_joke())
			
	elif "calculate" in query: 
			
		app_id = "WH9LQT-YVRGHP25WR"
		client = wolframalpha.Client(app_id)
		indx = query.lower().split().index('calculate') 
		query = query.split()[indx + 1:] 
		res = client.query(' '.join(query)) 
		answer = next(res.results).text
		print("The answer is " + answer) 
		speak("The answer is " + answer)  

	elif 'search' in query or 'play' in query:
		
		query = query.replace("search", "") 
		query = query.replace("play", "")		 
		webbrowser.open(query) 

	elif "who i am" in query:
		speak("If you talk then definitely your human.")
	elif "why you came to world" in query:
		speak("Thanks to Vivek. further It's a secret")
		
	elif 'is love' in query:
		speak("It is 7th sense that destroy all other senses")

	elif "who are you" in query:
		speak("I am your virtual assistant created by Vivek")

	elif 'reason for you' in query:
		speak("I was created as a Minor project by Mister Vivek ")


	elif "don't listen" in query or "stop listening" in query:
		speak("for how much time you want to stop jarvis from listening commands")
		a = int(takeCommand())
		time.sleep(a)
		print(a)

	elif "write a note" in query:
		speak("What should i write, sir")
		note = takeCommand()
		file = open('jarvis.txt', 'w')
		speak("Sir, Should i include date and time")
		snfm = takeCommand()
		if 'yes' in snfm or 'sure' in snfm:
			strTime = datetime.datetime.now().strftime("% H:% M:% S")
			file.write(strTime)
			file.write(" :- ")
			file.write(note)
		else:
			file.write(note)
	
	elif "show note" in query:
		speak("Showing Notes")
		file = open("jarvis.txt", "r") 
		print(file.read())
		speak(file.read(6))

	elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather 
		api_key = "2d466815cea8515560d217d7973fa7e9"
		speak(" City name ")
		print("City name : ")
		city_name = takeCommand().lower()
		
		complete_url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
		response = requests.get(complete_url) 
		x = response.json()
		print(x)
		
		if x["cod"] != "404": 
			y = x["main"] 
			current_temperature = y["temp"] 
			current_pressure = y["pressure"] 
			current_humidiy = y["humidity"] 
			z = x["weather"] 
			weather_description = z[0]["description"] 
			print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			speak(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 		
		else: 
			speak(" City Not Found ")
		
	elif "Good Morning" in query:
		speak("A warm" +query)
		speak("How are you Mister")
		speak(assname)

	elif "will you be my gf" in query or "will you be my bf" in query: 
		speak("I'm not sure about, may be you should give me some time")

	elif "how are you" in query:
		speak("I'm fine, glad you me that")

	elif "i love you" in query:
		speak("It's hard to understand")

	

