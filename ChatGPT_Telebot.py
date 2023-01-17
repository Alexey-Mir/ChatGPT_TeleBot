import telebot
import openai

openai.api_key = 'ENTER_YOUR_API_KEY'
bot = telebot.TeleBot("ENTER_YOUR_API_KEY")

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    print(message)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.polling()
