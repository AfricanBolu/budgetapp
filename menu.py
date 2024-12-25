class Menu:
    def __init__(self):
        self.choice = None
        # self.running = True

    def display_menu(self):
        print('\n--Main Menu--')
        print('1. Create Budget File')
        print('2. Load Budget File')
        print('3. Save Budget FIle')
        print('4. Quit')

    def get_choice(self):
        self.choice = int(input('Enter your choice: '))
        return self.choice

    def load_menu(self):
        print('\n--Load Menu--')
        print('1. Create New Budget')
        print('2. Return to Main Menu')

    # def run(self, budget):
    #     budget = BudgetCalculator()
    #     while self.running:
    #         self.display_menu()
    #         choice = self.get_choice()
    #
    #         match choice:
    #             case '1':
    #                 budget.add_data()
    #             case '2':
    #                 budget.load_data()
    #             case '3':
    #                 budget.save()
    #             case '4':
    #                 self.running = False
