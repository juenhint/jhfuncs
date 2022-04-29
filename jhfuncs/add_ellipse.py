def add_ellipse(ax, scores, group, comp1 = 0, comp2 = 1, palette=None, **kwargs):
    """Add ellipses to a PCA plot based on categorical variables. The indexes of scores and group must match.
    
    ax: Matplotlib ax object for plot
    scores: Pandas Dataframe containing Scores from PCA
    group: Pandas Series containing group labels
    comp1: Component on the X-axis
    comp2: Component on the Y-axis
    palette: Palette for colors
    """
    alpha = 0.95
    if (kwargs.get("alpha")):
        alpha=kwargs["alpha"]
    import scipy.stats as st
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
    
    for i, u in enumerate(group.unique()):
        c1h = scores.loc[group[group == u].index, comp1]
        c2h = scores.loc[group[group == u].index, comp2]
        w = st.t.interval(alpha=alpha, df=len(c1h)-1, loc=np.mean(c1h), scale=st.sem(c1h))[1] - st.t.interval(alpha=alpha, df=len(c1h)-1, loc=np.mean(c1h), scale=st.sem(c1h))[0]
        h = st.t.interval(alpha=alpha, df=len(c2h)-1, loc=np.mean(c2h), scale=st.sem(c2h))[1] - st.t.interval(alpha=alpha, df=len(c2h)-1, loc=np.mean(c2h), scale=st.sem(c2h))[0]
        elps = Ellipse((c1h.mean(), c2h.mean()), w, h, linewidth=2,edgecolor=palette[i],facecolor='none')
        ax.add_artist(elps)