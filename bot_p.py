import  textimageapi
import telebot
import  db
from telebot import types
TOKEN = '7084003544:AAFBwstlctq2cwX-qeoLtKbLAv9qMfZos6A'
bot = telebot.TeleBot(TOKEN)
rob =textimageapi.Text2ImageAPI('https://api-key.fusionbrain.ai/', '206AC6ED02E983F19B808E650CEF4817', '5ADDB25A31AC4CDC1B4F16339AFF94ED')

@bot.message_handler(commands= ['start'])
def start(messeg):
    db.table()
    db.add_user(messeg.chat.id)
    bot.send_message(messeg.chat.id,'Напишите сообщение и бот в ответ вам сгенерирует фотографию', reply_markup=main_menu())

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('👤 Профиль'),
            types.KeyboardButton('🎟 Добавить попытки'),
        )
    return markup

@bot.message_handler(regexp='[а-яА-Яa-zA-Z0-9 ]+')
def handle_message(message):
        balance = db.balance(message.chat.id)
        if balance != 0:
            model = rob.get_model()
            gen = rob.generate(message.text, model)
            chek = rob.check_generation(gen)[0]
            textimageapi.cod_to_png(chek, '1.png')
            bot.send_photo(message.chat.id, photo=open('1.png', 'rb'))
            balance = balance - 1
            db.update_balance(balance,message.chat.id)

        else:
            bot.send_message(message.chat.id,'У вас не осталось попыток')

@bot.message_handler(func=lambda message: message.text == '👤 Профиль')
def profil(message):
        bot.send_message(message.chat.id, 'Ваш профиль')
        bot.send_message(message.chat.id,f'Ваше имя: {message.from_user.first_name}\nВаш никнейм: {message.from_user.username}\nВаш id: {message.from_user.id}')
        if message.from_user.is_premium == None:
            bot.send_message(message.chat.id, 'Телеграм премиум отсутсвует')
        else:
            bot.send_message(message.chat.id, 'Телеграм премиум активирован')


bot.polling()









