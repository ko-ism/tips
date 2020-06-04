import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
    )


def worker1(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    time.sleep(5)
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        d['x'] = i + 1
        logging.debug(d)
        # ## RLockを利用すると、階層的にLockをかけられる
        # ## 通常のlockだとこれは異常終了する。lock.release()が実行されないで止まってしまうため
        # with lock:
        #     d['x'] += 1
        #     logging.debug(d)
    logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.Lock()
    # lock = threading.RLock()
    t1 = threading.Thread(name='worker1', target=worker1, args=(d, lock))
    t2 = threading.Thread(name='worker2', target=worker2, args=(d, lock))
    t1.start()
    t2.start()
