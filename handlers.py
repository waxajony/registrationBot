import asyncio
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from config import db

from states.reg_states import RegisterStates
from keyboard.keyboards import reg_start_btn, share_contact

rtr = Router()

@rtr.message(Command('start'))
async def start_comm(message: Message):
	
	user = db.get_user(message.from_user.id)
	if not user:
		msg = message.from_user
		db.add_user(tg_id=msg.id, tg_name=msg.first_name, tg_lastname=msg.last_name, username=msg.username)
		await message.answer(f"Assalomu alykum {msg.first_name}\nRo'yxatdan o'ting", reply_markup = reg_start_btn)	
	elif not user[8]:
		await message.answer(f"Ro'yxatdan o'ting", reply_markup = reg_start_btn)
	else:
		await message.answer('Siz qaytdingiz!')


## REGISTER ##
@rtr.message(F.text == "Ro'yxatdan o'tish")
async def register(message: Message, state=FSMContext):
	users = db.get_user(message.from_user.id)
	if users[8]:
		await message.answer('Siz royxatdan otgansiz', reply_markup = ReplyKeyboardRemove())
	else:
		await message.answer('Royxatdan otishni boshlaymiz', reply_markup = ReplyKeyboardRemove())
		await state.set_state(RegisterStates.regName)

@rtr.message(RegisterStates.regName)
async def reg_name(message: Message, state=FSMContext):
	await message.answer(f"Yaxshi {message.text} endi telni yuboring", reply_markup = share_contact)
	await state.update_data(regname=message.text)
	await state.set_state(RegisterStates.regPhone)

@rtr.message(RegisterStates.regPhone)
async def reg_phone(message: Message, state=FSMContext):
	try:
		await state.update_data(regphone = message.contact.phone_number)
		await message.answer('Yaxshi endi email', reply_markup = ReplyKeyboardRemove())
		await state.set_state(RegisterStates.regEmail)
	except:
	 	await message.answer('Tel raqamni yuboring', reply_markup = share_contact)

@rtr.message(RegisterStates.regEmail)
async def reg_email(message: Message, state=FSMContext):
	await state.update_data(regemail = message.text)
await await message.answer('Yaxshi endi tugulgan sananggiz', reply_markup = ReplyKeyboardRemove())
	await state.set_state(RegisterStates.regBday)

@rtr.message(RegisterStates.regBday)
async def reg_email(message: Message, state=FSMContext):
	try:
		await state.update_data(regbday = message.text)
	    reg_data = await state.get_data()
		reg_name = reg_data.get('regname')
		reg_phone = reg_data.get('regphone')
		reg_email = reg_data.get('regemail')
		reg_bday = reg_data.get('regbday')

		db.update_user(message.text.from_user.id, reg_name, reg_phone, reg_email, reg_bday)
		await message.answer("yaxshi! royxatdan o'ttiz")
		await state.clear()
	except:
		await message.answer('Boshqadan urinib koring', , reply_markup = ReplyKeyboardRemove())