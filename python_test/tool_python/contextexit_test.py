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

def cleanup2():
    print('clean up2')

with contextlib.ExitStack() as stack:
    stack.callback(cleanup)
    stack.callback(cleanup2)

    @stack.callback
    def cleanup3():
        print('clean up3')

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.pop_all()