======================
sphinxcontrib-pyscript
======================

Embed PyScript components into Sphinx documentation

Overview
========

This is extension of Sphinx to embed PyScript loader, script and REPL into your documents.

Library developer can provide experience "that what this can do it" for users easily as "Playground".

Installation
============

Install package from GitHub Releases.

.. code-block:: console

   pip install --find-links=https://github.com/attakei-lab/sphinxcontrib-pyscript/releases sphinxcontrib-pyscript

Usage
=====

First step
----------

Add this extension into your ``conf.py`` of Sphinx.

.. code-block:: python

   extensions = [
       "sphinxcontrib.pyscript",
   ]

Second step
-----------

Write it into your document.

.. code-block:: rst

   Title
   =====

   .. pyscript-env::

      googlefonts-markup

   Playground
   ----------

   .. pyscript-repl::

      from googlefonts_markup import Font
      noto_sans_jp = Font(family_name="Noto Sans JP")
      noto_sans_jp.css_url()

Third step
----------

Build document and access your document by browser.

You can see REPL input and result.

License
=======

Apache-2.0
