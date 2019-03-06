import json
from itertools import combinations


class Glygj(object):
    """
    目的是找出能推進至最多關卡的最佳`門客組合`
    To pass stages as much as possible, we try to find the best `guest combinations` with the minimum waste.
    """
    targets = [200110, 450310, 800680, 1251300, 1801800,
               2452500, 3203900, 4055700, 5008000, 6616990,
               8426000, 11238000, 20000000, 50000000, 100000000,
               200000000, 400000000, 600000000, 800000000, 1000000000]

    with open('guests.json', mode='r', encoding='utf-8') as fd:
        guests = json.load(fd)

    nb_guests = len(guests)
    nb_targets = len(guests)

    def __init__(self):
        self.verbose = False
        self.init_n = 1
        self.maxLimit = 7

    def run(self):
        """
        TODO: Instead of the Brute-force method, ML methods may be more efficient.
        """
        def f1(targetPower):
            scoreboard = []
            for n in range(init_n, len(guests) + 1):
                combs = combinations(guests.keys(), n)
                for comb_names in combs:
                    comb_powers = sum([guests[name] for name in comb_names])
                    waste = comb_powers - targetPower
                    if verbose:
                        print(
                            indents + f"{reversed(comb_names)}, {comb_powers}, {waste}")
                    if waste >= 0:
                        scoreboard.append((comb_names, comb_powers, waste))
                if n >= maxLimit:
                    break

            if not scoreboard:
                return None

            # check scoreboard
            comb = min(scoreboard, key=lambda x: x[2])
            return comb

        init_n = self.init_n
        guests = self.guests
        targets = self.targets
        maxLimit = self.maxLimit
        verbose = self.verbose

        for targetPower in targets:
            if len(guests) == 0:
                print('done')
                break
            print(f"targetPower: {targetPower}")
            comb = f1(targetPower)
            if comb is None:
                print('done')
                break
            indents = " " * 5
            print(indents + f"lowest_waste: {comb}")
            comb_names = comb[0]
            for comb_name in comb_names:
                guests.pop(comb_name)
            print(indents + f"remain: {len(guests)}")

        print('\n')
        print(f"remain: {guests}")
        print(f"remainPower: {sum([v for k, v in guests.items()])}")


if __name__ == '__main__':
    g = Glygj()
    g.run()
