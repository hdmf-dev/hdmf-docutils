import shutil
import os
import pytest
import tempfile

from pynwb.docutils.sg_prototype import build


@pytest.fixture(scope="function")
def tempdir():
    temp_dir = tempfile.mkdtemp()
    return temp_dir


def test_build(tempdir):

    tgt_dir = os.path.join(tempdir, '_html_sg-prototype_TEST')
    build(None, tgt_dir=tgt_dir)
    shutil.rmtree(tempdir)
