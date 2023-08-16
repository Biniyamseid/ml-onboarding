import string
import time
from ediblepickle import checkpoint





# A checkpointed expensive function
import os
import string
import time
from ediblepickle import checkpoint

import pickle


def checkpoint_decorator ( func ) :
    def wrapper (* args , ** kwargs ) :
        result = func (* args , ** kwargs )
        with open ('checkpoint . pkl ' , 'wb ') as f :
            pickle.dump ( result , f )
        return result
    return wrapper

# Define the directory path where intermediate results will be stored
intermediate_results = '/tmp/intermediate_results'

# Create the directory if it doesn't exist
if not os.path.exists(intermediate_results):
    os.makedirs(intermediate_results)

# A checkpointed expensive function
@checkpoint(key=string.Template('m{0}_n{1}_${iterations}_$stride.csv'), work_dir=intermediate_results, refresh=True)
def expensive_computation(m, n, iterations=4, stride=1):
    for i in range(iterations):
        time.sleep(1)
    return range(m, n, stride)




# First call, evaluates the function and saves the results
begin = time.time()
expensive_computation(-100, 200, iterations=4, stride=2)
time_taken = time.time() - begin

print(time_taken)

# Second call, since the checkpoint exists, the result is loaded from that file and returned.
begin = time.time()
expensive_computation(-100, 200, iterations=4, stride=2)
time_taken = time.time() - begin

print(time_taken)