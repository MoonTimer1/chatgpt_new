import openai
import telebot

openai.api_key = 
bot = telebot.TeleBot ("")

@bot.message_handler(func-lambda_: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt message.text,
        temperature=0.5,
        max_tokens 1000,
        top_p=1.0,
        frequency penalty=0.5,
        presenceIpenalty=0.0,
        )
        bot.send_message(chat_id=message.from. response['choices'][0]['text'])
bot.polling(none_stop=True)