import os

from Kclause_Smarch.Smarch.smarch import count


def check_combratio(dimacs_, combfile_, outfile_):
    total = count(dimacs_, [])

    out = open(outfile_, "w")
    with open(combfile_, "r") as f:
        i = 0

        for line in f:
            line = line[:len(line) - 1]
            comb = line.split(",")
            const = list()

            for c in comb:
                const.append([c])

            part = count(dimacs_, const)
            r = part/total

            out.write(str(r) + "\n")

            i += 1
            print(str(i) + ": " + str(r))

    out.close()


t = 2
target = "Financial_2018_05_09"

srcdir = os.path.dirname(os.path.abspath(__file__))
dimacs = srcdir + "/Data/" + target + ".dimacs"
combfile = srcdir + "/Data/" + target + "_" + str(t) + "_latter.comb"
ratiofile = srcdir + "/Data/" + target + "_" + str(t) + ".ratio"

check_combratio(dimacs, combfile, ratiofile)
