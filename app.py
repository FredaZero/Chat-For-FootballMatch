# import chainlit as cl
# import requests

# RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# @cl.on_message
# async def main(message: cl.Message):
#     user_message = message
#     # message.content

#     # Send the user message to Rasa
#     response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})
    
#     if response.status_code == 200:
#         rasa_response = response.json()
#         if rasa_response:
#             bot_message = rasa_response[0].get('text', '')
#             await cl.Message(content=bot_message).send()
#         else:
#             await cl.Message(content="Sorry, I didn't understand that.").send()
#     else:
#         await cl.Message(content="Error communicating with Rasa server.").send()
from flask import Flask, render_template, request, Response, stream_with_context
import requests, json, time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def extract():
    def generate():
        text = str(request.form.get('value1'))
        payload = json.dumps({"sender": "Rasa", "message": text})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post("http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
        response = response.json()
        count = 0
        for message in response:
            print(message)
        for msg in response:
            if 'text' in msg:
                yield f"data: {msg['text']}\n\n"
                print(msg['text'], count)
                count += 1
                time.sleep(2)  # 等待 1 秒钟再发送下一条消息

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)

