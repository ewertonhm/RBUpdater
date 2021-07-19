from pathlib import *

def create_routeros_folder():
    p = Path('./routeros')
    if not p.exists() and not p.is_dir():
        p.mkdir()
    return p.cwd()