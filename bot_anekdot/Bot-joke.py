import telebot
import random
token = "669101268:AAHqgVIfW5M6NyyqtD3HJav46g-2tmgT9xc"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
bot = telebot.TeleBot(token=token)
@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    user = message.chat.id
    with open('Анекдот1.txt')as f:
        a = f.read()
    with open('Анекдот2.txt')as f:
        b = f.read()
    with open('Анекдот3.txt')as f:
        c = f.read()
    with open('Анекдот4.txt')as f:
        d = f.read()
    with open('Анекдот5.txt')as f:
        e = f.read()
    with open('Анекдот6.txt')as f:
        z = f.read()
    rand = [a, b, c, d, z, e]
    if text == '/start' or text=='/help':
        bot.send_message(user,'Напиши /anek для получения анекдота')
    elif text =='/anek':
        bot.send_message(user,random.choice(rand))
    else:
        bot.send_message(user,'Хоу, хэй, лалалэй')

bot.polling(none_stop=True)
