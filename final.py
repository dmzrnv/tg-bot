import telebot
from circle import circle

TOKEN = "5912106944:AAGwwzGcZ3h2-9tHDXf-qIyrxPbSUS-MQTU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def sendWelcome(message):
    bot.reply_to(message, "Добро пожаловать! Отправьте команду /help для справки!")
    

help = """/help - справка
/length <радиус окружности> - вычисляет длину окружности
/area <радиус окружности> - вычисляет площадь окружности
/do_intersect <x1> <y1> <radius1> <x2> <y2> <radius2> - вычисляет пересекаются ли окружности
/is_equal <x1> <y1> <radius1> <x2> <y2> <radius2> - вычисляет, равны ли окружности
"""
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, help)


@bot.message_handler(commands=['length'])
def send_length(message):
    radius = float(message.text.split(' ')[1])
    length = circle.lengthFromRadius(radius)
    bot.reply_to(message, f'Длина окружности с радиусом {radius} составляет {length}')

@bot.message_handler(commands=['area'])
def send_area(message):
    radius = float(message.text.split(' ')[1])
    area = circle.areaFromRadius(radius)
    bot.reply_to(message, f'Площадь окружности с радиусом {radius} составляет {area}')

@bot.message_handler(commands=['do_intersect'])
def send_do_intersect(message):
     x1,y1,radius1,x2,y2,radius2 = map(float, message.text.split(' ')[1:])
     c1 = circle(x1, y1, radius1)
     c2 = circle(x2, y2, radius2)
     is_intersect = c1.do_intersect(c2)
     bot.reply_to(message, f'Окружности {"" if is_intersect else "не "}пересекаются')

@bot.message_handler(commands=['is_equal'])
def send_is_equal(message):
     x1,y1,radius1,x2,y2,radius2 = map(float, message.text.split(' ')[1:])
     c1 = circle(x1, y1, radius1)
     c2 = circle(x2, y2, radius2)
     is_equal = c1 == c2
     bot.reply_to(message, f'Окружности {"" if is_equal else "не "}равны')

bot.polling()