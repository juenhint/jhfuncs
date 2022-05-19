def relative_frequency(df, axis=0):
    """Count relative frequencies of OTUs or taxa in a sample from a matrix of raw abundances. 
    NOTE: When applied to a microbe abundance matrix, the function assumes that samples are listed in the columns and OTUs, or taxa, in the rows. This can be changed byt setting axis to 1
    
    Parameters
    ----------
    df : :py:class:`pandas.DataFrame`
        A dataframe containing the abundances
    axis : int
        Axis to use for total count, default = 1
    
    Returns
    -------
    new_df : :py:class:`pandas.DataFrame`
        The relative frequencies of the variables
    """
    import pandas as _pd
    from pandas import DataFrame as _DataFrame
    
    def handleRow(cs):
        t = sum(cs)
        cls = [c/t for c in cs]
        return cls
    new_df = df.apply(handleRow, axis=axis, result_type="expand")
    new_df.columns = df.columns
    return new_df