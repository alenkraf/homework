import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 200000

    def run(self):
        for _ in range(self.rounds):
            self.counter += 1

if __name__ == "__main__":
    thread1 = Counter()
    thread2 = Counter()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Counter value:", Counter.counter)
