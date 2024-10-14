from aiogram import types
from aiogram import Router
from aiogram.filters import Command, CommandObject

from src.utils.answer_constructor import generate_str_answer
from src.modules.damage_module import multiplier

damage_router = Router()


@damage_router.message(Command(commands=["multiplier"]))
async def multiplier_command(
    message: types.Message,
    command: CommandObject
):
    try:
        splitted_arg = command.args.split(" ")
        if len(splitted_arg) != 1:
            raise AttributeError
        damage_multi = float(splitted_arg[0].replace(',', '.'))
        if damage_multi < 1:
            raise ValueError
    except AttributeError:
        await message.answer('Проверь параметры команды. \n /multiplier "множитель урона"',
                             reply_to_message_id=message.message_id)
    except ValueError:
        await message.answer('Проверь параметры команды. \n /multiplier. Параметр "множитель урона" должен быть'
                             ' числом и быть больше 1',
                             reply_to_message_id=message.message_id)
    else:
        days = multiplier(damage_multi)
        await message.answer(
            generate_str_answer(
                days
            ),
            reply_to_message_id=message.message_id
        )


@damage_router.message(Command(commands=["нармулес_душнила"]))
async def multiplier_command(
    message: types.Message,
    command: CommandObject
):
    await message.answer(
        generate_str_answer(
            "Да"
        ),
        reply_to_message_id=message.message_id
    )