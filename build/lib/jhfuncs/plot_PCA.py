def plot_PCA(data, model=None, components=[0,1], ax=None, group=None, group2=None, palette=None, ellipse_kwargs={}, scatter_kwargs={}, **kwargs):
    """
    Parameters
    ----------
    data : :py:class:`pandas.DataFrame`
        A dataframe with samples in rows and variables in columns
    model : sklearn PCA instance
        The model to be used for PCA. The default model is PCA with default parameters, random_state 0.
    ax : matplotlib axes
        The axes object to plot onto
    group : list or pandas Series
        First grouping variable, determines marker color and ellipses, if used
    group2 : list or pandas Series
        Second grouping variable, determines the style of markers
    palette : list
        Color palette for groups, NOTE: len(palette) must match the number of groups
    ellipse_kwargs : dict
        Parameters to be passed on to jhfuncs.add_ellipse
    scatter_kwargs : dict
        Parameters to be passed on to seaborn.scatterplot
    
    Returns
    -------
    data : :py:class:`pandas.DataFrame`
        The scores from the sklearn PCA
    sp : matplotlib axes
        Matplotlib instance of the scatterplot
        
    Additional keyword arguments
    ----------------------------
    font_scale : float
        Scaling for the font size
    """
    import seaborn as _sns
    import matplotlib.pyplot as _plt
    import matplotlib.cm as _cm
    import pandas as _pd
    import numpy as _np
    from sklearn.decomposition import PCA as _PCA
    from jhfuncs import add_ellipse
    
    plotparams = {"font_scale": 1, "draw_ellipses": True}
    plotparams.update(kwargs)
    _plt.rcParams.update({'font.size': 15*plotparams.get("font_scale")})
    if (model is None):
        model = _PCA(random_state=0)
    scores = _pd.DataFrame(model.fit_transform(data), index=data.index)
    
    scatterparams = {"s": 200}
    scatterparams.update(scatter_kwargs)
    n_groups=1;
    if (ax is None):    
        fig, ax = _plt.subplots(1, 1, figsize=[10,10])
        scatterparams["ax"] = ax
    if (group is not None):
        scatterparams["hue"] = group
        n_groups = _np.unique(group).size
    if (group2 is not None):
        scatterparams["style"] = group2
    if (palette is None):
        palette = list(_cm.get_cmap("tab20").colors)[0:n_groups]
    
    scatterparams["palette"] = palette 
    sp = _sns.scatterplot(x=scores[components[0]], y=scores[components[1]], **scatterparams)
    
    ellipseparams = {"alpha":0.95}
    ellipseparams["palette"] = palette
    ellipseparams.update(ellipse_kwargs)

    if (plotparams.get("draw_ellipses")):
        add_ellipse(ax, scores, group=group, comp1=components[0], comp2=components[1], **ellipseparams)
    ax.set_xlabel(f"PC1 {round(model.explained_variance_ratio_[components[0]]*100,1)} %")
    ax.set_ylabel(f"PC2 {round(model.explained_variance_ratio_[components[1]]*100,1)} %")
    ax.legend(markerscale=2)
    _plt.show()
    return scores, sp