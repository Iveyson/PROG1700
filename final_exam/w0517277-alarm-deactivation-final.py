
alarm_status = True
alarm_activated_status = False
password_attempts = 3


def load_passwords_as_int(filepath="passwords.txt"):
    valid_passwords = set()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                pw = line.strip()
                if not pw or pw.startswith("#"):
                    continue
                if len(pw) == 5 and pw.isdigit():
                    valid_passwords.add(int(pw))
        return valid_passwords
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return set()


def prompt_once():
    user_input = input("Please enter your 5 digit password: ").strip()
    if len(user_input) == 5 and user_input.isdigit():
        return int(user_input)
    print("Invalid input: password must be exactly 5 digits.")
    return None


def main():
    global alarm_status, alarm_activated_status

    passwords = load_passwords_as_int("passwords.txt")
    if not passwords:
        print("No passwords loaded or file missing.")
        return

    while True:
        attempts_left = password_attempts
        while attempts_left > 0:
            print(f"Attempts left: {attempts_left}")
            user_pw = prompt_once()

            if user_pw is None:
                attempts_left -= 1
                continue

            if user_pw in passwords:
                print("Access granted.")
                alarm_status = False
                alarm_activated_status = False
                print("Alarm activation status:", alarm_activated_status)
                print("Alarm status:", alarm_status)
                return
            else:
                print("Access denied.")
                attempts_left -= 1

        print("Too many attempts. Alarm activated.")
        alarm_status = True
        alarm_activated_status = True
        print("Alarm status:", alarm_status, ", Alarm activated:", alarm_activated_status)
        print("Resetting tries...\n")


if __name__ == "__main__":
    main()
