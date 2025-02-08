# -*- coding: utf-8 -*-

import versioneer

from setuptools import setup, find_packages

with open('README.rst', 'r') as fp:
    readme = fp.read()


setup_args = {
    'name': 'hdmf_docutils',
    'version': versioneer.get_version(),
    'cmdclass': versioneer.get_cmdclass(),
    'description': 'Collection of CLIs, scripts and modules useful to generate the NWB documentation',
    'long_description': readme,
    'long_description_content_type': 'text/x-rst; charset=UTF-8',
    'author': 'Oliver Ruebel',
    'author_email': 'oruebel@lbl.gov',
    'url': 'https://github.com/hdmf-dev/hdmf-docutils',
    'license': "BSD",
    'install_requires': [
        'matplotlib',
        'networkx',
        'hdmf',
        'pillow',
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'ruamel.yaml'
    ],
    'setup_requires': 'pytest-runner',
    'packages': find_packages(),
    'package_data': {'hdmf_docutils': ["*.ipynb"]},
    'entry_points': {
        'console_scripts': [
            'hdmf_generate_format_docs=hdmf_docutils.generate_format_docs:main',
            'nwb_generate_format_docs=hdmf_docutils.generate_format_docs:nwb_main',
            'hdmf_init_sphinx_extension_doc=hdmf_docutils.init_sphinx_extension_doc:main',
            'nwb_init_sphinx_extension_doc=hdmf_docutils.init_sphinx_extension_doc:nwb_main',
        ]
    },
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Topic :: Documentation :: Sphinx",
    ],
    'keywords': 'Neuroscience '
                'python '
                'HDF '
                'HDF5 '
                'cross-platform '
                'open-data '
                'data-format '
                'open-source '
                'open-science '
                'reproducible-research '
                'NWB '
                'NWB:N '
                'NeurodataWithoutBorders',
    'zip_safe': False
}

if __name__ == '__main__':
    setup(**setup_args)
