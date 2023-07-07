import subprocess

result = subprocess.check_output("./lab0", shell=True).decode()
assert (result.startswith("Welcome to CS112 and C++, "))
assert (result.strip().endswith("!"))

print("All tests passed!")