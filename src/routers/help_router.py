from aiogram import types
from aiogram import Router
from aiogram.filters import Command, CommandObject

from src.models.common_models import NameValueModel
from src.utils.answer_constructor import generate_multi_simple_answer, generate_str_answer

help_router = Router()

commands_list = [
    NameValueModel(name='/multiplier', value='считает сколько даст дней хУрона'),
    NameValueModel(name='/calc_optimal_rewinds', value='считает оптимальное количестов ревов'),
    NameValueModel(name='/optimal_spot', value='высчитывает оптимальный спот для n+k дней'),
]


@help_router.message(Command(commands=["commands"]))
async def commands_command(
        message: types.Message
):
    await message.answer(
        generate_multi_simple_answer(
            commands_list
        ),
        reply_to_message_id=message.message_id
    )


@help_router.message(Command(commands=["multiplier_help"]))
async def multiplier_help_command(
        message: types.Message
):
    answer = "Считает, сколько дней прогресса даст множитель урона.\n" \
             "Комманда - '/multiplier arg1'\n" \
             "arg1 - множитель урона (число > 1)"
    await message.answer(
        generate_str_answer(
            answer
        ),
        reply_to_message_id=message.message_id
    )
