# Amigo
A bot that talks and listens to you, and works through your emotions

## Problem statement, and why this bot?
A lot of people in today's world have to live alone and have no one to talk to. Also, with the current advance in technology voice-based services like Alexa have become very popular.
Amigo is a voice based service itself, with an additional feature of having facial recognition security, perform certain simple tasks and being able to play songs based on the mood the person is in, just like a friend (hence the name Amigo, which means friend in Spanish).

## Flow of the project
1. Run "bot.py" file
&nbsp; You would see the main page with 2 options : 
<br />a. New User
<br />b. Authenticate

![image](https://user-images.githubusercontent.com/88290216/170872651-b4a97145-a008-486f-9752-5271daa26a82.png)

2. Since we're using the program for the first time, click on "New User"
&nbsp; You would see two options:
<br />a. Take Samples
<br />b. Model Training

![image](https://user-images.githubusercontent.com/88290216/170872904-ef62c6a2-c1d2-47f8-82ee-ef9f590204c5.png)

3. Click on "Take Samples" button. It would open a camera, recognise and take pictures of your face
4. Click on "Model Training" next. It would train the model so that the program recognises your face when you try to authenticate.
5. Once the program says "Model training successful", click on the "Back" button. You would see the main page again
6. Now click on "Authenticate" button. Make sure your face is in front of the camera so that it can recognise it. It also recognises the emotion on your face.
7. After the authentication is successful, you would see the main command-execution window.

![image](https://user-images.githubusercontent.com/88290216/170872676-ca84b3af-aa48-4d97-9966-c4e28963657e.png)

8. Click on "Speak" and try out commands like
&nbsp; <br />a. Open camera
&nbsp; <br />b. Open Spotify
&nbsp; <br />c. Open Notepad
&nbsp; <br />d. Open Calculator
&nbsp; <br />e. Search something on wikipedia
&nbsp; <br />f. Open Google
&nbsp; <br />g. Open Youtube
&nbsp; <br />h. Play music, etc

Here, the bot would play music according to the emotion you have, so you would get a different playlist for each mood the program recognises you in.
<br />
Additionally, all the details of the command-execution conversation is dynamically displayed as "logs" in the console of your IDE (VS Code in my case).
<br />One instance of the console:<br />
<br />Collecting samples. Please face the camera...
<br />Samples collected successfully.
<br />Model training in progress...
<br />Model training successful.
<br /><br />
<br />1/1 [==============================] - ETA: 0s
<br />1/1 [==============================] - 0s 149ms/step
<br />Face recognition performed successfully.
<br />Good Evening, Nidhi
<br />How may I help you?
<br />Say something...
<br />Analyzing...
<br />User:  open camera
<br />[ WARN:0@110.600] global D:\a\opencv-python\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (539) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback
<br />Say something...
<br />Analyzing...
<br />User:  notepad
<br />Say something...
<br />Analyzing...
<br />User:  open calculator
<br />Say something...
<br />Analyzing...
<br />User:  set as open the calculator open Notepad
<br />Say something...
<br />Analyzing...
<br />User:  open Google
<br />Say something...
<br />Analyzing...
<br />User:  this is how it is opening by
<br />Say something...
<br />Analyzing...
<br />User:  bye Amigo
<br />Goodbye, Nidhi. Have a great day.

## Libraries installed
* pyttsx3
* SpeechRecognition
* pyaudio
* opencv-python
* wikipedia
* pyinstaller
* tensorflow
* deepface
* tkinter
* pillow
* pyautogui
* numpy

