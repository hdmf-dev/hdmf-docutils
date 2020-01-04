import sys

import pytest

from hdmf_docutils.sg_prototype import build


def test_build(tmpdir):
    def _build():
        build(None, tgt_dir=str(tmpdir.join('_html_sg-prototype_TEST')))

    if sys.platform == 'win32':
        with pytest.raises(RuntimeError) as excinfo:
            _build()
            assert "Windows is not supported" in str(excinfo.value)
    else:
        _build()

    tmpdir.remove(rec=1)
