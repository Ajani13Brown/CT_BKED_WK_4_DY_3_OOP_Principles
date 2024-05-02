class BudgetCategory:
    def __init__(self, category_name, allocated_budget,expenses = 0):
        self.__category_name= category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = expenses

    def get_category(self):
        return self.__category_name
    
    def get_budget(self):
        return self.__allocated_budget
    
    def set_category(self,new_catg):
        print(f'Changing {self} category to {new_catg}')
        self.__category_name = new_catg

    def set_budget(self,new_budget):
        if new_budget > 0:
            print(f'Change {self} budget to {new_budget}')
            self.__allocated_budget = new_budget
        else:
            print('Sorry, not a valid budget')

    def get_expenses(self):
        return self.__expenses
    
    def set_expenses(self, new_expenses):
        self.__expenses = new_expenses
    
    def add_expense(self,expense):                  
        if expense < self.__allocated_budget:
            self.set_expenses(self.get_expenses() + expense)
            print(f'{expense} was added to your expenses')
            return self.get_expenses()
            
        else:
            print('Value enter is not valid')

    def display_budget(self):
        print(f'Name: {self.get_category()}')
        print(f'Allocated Budget: ${self.get_budget()}')
        print(f' Remaining Balance ${self.get_budget() - self.get_expenses()}')


groceries = BudgetCategory('groceries', 100)
groceries.add_expense(25)

groceries.display_budget()