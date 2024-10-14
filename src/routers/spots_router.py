from aiogram import types
from aiogram import Router
from aiogram.filters import Command, CommandObject

from src.utils.answer_constructor import generate_simple_answer
from src.modules.spots_module import SpotsModule

spots_router = Router()
spots = SpotsModule()


@spots_router.message(Command(commands=["optimal_spot"]))
async def optimal_spot_command(
        message: types.Message,
        command: CommandObject
):
    try:
        splitted_args = command.args.split(" ")

        if len(splitted_args) != 3:
            raise AttributeError

        day_start = int(splitted_args[0])
        days_range = int(splitted_args[1])
        titor_speed = float(splitted_args[2])

    except AttributeError:
        await message.answer('Проверь параметры команды. \n /optimal_spot "Стартовый день" "диапазон дней" '
                             '"ускорение игры от титора от 1 до 1.2"',
                             reply_to_message_id=message.message_id)
    else:
        best_spot = spots.best_spot(day_start, days_range, titor_speed)
        await message.answer(
            generate_simple_answer(
                best_spot
            ),
            reply_to_message_id=message.message_id
        )


@spots_router.message(Command(commands=["detailed_spots"]))
async def detailed_spots_command(
        message: types.Message,
        command: CommandObject
):
    try:
        splitted_args = command.args.split(" ")

        if len(splitted_args) != 3:
            raise AttributeError

        day_start = int(splitted_args[0])
        double_rewind = bool(splitted_args[1])
        titor_speed = float(splitted_args[2])

    except AttributeError:
        await message.answer('Проверь параметры команды. \n /optimal_spot "Стартовый день" "диапазон дней" '
                             '"ускорение игры от титора от 1 до 1.2"',
                             reply_to_message_id=message.message_id)
    else:
        best_spot = spots.detailed_spot(day_start, double_rewind, titor_speed)
        await message.answer(
            generate_simple_answer(
                best_spot
            ),
            reply_to_message_id=message.message_id
        )


@spots_router.message(Command(commands=["spots"]))
async def spots_command(
        message: types.Message,
        command: CommandObject
):
    try:
        splitted_args = command.args.split(" ")

        if len(splitted_args) != 3:
            raise AttributeError

        day_start = int(splitted_args[0])
        day_range = int(splitted_args[1])
        titor_speed = float(splitted_args[2])

    except AttributeError:
        await message.answer('Проверь параметры команды. \n /optimal_spot "Стартовый день" "диапазон дней" '
                             '"ускорение игры от титора от 1 до 1.2"',
                             reply_to_message_id=message.message_id)
    else:
        best_spot = spots.spots(day_start, day_range, titor_speed)
        # await message.answer(
        #     generate_simple_answer(
        #         best_spot
        #     ),
        #     reply_to_message_id=message.message_id
        # )
