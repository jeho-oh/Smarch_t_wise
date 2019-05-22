import os


def check_coverage(samplefile_, combfile_):

    total = 0
    exist = 0

    samples = list()

    with open(samplefile_, "r") as f:
        for line in f:
            line = line[:len(line)-2]
            s = line.split(",")
            samples.append(s)

    with open(combfile_, "r") as f:
        for line in f:
            line = line[:len(line) - 1]
            comb = line.split(",")
            for s in samples:
                if all(elem in s for elem in comb):
                    exist += 1
                    break
            total += 1
            print(total)

    print(str(exist/total))


t = 1
n = 3
target = "LLVM" #"Financial_2018_05_09"

srcdir = os.path.dirname(os.path.abspath(__file__))
dimacs = srcdir + "/Data/" + target + ".dimacs"
combfile = srcdir + "/Data/" + target + "_" + str(t) + ".comb"
samplefile = srcdir + "/Data/Samples/" + target + "_" + str(n) + ".samples"

check_coverage(samplefile, combfile)
