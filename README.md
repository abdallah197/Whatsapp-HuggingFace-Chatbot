# :fire::fire: Whatsapp-HuggingFace-Chatbot :fire::fire:
Using [DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium) dialogue response generation model by Microsoft to build a chatbot and integrate it with WhatsApp.

![Demo](images/chatbot.gif)


## Overview
The project uses the [Twilio API for Whatsapp](https://www.twilio.com/whatsapp) [1] together with
[Flask web application framework](https://palletsprojects.com/p/flask/) to handle sending
and receiving messages to WhatsApp. And [Huggingface](https://huggingface.co/) 
implementation of DialoGPT which is a large-scale pretrained dialogue response generation model
for multiturn conversations. 

## Installation
* Clone the repo <br/>
`git clone https://github.com/abdallah197/Whatsapp-HuggingFace-Chatbot.git`
* To Install all requirements run
```
pip install -r requirements.txt
sudo snap install ngrok
```

### Want to give the chatbot a try?



