# jhfuncs - A Python package of miscellaneous useful tools
jhfuncs 0.44    
A collection of bioinformatics tools for python utilizing pandas dataframes and pyplot. Originally built for managing the microbiome and metabolomics datasets in JH's PhD research in University of Jyväskylä, Finland. This package will be appended and updated ad hoc.

_plot_PCA_ - Perform Principal Component Analysis (PCA) and plot the results on a neat seaborn graph    
_center_log_ratio_ - Perform center log ratio (clr) -transformation to a data matrix    
_index_ouliers_ - Index datapoints outside 1.5*interquartile range    
_makeast_ - Transform a matrix of p-values to single or double asterixes, as per usual scientific notation    
_pearson_cor_ - Calculate a Pearson correlation matrix from two datasets    
_quade_rancova_ - Perform Quade's analysis of covariance (nonparametric ANCOVA)    
_relative_frequency_ - Transform a data matrix to relative frequencies    
_spearman_cor_ - Calculate a Spearman correlation matrix from two datasets    

Until published in pip, install on Windows by running:
```
>pip install https://github.com/juenhint/jhfuncs/tarball/main
```
or
```
pip install https://github.com/juenhint/jhfuncs/zipball/main  
```
Author: Hintikka, Jukka. jukka.e.hintikka@jyu.fi

ver 0.44
- Added the function plot_PCA

ver 0.43:
- Added example datasets
- Improved documentation
- Fixed bugs in correlation functions
- Added the function add_ellipse. 
- Added the option of omitting NaN-values in pearson_cor
