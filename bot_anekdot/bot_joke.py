import telebot
import random

token = "669101268:AAHqgVIfW5M6NyyqtD3HJav46g-2tmgT9xc"

# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)

# content_types=['text'] - сработает, если нам прислали текстовое сообщение
@bot.message_handler(content_types=['text'])
def echo(message):
    # message - входящее сообщение
    # message.text - это его текст
    # message.chat.id - это номер его автора
    text = message.text
    user = message.chat.id

    #отправляем картинку с попугаем
    #отправляем сообщение тому же пользователю с тем же текстом
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
    if text =='/anek':
        bot.send_message(user,random.choice(rand))
        

# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)
