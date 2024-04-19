#Install all these py modules
import sys
from bs4 import BeautifulSoup
from more_itertools import take
import pyttsx3
import scipy as sp
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pyjokes
from pynput.keyboard import Key, Controller
import requests
from random import randint
import Functions.TarTalks as TarTalks
import pyautogui
import operator
import time
import winshell as ws
from googletrans import Translator
import Commands_Atlas

def closee():
    sys.exit()
transl = Translator()
print("""
░█████╗░████████╗██╗░░░░░░█████╗░░██████╗
██╔══██╗╚══██╔══╝██║░░░░░██╔══██╗██╔════╝
███████║░░░██║░░░██║░░░░░███████║╚█████╗░
██╔══██║░░░██║░░░██║░░░░░██╔══██║░╚═══██╗
██║░░██║░░░██║░░░███████╗██║░░██║██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░ Ai

By Chetna A. G
https://github.com/Coolness-glitch\n""")

name = input("Enter your name: ")
keyboard = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# 0 for David(it actually sounds cool) 1 for Mark 2 for Zira
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

#all the important stuff
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    speak("Im Atlas. tell me how can i help you?")  
def takeCommand():
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Speak Now...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Processing...")    
            cmds = r.recognize_google(audio, language='en-us')
            print(f"You said: {cmds}\n")

        except Exception as e:
            # print(e)    
            print("Say that again...")  
            return "None"
        return cmds

  

