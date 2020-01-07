===========================
HDMF Documentation Utilities
===========================

*This project is under active development. Its content, API and behavior may change at any time. We mean it.*

.. image:: https://img.shields.io/pypi/l/hdmf-docutils.svg
    :target: https://github.com/hdmf-dev/hdmf-docutils/blob/master/license.txt
    :alt:    PyPI - License

.. image:: https://img.shields.io/pypi/v/hdmf-docutils.svg
    :target: https://pypi.org/project/hdmf-docutils/
    :alt:    PyPI

.. image:: https://dev.azure.com/hdmf-dev/hdmf-docutils/_apis/build/status/hdmf-dev.hdmf-docutils?branchName=master
    :target: https://dev.azure.com/hdmf-dev/hdmf-docutils/_build/latest?definitionId=1&branchName=master
    :alt:    Build Status

Overview
--------

This project is a collection of CLIs, scripts and modules useful to generate the HDMF documentation.

Using hdmf-docutils to generate documentation for an extension: http://pynwb.readthedocs.io/en/latest/extensions.html#documenting-extensions


Installation
------------

::

  pip install hdmf-docutils



Available Tools
---------------

* ``hdmf_generate_format_docs``: Generate figures and RST documents from the HDMF YAML specification for the
  format specification documentation. Previously called "nwb_generate_format_docs".

* ``hdmf_init_sphinx_extension_doc``: Create format specification SPHINX documentation for an HDMF extension.
  Previously called "nwb_init_sphinx_extension_doc".

* ``hdmf_gallery_prototype``: Tool for prototyping sphinx gallery examples. Previously called "nwb_gallery_prototype".


Available Modules
-----------------

* ``hdmf_docutils/doctools/*``: This package contains modules used to generate figures of the hierarchies of
  HDMF files and specifications as well as to help with the programmatic generation of reStructuredText (RST)
  documents.


Available Notebooks
-------------------

* `compare-hdf5-files.ipynb <https://github.com/hdmf-dev/hdmf-docutils/blob/master/hdmf_docutils/compare-hdf5-files.ipynb>`_: This
  notebook illustrates how to compare hdf5 files.


History
-------

nwb-docutils was renamed to hdmf-docutils and generalized to be (mostly) independent of NWB in January, 2020.

nwb-docutils was initially a sub-directory of the nwb-schema project. Corresponding history was extracted during
the `4th NWB Hackathon <https://neurodatawithoutborders.github.io/nwb_hackathons/HCK04_2018_Seattle/>`_ into a
dedicated *pip-installable* project to facilitate its use by both core NWB documentation projects and various
NWB extensions.
