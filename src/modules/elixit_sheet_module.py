from src.constants.shared_constants import levels
from src.models.common_models import NameValueModel


def elixir_sheet(
        em_level: str,
        elixir_per_rewind: str,
        all_skills_old: str,
        all_skills_new: str,
        include_boss_slayer: bool,
):

    em_level = em_level.lower()
    elixir_per_rewind = elixir_per_rewind.lower()
    all_skills_old = all_skills_old.lower()
    all_skills_new = all_skills_new.lower()

    def sn(p, b):
        return int(p * ((2 * (b * 5) + (p - 1) * 5) / 2))

    def newem(
            em_level_int: int,
            elixir_rew_int: int
    ):
        p = 1
        em_copy = em_level_int
        while sn(p, em_level_int) < elixir_rew_int and len(str(sn(p, em_level_int))) < len(str(elixir_rew_int)):
            p *= 10

        p //= 10
        p = int(p)
        prev = 0
        num_length = len(str(p))

        while sn(p, em_level_int) <= elixir_rew_int:
            p += 10 ** (num_length - 1)
            if sn(p, em_level_int) == prev:
                break
            prev = sn(p, em_level_int)
            if sn(p, em_level_int) > elixir_rew_int:
                p -= 10 ** (num_length - 1)
                if num_length > 1:
                    num_length -= 1

        p += em_copy
        em_multi = em_level_int / p

        return em_multi, p

    def funni_loop(min_rew: int, skills_int: float, em_level_int: int, elixir_rew_int: int, old_multi: int):
        i = 0
        min_skill = 0

        while True:
            em_multi, p = newem(em_level_int=em_level_int, elixir_rew_int=elixir_rew_int)
            em_rewinds = i
            skill_rewinds = skills_int / elixir_rew_int

            if min_rew > skill_rewinds + em_rewinds:
                min_rew = skill_rewinds + em_rewinds
                min_skill = skill_rewinds
            else:
                min_rew -= 1
                em_rewinds -= 1
                em_level_int *= old_multi
                em_level_int = int(em_level_int)
                elixir_rew_int *= old_multi
                elixir_rew_int = int(elixir_rew_int)
                break

            em_level_int /= em_multi
            em_level_int = int(em_level_int)
            elixir_rew_int /= em_multi
            elixir_rew_int = int(elixir_rew_int)
            old_multi = em_multi

            i += 1

        return min_rew, min_skill, em_rewinds, em_level_int, elixir_rew_int

    def nice_output(prim: int, secun: int):
        prim_suffix = ''

        while prim > 1000:
            prim /= 1000
            prim_suffix = levels[levels.index(prim_suffix) + 1]
        nice_em_level = prim

        secun_suffix = ''
        while secun > 1000:
            secun /= 1000
            secun_suffix = levels[levels.index(secun_suffix) + 1]

        nice_secun = secun

        return nice_em_level, prim_suffix, nice_secun, secun_suffix

    print("am inceput timeru fraiere")

    try:
        all_skills_old_suffix = '' if all_skills_old[-1].isdigit() else (all_skills_old[-1:] if all_skills_old[-2].isdigit() else all_skills_old[-2:])
        all_skills_old_int = abs(float(all_skills_old) if all_skills_old[-1].isdigit() else (float(all_skills_old[:-1]) if all_skills_old[-2].isdigit() else abs(float(all_skills_old[:-2]))))
        all_skills_old_int *= (1000 ** (levels.index(all_skills_old_suffix))) * 2

        all_skills_new_suffix = '' if all_skills_new[-1].isdigit() else (all_skills_new[-1:] if all_skills_new[-2].isdigit() else all_skills_new[-2:])
        all_skills_new_int = abs(float(all_skills_new) if all_skills_new[-1].isdigit() else (float(all_skills_new[:-1]) if all_skills_new[-2].isdigit() else abs(float(all_skills_new[:-2]))))
        all_skills_new_int *= ((1000 ** (levels.index(all_skills_new_suffix))) * 2)
        all_skills_new_int -= 2

        skills_int = ((((all_skills_new_int + 2) / 2 - all_skills_old_int / 2) / 2) * (all_skills_old_int + all_skills_new_int)) * 5
        skills_int2 = ((((all_skills_new_int + 2) / 2 - all_skills_old_int / 2) / 2) * (all_skills_old_int + all_skills_new_int)) * 6

        em_level_suffix = '' if em_level[-1].isdigit() else (em_level[-1:] if em_level[-2].isdigit() else em_level[-2:])
        original_em_suffix = em_level_suffix
        em_level_int = abs(float(em_level) if em_level[-1].isdigit() else (float(em_level[:-1]) if em_level[-2].isdigit() else abs(float(em_level[:-2]))))
        original_em_level = em_level_int
        em_level_int *= 1000 ** (levels.index(em_level_suffix))
        original_em_multi = em_level_int

        elixir_rew_suffix = '' if elixir_per_rewind[-1].isdigit() else (elixir_per_rewind[-1:] if elixir_per_rewind[-2].isdigit() else elixir_per_rewind[-2:])
        original_rewind_suffix = elixir_rew_suffix
        elixir_rew_int = abs(float(elixir_per_rewind) if elixir_per_rewind[-1].isdigit() else (float(elixir_per_rewind[:-1]) if elixir_per_rewind[-2].isdigit() else abs(float(elixir_per_rewind[:-2]))))
        original_rewind_level = elixir_rew_int
        elixir_rew_int *= 1000 ** (levels.index(elixir_rew_suffix))

        em_level_int = int(em_level_int)
        elixir_rew_int = int(elixir_rew_int)
    except ValueError:
        return 0

    if elixir_rew_int == 0.0 or em_level_int == 0.0 or all_skills_new_int == 0.0 or all_skills_old_int == 0.0:
        print('UNDE ESTE ANDY?')
        return 0

    print("intru in loop fraiere")

    p = 1
    old_multi = 1

    all_skills_old_int = abs(float(all_skills_old) if all_skills_old[-1].isdigit() else (float(all_skills_old[:-1]) if all_skills_old[-2].isdigit() else abs(float(all_skills_old[:-2]))))
    all_skills_new_int = abs(float(all_skills_new) if all_skills_new[-1].isdigit() else (float(all_skills_new[:-1]) if all_skills_new[-2].isdigit() else abs(float(all_skills_new[:-2]))))
    print("merge?")
    while original_rewind_level >= 1000:
        original_rewind_level /= 1000
        original_rewind_suffix = levels[levels.index(original_rewind_suffix) + 1]

    while original_rewind_level < 1:
        original_rewind_level *= 1000
        original_rewind_suffix = levels[levels.index(original_rewind_suffix) - 1]

    while original_em_level >= 1000:
        original_em_level /= 1000
        original_em_suffix = levels[levels.index(original_em_suffix) + 1]

    while original_em_level < 1:
        original_em_level *= 1000
        original_em_suffix = levels[levels.index(original_em_suffix) - 1]

    while all_skills_old_int < 1:
        all_skills_old_int *= 1000
        all_skills_old_suffix = levels[levels.index(all_skills_old_suffix) - 1]

    while all_skills_new_int < 1:
        all_skills_new_int *= 1000
        all_skills_new_suffix = levels[levels.index(all_skills_new_suffix) - 1]

    while all_skills_old_int >= 1000:
        all_skills_old_int /= 1000
        all_skills_old_suffix = levels[levels.index(all_skills_old_suffix) + 1]

    while all_skills_new_int >= 1000:
        all_skills_new_int /= 1000
        all_skills_new_suffix = levels[levels.index(all_skills_new_suffix) + 1]

    if levels.index(all_skills_old_suffix) > levels.index(all_skills_new_suffix):
        print("TALPA N PIEPT MERITI")
        return 0
    elif levels.index(all_skills_old_suffix) == levels.index(all_skills_new_suffix):
        if all_skills_old_int > all_skills_new_int:
            print("TALPA N PIEPT MERITI")
            return 0

    # skill_days = 2 * log((all_skills_new_int * 1000 ** (levels.index(all_skills_new_suffix) - levels.index(all_skills_old_suffix)))
    #                      / all_skills_old_int * (milestone ** (round(math.log(all_skills_new_int * (1000 ** (levels.index(all_skills_new_suffix) -
    #                                                                                                          levels.index(all_skills_old_suffix))), 10)) - math.floor(math.log(all_skills_old_int, 10)))), 2) * 11

    # skill_days += log((all_skills_new_int * 1000 ** (levels.index(all_skills_new_suffix) - levels.index(all_skills_old_suffix)))
    #                   / all_skills_old_int * (3 ** (round(math.log(all_skills_new_int * (1000 ** (levels.index(all_skills_new_suffix) -
    #                                                                                               levels.index(all_skills_old_suffix))), 10)) - math.floor(math.log(all_skills_old_int, 10)))), 2) * 11

    # skill_days += 4 * log((all_skills_new_int * 1000 ** (levels.index(all_skills_new_suffix) - levels.index(all_skills_old_suffix)))
    #                       / all_skills_old_int * (2 ** (round(math.log(all_skills_new_int * (1000 ** (levels.index(all_skills_new_suffix) -
    #                                                                                                   levels.index(all_skills_old_suffix))), 10)) - math.floor(math.log(all_skills_old_int, 10)))), 2) * 11
    # print(skill_days)
    print("haha loop1")
    min_rew, min_skill, em_rewinds, em_level_int, elixir_rew_int = funni_loop(10 ** 200, skills_int, em_level_int, elixir_rew_int,
                                                                              old_multi=old_multi)
    if min_skill > 10 ** 12:
        print("FABRICA DE BELELE")
        return 0

    if elixir_rew_int == 0:
        print("PETRECEREA I GATA MA")
        return 0
    print("haha loop1 ok")

    nice_em_level, em_level_suffix, nice_rewind_level, elixir_rew_suffix = nice_output(em_level_int, elixir_rew_int)

    print("haha loop2")
    if include_boss_slayer:
        min_rew2, min_skill2, em_rewinds2, em_level_int2, elixir_rew_int2 = funni_loop(10 ** 200, skills_int2, em_level_int,
                                                                                       elixir_rew_int, old_multi=1)
    else:
        min_rew2, min_skill2, em_rewinds2, em_level_int2, elixir_rew_int2 = funni_loop(10 ** 200, skills_int, em_level_int,
                                                                                       elixir_rew_int, old_multi=1)
    print("haha loop2 ok")
    nice_em_level2, em_level_suffix2, nice_rewind_level2, elixir_rew_suffix2 = nice_output(em_level_int2, elixir_rew_int2)

    print("???")

    print(f"min rewinds {min_rew} ({min_rew2 + em_rewinds}): em {em_rewinds} ({em_rewinds2 + em_rewinds}) "
          f"skill {min_skill} ({min_skill2}) em {format(nice_em_level, '.2f')}{em_level_suffix} "
          f"({format(nice_em_level2, '.2f')}{em_level_suffix2}) "
          f"elixir {format(nice_rewind_level, '.2f')}{elixir_rew_suffix} ({format(nice_rewind_level2, '.2f')}{elixir_rew_suffix2})")

    # print(f"Minimum rewinds required for {format(all_skills_old_int, '.2f')}{all_skills_old_suffix} - "
    #       f"{format(all_skills_new_int, '.2f')}{all_skills_new_suffix} skills (+{round(skill_days)} days)\n"
    #       f"----------------------------------\n"
    #       f"{format(original_em_level, '.2f')}{original_em_suffix} -> {format(nice_em_level, '.2f')}{em_level_suffix} ({format(nice_em_level2, '.2f')}{em_level_suffix2}) EM \n"
    #       f"{format(original_rewind_level, '.2f')}{original_rewind_suffix} -> {format(nice_rewind_level, '.2f')}{elixir_rew_suffix} "
    #       f"({format(nice_rewind_level2, '.2f')}{elixir_rew_suffix2}) Elixir\nx{nice_rewind_level / original_rewind_level} "
    #       f"(x{format(em_level_int2 / original_em_multi, '.2f')}) increase----------------------------------\n"
    #       f'{em_rewinds} ({em_rewinds2 + em_rewinds}) EM Rewinds\n'
    #       f'{max(1, round(min_skill))} ({max(1, round(min_skill2))}) Skill Rewinds\n----------------------------------\n'
    #       f'{max(1, round(em_rewinds + min_skill))} ({max(1, round(em_rewinds2 + em_rewinds + min_skill2))}) Total Rewinds')

    print(skills_int2)
    msg = NameValueModel(
        name=f"Минимум ревов для {format(all_skills_old_int, '.2f')}{all_skills_old_suffix} - "
             f"{format(all_skills_new_int, '.2f')}{all_skills_new_suffix} "
             f"скиллов \n",
        value=f""
              f"{format(original_em_level, '.2f')}{original_em_suffix} -> {format(nice_em_level2, '.2f')}{em_level_suffix2} EM \n"
              f"Элик за рев увеличился с {format(original_rewind_level, '.2f')}{original_rewind_suffix} до {format(nice_rewind_level2, '.2f')}{elixir_rew_suffix2} \n"
              f'{em_rewinds2 + em_rewinds} ревов для ЕМ \n'
              f'{max(1, round(min_skill2))} ревов для скиллов \n'
              f'{max(1, round(em_rewinds2 + em_rewinds + min_skill2))} суммарно ревов')

    return msg
