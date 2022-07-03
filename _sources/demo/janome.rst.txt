===============================
Japanese morphological analysis
===============================

Demo to run Japanese morphological analysis by `janome <https://pypi.org/project/Janome/>`_.

.. pyscript-env::

   - janome

Code
====

.. code-block:: rst

   .. pyscript-env::

      - janome

Playground
==========

.. note:: Need long-time waiting to initialize tokenizer.

.. pyscript-repl::

   from janome.tokenizer import Tokenizer

   t = Tokenizer()
   for token in t.tokenize('すもももももももものうち'):
       print(token)
