from sphinxcontrib import pyscript

import pytest
from sphinx.testing.util import SphinxTestApp
from sphinxcontrib import extension  # noqa


def test_it():
    assert True is True
    # TODO: Write testing for your library indepency


@pytest.mark.sphinx("html")
def test_default(app: SphinxTestApp, status: StringIO, warning: StringIO):
    app.build()
    # TODO: Write testing for your library with sphinx-build
