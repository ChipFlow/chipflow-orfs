import pytest

def test_orfs_dir():

    from chipflow_orfs import orfs_dir

    with orfs_dir() as d:
        assert d.is_dir()

