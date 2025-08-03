def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice =='1':
            added_item=input("Enter the item to add: ")
            shopping_list.append(added_item)
        elif choice =='2':
            removed_item=input("Which element would you like to remove: ")
            if removed_item:
                shopping_list.remove(removed_item)
            else:
                print(f"{removed_item} does not exist")
        elif choice =='3':
            if shopping_list !=[]:
                for index,item in enumerate(shopping_list,start=1):
                    print(f"{index}. {item}")
            else:
                print("Your list is empty!!")
        elif choice =='4':
            print('Goodbye')
            break
        else:
            print("Invali choice. Pleade try again.")
if __name__ == "__main__":
    main()

