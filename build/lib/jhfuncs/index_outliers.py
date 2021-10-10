def index_outliers(data):
    """
    Return indexes of values that are not outliers. i.e. outside 1.5 * interquartile range
    data: List or numpy array
    returns List
    """
    from scipy.stats import iqr
    import numpy as np
    
    iq_range = iqr(data, axis=0)
    llim = np.quantile(data,0.25) - (1.5 * iq_range)
    ulim = np.quantile(data,0.75) + (1.5 * iq_range)
    to_keep = []
    for i, n in enumerate(data):
        if n > ulim or n < llim:
            continue
        else:
            to_keep.append(i)
    return to_keep