def Exe():
        wishMe()
        while True:
                cmds = takeCommand().lower()
        #It does cool stuff from here on...
        #Basic command stuff=------------------------------------------------------------------------------
                if 'wikipedia' in cmds:
                    speak('Searching Wikipedia...')
                    cmds = cmds.replace("wikipedia", "")
                    results = wikipedia.summary(cmds, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                
                elif 'bye' in cmds or 'take a break' in cmds:
                    speak("wake me up if u need me. Bye-Bye")
                    exit()

                elif 'open youtube' in cmds:
                    speak("opening youtube")
                    webbrowser.open("www.youtube.com")

                elif 'netflix' in cmds:
                    speak("opening netflix")
                    webbrowser.open("www.netflix.com")

                elif 'open chrome' in cmds or 'open google chrome' in cmds:
                    os.system("start chrome")
                    speak("Opening Chrome")

                elif "instagram" in cmds:
                    webbrowser.open("instagram.com")

                elif "whatsapp" in cmds:
                    whatss = "opening whatsapp"
                    speak(whatss)
                    webbrowser.open("https://web.whatsapp.com/")

                elif "open explorer" in cmds:
                    speak("opening explorer")
                    os.system("start explorer")
            
                elif "open maps" in cmds:
                    map = "opening maps"
                    speak(map)
                    webbrowser.open("https://www.google.com/maps")

                elif 'the time' in cmds:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f", the time is {strTime}")

                elif 'code' in cmds:
                    speak("Opening Visual Studio Code")
                    codePath = "C:\\Users\\agche\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
 

                elif 'play music' in cmds:
                    speak("playing music")
                    webbrowser.open("https://open.spotify.com/")#6/3/09

                elif 'notepad' in cmds:
                    speak("Opening Notepad")
                    os.system("start notepad")

                elif "tell me a joke" in cmds:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(f"Im not a comedian but here we go.....{joke}")

                elif 'are you single' in cmds:
                        speak('I am in a relationship with wifi')

                elif "the date" in cmds:
                    date =  datetime.datetime.now()
                    speak(date)
                    #nope
                    

                elif "photos" in cmds:
                    photos = "opening google photos"
                    speak(photos)
                    webbrowser.open("https://photos.google.com/")

                elif "call" in cmds:
                    calls = "opening duo to call"
                    speak(calls)
                    webbrowser.open("https://duo.google.com/?web&utm_source=marketing_page_button_main") #u need an account in gl duo 

                elif "camera" in cmds or "picture" in cmds:
                    cam = "opening camera"
                    speak(cam)
                    os.system("start microsoft.windows.camera:") 

                elif 'record' in cmds:
                    os.system("explorer.exe shell:appsFolder\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App")

                elif "cmd" in cmds:
                    cmdd = "opening command prompt"
                    speak(cmdd)
                    os.system("start cmd")
                
                elif "mail" in cmds or "inbox" in cmds:
                    maill = "opening g-mail"
                    speak(maill)
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                
                elif 'shutdown' in cmds: #Dangarous AF
                    whatsss = "shutting down the system"
                    speak(whatsss)
                    os.system("shutdown -s")
                
                elif "open website" in cmds:
                    speak("which website are you searching for")
                    ss = takeCommand()
                    speak('Searching for ' + cmds.split('open website')[1])
                    url = 'https://google.com/search?q=' + ss
                    try:
                        webbrowser.get().open(url)
                        speak('This is what I found')
                    except:
                        print('')
        #Basic Commands And Stuff the End---------------------------------------------------------------------------
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        #Conversation With The AI(Very boring lol)=----------------------------------------------------------------------------------
                elif "hello" in cmds or "hi" in cmds:
                    while True:
                        speak(Commands_Atlas.Greets[randint(0,len(Commands_Atlas.Greets)-1)]+name)
                        break
                
                elif "you up" in cmds:
                    speak("Yes. I am always awake.")
                
                elif "is cereal a soup" in cmds:
                    no = "Cereal is not a soup and if you think otherwise.. you are stupid"
                    speak(no)
                
                elif "where do you live" in cmds:
                    shit = "well, i live in your computer, by the way.. i gotta say nice computer"
                    speak(shit)
                
                elif 'atlas mean' in cmds:
                    speak("Well Atlas is an greek god whom i am named after")#<------kinda true but i named him atlas cause it sounds cool

                elif 'who are you' in cmds:
                    speak("Im Atlas, Your Favorite Virtual Assistant.")

                elif 'what is your name' in cmds:
                    speak("Im Atlas")

                elif "who am i" in cmds:
                    whoami = ["If you talk then definitely your human.", f"you are {name}"]
                    speak(whoami[randint(0,len(whoami)-1)])

                elif "what is my name" in cmds:
                    speak(f"you are{name}")

                elif "what do you eat" in cmds:
                    speak("i eat data, which surprisingly is tasty")

                elif "introduce yourself" in cmds:
                    intro = "Allow me to introduce myself, im Atlas, im here to assist you with variety of tasks as best as i can, 24 hours a day, 7 days a week."
                    speak(intro)
                
                elif "rock paper scissors" in cmds:
                    speak("ok, lets play rock, paper and scissors")
                    os.startfile("Functions\Rockpapsci.py")
                
                elif "lets play snake game" in cmds:
                    os.startfile("Functions\Snake.py")
                
                elif "how are you" in cmds:
                    speak("im fine thank you.")

        #Conversations with AI the End------------------------------------------------------------------------------
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        #complex commands=------------------------------------------------------------------------------------------
            
            #KEYBOARD 
            
                elif 'copy' in cmds:
                    with keyboard.pressed(Key.ctrl):
                         keyboard.press('c')
                         keyboard.release('c')
                         speak('Copied')
                
                elif 'paste' in cmds or 'pest'  in cmds or 'page' in cmds:
                    with keyboard.pressed(Key.ctrl):
                         keyboard.press('v')
                         keyboard.release('v')
                         speak('Pasted')

                elif 'select' in cmds or 'all' in cmds:
                    with keyboard.pressed(Key.ctrl):
                         keyboard.press('a')
                         keyboard.release('a')
                         speak('Selected all')

                elif 'undo' in cmds or 'go back' in cmds:
                    with keyboard.pressed(Key.ctrl):
                          keyboard.press('z')
                          keyboard.release('z')
                          speak('Done!')

                elif 'redo' in cmds:
                    with keyboard.pressed(Key.ctrl):
                     keyboard.press('y')
                     keyboard.release('y')
                     speak('Done!')

                elif 'cut' in cmds:
                    with keyboard.pressed(Key.ctrl):
                     keyboard.press('x')
                     keyboard.release('x')
                     speak('Cut!')

                elif 'delete' in cmds:
                    pyautogui.press("delete")
                    speak('Deleted!')

                elif 'volume up' in cmds:
                    pyautogui.press("volumeup")

                elif 'volume down' in cmds:
                    pyautogui.press("volumedown")

                elif 'mute' in cmds or 'volume mute' in cmds:
                    pyautogui.press("volumemute")
                
                elif 'enter' in cmds:
                    pyautogui.press("enter")
                    speak("entered")
                
                elif 'space' in cmds:
                    pyautogui.press("space")
                    
                elif 'new tab' in cmds:
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("t")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("t")

                elif 'close tab' in cmds or 'close chrome' in cmds:
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("w")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("w")
                
                elif 'switch tab' in cmds:
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("tab")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("tab")

                elif "switch the window" in cmds or "switch window" in cmds:
                    speak("Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(0.01)
                    pyautogui.keyUp("alt")

                    #Keyboards the end

                elif 'exit window' in cmds:
                    speak("which window do you wand to exit?")
                    exitt = takeCommand()
                    os.system(f"Taskkill /IM {exitt}.exe")
                    
                elif "write a note" in cmds:
                    speak("What should i write in it?")
                    file = open("AINote.txt", "w")
                    hell = takeCommand()
                    strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%I%p" + ":- ")
                    file.write(strTime)
                    file.write(str(hell))
                    file.close()

                elif 'riddle' in cmds:
                    speak(TarTalks.riddle[randint(0,len(TarTalks.riddle)-1)])
                    break
                
                elif 'story' in cmds:
                    while True:
                        speak(TarTalks.stories[randint(0,len(TarTalks.stories)-1)])
                        break

                elif 'screenshot' in cmds:
                    image = pyautogui.keyDown("win", "printscreen")
                    image = pyautogui.keyUp("win", "printscreen")
                    speak('Screenshot taken.')
                
                elif "stop listening" in cmds:
                    speak("For how many seconds do you want me to stop listening?")
                    wut = takeCommand()
                    time.sleep(int(wut))

                elif 'translate' in cmds:
                    from_lang = input("Which Language do you want to trnslate from>> ")
                    to_lang = "en"
                    get_sentence = takeCommand()
                    text_to_translate = transl.translate(get_sentence,
                                                                        src= from_lang,
                                                                        dest= to_lang)
                    text = text_to_translate.text
                    speak(text)

                elif 'calculate' in cmds or 'calculator' in cmds:
                    try:
                        r = sr.Recognizer()
                        my_mic_device = sr.Microphone(device_index=1)
                        with my_mic_device as source:
                            speak("Say what you want to calculate, example: 300 plus 100")
                            print("Speak...")
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                            my_string=r.recognize_google(audio)#who knows wt shit dis
                        print(my_string)
                        def get_operator_fn(op):
                            return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]
                        def eval_binary_expr(op1, oper, op2):
                            op1,op2 = int(op1), int(op2)
                            return (oper)(op1, op2)
                        speak(eval_binary_expr(*(my_string.split())))
                        print(eval_binary_expr(*(my_string.split())))
                    except:
                        speak("question is not in the right form")

                elif "weather" in cmds:
                    search = "temprature in banglore"
                    urlplace = f'https://google.com/search?q={search}'
                    r = requests.get(urlplace)
                    data = BeautifulSoup(r.text,"html.parser")
                    tempr = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {tempr}")
                
                elif 'recipe' in cmds:
                    speak("what food recipe are you looking for?")
                    print("Speak....")
                    input = takeCommand()
                    searches = f"https://www.allrecipes.com/article/how-to-make-{input}"
                    webbrowser.open(searches)
                
                elif 'empty recycle bin' in cmds or "empty the recycle bin" in cmds:
                     ws.recycle_bin().empty()
                     pyautogui.press("enter")

                elif "ip address" in cmds:
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    speak(f"Your ip address is {ip}")
                
                elif 'set timer' in cmds:
                    # countdown timer
                    def countdown(t):
                        while t:  # while t > 0 for clarity
                            mins = t // 60
                            secs = t % 60
                            timer = '{:02d}:{:02d}'.format(mins, secs)
                            print(timer, end="\r")  # overwrits previous line
                            time.sleep(1)
                            t -= 1
                        speak('timer Complete, Blast off!!')

                    speak("Please tell how many seconds to set the timer for.")
                    t = takeCommand()

                    countdown(int(t))

                elif 'where is' in cmds:
                    daplace = cmds.replace("where is", "")
                    url = 'https://google.nl/maps/place/' + daplace + '/&amp;'
                    try:
                       webbrowser.get().open(url)
                       speak('This is what I found')
                    except:
                         print('')

                elif 'search youtube' in cmds:
                    speakk = "What do you want me to search?"
                    speak(speakk)
                    yt = takeCommand()
                    speak('Searching for ' + yt)
                    url = 'https://www.youtube.com/results?search_query=' + yt
                    try:
                        webbrowser.get().open(url)
                        speak('This is what I found')
                    except:
                        print('')

                elif 'search' in cmds:
                    speak('Searching for ' + cmds.split('search')[1])
                    url = 'https://google.com/search?q=' + cmds.split('search')[1]
                    try:
                        webbrowser.get().open(url)
                        speak('This is what I found')
                    except:
                        print('')
Exe()
