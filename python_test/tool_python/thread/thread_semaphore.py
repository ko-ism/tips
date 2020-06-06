import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
    )


def worker1(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def worker2(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def worker3(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(name='worker1', target=worker1, args=(semaphore, ))
    t2 = threading.Thread(name='worker2', target=worker2, args=(semaphore, ))
    t3 = threading.Thread(name='worker3', target=worker3, args=(semaphore, ))
    t1.start()
    t2.start()
    t3.start()
