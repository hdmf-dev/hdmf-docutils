
from nwb_docutils.sg_prototype import build


def test_build(tmpdir):
    build(None, tgt_dir=str(tmpdir.join('_html_sg-prototype_TEST')))
    tmpdir.remove(rec=1)
