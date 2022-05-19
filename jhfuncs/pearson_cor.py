def pearson_cor(a, b, nan="raise"):
    """Calculate Pearson correlation matrix for two dataframes with equal amount of obs
    
    Parameters
    ----------
    a : :py:class:`pandas.DataFrame` or :py:class:`pandas.Series`
        First set of measurement
    b :  :py:class:`pandas.DataFrame` or :py:class:`pandas.Series`
        Second set of measurements
    nan : string
        How to handle nan-values in the data. One of the following:
        "raise" : Raises an exception if nan-values are observed
        "omit" : Omits the datapoints with nan-values in each pair of variables
        
    Returns
    -------
    coef_df :  :py:class:`pandas.DataFrame`
        Matrix of correlation coefficients between each variable
    p : :py:class:`pandas.DataFrame`
        Matrix of correlation p-values between each variable    
    """
    from pandas import DataFrame as _DataFrame
    from scipy.stats import pearsonr as _pearsonr
    
    coef_a = []
    p_a = []
    if (type(a) != _DataFrame):
        a = _DataFrame(a)
    if (type(b) != _DataFrame):
        b = _DataFrame(b)
    
    for ri in range(0, a.shape[1]):
        new_c_row = []
        new_p_row = []
        for ci in range(0, b.shape[1]):
            x = a.iloc[:,ri]
            y = b.iloc[:,ci]
            if (nan == "omit"):
                idd = x[~x.isna()].index.intersection(y[~y.isna()].index)
                x = x[idd]
                y = y[idd]
            coef, p = _pearsonr(x = x, y = y)
            new_c_row.append(coef)
            new_p_row.append(p)
        coef_a.append(new_c_row)
        p_a.append(new_p_row)
    
    coef_df = _DataFrame(data=coef_a, index=a.columns, columns=b.columns)
    p_df = _DataFrame(data=p_a, index=a.columns, columns=b.columns)
    return coef_df, p_df