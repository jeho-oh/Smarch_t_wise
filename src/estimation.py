import os


def estimate_coverage(ratiofile_, n_):
    with open(ratiofile_, "r") as f:
        i = 0.0
        e = 0.0

        for line in f:
            r = float(line)

            p = 1 - (1 - r)**n_

            e += p

            # if p >= c_:
            #     e += 1

            i += 1

        print(str(n_) + "," + str(e/i))


t = 1
target = "Financial_2018_05_09"

srcdir = os.path.dirname(os.path.abspath(__file__))
rootdir = os.path.abspath(os.path.join(srcdir, os.pardir))
ratiofile = rootdir + "/" + target + "/" + target + "_" + str(t) + ".ratio"

nlist = {5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 1518}

for i in range(0, 15):
    estimate_coverage(ratiofile, 10**i)