import denv
import os

denv.load(".denv")

print(f"Example key: {os.getenv("key1")}")