import os

def load(denvPath: str = ".denv"):
    if os.path.exists(denvPath):
        with open(denvPath) as f:
            for line in f.read().strip().split("\n"):
                if not line:
                    continue

                line = line.split("#", 1)[0].strip()

                if not line:
                    continue
                
                if "=>" in line:
                    key, val = line.replace("@", "").strip().split("=>", 1)
                    os.environ[key.strip()] = val.strip()
    else:
        print("No .denv file found, please create one!")
