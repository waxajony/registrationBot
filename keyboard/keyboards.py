from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

reg_start_btn = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = "Ro'yxatdan o'tish")
		],
	],
	resize_keyboard = True
)

share_contact = ReplyKeyboardMarkup(
	keyboard = [
			[
				KeyboardButton(text='Telefon raqamni yuborish', request_contact = True)
			],
		],
		resize_keyboard = True
	)