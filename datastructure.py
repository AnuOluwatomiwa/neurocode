import scipy.io
from tabulate import tabulate

# Load the .mat files
#data_s1 = scipy.io.loadmat('dataset/S1.mat')
#data_s2 = scipy.io.loadmat('dataset/S2.mat')
#
## Print keys to understand the structure
#print("Keys in S1.mat:", data_s1.keys())
#print("Keys in S2.mat:", data_s2.keys())
#
##Inspect the 'Info' key
#info_s1 = data_s1['Info']
#info_s2 = data_s2['Info']
#
#print("Info for S1.mat:\n", info_s1)
#print("\nInfo for S2.mat:\n",info_s2)
#
## Check the structure of 'training_data' and 'test_data'
#training_data_s1 = data_s1['training_data']
#test_data_s1 = data_s1['test_data']
#
#print("\nShape of training_data in S1.mat:", training_data_s1.shape)
#print("Shape of test_data in S1.mat:", test_data_s1.shape)




def print_menu(keys):
    # Print the menu with numbered options for each key.
    print("\nSelect an option:")
    for i, key in enumerate(keys, 1):
        print(f"{i}. {key}")
    print(f"{len(keys) + 1}. Exit")


def display_info(data, choice):
    #   Display the selected key's data in a tabulated format.
    keys = list(data.keys())
    if 1 <= choice <= len(keys):
        selected_key = keys[choice - 1]
        value = data[selected_key]
        print(f"\nData for '{selected_key}':\n")
        if isinstance(value, (list, tuple, dict)):
            # Use tabulate for lists or dicts
            if isinstance(value, dict):
                table = [[k, str(v)] for k, v in value.items()]
                print(tabulate(table, headers=['Key', 'Value'], tablefmt='grid'))
            else:
                table = [[str(i), str(v)] for i, v in enumerate(value)]
                print(tabulate(table, headers=['Index', 'Value'], tablefmt='grid'))
        else:
            print(value)
    else:
        print("Invalid choice!")

def main():
    # Load the .mat files
    data_s1 = scipy.io.loadmat('dataset/S1.mat')
    data_s2 = scipy.io.loadmat('dataset/S2.mat')

    files = {'1': data_s1, '2': data_s2}
    file_names = {'1': 'S1.mat', '2': 'S2.mat'}

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