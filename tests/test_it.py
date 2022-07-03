from io import StringIO

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test_default(app: SphinxTestApp, status: StringIO, warning: StringIO):
    app.build()
    soup = BeautifulSoup(open(app.outdir / "index.html").read(), "html.parser")
    assert soup.find("py-env") is None


@pytest.mark.sphinx("html")
def test_render_repl(app: SphinxTestApp, status: StringIO, warning: StringIO):
    app.build()
    soup = BeautifulSoup(open(app.outdir / "repl-no-env.html").read(), "html.parser")
    assert soup.find("py-env") is None
    assert soup.find("py-repl")
    assert soup.find("script", attrs={"src": "https://pyscript.net/alpha/pyscript.js"})


@pytest.mark.sphinx("html")
def test_render_env_and_repl(app: SphinxTestApp, status: StringIO, warning: StringIO):
    app.build()
    soup = BeautifulSoup(open(app.outdir / "repl-with-env.html").read(), "html.parser")
    assert soup.find("py-repl")
    assert soup.find("script", attrs={"src": "https://pyscript.net/alpha/pyscript.js"})
    py_env = soup.find("py-env")
    assert py_env
    assert "- docutils" in py_env.contents[0]
