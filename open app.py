import pyttsx3
import os
engine=pyttsx3.init()
pyttsx3.speak("Enter number to open application")
while True:
    print("Enter number to open application")
    print("\n1.NOTEPAD \t 2.MICROSOFT EDGE \n\t 3.SOLITAIRE \t 4.ZOOM \t 5.GOOGLE CHROME \t 6.WHATSAPP \t 0.exit")
    p=input()
    p=p.upper()
    print(p)
    if("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        continue
    elif("5" in p):
        os.system("start chrome")
    elif("2" in p):
        os.system("start msedge")
    elif("6" in p):
        os.system("start WhatsApp")
    elif ("1" in p):
        os.system("start Notepad")
    elif ("3" in p):
        os.system("start Solitaire")
    elif ("4" in p):
        os.system("start Zoom")
    elif ("0" in p):
        os.system("Exiting")
        break
    else:
        pyttsx3.speak(p)
        print("Is invalid.Please Try Again")
        pyttsx3.speak("Is Invalid.Please try again")