Maintainers: How to make a new release ?
----------------------------------------

*Fixed font text area below list commands expected to be entered in a bash shell*

1. Configure ``~/.pypirc`` as described `here <https://packaging.python.org/distributing/#uploading-your-project-to-pypi>`_.

2. Make sure the cli and module work as expected.

3. Choose the next release version number:

::

    release="X.Y.Z"

4. Update `setup.py`

::

    sed -i -re "s/'version':.+/'version': '${release}'/" setup.py
    git add setup.py
    git commit -m "setup.py: Update version to \"${release}\"

Review commit, then push:

::

    git push origin master

5. Tag the release and push:

*If you don't have a GPG key, omit the ``-s`` option.*

::

    git tag -s -m "nwb-docutils ${release}" ${release} origin/master
    git push origin ${release}

6. Create the source tarball and wheel:

::

    rm -rf dist/
    python setup.py sdist bdist_wheel

7. Upload the packages to the testing PyPI instance:

::

    twine upload -r pypitest dist/*

8. Check the `PyPI testing package page <https://test.pypi.org/project/nwb-docutils/>`_.

9. Upload the packages to the PyPI instance::

::

    twine upload --sign dist/*

10. Check the `PyPI package page <https://pypi.org/project/nwb-docutils/>`_.
