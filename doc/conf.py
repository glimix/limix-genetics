# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
os.environ['BOKEH_DOCS_MISSING_API_KEY_OK'] = 'yes'

try:
    import limix_genetics
    version = limix_genetics.__version__
except ImportError:
    version = 'unknown'

needs_sphinx = '1.5'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'bokeh.sphinxext.bokeh_autodoc',
    'bokeh.sphinxext.bokeh_enum',
    'bokeh.sphinxext.bokeh_gallery',
    'bokeh.sphinxext.bokeh_github',
    'bokeh.sphinxext.bokeh_jinja',
    'bokeh.sphinxext.bokeh_index_toctree',
    'bokeh.sphinxext.bokeh_model',
    'bokeh.sphinxext.bokeh_options',
    'bokeh.sphinxext.bokeh_palette',
    'bokeh.sphinxext.bokeh_palette_group',
    'bokeh.sphinxext.bokeh_plot',
    'bokeh.sphinxext.bokeh_prop',
    'bokeh.sphinxext.collapsible_code_block',
]
napoleon_google_docstring = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'limix-genetics'
copyright = '2016, Danilo Horta'
author = 'Danilo Horta'
release = version
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'conf.py']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'default'
htmlhelp_basename = 'limix-geneticsdoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'limix-genetics.tex', 'limix-genetics Documentation',
     'Danilo Horta', 'manual'),
]
man_pages = [
    (master_doc, 'limix-genetics', 'limix-genetics Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'limix-genetics', 'limix-genetics Documentation',
     author, 'limix-genetics', 'One line description of project.',
     'Miscellaneous'),
]
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None)
}
html_context = {
    'SITEMAP_BASE_URL': 'https://limix-genetics.readthedocs.io/en/latest/',
    'DESCRIPTION': 'Genetic related tools for Limix',
    'AUTHOR': author,
    'VERSION': version,
}
html_show_sourcelink = True
