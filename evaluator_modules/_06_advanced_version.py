import subprocess
import random

def	advanced_version(program, valgrind, valgrind_check, colours, exit_status):

	# Definig args
	numbers_500 = list(range(0, 500, 1))
	random.shuffle(numbers_500)
	arg = [str(i) for i in numbers_500]
	arg_checker = ' '.join(arg)
	arg_checker = "'" + arg_checker + "'"
	ref = "OK\n"
	max_moves = 11500

	# Checker
	arg_checker = f"ARG={arg_checker}; ../push_swap $ARG | ../checker_linux $ARG"
	output_checker = subprocess.run(arg_checker, stdout=subprocess.PIPE, text=True, shell=True)
	output_checker = output_checker.stdout
	
	# Count moves
	cmd = program + arg
	output_moves = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
	output_moves = output_moves.stdout.count("\n")
	output_moves = int(output_moves)

	# Valgrind
	cmd_val = valgrind + cmd
	output_val = subprocess.run(cmd_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	output_val = output_val.stderr
	
	# Checking ref with outputs
	if (output_checker == ref and output_moves <= max_moves):
		print(f"{colours[0]}1/1.	OK  {colours[2]}")
	else:
		print(f"{colours[1]}1/1.	KO  {colours[2]}")
		exit_status = 1
	if valgrind_check in output_val:
		print(f"{colours[0]}	MOK{colours[2]}")
	else:
		print(f"{colours[1]}   MKO{colours[2]}")
		exit_status = 1
	if output_moves < 5500:
		print(f"5/5 | {output_moves} < 5500")
	elif output_moves < 7000:
		print(f"4/5 | {output_moves} < 7000")
	elif output_moves < 8500:
		print(f"3/5 | {output_moves} < 8500")
	elif output_moves < 10000:
		print(f"2/5 | {output_moves} < 10000")
	elif output_moves < 11500:
		print(f"1/5 | {output_moves} < 11500")

	return (exit_status)