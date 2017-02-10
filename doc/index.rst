===============================
Limix-genetics's documentation
===============================

Genetic related tools for Limix.

.. toctree::
    :caption: Table of contents
    :name: mastertoc
    :maxdepth: 2

    install
    functions

.. bokeh-plot::

  from bokeh.plotting import figure, output_file, show

  output_file("example_bokeh.html")

  x = [1, 2, 3, 4, 5]
  y = [6, 7, 6, 4, 5]

  p = figure(title="example_bokeh", plot_width=300, plot_height=300)
  p.line(x, y, line_width=2)
  p.circle(x, y, size=10, fill_color="white")

  show(p)

-----------------
Comments and bugs
-----------------

You can get the source and open issues `on Github.`_

.. _on Github.: https://github.com/glimix/limix-genetics
