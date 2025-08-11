import datetime as dt
import json as jsn

print("Welcome to the Expense Tracker 😊")

class Expense:
    def __init__(self, amount, category, description, time):
        self.amount = amount
        self.category = category
        self.description = description
        self.time = time
    
    def to_dict(self):
        return {
            "amount" : self.amount,
            "category" : self.category,
            "description" : self.description,
            "time" : self.time
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(amount=data["amount"], category = data["category"], description = data["description"], time = data["time"])


class ExpenseTracker:
    def __init__(self):
        self.expenses = [] # All the expenses are stored here
        self.load_from_file() # load the data into the expenses list
        
    
    # add new expense to the tracker
    def add_Expense(self):
        while True:
            try:
                amount = float(input("Enter the Amount: "))
                category = input("Enter the category: ")
                description = input("Enter the description: ")
                break
            except ValueError:
                print("Enter a valid amount!")
        
        now = dt.datetime.now()
        time = now.strftime("%d %B | %I:%M")

        newExpense = Expense(amount, category, description, time)
        self.expenses.append(newExpense)
        print("----------------------------------------------------")
        print("Expense has been added to the Tracker ✅")
        print("----------------------------------------------------")

    # view total spend
    def totalSpend(self):
        total=0
        for expense in self.expenses:
            total += expense.amount
        
        if(total == 0):
            print("You didn't spend yet!")
        else:
            print("----------------------------------------------------")
            print(f"Total ${total} has been spent 💰")
            print("----------------------------------------------------")

    # view expenses by category
    def show_by_category(self):
        category = input("Enter the category to filter the expenses: ")

        # filtered category expense object.
        filtr_Category = [expense for expense in self.expenses if category.lower() == expense.category.lower()]

        print("-----------------------------------------------------")

        # to check if the filtr_Category list is empty or not.
        if(not filtr_Category):
            print("No Category Found!")

        else:
            # shows the filtered category object.
            for catgry in filtr_Category:
                print("-----------------")
                print(f'{catgry.description}(${catgry.amount}) : {catgry.category}')
                print("-----------------")
        print("-----------------------------------------------------")
    
    # view expense history
    def viewHistory(self):
        if(len(self.expenses) < 1):
            print("----------------------------------------------------")
            print("No expense history found!")
            print("----------------------------------------------------")

        else:
            print("----------------------------------------------------")
            for expense in self.expenses:
                print("-------------------------------------")
                print(f"${expense.amount}\n {expense.category}\n {expense.description}\n on {expense.time}")
                print("-------------------------------------")
            print("----------------------------------------------------")

    def edit_Expense(self):
        idx = 0 # index to track the expense

        # check if Expenses are present or not
        if(not self.expenses):
            print("There is No Expense available to Edit!")
        
        else:
            for expense in self.expenses:
                print("-----------------------------------------------------------------------")
                print(f"{idx}) | {expense.amount} | {expense.category} | {expense.description}")
                print("-----------------------------------------------------------------------")
                idx+=1
            expense_choice = int(input("Which Expense you want to Edit from the above listed?"))

            # editing loop
            while True:

                # input validation loop
                while True:
                    try:
                        print("----------------------------------------------------")
                        edit_choice = int(input(" Which of these you want to edit:\n 1) Amount\n 2) Category\n 3) Description\n 4) Don't need edit\n"))
                        break
                    except ValueError:
                        print("Enter the Valid Option!")

                if(edit_choice == 1):
                    while True:
                        try:
                            user_edit = float(input("Enter the New Amount: "))
                            break
                        except ValueError:
                            print("Enter the valid Amount!")
                    self.expenses[expense_choice].amount = user_edit
                    print("Amount has been changed ✅")

                elif(edit_choice == 2):
                    user_edit = input("Enter the New Category: ")
                    self.expenses[expense_choice].category = user_edit.lower()
                    print("Category has been Changed ✅")

                elif(edit_choice == 3):
                    user_edit = input("Enter the New Description: ")
                    self.expenses[expense_choice].description = user_edit
                    print("Description has been Changed ✅")

                elif(edit_choice < 1 or 4 < edit_choice):
                    print("Choose from the above listed 👀")
                
                else:
                    break

    def delete_Expense(self):
        exp_nmbr = 0

        if(not self.expenses):
            print("You don't have Expenses to Delete!")
        else:
            for expense in self.expenses:
                print("-----------------------------------------------------------------------")
                print(f"{exp_nmbr}) {expense.amount} | {expense.category} | {expense.description}")
                exp_nmbr+=1
                print("-----------------------------------------------------------------------")
            while True:
                try:
                    ask_user = int(input("Which one of You want to Delete from the Below Expenses: "))
                    break
                except ValueError:
                    print("Enter the Right Number!")
                

            del self.expenses[ask_user]
            print("Expense has been deleted ✅")
    
    
    def save_to_file(self):
        with open(r"D:\Python\JSONS\expense.json", "w") as expense_data:
            exp_dict = [expense.to_dict() for expense in self.expenses]
            jsn.dump(exp_dict, expense_data) # params: json.dump("dict/list", "file_obj")
        print("Expenses have been Saved ✅")

    def load_from_file(self):
        with open(r"D:\Python\JSONS\expense.json", "r") as rtrn_exp_data:
            returned_data = jsn.load(rtrn_exp_data)

        for data in returned_data: # convert the dict into expense obj one-by-one and add them in the list
            exp_obj = Expense.from_dict(data)
            self.expenses.append(exp_obj)




newTracker = ExpenseTracker() # tracker object

# main loop
while True:
    # input validation loop
    while True:
        try:
            user_choice = int(input(" 1) Add an Expense\n 2) View Total Expenses\n 3) View Expenses by Category\n 4) View Expense History\n 5) Edit an Expense\n 6) Delete an Expense\n  7) Exit\n "))
            break
        except ValueError:
            print("Choose a valid Option!")

    if(user_choice == 1): # add expense
        newTracker.add_Expense()
    
    elif(user_choice == 2): # total spendings 
        newTracker.totalSpend()
    
    elif(user_choice == 3): # filter expenses by category
        newTracker.show_by_category()

    elif(user_choice == 4): # View Expense History
        newTracker.viewHistory()
    
    elif(user_choice == 5): # Edit Expense
        newTracker.edit_Expense()
    
    elif(user_choice == 6): # Delete Expense
        newTracker.delete_Expense()

    elif(user_choice>7 or user_choice<1):
        print("Invalid Option! Enter it again")
    else:
        newTracker.save_to_file() # Auto_Save
        break