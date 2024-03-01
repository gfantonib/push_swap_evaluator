import subprocess

def error_management(program, valgrind, valgrind_check, colours, exit_status):

	# Creating args
	battery = ["str on list", "dup on list", "max on list", "nothing on list"]
	str_on_list = ["1", "2", "3", "abc", "5", "6", "7"]
	dup_on_list = ["1", "2", "3", "3", "5", "6", "7"]
	max_on_list = ["1", "2", "3", "2147483648", "5", "6", "7"]
	nothing_on_list = [""]
	args = [str_on_list, dup_on_list, max_on_list, nothing_on_list]

	# Reference output
	stderr_ref_list = ["Error\n", "Error\n", "Error\n", ""]

	# Runing and collecting output and error
	stderr_list = []
	stderr_val_list = []
	for arg in args:
		cmd = program + arg
		output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		cmd_val = valgrind + cmd
		output_val = subprocess.run(cmd_val, stderr=subprocess.PIPE, text=True)
		stderr_list.append(output.stderr)
		stderr_val_list.append(output_val.stderr)
		
	# Printing test check
	i = 0
	for err, err_val in zip(stderr_list, stderr_val_list):
		print(f"{battery[i].upper()}")
		if (err == stderr_ref_list[i]):
			print(f"{colours[0]}{i + 1}/{len(args)}.	OK{colours[2]}")
		else:
			print(f"{colours[1]}{i + 1}/{len(args)}.	KO{colours[2]}")
			exit_status = 1
		if valgrind_check in err_val:
			print(f"{colours[0]}	MOK\n{colours[2]}")
		else:
			print(f"{colours[1]}	MKO\n{colours[2]}")
			exit_status = 1
		i = i + 1

	return (exit_status)