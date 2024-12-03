import glob
import os

CWD = os.path.dirname(__file__)
DATA_PATH = glob.glob(f"{CWD}/*.txt")[0]

from utils.fileio import read_line_by_line

__all__ = ["DATA_PATH", "read_line_by_line"]
