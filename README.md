To deploy my Text-to-Speech Translation app, I utilized Visual Studio Code (VS Code) as my primary development environment. my app serves the purpose of translating text to speech in Southeast Asian (SEA) languages, specifically Tagalog and Malay. Users can input text in either language and select their desired output language, including English. This capability allows for translations between Tagalog and Malay, as well as English and both Tagalog and Malay.

The main components of my application include an HTML interface (index.html) and a Flask backend (app.py). The HTML file provides a user-friendly interface for inputting text and selecting the desired output language. Meanwhile, the Flask backend handles the translation and text-to-speech conversion using libraries such as googletrans and gTTS.

For the deployment process, i utilized Render, a platform for hosting web applications. I first pushed my application code to GitHub and then linked my GitHub repository to Render. This integration allowed me to easily deploy my app on Render's infrastructure. With Render, I ensured my app's availability and scalability, providing a seamless experience for users to access my text-to-speech translation service. 

I recommend if the code fails on the website link,you can try deploying through render or pythoneverywhere.


website links: Running on http://127.0.0.1:10000
               Running on http://10.223.40.187:10000
