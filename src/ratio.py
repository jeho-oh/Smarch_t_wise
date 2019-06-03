"""
Compute configuration ratio of combinations
Code for paper "t-wise Coverage by Uniform Sampling"
Author: Jeho Oh
"""


import os

from Kclause_Smarch.Smarch.smarch import count


def check_combratio(dimacs_, combfile_, outfile_):
    # count total number of configurations
    total = count(dimacs_, [])

    out = open(outfile_, "w")
    with open(combfile_, "r") as f:
        i = 0

        for line in f:
            # get combination
            line = line[:len(line) - 1]
            comb = line.split(",")
            const = list()

            # count configurations with combination
            for c in comb:
                const.append([c])

            # compute ratio
            part = count(dimacs_, const)
            r = part/total

            out.write(str(r) + "\n")

            i += 1

            # print progress
            print(str(i) + ": " + str(r))

    out.close()


# run script
if __name__ == "__main__":
    t = 1  # modify (t=2 will take quite a while)
    target = "Financial_2018_05_09"

    srcdir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))

    dimacs = rootdir + "/" + target + "/Data/" + target + ".dimacs"
    combfile = rootdir + "/" + target + "/Data/" + target + "_" + str(t) + ".comb"
    ratiofile = rootdir + "/" + target + "/Data/" + target + "_" + str(t) + ".ratio"

    check_combratio(dimacs, combfile, ratiofile)
