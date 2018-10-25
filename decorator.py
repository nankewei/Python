import functools, time

def log(text):
    # 如果传入的参数是字符串
    if isinstance(text, str):

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print("%s %s" % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print("%s " % text.__name__)
            return text(*args, **kw)
        return wrapper

@log
def now():
    print(time.time())

now()

time.sleep(1)

@log("hello")
def now():
    print(time.time())

now()