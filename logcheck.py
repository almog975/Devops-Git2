def check_log():
    filename = input("Enter log filename: ")
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            errors = [line for line in lines if "ERROR" in line]
            if errors:
                print("\n===== ERROR Lines Found =====")
                for line in errors:
                    print(line.strip())
            else:
                print("No ERROR lines found.")
    except FileNotFoundError:
        print(f"Error: file '{filename}' does not exist.")
