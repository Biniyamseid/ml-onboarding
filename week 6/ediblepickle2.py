
import pickle


def checkpoint_decorator ( func ) :
    def wrapper (* args , ** kwargs ) :
        result = func (* args , ** kwargs )
        with open ('checkpoint . pkl ' , 'wb ') as f :
            pickle.dump ( result , f )
        return result
    return wrapper

