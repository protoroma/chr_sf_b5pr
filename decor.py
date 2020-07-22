import time

class Calc:
    import time
    def __init__(self, func, num_runs=10, avg_time=0):
        self.func = func
        self.num_runs = num_runs
        self.avg_time = avg_time

    def __call__(self, *args):
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func()
            t1 = time.time()
            self.avg_time += (t1 - t0)
        self.avg_time /= self.num_runs
        print("Выполнение заняло %.5f секунд" % self.avg_time)
        return self.func()