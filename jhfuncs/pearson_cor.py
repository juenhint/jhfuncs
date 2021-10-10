def pearson_cor(a, b):
    """Calculate Pearson correlation matrix for two dataframes with equal amount of obs
    a: First pandas dataframe
    b: Second pandas dataframe
    """
    from pandas import DataFrame as _DataFrame
    from scipy.stats import pearsonr as _pearsonr
    
    coef_a = []
    p_a = []
    for ri in range(0, a.shape[1]):
        new_c_row = []
        new_p_row = []
        for ci in range(0, b.shape[1]):
            coef, p = _pearsonr(x = a.iloc[:,ri], y = b.iloc[:,ci])
            new_c_row.append(coef)
            new_p_row.append(p)
        coef_a.append(new_c_row)
        p_a.append(new_p_row)
    
    coef_df = _DataFrame(data=coef_a, index=a.columns, columns=b.columns)
    p_df = _DataFrame(data=p_a, index=a.columns, columns=b.columns)
    return coef_df, p_df