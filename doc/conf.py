# -- Path setup

# -- Project information
project = "sphinxcontrib-pyscript"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = "0.1.0"

# -- General configuration
extensions = [
    "sphinxcontrib.pyscript",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]
