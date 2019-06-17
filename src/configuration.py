"""
Convert Smarch samples to configurations for SPLC challenge case format.
Code for paper "t-wise Coverage by Uniform Sampling"
Author: Jeho Oh
"""


import os
from sys import path

srcdir = os.path.dirname(os.path.abspath(__file__))
rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))
path.append(rootdir + "/Kclause_Smarch/Smarch")

from smarch import read_dimacs


def gen_config(dimacs_, samplefile_, n_):
    _features, _clauses, _vcount = read_dimacs(dimacs_)

    sampledir = os.path.dirname(samplefile_)
    configdir = sampledir + "/" + str(n_)

    # create configuration folder
    if not os.path.exists(configdir):
        os.makedirs(configdir)

    with open(samplefile_, "r") as sf:
        i = 1
        for line in sf:
            raw = line.split(",")
            if len(raw) == (len(_features) + 1):
                f = open(configdir + "/" + str(i) + ".config", "w")
                for v in raw:
                    if v != '\n':
                        if int(v) > 0:
                            f.write(_features[int(v)-1][1] + "\n")
                f.close()
                i += 1


# run script
if __name__ == "__main__":
    target = "Financial_2018_05_09"

    srcdir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))

    dimacs = rootdir + "/" + target + "/Data/" + target + ".dimacs"

    nlist = [5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 1518]

    for n in nlist:
        samplefile = rootdir + "/" + target + "/Samples/Memory/" + target + "_" + str(n) + ".samples"
        gen_config(dimacs, samplefile, n)
