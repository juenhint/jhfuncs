def center_log_ratio(df, axis=0, pseudocount=0):
    """Create a clr-transformed dataframe. 
    NOTE: When applied to a microbe abundance matrix, the function assumes that samples are listed in the columns and OTUs, or taxa, in the rows. This can be changed byt setting axis to 1
    Validated using *skbio* and the R package *mia*
    
    Parameters
    ----------
    df : :py:class:`pandas.DataFrame` 
        A dataframe containing the values
    axis: int
        Which axis to apply the transformation along, by default 0 (rows) 
    pseudocount: float
        A pseudocount to add to the values to mitigate 0-values, by default 0
        
    Returns
    -------
    new_df : pandas.DataFrame
        The clr-transformed data
    """
    from scipy.stats import gmean as _gmean
    import numpy as _np
    
    def handleRow(cs):
        gm = _gmean(cs)
        cls = _np.log([c/gm for c in cs])
        return cls
    new_df = df + pseudocount
    new_df = df.apply(handleRow, axis=axis, result_type="expand")
    new_df.columns = df.columns
    return new_df