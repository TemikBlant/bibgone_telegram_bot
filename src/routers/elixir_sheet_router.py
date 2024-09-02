from aiogram import types
from aiogram import Router
from aiogram.filters import Command, CommandObject

from src.utils.answer_constructor import generate_simple_answer
from src.modules.elixit_sheet_module import elixir_sheet

elixir_sheet_router = Router()


@elixir_sheet_router.message(Command(commands=["calc_optimal_rewinds"]))
async def elixir_sheet_command(
    message: types.Message,
    command: CommandObject
):
    try:
        splitted_arg = command.args.split(" ")
        if len(splitted_arg) != 5:
            raise AttributeError
    except AttributeError:
        await message.answer('Проверь параметры команды. \n /calc_optimal_rewinds "уровень ем" "элик за рев" '
                             '"текущие скиллы" "необходимые скиллы" "учитывать БС"',
                             reply_to_message_id=message.message_id)
    else:
        result_from_elixir_sheet = elixir_sheet(*splitted_arg)
        await message.answer(
            generate_simple_answer(
                result_from_elixir_sheet
            ),
            reply_to_message_id=message.message_id
        )
