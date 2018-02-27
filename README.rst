Bootstrap RST
=============

Bootstrap RST offers an easy access to the `bootstrap <http://getbootstrap.com>`_
framework using the `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ markup language.
Bootstrap RST provides a set of new directives and roles (row, column, button, list, etc.)
that allow seamless integration of the bootstrap framework.
Have a look at the source of this page for example and see below for what is available so far.

See demo at: `http://rougier.github.io/bootstrap-rst/ <http://rougier.github.io/bootstrap-rst/>`_.

Creators
========

**Nicolas P. Rougier** :

* `http://www.labri.fr/perso/nrougier/ <http://www.labri.fr/perso/nrougier/>`_
* `https://github.com/rougier <https://github.com/rougier>`_

Copyright and license
=====================

Code and documentation copyright 2014 Nicolas P. Rougier.
Code released under the MIT license. Docs released under Creative Commons.

Setting
=======

Requirements
------------

On Ubuntu::

   $ sudo -H -s
   # apt install python3-pip
   # pip3 install docutils
   # exit


Install
-------

On Ubuntu::

   $ cd bootstrap-rst/
   $ git checkout -b browse-code
   $ python3 setup.py --help
   $ python3 setup.py clean --all
   $ sudo -H -s
   # pip3 uninstall bootstrap-rst
   # python3 setup.py install
   # exit


Test
----

::

   $ cd bootstrap-rst/
   $ git checkout -b test-code
   $ make clean
   $ make
   $ firefox *.html


Commands
========

::

   $ mkdir test && cd test
   $ rst2bootstrap4 --help
   $ rst2bootstrap4 test.rst test.html

If you want to use Glyphicons icon font, you need Bootstrap v3::

  $ cd test/
  $ rst2bootstrap3 /usr/local/lib/python3.5/dist-packages/bootstrap_rst-0.1.dev20180222-py3.5.egg/doc/components.rst components.html

Carousel example needs some files::

  $ cd test/
  $ rst2bootstrap-carousel ~/src/bootstrap-rst/doc/carousel.rst carousel.html
