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


t = 1
target = "Financial_2018_05_09"

srcdir = os.path.dirname(os.path.abspath(__file__))
rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))

dimacs = rootdir + "/" + target + "/" + target + ".dimacs"
combfile = rootdir + "/" + target + "/" + target + "_" + str(t) + ".comb"
ratiofile = rootdir + "/" + target + "/" + target + "_" + str(t) + ".ratio"


check_combratio(dimacs, combfile, ratiofile)
