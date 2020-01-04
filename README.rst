===========================
NWB Documentation Utilities
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

This project is a collection of CLIs, scripts and modules useful to generate the NWB documentation.

Using hdmf-docutils to generate documentation for an extension: http://pynwb.readthedocs.io/en/latest/extensions.html#documenting-extensions


Installation
------------

::

  pip install hdmf-docutils



Available Tools
---------------

* ``nwb_generate_format_docs``: Generate figures and RST documents from the NWB YAML specification for the
  format specification documentation.

* ``nwb_init_sphinx_extension_doc``: Create format specification SPHINX documentation for an NWB extension.

* ``nwb_gallery_prototype``


Available Modules
-----------------

* ``hdmf_docutils/doctools/*``: This package contains modules used to generate figures of the hierarchies of
  NWB-N files and specifications as well as to help with the programmatic generation of reStructuredText (RST)
  documents.


Available Notebooks
-------------------

* `compare-hdf5-files.ipynb <https://github.com/hdmf-dev/hdmf-docutils/blob/master/hdmf_docutils/compare-hdf5-files.ipynb>`_: This
  notebook illustrates how to compare hdf5 files.


History
-------

nwb-utils was initially a sub-directory of the nwb-schema project. Corresponding history was extracted during
the `4th NWB Hackathon <https://neurodatawithoutborders.github.io/nwb_hackathons/HCK04_2018_Seattle/>`_ into a
dedicated *pip-installable* project to facilitate its use by both core NWB documentation projects and various
NWB extensions.


maintainers: how to make a release ?
------------------------------------

1. Configure ``~/.pypirc`` as described `here <https://packaging.python.org/distributing/#uploading-your-project-to-pypi>`_.


2. Make sure the cli and module work as expected.


3. List all tags sorted by version

   ::

       $ git fetch --tags && \
         git tag -l | sort -V


4. Choose the next release version number::

    release="X.Y.Z"


5. Tag the release. Requires a GPG key with signatures

   ::

       git tag -s -m "hdmf-docutils ${release}" ${release} origin/master

   And push

   ::

       git push origin ${release}


6. Create the source tarball and binary wheels

   ::

       rm -rf dist/
       python setup.py sdist bdist_wheel


7. Upload the packages to the testing PyPI instance

   ::

       twine upload --sign -r pypitest dist/*


8. Check the `PyPI testing package page <https://test.pypi.org/project/hdmf-docutils/>`_.


9. Upload the packages to the PyPI instance::

    twine upload --sign dist/*


10. Check the `PyPI package page <https://pypi.org/project/hdmf-docutils/>`_.


11. Create a virtual env, and make sure the package can be installed

    ::

        mkvirtualenv test-hdmf-docutils-install
        pip install hdmf-docutils


12. Cleanup

    ::

        deactivate
        rmvirtualenv test-hdmf-docutils-install
