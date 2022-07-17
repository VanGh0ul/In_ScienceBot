from aiogram import types,Dispatcher
from create_bot import dp, bot
import requests
import telebot
import json


#@dp.message_handler()


async def echo_send(message : types.Message):
	await message.reply('Я не знаю что на это ответить😢 \n \nВоспользуйтесь командой /help')

def register_handlers_echoHelp(dp : Dispatcher):
	dp.register_message_handler(echo_send)
