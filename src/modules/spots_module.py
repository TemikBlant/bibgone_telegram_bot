from src.utils.csv_helper import read_csv
from src.constants.shared_constants import boss, mob_scores, boss_scores, boss_scores2, mobs
from src.models.common_models import NameValueModel


class SpotsModule:

    def __init__(self):
        self.lista_csv = read_csv()

    @staticmethod
    def get_fudge(initial: int):
        if initial < 1000:
            return 0
        elif initial < 2000:
            fudge = 0.7
        elif initial < 4000:
            fudge = 0.89
        elif initial < 5000:
            fudge = 0.82
        elif initial < 6000:
            fudge = 0.78
        elif initial < 8500:
            fudge = 0.87
        elif initial < 9500:
            fudge = 0.95
        elif initial < 10500:
            fudge = 1.05
        elif initial < 11500:
            fudge = 1.17
        elif initial < 12500:
            fudge = 1.31
        elif initial < 13500:
            fudge = 1.38
        elif initial < 14500:
            fudge = 1.45
        elif initial < 15000:
            fudge = 1.48
        elif initial < 15500:
            fudge = 1.53
        elif initial < 16000:
            fudge = 1.57
        elif initial < 20000:
            fudge = 1.63
        elif initial < 25000:
            fudge = (0.21 / 15000) * initial + (1.8 - (0.21 / 15000) * 23000)
        elif initial < 28000:
            fudge = 1.92
        elif initial < 30000:
            fudge = 1.95
        else:
            fudge = 1.99

        return fudge

    @staticmethod
    def secunda(numar: int):
        ceva = ""
        ceva += f"{numar // 60}:"
        if numar % 60 < 10:
            ceva += "0"
            ceva += f"{numar % 60}"
        else:
            ceva += f"{numar % 60}"

        return ceva

    def spot_score(self, day: int, titor: float, express: bool, tj: bool, double_rewind: bool, mode: int):
        lista = []
        score = 0
        fudge = 0
        if express:
            portal = 10 if day // 500 == 0 else (day // 500) * 10
        else:
            portal = 5 if day // 500 == 0 else (day // 500) * 5
        portal_count = 1
        initial = day
        if tj:
            if double_rewind:
                day = int(self.spot_round(self.spot_round(day * 0.75) * 0.75))
            else:
                day = int(self.spot_round(day * 0.75))
        else:
            if double_rewind:
                day = int(self.spot_round(self.spot_round(day * 0.5) * 0.5))
            else:
                day = int(self.spot_round(day * 0.5))

        froskScore = mob_scores[3]

        while day < initial:
            if mode == 1:
                mobScore = mob_scores[mobs.index(self.lista_csv[(day // 5) - 1][1].lower())]
            else:
                mobScore = float(self.lista_csv[(day // 5) - 1][2])
                fudge = self.get_fudge(initial)
                if fudge == 0:
                    return 0

            # currentDay = day if day - 10000 > 0 else 0

            if mode == 1:
                bossScore = boss_scores[day % 100 // 5]
            else:
                bossScore = boss_scores2[day % 100 // 5]

            if express:
                speed = -12 * (day / initial) + 13
            else:
                speed = -4 * (max(day / initial, 0.75)) + 5

            if mode == 2:
                speed *= titor
            if mode == 1:
                score += (froskScore + (mobScore - froskScore) * (
                        1 + (max(day - 10000, 0) / 20000)) + bossScore) / speed
            else:
                score += ((mobScore * fudge) + bossScore) / speed
            day += portal
            portal_count += 1

        dodo_score = score * 19.3191489361702
        lista.append(initial)
        lista.append(round(score, 2) if mode == 1 else round(score))
        lista.append(boss[(day - portal) % 100 // 5].title())
        lista.append(round(dodo_score))
        lista.append(initial - (day - portal))

        return lista

    @staticmethod
    def spot_round(day: float):
        if day % 10 == 7.5:
            return day + 2.5
        elif day % 10 == 2.5:
            return day - 2.5

        upper, lower = day, day
        while upper % 5 != 0 and lower % 5 != 0:
            upper += 0.25
            lower -= 0.25

        return upper if upper % 5 == 0 else lower

    def portal_compare(self, spot1: int, spot2: int, tj: bool, express: bool, double_rewind: bool):
        # mobs = ["dino", "rex", "shade", "frosk", "blob", "gargoyle", "caps", "warmonger", "banshee"]
        # with open("ceva.csv") as csv_file:
        #     csv_reader = csv.reader(csv_file)
        #     lista_csv = list(csv_reader)

        if express:
            portal1 = 10 if spot1 // 500 == 0 else (spot1 // 500) * 10
            portal2 = 10 if spot2 // 500 == 0 else (spot2 // 500) * 10
        else:
            portal1 = 5 if spot1 // 500 == 0 else (spot1 // 500) * 5
            portal2 = 5 if spot2 // 500 == 0 else (spot2 // 500) * 5

        if tj:
            if double_rewind:
                start1 = int(self.spot_round(self.spot_round(spot1 * 0.75) * 0.75))
                start2 = int(self.spot_round(self.spot_round(spot2 * 0.75) * 0.75))
            else:
                start1 = int(self.spot_round(spot1 * 0.75))
                start2 = int(self.spot_round(spot2 * 0.75))
        else:
            if double_rewind:
                start1 = int(self.spot_round(self.spot_round(spot1 * 0.5) * 0.5))
                start2 = int(self.spot_round(self.spot_round(spot2 * 0.5) * 0.5))
            else:
                start1 = int(self.spot_round(spot1 * 0.5))
                start2 = int(self.spot_round(spot2 * 0.5))

        while spot2 > start1:
            mob1 = start1
            mob2 = start2
            if mob1 != mob2:
                return 0

            if start1 < spot1:
                start1 += portal1
            else:
                return 0

            if start2 < spot2:
                start2 += portal2
            else:
                return 0
        # if

        return 1

    def spot_range(self, day: int, tj: bool, express: bool, mode: int, double_rewind: bool):
        copy = copy2 = day - 50
        upper, lower = 0, 0
        for i in range(copy, day + 50):
            if self.portal_compare(copy2, i, tj, express, double_rewind):
                pass
            else:
                if i <= day:
                    lower = i
                copy2 = i
                upper = i - 1
                if upper >= day:
                    if mode == 1:
                        return f'{lower}-{str(upper)[-2:]}'
                    else:
                        return upper

    def best_spot(self, daya: int, day_range: int, titor: float, express: bool = True, tj: bool = True, mode: int = 2,
                  double_rewind: bool = False):
        kek = daya
        spots = []
        alta_matrice_babana = []
        start = startcopy = self.spot_range(daya, tj, express, 2, double_rewind)
        spots.append(start)

        while start - startcopy < day_range:
            start = self.spot_range(start + 1, tj, express, 2, double_rewind)
            spots.append(start)

            for day in spots:
                lista = self.spot_score(
                    day=day,
                    titor=titor,
                    express=express,
                    tj=tj,
                    double_rewind=double_rewind,
                    mode=mode
                )
                alta_matrice_babana.append(lista)

        def minim():
            index_fishy = 1000000
            minim_dodo = 0
            day_minim = 0
            minim_fishy = 1000000
            skip = 0
            for i in range(0, len(alta_matrice_babana)):
                if minim_fishy > alta_matrice_babana[i][1]:
                    minim_fishy = alta_matrice_babana[i][1]
                    index_fishy = i
                    minim_dodo = alta_matrice_babana[i][3]
                    day_minim = alta_matrice_babana[i][0]
                    skip = alta_matrice_babana[i][4]

            return index_fishy, minim_fishy, minim_dodo, day_minim, skip

        print(alta_matrice_babana)
        index_fishy1, minim_fishy, minim_dodo, day_minim, skip = minim()
        alta_matrice_babana[index_fishy1][1] = 1000000
        index_fishy2, minim_fishy2, minimdodo2, day2, skip2 = minim()
        alta_matrice_babana[index_fishy2][1] = 1000000

        msg = NameValueModel(name=f"Лучшее время спота для следующих {day_range} дней \n",
                             value=f"дни {self.spot_range(day_minim, tj, express, 1, double_rewind)} "
                                   f"имеют лучшее время рева - {self.secunda(int(minim_fishy))}")
        return msg

    def detailed_spot(self, daya: int, double_rewind: bool, titor: float, express: bool = True, tj: bool = True):
        response = {}
        response['head_response'] = "PORTAL --- DAY --- MOB --- BOSS\n--------------------------------\n" \
                                    "Rewind Spot Calculator\n-----------------------------------------"

        score_fishy_list = self.spot_score(day=daya, titor=titor, express=express, tj=tj, double_rewind=double_rewind,
                                           mode=1)
        score_fishy = score_fishy_list[1]
        score_dodo = score_fishy_list[3]
        if daya > 1000:
            score_seconds = self.secunda(
                self.spot_score(day=daya, titor=titor, express=express, tj=tj, double_rewind=double_rewind, mode=2)[1])
            print( f"This spot has a score of {score_fishy} ({score_dodo}) or " \
                              f"{score_seconds} minutes, with a {score_fishy_list[4]} Day last portal.")
        else:
            print( f"This spot has a score of {score_fishy} ({score_dodo}), with a {score_fishy_list[4]}" \
                      " Day last portal.")
        if express:
            portal = 10 if daya // 500 == 0 else (daya // 500) * 10
        else:
            portal = 5 if daya // 500 == 0 else (daya // 500) * 5
        portal_count = 1
        initial = daya
        if tj:
            if double_rewind:
                daya = int(self.spot_round(self.spot_round(daya * 0.75) * 0.75))
            else:
                daya = int(self.spot_round(daya * 0.75))
        else:
            if double_rewind:
                daya = int(self.spot_round(self.spot_round(daya * 0.5) * 0.5))
            else:
                daya = int(self.spot_round(daya * 0.5))
        i = 0
        if daya % 5 != 0:
            return 0
        ceva = "```\n"
        while daya < initial:
            if i < 9:
                ceva += f"{portal_count}:  " f"{daya} " + f"M. {self.lista_csv[(daya // 5) - 1][1]}" + f" B. " \
                                                                                                       f"{boss[daya % 100 // 5].title()}\n"
            else:
                ceva += f"{portal_count}: " f"{daya} " + f"M. {self.lista_csv[(daya // 5) - 1][1]}" + f" B. " \
                                                                                                      f"{boss[daya % 100 // 5].title()}\n"
            if i % 14 == 0 and i >= 14:
                ceva += "\n```"
                ceva = "```\n"
                ceva += f"{portal_count}: " f"{daya} " + f"M. {self.lista_csv[(daya // 5) - 1][1]}" + f" B. " \
                                                                                                      f"{boss[daya % 100 // 5].title()}\n"
            daya += portal
            portal_count += 1
            i += 1

        ceva += "\n```"
        print(response)
        print(ceva)
        return ceva

    def spots(self, daya: int, day_range: int, titor: float, tj: bool=True, express: bool=True, mode: int=2, double_rewind: bool=False):
        kek = daya
        spots = []
        matrice = []
        lista = []
        skip = 0
        start = startcopy = self.spot_range(daya, tj, express, 2, double_rewind)
        spots.append(start)

        while start - startcopy < day_range:
            start = self.spot_range(start + 1, tj, express, 2, double_rewind)
            spots.append(start)

        minim_fishy, minim_dodo = 100000000, 100000000
        day_minim = 0
        if mode == 1:
            print("DAY --- SCORE --- LAST BOSS --- LAST PORTAL SKIP\n--------------------------------")
        else:
            print("DAY --- TIME --- LAST BOSS --- LAST PORTAL SKIP\n--------------------------------")
        print("Rewind Spot Calculator <a:kafkakurukuru:1118233531110412461>\n------------------------")
        for day in spots:
            lista = self.spot_score(day=day, titor=titor, express=express, tj=tj, double_rewind=double_rewind, mode=mode)
            initial = lista[0]
            score = lista[1]
            dodo_score = round(lista[3])
            if minim_fishy > score:
                day_minim = initial
                minim_fishy = score
                minim_dodo = dodo_score
                skip = lista[4]
            matrice.append(lista)

        print(matrice)
        if mode == 1:
            value = f"**At Day {kek}, __Day {self.spot_range(day_minim, tj, express, 1, double_rewind)}__ has the best rewind score of {format(minim_fishy, '.2f')} " \
                    f"({round(minim_dodo)}) with a {skip} Day last portal skip for the next " \
                    f"{day_range} days. The scores inside brackets represent [Dodora's Rewind Sheet]" \
                    f"(https://bit.ly/Dodo_Rewind_Sheet) Costs.**"
        else:
            value = f"**At Day {kek}, __Day {self.spot_range(day_minim, tj, express, 1, double_rewind)}__ has the best time of __{self.secunda(int(minim_fishy))}__ with a " \
                    f"{skip} day last portal skip for the next " \
                    f"{day_range} days.**"
        print(value)
        ceva = '```\n'
        counter = 0
        min_fishy = 1000000000
        min_dodo = 0
        min_day = 0
        prev = 0
        for lista in matrice:
            spots = self.spot_range(lista[0], tj, express, 1, double_rewind)
            if prev == spots:
                pass
            else:
                if counter < 10:
                    if mode == 1:
                        ceva += f"{self.spot_range(lista[0], tj, express, 1, double_rewind)}" + " - " + f"{format(lista[1], '.2f')}" + f" ({lista[3]})" + " - " + f"{lista[2]} ({lista[4]} skip)\n"
                    else:
                        ceva += f"{self.spot_range(lista[0], tj, express, 1, double_rewind)}" + " - " + f"{self.secunda(int(lista[1]))}" + " - " + f"{lista[2]} ({lista[4]} skip)\n"
                    counter += 1
                    if min_fishy > lista[1]:
                        min_day = lista[0]
                        min_fishy = lista[1]
                        min_dodo = lista[3]
                elif counter == 10:
                    ceva += "\n```"
                    counter = 0
                    if mode == 1:
                        print(ceva)
                    else:
                        print(ceva)
                    ceva = '```\n'
                    min_fishy = 1000000000
                    if min_fishy > lista[1]:
                        min_day = lista[0]
                        min_fishy = lista[1]
                        min_dodo = lista[3]
                    if mode == 1:
                        ceva += f"{self.spot_range(lista[0], tj, express, 1, double_rewind)}" + " - " + f"{format(lista[1], '.2f')}" + f" ({lista[3]})" + " - " + f"{lista[2]} ({lista[4]} skip)\n"
                    else:
                        ceva += f"{self.spot_range(lista[0], tj, express, 1, double_rewind)}" + " - " + f"{self.secunda(int(lista[1]))}" + " - " + f"{lista[2]} ({lista[4]} skip)\n"
            prev = spots

        ceva += "\n```"
        if min_fishy > lista[1]:
            min_day = lista[0]
            min_fishy = lista[1]
            min_dodo = lista[3]

        print(ceva)
