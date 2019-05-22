# importing the multiprocessing module
import multiprocessing
import os


def print_cube(num, q):
    """
    function to print cube of given num
    """
    print(os.getpid())

    for i in range(0, 100):
        q.put((i,))
    return "cube"


def print_square(num, q):
    print(os.getpid())

    for i in range(100, 200):
        q.put((i,))
    return "square"


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
    # creating processes
        q = manager.Queue()
        list2 = list()

        p1 = multiprocessing.Process(target=print_square, args=(10,q, ))
        p2 = multiprocessing.Process(target=print_cube, args=(10,q, ))

        print(13 % 7)

        # starting process 1
        p1.start()
        # starting process 2
        p2.start()

        # wait until process 1 is finished
        p1.join()
        # wait until process 2 is finished
        p2.join()

        while not q.empty():
            print(q.get())

        # both processes finished
        print("Done!")
