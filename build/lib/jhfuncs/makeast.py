def makeast(dfr):
    """Transform a matrix of p-values to asterix-annotations, where * < 0.05 and ** < 0.01, otherwise blank.
    
    Parameters
    ----------
    dfr : :py:class:`pandas.DataFrame` or :py:class:`pandas.Series`
        A matrix or list containing the p values
        
    Returns
    -------
    asterix : :py:class:`pandas.DataFrame`
        A matrix of strings indicating statistical significance.
    """
    from pandas import DataFrame
    import numpy as np
    
    ndf = []
    for r in dfr.values:
        nr = []
        try:
            for c in r:
                if (c < 0.01):
                    nr.append('**')
                elif (c < 0.05):
                    nr.append('*')
                else:
                    nr.append('')
        except:
            if (r < 0.01):
                nr.append('**')
            elif (r < 0.05):
                nr.append('*')
            else:
                nr.append('')
        ndf.append(nr)
    asterix = DataFrame(np.array(ndf))
    return asterix