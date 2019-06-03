"""
Measure t-wise coverage of samples from Smarch
Code for paper "t-wise Coverage by Uniform Sampling"
Author: Jeho Oh
"""


import os


def check_coverage(samplefile_, combfile_):

    total = 0
    exist = 0

    samples = list()

    # read samples
    with open(samplefile_, "r") as f:
        for line in f:
            line = line[:len(line)-2]
            s = line.split(",")
            samples.append(s)

    # check each combination exists in samples
    with open(combfile_, "r") as f:
        for line in f:
            line = line[:len(line) - 1]
            comb = line.split(",")
            for s in samples:
                if all(elem in s for elem in comb):
                    exist += 1
                    break
            total += 1

    print(str(exist/total))


# run script
if __name__ == "__main__":
    target = "Financial_2018_05_09"

    srcdir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))
    dimacs = rootdir + "/" + target + "/Data/" + target + ".dimacs"

    nlist = [5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 1518]

    # get 1-wise coverage or all sample sizes
    print("1-wise coverage:")
    combfile = rootdir + "/" + target + "/Data/" + target + "_" + "1.comb"
    for i in nlist:
        samplefile = rootdir + "/" + target + "/Samples/Memory/" + target + "_" + str(i) + ".samples"
        print(str(i), end=",")
        check_coverage(samplefile, combfile)

    # get 2-wise coverage or all sample sizes
    print("2-wise coverage:")
    combfile = rootdir + "/" + target + "/Data/" + target + "_" + "2.comb"
    for i in nlist:
        samplefile = rootdir + "/" + target + "/Samples/Memory/" + target + "_" + str(i) + ".samples"
        print(str(i), end=",")
        check_coverage(samplefile, combfile)
