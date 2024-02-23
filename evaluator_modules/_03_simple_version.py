import subprocess

def	simple_version(program, valgrind, valgrind_check, colours):

	# Definig args
	all_tiny_sort_args_checker = ["'1 3 2'", "'2 1 3'", "'2 3 1'", "'3 1 2'", "'3 2 1'"]
	all_tiny_sort_args = [["1", "3", "2"], ["2", "1", "3"], ["2", "3", "1"], ["3", "1", "2"], ["3", "2", "1"]]
	ref_list = ["OK\n", "OK\n", "OK\n", "OK\n", "OK\n"]
	max_moves = 3

	# Colecting outputs
	all_outputs_checker = []
	all_outputs_moves = []
	all_outputs_val = []
	for tiny_sort_arg, all_tiny_sort_arg in zip(all_tiny_sort_args_checker, all_tiny_sort_args):

		# Checker
		arg = f"ARG={tiny_sort_arg}; ../push_swap $ARG | ../checker_linux $ARG"
		output = subprocess.run(arg, stdout=subprocess.PIPE, text=True, shell=True)
		all_outputs_checker.append(output.stdout)

		# Count moves
		cmd = program + all_tiny_sort_arg
		output_moves = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
		all_outputs_moves.append(str(output_moves.stdout.count("\n")))

		# Valgrind
		cmd_val = valgrind + cmd
		output_val = subprocess.run(cmd_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		all_outputs_val.append(output_val.stderr)
	
	# Checking ref with outputs
	i = 1
	for out_checker, out_moves, out_val, out_ref in zip(all_outputs_checker, all_outputs_moves, all_outputs_val, ref_list):
		print("--------")
		print(all_tiny_sort_args_checker[i - 1])
		if (out_checker == out_ref and int(out_moves) <= max_moves):
			print(f"{colours[0]}{i}. OK  {colours[2]}")
		else:
			print(f"{colours[1]}{i}. KO  {colours[2]}")
		if valgrind_check in out_val:
			print(f"{colours[0]}   MOK{colours[2]}")
		else:
			print(f"{colours[1]}   MKO{colours[2]}")
		i = i + 1