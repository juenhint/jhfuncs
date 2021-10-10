def makeast(dfr):
    """Transform a matrix of p-values to asterix-annotations, where * < 0.05 and ** < 0.01
    """
    from pandas import DataFrame
    import numpy as np
    
    ndf = []
    for r in dfr.values:
        nr = []
        for c in r:
            if (c < 0.01):
                nr.append('**')
            elif (c < 0.05):
                nr.append('*')
            else:
                nr.append('')
        ndf.append(nr)
    return DataFrame(np.array(ndf))