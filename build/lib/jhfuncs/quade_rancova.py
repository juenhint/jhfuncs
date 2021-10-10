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