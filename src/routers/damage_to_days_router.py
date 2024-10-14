from aiogram import types
from aiogram import Router
from aiogram.filters import Command, CommandObject

from src.utils.answer_constructor import generate_str_answer
from src.modules.damage_to_days_module import damage_to_days

damage_to_days_router = Router()


@damage_to_days_router.message(Command(commands=["damage_to_days"]))
async def damage_to_days_coomand(
    message: types.Message,
    command: CommandObject
):
    try:
        splitted_arg = command.args.split(" ")
        if len(splitted_arg) != 1:
            raise AttributeError
        damage_multi = int(splitted_arg[0])
    except AttributeError:
        await message.answer('Проверь параметры команды. \n /damage_to_days "множитель дней"',
                             reply_to_message_id=message.message_id)
    else:
        days = damage_to_days(damage_multi)
        await message.answer(
            generate_str_answer(
                days
            ),
            reply_to_message_id=message.message_id
        )
