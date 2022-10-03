from os import mkdir
from pathlib import Path

class Site:

    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)
        pass

    def create_dir(self,path):
        directory = f"{self.dest}/{self.dest.relative_to(path)}"
        mkdir(directory, parents = True, exists_ok = True)
    
    def build(self):
        mkdir(self.dest, parents = True, exists_ok = True)
        
        
        for path in self.source.rglob("*"):
            if path.is_dir():    
                self.create_dir(path)
