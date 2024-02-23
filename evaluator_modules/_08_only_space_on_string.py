import subprocess

def	only_space_on_string(program, valgrind, valgrind_check, colours):

	# Definig args
	program_shell_true = program[0]
	valgrind_shell_true = valgrind[0] + ' ' + valgrind[1] + ' ' + valgrind[2] + ' ' + valgrind[3]
	arg_shell_true = "' '"

	# Output ref
	output_ref = "Error\n"

	# Run normal 
	cmd_shell_true = program_shell_true + ' ' + arg_shell_true
	output = subprocess.run(cmd_shell_true, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
	output = output.stderr


	# Valgrind
	cmd_val_shell_true = valgrind_shell_true + ' ' + program_shell_true + ' ' + arg_shell_true
	output_val = subprocess.run(cmd_val_shell_true, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
	output_val = output_val.stderr
	
	# Checking ref with outputs
	if (output == output_ref):
		print(f"{colours[0]}   OK  {colours[2]}")
	else:
		print(f"{colours[1]}   KO  {colours[2]}")
	if valgrind_check in output_val:
		print(f"{colours[0]}   MOK{colours[2]}")
	else:
		print(f"{colours[1]}   MKO{colours[2]}")