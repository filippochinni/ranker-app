def get_user_bool(prompt):
	while True:
		user_input = input(f"{prompt} (y/n): ").strip().lower()
		if user_input == 'y':
			return True
		elif user_input == 'n':
			return False