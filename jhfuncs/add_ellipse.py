def add_ellipse(ax, scores, group, comp1 = 0, comp2 = 1, palette=None, alpha=0.95, **kwargs):
    """Add ellipses to a PCA ordination plot based on categorical variables. The indexes of scores and group must match.
    
    Parameters
    ----------
    ax : matplotlib axes
        The axis of the plot
    scores : :py:class:`pandas.DataFrame`
        A pandas dataframe containing Scores from PCA
    group : :py:class:`pandas.Series`
        A pandas series containing group labels
    comp1 : int
        Index of the component to put on the X-axis, by default 0 or the first component
    comp2 : int
        Index of the component to put on the Y-axis, by default 1 or the second component
    palette : list
        Palette for colors
    alpha : float
        Alpha-value for the confidence interval, 0.95 by default
    **kwargs:
        Keyword arguments are passed on to matplotlib.patches.Ellipse
    """
    import scipy.stats as st
    import numpy as np
    from matplotlib import cm
    from matplotlib.patches import Ellipse
    
    if (palette == None):
        palette = cm.get_cmap("tab20").colors
    try:
        bb = (scores.index == group.index).all()
    except:
        print("indexes of scores and group must match!")
        return
    if (bb == False):
        print("indexes of scores and group must match!")
        return
    _ellipse_kwargs = {"linewidth": 2}
    _ellipse_kwargs.update(**kwargs)
    
    for i, u in enumerate(group.unique()):
        c1h = scores.loc[group[group == u].index, scores.columns[comp1]]
        c2h = scores.loc[group[group == u].index, scores.columns[comp2]]
        w = st.t.interval(alpha=alpha, df=len(c1h)-1, loc=np.mean(c1h), scale=st.sem(c1h))[1] - st.t.interval(alpha=alpha, df=len(c1h)-1, loc=np.mean(c1h), scale=st.sem(c1h))[0]
        h = st.t.interval(alpha=alpha, df=len(c2h)-1, loc=np.mean(c2h), scale=st.sem(c2h))[1] - st.t.interval(alpha=alpha, df=len(c2h)-1, loc=np.mean(c2h), scale=st.sem(c2h))[0]
        elps = Ellipse((c1h.mean(), c2h.mean()), w, h, edgecolor=palette[i],facecolor='none', **_ellipse_kwargs)
        ax.add_artist(elps)