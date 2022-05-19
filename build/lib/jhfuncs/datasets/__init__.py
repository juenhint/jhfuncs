import pandas as _pd
import os.path as _op

ddir = _op.dirname(_op.realpath(__file__))
dts = _pd.read_csv(_op.join(ddir, 'datasets.csv'), sep=',')

__all__ = ["read_dataset", "list_dataset"]

def read_dataset(dname):
    """Read example datasets.

    Parameters
    ----------
    dname : string
        Name of dataset to read (without extension).
        Must be a valid dataset present in the datasets

    Returns
    -------
    data : :py:class:`pandas.DataFrame`
        Requested dataset.
    """
    # Check extension
    d, ext = _op.splitext(dname)
    if ext.lower() == '.csv':
        dname = d
    # Check that dataset exist
    if dname not in dts['dataset'].to_numpy():
        raise ValueError('Dataset does not exist. Valid datasets names are',
                         dts['dataset'].to_numpy())
    # Load dataset
    return _pd.read_csv(_op.join(ddir, dname + '.csv'), index_col=0, sep=',')

def list_dataset():
    """List available example datasets.

    Returns
    -------
    datasets : :py:class:`pandas.DataFrame`
        A dataframe with the name, description and reference of all the
        datasets.
     """
    return dts.set_index('dataset')
