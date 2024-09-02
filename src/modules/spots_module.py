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
        index_fishy3, minim_fishy3, minimdodo3, day3, skip3 = minim()

        # embed = discord.Embed(title="Rewind Spot Calculator <a:kafkakurukuru:1118233531110412461>", color=0x71368a)
        # if mode == 1:
        #     embed.add_field(name='', value=f"**At Day {kek}, __Day {spot_range(day_minim, tj, express, 1, double_rewind)}__ ({skip} Days last portal) has the best rewind score of __{format(minim_fishy, '.2f')}__ "
        #                                    f"({round(minim_dodo)}) for the next "
        #                                    f"{day_range} days.\n\nThe next best 2 spots are __{spot_range(day2, tj, express, 1, double_rewind)}__ ({skip2} Days last portal) with a score of __{format(minim_fishy2, '.2f')}__"
        #                                    f" ({round(minimdodo2)}) and __{spot_range(day3, tj, express, 1, double_rewind)}__ ({skip3} Days last portal) with a score of __{format(minim_fishy3, '.2f')}__ ({round(minimdodo3)}). "
        #                                    f"The score inside brackets represents [Dodora's Rewind Sheet](https://bit.ly/Dodo_Rewind_Sheet) Cost.**", inline=False)
        # else:
        #     embed.add_field(name='', value=f"**At Day {kek}, __Day {spot_range(day_minim, tj, express, 1, double_rewind)}__ ({skip} Days last portal) has the best rewind time of __{secunda(int(minim_fishy))}__ for the next "
        #                                    f"{day_range} days.\n\nThe next best 2 spots are __{spot_range(day2, tj, express, 1, double_rewind)}__ ({skip2} Days last portal) with a time of __{secunda(int(minim_fishy2))}__"
        #                                    f" and __{spot_range(day3, tj, express, 1, double_rewind)}__ ({skip3} Days last portal) with a time of __{secunda(int(minim_fishy3))}__.**\n\n***__Note: These times are approximations"
        #                                    f" and may not be 100% accurate.__***", inline=False)
    #
    # embed.add_field(name='', value="*These calculations are using data from [Fishy's Rewind Sheet]"
    #                                "(https://bit.ly/Fishy_Rewind_Sheet). If you want to use No TJ/No Express/Titor/Double rewind options, look at the optional parameters.*")
    # embed.set_footer(text="If you spot any issues with this bot, please ping '@_tyrael.'",
    #                  icon_url="https://cdn.discordapp.com/emojis/1139252590278889529.gif")
    #
    # return embed
    #
        msg = NameValueModel(name=f"Лучшее время спота для следующих {day_range} дней \n",
                             value=f"дни {self.spot_range(day_minim, tj, express, 1, double_rewind)} "
                                   f"имеют лучшее время рева - {self.secunda(int(minim_fishy))}")
        return msg
