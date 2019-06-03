"""
Estimate t-wise coverage from given configuration ratio and sample size.
Code for paper "t-wise Coverage by Uniform Sampling"
Author: Jeho Oh
"""


import os


def estimate_coverage(ratiofile_, n_):
    with open(ratiofile_, "r") as f:
        c = 0.0
        e = 0.0

        # get probability from all ratios
        for line in f:
            r = float(line)

            p = 1 - (1 - r)**n_
            e += p
            c += 1

        # print average probability for given n
        print(str(n_) + "," + str(e/c))


# run script
if __name__ == "__main__":
    target = "Financial_2018_05_09"

    srcdir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))

    # estimate of experimental data
    print("Estimation of experimental data")
    nlist = [5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 1518]

    print("1-wise:")
    ratiofile = rootdir + "/" + target + "/Data/" + target + "_" + "1.ratio"
    for n in nlist:
        estimate_coverage(ratiofile, n)

    print("2-wise:")
    ratiofile = rootdir + "/" + target + "/Data/" + target + "_" + "2.ratio"
    for n in nlist:
        estimate_coverage(ratiofile, n)

    # estimate of large sample sizes
    print("Estimation of large sample sizes")

    print("1-wise:")
    ratiofile = rootdir + "/" + target + "/Data/" + target + "_" + "1.ratio"
    for i in range(0, 15):
        estimate_coverage(ratiofile, 10**i)

    print("2-wise:")
    ratiofile = rootdir + "/" + target + "/Data/" + target + "_" + "2.ratio"
    for i in range(0, 15):
        estimate_coverage(ratiofile, 10**i)
