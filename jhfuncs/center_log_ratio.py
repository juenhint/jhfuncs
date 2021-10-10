def center_log_ratio(df, axis=0):
    """Create a clr-transformed dataframe
    df: Pandas dataframe
    axis: Axis to use for geometric means
    
    returns a Pandas dataframe
    """
    from scipy.stats import gmean as _gmean
    import numpy as _np
    
    def handleRow(cs):
        gm = _gmean(cs)
        cls = _np.log([c/gm for c in cs])
        return cls
    new_df = df.apply(handleRow, axis=axis, result_type="expand")
    new_df.columns = df.columns
    return new_df