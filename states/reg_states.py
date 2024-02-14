from aiogram.fsm.state import StatesGroup, State

class RegisterStates(StatesGroup):
	regName = State()
	regPhone = State()
	regEmail = State()
	regBday = State()