# -- Path setup

# -- Project information
project = "sphinxcontrib-pyscript"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = "0.1.0"

# -- General configuration
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinxcontrib.pyscript",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "nature"
html_static_path = ["_static"]

# sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
