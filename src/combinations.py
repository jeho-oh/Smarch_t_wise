"""
Generate valid t-wise combinations for coverage analysis
Code for paper "t-wise Coverage by Uniform Sampling"
Author: Jeho Oh
"""


from itertools import combinations
import os
import pycosat
from sys import path

srcdir = os.path.dirname(os.path.abspath(__file__))
rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))
path.append(rootdir + "/Kclause_Smarch/Smarch")

from smarch import read_dimacs


def get_combinations_1(dimacs_, outfile_):
    _comb = list()

    # get list of features
    _features, _clauses, _vcount = read_dimacs(dimacs_)

    _vlist = set()
    for i in range(1, len(_features)):
        _vlist.add(i)
        _vlist.add(-1 * i)

    # get t wise combinations
    raw = combinations(_vlist, 1)
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
                _comb.append(c[i])

                if i < len(c)-1:
                    f.write(",")

            f.write("\n")
            j += 1

        # print progress
        if j % 100 == 0:
            print(str(j))

    f.close()

    return _comb


def get_combinations_t(dimacs_, t_, outfile_, vlist_):
    # get list of features
    _features, _clauses, _vcount = read_dimacs(dimacs_)

    # get t wise combinations
    raw = combinations(vlist_, t_)
    raw = list(raw)
    f = open(outfile_, "w")

    # filter out combinations that are invalid
    j = 0

    while raw:
        c = raw.pop()
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
        if j % 10000 == 0:
            print(str(j))

    f.close()

    return


# run script
if __name__ == "__main__":
    target = "Financial_2018_05_09"

    dimacs = rootdir + "/" + target + "/Data/" + target + ".dimacs"

    # generate 1-wise combinations
    print("Generating 1-wise combinations")
    combfile = rootdir + "/" + target + "/Data/" + target + "_" + str(1) + ".comb"
    vlist = get_combinations_1(dimacs, combfile)

    # generate 2-wise combinations
    print("Generating 2-wise combinations")
    combfile = rootdir + "/" + target + "/Data/" + target + "_" + str(2) + ".comb"
    get_combinations_t(dimacs, 2, combfile, vlist)
