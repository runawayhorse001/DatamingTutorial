# -*- coding: utf-8 -*-
#
# theano documentation build configuration file, created by
# sphinx-quickstart on Tue Oct  7 16:34:06 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.
import sys, os

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#sys.path.append(os.path.abspath('some/directory'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo',"sphinxtogithub"]

sphinx_to_github = True
sphinx_to_github_verbose = True
sphinx_to_github_encoding = "utf-8"

try:
    from sphinx.ext import pngmath
    extensions.append('sphinx.ext.pngmath')
except ImportError:
    print >>sys.stderr, 'Warning: could not import sphinx.ext.pngmath'
    pass

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

show_authors = True

# General substitutions.
project = 'Data Mining With Python and R'
copyright = '2016, Wenqiang Feng'

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
#
# The short X.Y version.
version = '1.01'
# The full version, including alpha/beta/rc tags.
release = 'v1.01'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directories, that shouldn't be searched
# for source files.
exclude_dirs = ['scripts']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
#html_style = 'default.css'
#html_theme = 'sphinxdoc'
html_theme = 'sphinx_rtd_theme'
#html_theme_options = {
#    "rightsidebar": "true",
#    "relbarbgcolor": "black"
#}
#html_theme = 'traditional'
#html_theme = "classic"
#html_theme_options = {
#    "rightsidebar": "true",
#    "relbarbgcolor": "black"
#}
# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (within the static path) to place at the top of
# the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['.static', 'images']
html_static_path = ['images']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, the number of figure will show
numfig = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'testdoc'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '11pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).

latex_documents = [
  ('index', 'datamining.tex', 'Data Mining With Python and R Tutorials',
   'Wenqiang Feng', 'manual'),
]
# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
#on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

#if not on_rtd:  # only import and set the theme if we're building docs locally
#    import sphinx_rtd_theme
#    html_theme = 'sphinx_rtd_theme'
#    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# otherwise, readthedocs.org uses their theme by default, so no need to specify it
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# Additional stuff for the LaTeX preamble.
latex_preamble =  '\\usepackage{amsmath}\n'+\
                          '\\usepackage{mathtools}\n'+\
                          '\\usepackage{amsfonts}\n'+\
                          '\\usepackage{amssymb}\n'+\
                          '\\usepackage{dsfont}\n'+\
                          '\\def\\Z{\\mathbb{Z}}\n'+\
                          '\\def\\R{\\mathbb{R}}\n'+\
                          '\\def\\bX{\\mathbf{X}}\n'+\
        '\\def\\bU{\\mathbf{U}}\n'+\
                          '\\def\\bV{\\mathbf{V}}\n'+\
                          '\\def\\V1{\\mathds{1}}\n'+\
        '\\def\\hU{\\mathbf{\hat{U}}}\n'+\
                          '\\def\\hS{\\mathbf{\hat{\Sigma}}}\n'+\
                          '\\def\\hV{\\mathbf{\hat{V}}}\n'+\
                          '\\def\\E{\\mathbf{E}}\n'+\
                          '\\def\\F{\\mathbf{F}}\n'+\
                          '\\def\\x{\\mathbf{x}}\n'+\
                          '\\def\\h{\\mathbf{h}}\n'+\
                          '\\def\\v{\\mathbf{v}}\n'+\
                          '\\def\\nv{\\mathbf{v^{{\bf -}}}}\n'+\
                          '\\def\\nh{\\mathbf{h^{{\bf -}}}}\n'+\
                          '\\def\\s{\\mathbf{s}}\n'+\
                          '\\def\\b{\\mathbf{b}}\n'+\
                          '\\def\\c{\\mathbf{c}}\n'+\
                          '\\def\\W{\\mathbf{W}}\n'+\
                          '\\def\\C{\\mathbf{C}}\n'+\
                          '\\def\\P{\\mathbf{P}}\n'+\
                          '\\def\\T{{\\bf \\mathcal T}}\n'+\
                          '\\def\\B{{\\bf \\mathcal B}}\n'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

default_role = 'math'
pngmath_divpng_args = ['-gamma 1.5','-D 110']
#pngmath_divpng_args = ['-gamma', '1.5', '-D', '110', '-bg', 'Transparent'] 
pngmath_latex_preamble =  '\\usepackage{amsmath}\n'+\
                          '\\usepackage{mathtools}\n'+\
                          '\\usepackage{amsfonts}\n'+\
                          '\\usepackage{amssymb}\n'+\
                          '\\usepackage{dsfont}\n'+\
                          '\\def\\Z{\\mathbb{Z}}\n'+\
                          '\\def\\R{\\mathbb{R}}\n'+\
                          '\\def\\bX{\\mathbf{X}}\n'+\
        '\\def\\U{\\mathbf{U}}\n'+\
                          '\\def\\V{\\mathbf{V}}\n'+\
                          '\\def\\V1{\\mathds{1}}\n'+\
        '\\def\\hU{\\mathbf{\hat{U}}}\n'+\
                          '\\def\\hS{\\mathbf{\hat{\Sigma}}}\n'+\
                          '\\def\\hV{\\mathbf{\hat{V}}}\n'+\
                          '\\def\\E{\\mathbf{E}}\n'+\
                          '\\def\\F{\\mathbf{F}}\n'+\
                          '\\def\\x{\\mathbf{x}}\n'+\
                          '\\def\\h{\\mathbf{h}}\n'+\
                          '\\def\\v{\\mathbf{v}}\n'+\
                          '\\def\\nv{\\mathbf{v^{{\bf -}}}}\n'+\
                          '\\def\\nh{\\mathbf{h^{{\bf -}}}}\n'+\
                          '\\def\\s{\\mathbf{s}}\n'+\
                          '\\def\\b{\\mathbf{b}}\n'+\
                          '\\def\\c{\\mathbf{c}}\n'+\
                          '\\def\\W{\\mathbf{W}}\n'+\
                          '\\def\\C{\\mathbf{C}}\n'+\
                          '\\def\\P{\\mathbf{P}}\n'+\
                          '\\def\\T{{\\bf \\mathcal T}}\n'+\
                          '\\def\\B{{\\bf \\mathcal B}}\n'
