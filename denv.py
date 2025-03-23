import os

def load(denvPath: str = ".denv"):
    if os.path.exists(denvPath):
        with open(denvPath) as f:
            for line in f.read().strip().split("\n"):
                if not line or line.startswith("#"):
                    continue
                key, val = line.strip().split(": ", 1)
                os.environ[key] = val
    else:
        print("No .denv file found, please create one!")
