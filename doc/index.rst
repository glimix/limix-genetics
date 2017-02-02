===============================
Limix-genetics's documentation
===============================

Genetic related tools for Limix.

-------
Install
-------

The recommended way of installing it is via `conda`_

.. code-block:: bash

  conda install -c conda-forge limix-genetics

An alternative way would be via pip

.. code-block:: bash

  pip install limix-genetics

.. _conda: http://conda.pydata.org/docs/index.html

--------
Examples
--------

.. bokeh-plot::
  :include-source:

  from bokeh.plotting import output_file
  from pandas import DataFrame
  from numpy import arange
  from numpy.random import RandomState

  from limix_genetics import qqplot

  def _create_df(label, pvals, marker):
    df_ = DataFrame(columns=['label', 'marker', 'p-value'])
    df_['p-value'] = df_['p-value'].astype(float)
    df_['p-value'] = pvals
    df_['label'] = label
    df_['marker'] = marker
    df_.set_index(['label', 'marker'], inplace=True)
    return df_

  random = RandomState(0)
  n = 1000
  pvals0 = random.rand(n)
  pvals1 = random.rand(n)
  marker = arange(n)

  df = DataFrame(columns=['label', 'marker', 'p-value']).set_index(
      ['label', 'marker'])
  df['p-value'] = df['p-value'].astype(float)

  df = df.append(_create_df('qep', pvals0, marker))
  df = df.append(_create_df('lmm', pvals1, marker))

  df.sort_index(inplace=True)


  qqplot(df, output=lambda:output_file("example.html"))

*****************
Comments and bugs
*****************

You can get the source and open issues `on Github.`_

.. _on Github.: https://github.com/glimix/limix-genetics
