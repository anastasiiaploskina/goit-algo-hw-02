import uuid
import time
from random import randint

from queue import Queue

# Створити чергу заявок
queue = Queue(maxsize=10)


def generate_request():
    id = uuid.uuid4()
    queue.put(id)
    print(f"Request {id} generated.")
    time.sleep(1)


def process_request():
    print(f"-----Processing request {queue.get()}.")
    time.sleep(3)


def main():
    try:
        while True:

            for i in range(randint(1, 10)):
                generate_request()
                if queue.full():
                    print("Queue is full.")
                    break

            for j in range(randint(1, 10)):
                process_request()
                if queue.empty():
                    print("Queue is empty.")
                    break

            print("----------QUEUE----------")
            print(queue.queue)

    except KeyboardInterrupt:
        print("!!!Stopped by user!!!")


if __name__ == "__main__":
    main()
