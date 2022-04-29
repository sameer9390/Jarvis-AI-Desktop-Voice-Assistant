import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)#0--boy,1--girl

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("I am Jarvis Sir . Please tell me how may i help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query
        
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sameerofficial058@gmail.com','sameergmail45')
    server.sendmail('sameerofficial058@gmail.com',to,content)
    server.close()
    
    

if __name__=="__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir='C:\\Users\\SAMEER\Music\\best music\\ArjitSingh'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir ,The time is {strTime}")    
        elif 'open code' in query:
            codePath="C:\\Users\\SAMEER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to sameer' in query:
            try:
                speak("What should i say ?")
                content=takeCommand()
                to="sameerbixby@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am unable to send this Email")
                
                