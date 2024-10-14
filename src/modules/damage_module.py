from math import log2


def multiplier(damage):
    return f'Множитель урона x{damage} даст {round(log2(damage) * 11)} дней'
