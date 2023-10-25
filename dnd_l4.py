def name_trait():
    x = int(input("How many traits u want?: "))
    for i in range(x):
        a = input("Trait: ")
        trt.append(a)
    for j in trt:
        f.write(',')
        f.write(str(j))
    y = int(input("How many char: "))
    for j in range(y):
        b = input("Their names: ")
        nme.append(b)


def points():
    point = int(input("How many points for each character?: "))
    for k in nme:
        t = 0
        for h in trt:
            print("You have " + str(point - t) + " points  ")
            c = int(input("Number of points for " + k + "'s " + h + " : "))
            stats.append(c)
            t += c
        Sum = sum(stats)
        if point >= Sum:
            nstats = str(stats)[1: -1]
            f.write('\n')
            f.write(str(k) + "," + str(nstats))
            stats.clear()
        elif point << Sum:
            print("no too big of a number for a player,  ALL character stats reset now")
            points()


if __name__ == "__main__":
    trt = list()
    nme = list()
    stats = list()

    dnd = open('dndstats_fin.csv', 'w')

    with open('dndstats_fin.csv', 'w') as f:
        name_trait()
        points()










