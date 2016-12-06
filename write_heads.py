from keras import backend as K


def writing(
        head_num, memory_size, memory_dim, memory_t_1,
        weight_t, eraser_t, adder_t):
    memory_t = memory_t_1

    for i in xrange(head_num):
        # get the addressing for writing
        address_begin = i * memory_size
        address_end = address_begin + memory_size
        content_begin = i * memory_dim
        content_end = content_begin + memory_dim
        memory_t = writing(
            memory_t_1,
            weight_t[address_begin:address_end],
            eraser_t[content_begin:content_end],
            adder_t[content_begin:content_end])
        memory_t_1 = memory_t

    return memory_t


def writing(memory_t_1, weight_t, eraser_t, adder_t):
    """
    Each writing process contain two parts: an erase followed by an add.
    :param memory_t_1: the $N \times M$ memory matrix at time $t-1$, where $N$
    is the number of memory locations, and $M$ is the vector size at each
    location.
    :param weight_t: $w_t$ is a vector of weightings over the $N$ locations
    emitted by a writing head at time $t$.
    :param eraser_t:
    :param adder_t:
    :return:
    """
    # erase
    _memory_t = erase(memory_t_1, weight_t, eraser_t)

    # add
    memory_t = add(_memory_t, weight_t, adder_t)
    return memory_t


def erase(memory_t_1, weight_t, eraser_t):
    '''

    :param memory_t_1:
    :param weight_t:
    :param eraser_t:
    :return:
    '''
    memory = memory_t_1 * (1 - weight_t * eraser_t)
    return memory


def add(_memory_t, weight_t, adder_t):
    '''

    :param _memory_t:
    :param weight_t:
    :param adder_t:
    :return:
    '''
    memory_t = _memory_t + weight_t * adder_t
    return memory_t
