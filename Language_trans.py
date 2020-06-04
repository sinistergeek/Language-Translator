print('''

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.____                                                             
|    |   _____    ____  __ __  ____  __ _______     ____   ____   
|    |   \__  \  /    \|  |  \/ ___\|  |  \__  \   / ___\_/ __ \  
|    |___ / __ \|   |  \  |  / /_/  >  |  // __ \_/ /_/  >  ___/  
|_______ (____  /___|  /____/\___  /|____/(____  /\___  / \___  > 
        \/    \/     \/     /_____/            \//_____/      \/  
_________                                   __                    
\_   ___ \  ____   _______  __ ____________/  |_  ___________     
/    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\/ __ \_  __ \    
\     \___(  <_> )   |  \   /\  ___/|  | \/|  | \  ___/|  | \/    
 \______  /\____/|___|  /\_/  \___  >__|   |__|  \___  >__|       
        \/            \/          \/                 \/           
        
Made By: Sinister Geek!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')


from tkinter import *
from tkinter.filedialog import askopenfilename
import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
import sys

print('''
1 - Convert Video into audio In .mp3 and wav
2 - Convert mp3 into text file 
3 - Open Language translation

''')
choices = int(input("Enter the Number :"))
try:
    if choices == 1:


        def video_to_audio():

            print("Select a Video to convert into wav file")
            Tk().withdraw()
            file_location_video = askopenfilename()

                #select the file from Drive!!
            clip = mp.VideoFileClip(file_location_video)

            input_audio = input(print("Output audio file name:  "))

            audio_render = clip.audio.write_audiofile(input_audio)
            print("Your Audio Has Been Complete Rendering!!!\n\n")

        video_to_audio()
    #Convert audio to text
    #works with .wav file
    elif choices == 2:
        print("Audio to text Converter")
        print("Use .wav audio for generating")
        def audio_to_text():

            Tk().withdraw()
            file_location_audio = askopenfilename()

            r = sr.Recognizer()
            with sr.AudioFile(file_location_audio) as source:

                print("listening audio file....")
                audio = r.record(source)
                try:
                    text = r.recognize_google(audio)
                    print("Example lame.text")
                    user_audio = input(print("Enter the filename to save"))
                    print("Please, Wait audio has been translating to text")
                    f = open(user_audio,"w")
                    f.write(str(text))
                except:
                    print("Try again!!")
        audio_to_text()


    #Last part where translatio happen
    elif choices == 3 :
        print("Open the text file location")
        def text_trans():

            Tk().withdraw()
            file_location_text = askopenfilename()

            f = open(file_location_text,"r")
            if f.mode == "r":
                content = f.read()
                translator = Translator()
                print('''
                Language Name	Language Code
                Afrikaans	    af
                Irish	        ga
                Albanian	    sq
                Italian	        it
                Arabic	        ar
                Japanese	    ja
                Azerbaijani	    az
                Kannada	        kn
                Basque	        eu
                Korean	        ko
                Bengali	        bn
                Latin	        la
                Belarusian	    be
                Latvian	        lv
                Bulgarian	    bg
                Lithuanian	    lt
                Catalan	        ca
                Macedonian	    mk
                Chinese Simplified	zh-CN
                Malay	        ms
                Chinese Traditional	zh-TW
                Maltese	        mt
                Croatian	    hr
                Norwegian	    no
                Czech	        cs
                Persian	        fa
                Danish	        da
                Polish	        pl
                Dutch	        nl
                Portuguese	    pt
                English	        en
                Romanian	    ro
                Esperanto	    eo
                Russian	        ru
                Estonian	    et
                Serbian	        sr
                Filipino	    tl
                Slovak	        sk
                Finnish	        fi
                Slovenian	    sl
                French	        fr
                Spanish	        es
                Galician	    gl
                Swahili	        sw
                Georgian	    ka
                Swedish	        sv
                German	        de
                Tamil	        ta
                Greek	        el
                Telugu	        te
                Gujarati	    gu
                Thai	        th
                Haitian Creole	ht
                Turkish	        tr
                Hebrew	        iw
                Ukrainian	    uk
                Hindi	        hi
                Urdu	        ur
                Hungarian	    hu
                Vietnamese	    vi
                Icelandic	    is
                Welsh	        cy
                Indonesian	    id
                Yiddish	        yi
                ''')
                print("What is the name type of text file is written??")
                sources = input(print("Enter source language eg: en for english"))
                print("Which language do you want to convert to??")
                destination = input(print("Enter the destination language eg: es for spanhish"))
                translatorPage = translator.translate(content,src='en', dest ='es')
                #For saving File!!
                file_name_to_save=input("Enter the file name")
                p=open(file_name_to_save, "w")
                p.write(str(translatorPage))
                print("Your File has been save")
                p.close
        text_trans()
    else:
        print("Look at the menu care fully!!")

except ValueError:
    print("Don't use strings!! \n *!warning!*")

