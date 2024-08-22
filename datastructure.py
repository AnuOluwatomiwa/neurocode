import scipy.io

def print_menu(keys):
    # Print the menu with numbered options for each key.
    print("\nSelect an option:")
    for i, key in enumerate(keys, 1):
        print(f"{i}. {key}")
    print(f"{len(keys) + 1}. Exit")

def display_info(data, choice):
    # Display the selected key's data.
    keys = list(data.keys()) 
    if 1 <= choice <= len(keys):
        selected_key = keys[choice - 1]
        value = data[selected_key]
        print(f"\nData for '{selected_key}':\n")
        if isinstance(value, (list, tuple, dict)):
            # Handle dict or list/tuple
            if isinstance(value, dict):
                print("Key - Value")
                print("----------")
                for k, v in value.items():
                    print(f"{k}: {v}")
            else:
                print("Index - Value")
                print("-------------")
                for i, v in enumerate(value):
                    print(f"{i}: {v}")
        else:
            print(value)
    else:
        print("Invalid choice!")

def main():
    # Load the .mat files
    data_s1 = scipy.io.loadmat('dataset/S1.mat')
    data_s2 = scipy.io.loadmat('dataset/S2.mat')

    files = {'1': data_s1, '2': data_s2}

    while True:
        print("\nSelect a file:")
        print("1. S1.mat")
        print("2. S2.mat")
        print("3. Exit")

        file_choice = input("Enter your choice: ")
        
        if file_choice in files:
            data = files[file_choice]
            keys = list(data.keys())
            while True:
                print_menu(keys)
                try:
                    option = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue
                
                if option == len(keys) + 1:
                    break
                display_info(data, option)
        elif file_choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
