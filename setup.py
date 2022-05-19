from setuptools import setup, find_packages

VERSION = '0.44' 
DESCRIPTION = 'Tools for dataframe handling and analysis'
LONG_DESCRIPTION = 'Tools for handling and analysis of dataframes containing microbiome and metabolomics data. This packace utilizes mostly pandas, numpy and pyplot.'

setup(name='jhfuncs',
version=VERSION,
description= DESCRIPTION,
long_description=LONG_DESCRIPTION,
url='#',
author='Jukka Hintikka',
author_email='juenhint@jyu.fi',
license='MIT',
packages=find_packages(),
zip_safe=False,
install_requires=["pandas","numpy","scipy","matplotlib","pingouin"],
include_package_data=True,
package_data={'': ['datasets/*.csv']}
)