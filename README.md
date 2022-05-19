# jhfuncs - A Python package of miscellaneous useful tools
jhfuncs 0.42    
A collection of bioinformatics tools for python utilizing pandas dataframes and pyplot. Originally built for managing the microbiome and metabolomics datasets in JH's PhD research in University of Jyväskylä, Finland. This package will be appended and updated ad hoc.

_add_ellipse_ - Add ellipses to a plt scatterplot, indicating 95 % CIs of selected groups    
_center_log_ratio_ - Perform center log ratio (clr) -transformation to a data matrix    
_index_ouliers_ - Index datapoints outside 1.5*interquartile range    
_makeast_ - Transform a matrix of p-values to single or double asterixes, as per usual scientific notation    
_pearson_cor_ - Calculate a Pearson correlation matrix from two datasets    
_quade_rancova_ - Perform Quade's analysis of covariance (nonparametric ANCOVA)    
_relative_frequency_ - Transform a data matrix to relative frequencies    
_spearman_cor_ - Calculate a Spearman correlation matrix from two datasets    

Until published, install by running:
```
>pip install https://github.com/juenhint/jhfuncs/zipball/main
```
or
```
pip install https://github.com/juenhint/jhfuncs/tarball/main  
```
Author: Hintikka, Jukka. jukka.e.hintikka@jyu.fi

ver 0.42:
- Improved documentation
- Fixed bugs in correlation functions

ver 0.41:
- Added the function add_ellipse. 
- Added the option of omitting NaN-values in pearson_cor
