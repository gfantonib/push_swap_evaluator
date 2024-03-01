#!/usr/bin/env python3

import subprocess
import sys

from evaluator_modules import _01_error_management
from evaluator_modules import _02_identity_test
from evaluator_modules import _03_simple_version
from evaluator_modules import _04_another_simple_version
from evaluator_modules import _05_middle_version
from evaluator_modules import _06_advanced_version
from evaluator_modules import _07_nothing_on_string
from evaluator_modules import _08_only_space_on_string
from evaluator_modules import _00_preparing_environment

# Exit Status
exit_status = 0

# Constant args
program = ["../push_swap"]
valgrind = ["valgrind", "--leak-check=full", "--show-leak-kinds=all", "--track-origins=yes"]
valgrind_check = "All heap blocks were freed -- no leaks are possible"

# Colours
GREEN = "\033[32;1m"
RED = "\033[31;1m"
COLOR_LIMITER = "\033[0m"
colours = [GREEN, RED, COLOR_LIMITER]

# Make clean and Make
clean = ["make", "clean", "-C", "../"]
subprocess.run(clean, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
make = ["make", "-C", "../"]
subprocess.run(make, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Preparing environment
print("\nPreparing environment")
_00_preparing_environment.preparing_environment()
print("\n")

# Error management test
print("Error management")
exit_status = _01_error_management.error_management(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

# Identity test
print("Identity test")
exit_status = _02_identity_test.identity_test(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

# Simple version
print("Simple version")
exit_status = _03_simple_version.simple_version(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

# Another simple version
print("Another simple version")
exit_status = _04_another_simple_version.another_simple_version(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

# Middle version
print("Middle version")
exit_status = _05_middle_version.middle_version(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

# Advanced version
print("Advanced version")
exit_status = _06_advanced_version.advanced_version(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

# Nothing on string
print("Nothing on string")
exit_status = _07_nothing_on_string.nothing_on_string(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

# Only space on string
print("Only space on string")
exit_status = _08_only_space_on_string.only_space_on_string(program, valgrind, valgrind_check, colours, exit_status)
print("\n")

subprocess.run(clean, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if exit_status == 0:
	print("🎉🎊🌟✨👏🎈🎈👏👏👏🎈🎈👏🌟✨🎉🎊\n")

exit(exit_status)