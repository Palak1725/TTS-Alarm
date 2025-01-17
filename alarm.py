import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Voice = speaker.GetVoices().Item(2)

t = time.localtime()
print(t)
formatted_time = time.strftime("%I:%M:%S", t)

while formatted_time < "06:05:30":
    time.sleep(5) #waiting
    t = time.localtime()
    formatted_time = time.strftime("%I:%M:%S", t)
    print(formatted_time)

speaker.Speak("You gotta go!")

#%A, %d %B 
