from timeit import default_timer as timer

def timefun(func):
        def  inner(*args, **kwargs):
                start = timer()
                results = timer()
                results = func(*args, **kwargs)
                end = timer()
                message = "{} took {} seconds".format(func.__name__, end - start)
                print(message)
                return results
        return inner

