def quade_rancova(df, dv, covars, group, **kwargs):
    """Perform Quade's ANCOVA (nonparametric analysis of covariance) on dataset
    
    Parameters
    ----------
    df: :py:class:`pandas.DataFrame`
        Pandas dataframe containing dependent, grouping and confounding variables
    dv: string
        Name of the columns containing the dependent variable
    covars: string or list<string>
        Names of the columns containing the covariables
    group: string
        Name of the grouping (independent) variable. Must be discrete.
    **kwargs:
        Keyword arguments are passed to pingouin.ancova
    
    Returns
    -------
    aov_table : :py:class:`pandas.DataFrame`
        ANCOVA summary from pingouin:

        * ``'Source'``: Names of the factor considered
        * ``'SS'``: Sums of squares
        * ``'DF'``: Degrees of freedom
        * ``'F'``: F-values
        * ``'p-unc'``: Uncorrected p-values
        * ``'np2'``: Partial eta-squared
    """
    import pandas as pd
    import numpy as np
    from scipy import stats
    from pingouin import ancova
    
    _ancova_kwargs = {"effsize": "np2"}
    _ancova_kwargs.update(**kwargs)
    ranks_dv = stats.rankdata(df[dv], axis=0)
    ranks_covars = stats.rankdata(df[covars], axis=0)
    cols = covars
    if (len(ranks_covars.shape) == 1):
        ranks_covars = ranks_covars.reshape(-1, 1)
        cols = [covars]
    residual = pd.concat([pd.DataFrame({"DV": ranks_dv,group: df[group]}, index=df.index), pd.DataFrame(ranks_covars, columns=cols, index=df.index)], axis=1)
    aov_table = ancova(data=residual, dv="DV", covar=covars, between=group, **_ancova_kwargs)
    return aov_table