from itertools import combinations
import os
import pycosat

from Kclause_Smarch.Smarch.smarch import read_dimacs


def get_combinations(dimacs_, t_, outfile_):
    comb = list()

    # get list of features
    _features, _clauses, _vcount = read_dimacs(dimacs_)

    vars = set()
    for i in range(1, len(_features)):
        vars.add(i)
        vars.add(-1 * i)

    # get t wise combinations
    raw = combinations(vars, t_)

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
            #comb.append(c)
        #else:
            #print(c)

        print(str(j))

    f.close()

    return


t = 1
target = "Financial_2018_05_09"

srcdir = os.path.dirname(os.path.abspath(__file__))
rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))

dimacs = rootdir + "/" + target + "/" + target + ".dimacs"
combfile = rootdir + "/" + target + "/" + target + "_" + str(t) + ".comb"

get_combinations(dimacs, t, combfile)

