import speech_recognition as sr
import pyttsx3
from datetime import date,datetime
engine = pyttsx3.init()
robot_ear = sr.Recognizer()
robot_brain = ""
while True:
    with sr.Microphone() as source:
        print("Robot:I'm listening")
        audio = robot_ear.listen(source)
    print('Robot:....')
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    if you == " ":
        robot_brain = 'I can"t hear you , try again '
    elif 'Hello' in you:
        robot_brain = "Hello quyet"
    elif "today" in you :
        today = date.today()
        robot_brain = today.strftime("%B %d ,%y")
    elif "time" in you:
        time = datetime.now()
        robot_brain = time.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain = "Joe Biden"
    elif "bye" in you:
        robot_brain = "bye quyet"
        break
    else:
        robot_brain = "I'm fine thank you,and you"
    print("You:",you)
    print("Robot:",robot_brain)
    engine.say(robot_brain)
    engine.runAndWait()
