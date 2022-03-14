import telebot
from main import make_qr
bot = telebot.TeleBot('YOUR TOKEN')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне текст, чтобы я преобразовал его в QR-код.") 
@bot.message_handler(content_types=['text'])
def menu(message):    
        make_qr(message.text)
        #print(message.text)
        bot.send_photo(message.chat.id, photo=open('readyqr.png', 'rb'), caption='Вот твой QR-код!')

bot.polling(none_stop=True)
