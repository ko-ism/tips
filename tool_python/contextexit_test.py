import contextlib

def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception as e:
        print('error:' + str(e))
        return False

def cleanup():
    print('clean up')

with contextlib.ExitStack() as stack:
    stack.callback(cleanup)

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.pop_all()