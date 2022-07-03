=================
Custom directives
=================

Directives for page
===================

These directives are only one per pages.

.. todo::

   I plan to show warnings if declare mutilples.
   But it does not until implement.

.. rst:directive:: pyscript-env

   Define PyScript runtime environment as ``py-env``.

   Example:

   .. code-block:: rst

      .. pyscript-env::

         - beautifulsoup4
         - requests

Directives for content
======================

.. rst:directive:: pyscript-repl

   Render PyScript REPL as ``py-repl``.

   Example:

   .. code-block:: rst

      .. pyscript-repl::

         print("hello world")
