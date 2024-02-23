import subprocess

def identity_test(program, valgrind, valgrind_check, colours):

	# Creating args
	battery = ["One arg ordered", "Two args ordered", "Four args ordered", "Nine args ordered"]
	one_arg_ordered = ["42"]
	two_arg_ordered = ["2", "3"]
	four_arg_ordered = ["0", "1", "2", "3"]
	nine_arg_ordered = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

	args = [one_arg_ordered, two_arg_ordered, four_arg_ordered, nine_arg_ordered]

	# Reference output
	stdout_ref_list = ["", "", "", "", ""]

	# Runing and collecting output and error
	stdout_list = []
	stderr_val_list = []
	for arg in args:

		cmd = program + arg
		output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		stdout_list.append(output.stdout)

		cmd_val = valgrind + cmd
		output_val = subprocess.run(cmd_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		stderr_val_list.append(output_val.stderr)
		
	# Printing test check
	i = 0
	for err, err_val in zip(stdout_list, stderr_val_list):
		print(f"{battery[i].upper()}")
		if (err == stdout_ref_list[i]):
			print(f"{colours[0]}{i + 1}. OK{colours[2]}")
		else:
			print(f"{colours[1]}{i + 1}. KO{colours[2]}")
		if valgrind_check in err_val:
			print(f"{colours[0]}   MOK\n{colours[2]}")
		else:
			print(f"{colours[1]}   MKO\n{colours[2]}")
		i = i + 1