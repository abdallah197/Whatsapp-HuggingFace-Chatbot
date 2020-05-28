from flask import Flask, request
import requests
from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

from twilio.twiml.messaging_response import MessagingResponse

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    for step in range(5):
        incoming_msg = request.values.get('Body', '').lower()

        new_user_input_ids = tokenizer.encode(incoming_msg + tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        resp = MessagingResponse()
        msg = resp.message()
        msg.body(f'{tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)}')
        return str(resp)


if __name__ == '__main__':
    app.run()
