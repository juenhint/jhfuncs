# jhfuncs
jhfuncs 0.42
A collection of bioinformatics tools for python utilizing pandas dataframes and pyplot. Originally built for managing the microbiome and metabolomics datasets in JH's PhD research in University of Jyväskylä, Finland. This package will be appended and updated ad hoc.

add_ellipse - Add ellipses to a plt scatterplot, indicating 95 % CIs of selected groups
center_log_ratio - Perform center log ratio (clr) -transformation to a data matrix
index_ouliers - Index datapoints outside 1.5*interquartile range
makeast - Transform a matrix of p-values to single or double asterixes, as per usual scientific notation
pearson_cor - Calculate a Pearson correlation matrix from two datasets
quade_rancova - Perform Quade's analysis of covariance (nonparametric ANCOVA)
relative_frequency - Transform a data matrix to relative frequencies
spearman_cor - Calculate a Spearman correlation matrix from two datasets

Until published, install by running:
# pip install git+ssh://git@github.com/juenhint/jhfuncs.git
or
# pip install git+https://github.com/juenhint/jhfuncs.git@main

Author: Hintikka, Jukka. jukka.e.hintikka@jyu.fi

ver 0.42:
- Improved documentation

ver 0.41:
- Added the function add_ellipse. 
- Added the option of omitting NaN-values in pearson_cor