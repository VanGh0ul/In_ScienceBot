from aiogram import types,Dispatcher
from create_bot import dp, bot
from aiogram import types
import requests
from bs4 import BeautifulSoup
import json

#@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):

	try:
		keyboardStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
		buttonbFindAgent = ["Найти сотрудника"]
		buttonsStart = ["Помощь", "Информация"]
		buttonsFile = ["Поиск по цели", "Удалить - цель по индексу"]
		keyboardStart.add(*buttonsStart).add(*buttonbFindAgent).add(*buttonsFile)
		await bot.send_message(message.from_user.id, 'Данный сервис предназначен для анализа и обработки сообщений💬 \nНажмите Найти сотрудника👨‍🔬 \nДалее введите ФИО сотрудника для уточнения!', reply_markup=keyboardStart)

	except:
		await message.reply('Произошла ошибка,следите за информацией в :\nhttps://t.me/inscience_news')
		#await message.reply('Общение с ботом через ЛС, напишите ему:\nhttp://t.me/IN_SCIENCEBot')


async def info_command(message : types.Message,):

	info = "inScience - система анализа достижений ученых\n \nВ inScience можно быстро получить основную информацию о научных публикациях по наукометрическим базам WoS, Scopus, Elibrary. Работа с inScience проходит в обычном веб-браузере, а это значит, что платформа и аналитика доступны пользователям и вне сети ВУЗа.\n \nДля того, чтобы воспользоваться тестовой версией нашей системы нужно перейти в браузере по адресу https://inscience.kovalev.team";
	await bot.send_message(message.from_user.id, info)

		
#Регистраци хендов
def register_handlers_menu(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start','help'])
	dp.register_message_handler(command_start,lambda message: message.text == "Помощь")
	dp.register_message_handler(info_command,lambda message: message.text == "Информация")
	#dp.register_message_handler()