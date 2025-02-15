import importlib.metadata
from importlib.resources import as_file, files

__version__ = importlib.metadata.version(__name__)


def orfs_dir():
    return as_file(files(__name__))
