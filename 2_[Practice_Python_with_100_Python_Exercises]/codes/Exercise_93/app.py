import glob

files = glob.glob("subdirs/**/*.py", recursive=True)
print((files))
