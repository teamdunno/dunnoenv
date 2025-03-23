# dunnoenv
A different version of .env files without the boring `KEY1="VALUE"` syntax.

.denv files are handled using Python.

# Usage
- Make a .denv file (No need to hide it, just add it to your .gitignore if you plan on sharing the code on GitHub or hosting it)
- Edit the file with the following syntax:
```denv
# .denv files also support comments!
@apiKey => test-0cgiclfifxji3a0aq8x1i81j1
```
- Download the denv.py file.
- Move the file to your script's path.
- Import it using `import denv`
- Now load the .denv file using:
```py
import denv
denv.load()

# Or specify a custom path!
# denv.load("path/to/your/denv/file/filename.denv")
import os

os.getenv("apiKey") # test-0cgiclfifxji3a0aq8x1i81j1
# or os.environ["apiKey"]
```
For an example, run example.py
