from math import log2


def damage_to_days(damage):
    return f'Множитель урона x{damage} даст {int(log2(damage) * 11)} дней'
