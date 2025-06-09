def main():
    print("\n==== Penetration Testing Toolkit ====")
    print("1. Port Scanner")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Port scanner selected (to be implemented).")
    elif choice == '0':
        print("Exiting...")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
