import numpy as np

def calc_res(shape):
    base0 = 2**int(np.log2(shape[0]))
    base1 = 2**int(np.log2(shape[1]))
    base = min(base0, base1)
    min_res = min(shape[0], shape[1])

    def int_log2(xs, base):
        return [x * 2**(2-int(np.log2(base))) % 1 == 0 for x in xs]
    if min_res != base or max(*shape) / min(*shape) >= 2:
        if np.log2(base) < 10 and all(int_log2(shape, base*2)):
            base = base * 2

    return base # , [shape[0]/base, shape[1]/base]

def calc_init_res(shape, resolution=None):
    if len(shape) == 1:
        shape = [shape[0], shape[0], 1]
    elif len(shape) == 2:
        shape = [*shape, 1]
    size = shape[:2] if shape[2] < min(*shape[:2]) else shape[1:] # fewer colors than pixels
    if resolution is None:
        resolution = calc_res(size)
    res_log2 = int(np.log2(resolution))
    init_res = [int(s * 2**(2-res_log2)) for s in size]
    return init_res, resolution, res_log2