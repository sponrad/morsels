import random
import itertools

def RandomLooper(*source_list):
    if not source_list:
        return []
    the_list = list(itertools.chain(*source_list))
    random.shuffle(the_list)
    return the_list
