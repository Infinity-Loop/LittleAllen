import subprocess
print "clean"
subprocess.call(['python clean.py'], shell=True)
print "build model"
subprocess.call(['python buildmodel.py'], shell=True)
print "generate solution"
subprocess.call(['python solution.py'], shell=True)
