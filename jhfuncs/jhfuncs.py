""" Functions for dataframe transformation
"""


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

def spearman_cor(a, b, nan="raise"):
    """Calculate Spearman correlation matrix for two dataframes with equal amount of obs
    a: First pandas dataframe
    b: Second pandas dataframe
    """
    from pandas import DataFrame as _DataFrame
    from scipy.stats import spearmanr as _spearmanr
    
    coef_a = []
    p_a = []
    for ri in range(0, a.shape[1]):
        new_c_row = []
        new_p_row = []
        for ci in range(0, b.shape[1]):
            coef, p = _spearmanr(a = a.iloc[:,ri], b = b.iloc[:,ci], nan_policy=nan)
            new_c_row.append(coef)
            new_p_row.append(p)
        coef_a.append(new_c_row)
        p_a.append(new_p_row)
    
    coef_df = _DataFrame(data=coef_a, index=a.columns, columns=b.columns)
    p_df = _DataFrame(data=p_a, index=a.columns, columns=b.columns)
    return coef_df, p_df

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


def index_outliers(data):
    """
    Return indexes of values that are note outliers. i.e. outside 1.5 * interquartile range
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

def quade_rancova(df, dv, covars, group):
    """Perform Quade's ANCOVA (nonparametric analysis of covariance) on dataset
    
    df: Pandas dataframe containing dependent, grouping and confounding variables
    dv: Dependent variable
    covars: One or more covariable
    group: Grouping (independent) variable. Must be discrete.
    
    returns ANCOVA table of results
    """
    import pandas as pd
    import numpy as np
    from scipy import stats
    from pingouin import ancova
    
    ranks_dv = stats.rankdata(df[dv], axis=0)
    ranks_covars = stats.rankdata(df[covars], axis=0)
    cols = covars
    if (len(ranks_covars.shape) == 1):
        ranks_covars = ranks_covars.reshape(-1, 1)
        cols = [covars]
    residual = pd.concat([pd.DataFrame({"DV": ranks_dv,group: df[group]}, index=df.index), pd.DataFrame(ranks_covars, columns=cols, index=df.index)], axis=1)
    aov_table = ancova(data=residual, dv="DV", covar=covars, between=group)
    return aov_table