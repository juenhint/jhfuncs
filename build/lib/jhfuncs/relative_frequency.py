def relative_frequency(df, axis=1):
    """Count relative frequencies of genus in a sample
    df: Pandas dataframe
    axis: Axis to use for total count, default = 1
    
    returns a Pandas dataframe 
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