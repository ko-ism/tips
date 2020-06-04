import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
    )


def worker1(d, lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def worker2(d, lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def worker3(d, lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.Lock()
    # lock = threading.RLock()
    t1 = threading.Thread(name='worker1', target=worker1, args=(d, lock))
    t2 = threading.Thread(name='worker2', target=worker2, args=(d, lock))
    t1.start()
    t2.start()
