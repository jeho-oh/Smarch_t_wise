"""
Generate valid t-wise combinations for coverage analysis
Code for paper "t-wise Coverage by Uniform Sampling"
Author: Jeho Oh
"""


from itertools import combinations
import os
import pycosat

from Kclause_Smarch.Smarch.smarch import read_dimacs


def get_combinations(dimacs_, t_, outfile_):
    # get list of features
    _features, _clauses, _vcount = read_dimacs(dimacs_)

    vlist = set()
    for i in range(1, len(_features)):
        vlist.add(i)
        vlist.add(-1 * i)

    # get t wise combinations
    raw = combinations(vlist, t_)

    f = open(outfile_, "w")

    # filter out combinations that are invalid
    j = 0
    for c in raw:
        assigned = list(map(int, c))
        aclause = [assigned[i:i + 1] for i in range(0, len(assigned))]
        cnf = _clauses + aclause
        s = pycosat.solve(cnf)

        if s != 'UNSAT':
            for i in range(0, len(c)):
                f.write(str(c[i]))
                if i < len(c)-1:
                    f.write(",")
            f.write("\n")
            j += 1

        # print progress
        print(str(j))

    f.close()

    return


# run script
if __name__ == "__main__":
    target = "Financial_2018_05_09"

    srcdir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))

    dimacs = rootdir + "/" + target + "/Data/" + target + ".dimacs"

    # generate 1-wise combinations
    print("Generating 1-wise combinations")
    combfile = rootdir + "/" + target + "/Data/" + target + "_" + str(1) + ".comb"
    get_combinations(dimacs, 1, combfile)

    # generate 2-wise combinations
    print("Generating 1-wise combinations")
    combfile = rootdir + "/" + target + "/Data/" + target + "_" + str(2) + ".comb"
    get_combinations(dimacs, 2, combfile)
