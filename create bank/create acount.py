def show_balance():
        print(f"your balanace is  0")

def deposit():
    amount =  int(input("Enter an mount to be deposited"))


    if amount < 0:
               print("thats not valid amount")
               return 0 
    else:
        return amount
def withdraw():
        amount = int(input("enter your amount of withdraw"))

        if amount > balance :
              print("insufficiet fandas")
        elif amount < 0 :
              return 0 
        
 
     
   
balance = 0
is_running = True

while is_running:
                print("***************")
                print("  Banking program ")
                print("******************")
                print("Banking Program")
                print("1.show Balance")
                print("2.deposit")
                print("3.withdraw")
                print("Exit")

                choice = input("enter your choice (1-4):")

                if choice == '1':
                    show_balance()
                elif choice == '2':
                      deposit()
                elif choice == '3':
                   balance == withdraw()
                elif choice == '4':
                    is_running = False

                else:
                    print("taht is not vaild choice")

print("thanks you! Have a nice day")



