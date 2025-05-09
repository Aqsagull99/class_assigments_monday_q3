import json
import csv
import os
import platform
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from colorama import init, Fore, Back, Style
from typing import List, Dict, Optional

# Initialize colorama
init(autoreset=True)

class Transaction(ABC):
    """Base abstract class for all transactions"""
    def __init__(self, amount: float, category: str, description: str = ""):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @abstractmethod
    def get_type(self) -> str:
        pass
    
    def to_dict(self) -> Dict:
        return {
            "type": self.get_type(),
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

class Income(Transaction):
    def get_type(self) -> str:
        return "income"

class Expense(Transaction):
    def get_type(self) -> str:
        return "expense"

class Budget:
    """Class to handle budget categories"""
    def __init__(self, category: str, limit: float):
        self.category = category
        self.limit = limit
        self.spent = 0.0
    
    def add_spending(self, amount: float):
        self.spent += amount
    
    def get_remaining(self) -> float:
        return self.limit - self.spent
    
    def to_dict(self) -> Dict:
        return {
            "category": self.category,
            "limit": self.limit,
            "spent": self.spent
        }

class FinanceManager:
    """Core financial operations manager"""
    def __init__(self, data_file: str = "finance_data.json", budget_file: str = "budgets.json"):
        self.data_file = data_file
        self.budget_file = budget_file
        self.transactions: List[Transaction] = []
        self.budgets: Dict[str, Budget] = {}
        self.load_data()
    
    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        
        if isinstance(transaction, Expense):
            self.update_budget(transaction.category, transaction.amount)
        
        self.save_data()
    
    def update_budget(self, category: str, amount: float):
        if category in self.budgets:
            self.budgets[category].add_spending(amount)
            self.save_budgets()
    
    def add_budget(self, category: str, limit: float):
        if category not in self.budgets:
            self.budgets[category] = Budget(category, limit)
            self.save_budgets()
        else:
            raise ValueError(f"Budget for category '{category}' already exists")
    
    def get_budget_status(self, category: str) -> Optional[Dict]:
        if category in self.budgets:
            budget = self.budgets[category]
            return {
                "limit": budget.limit,
                "spent": budget.spent,
                "remaining": budget.get_remaining(),
                "percentage": (budget.spent / budget.limit) * 100 if budget.limit > 0 else 0
            }
        return None
    
    def get_all_budgets(self) -> List[Dict]:
        return [budget.to_dict() for budget in self.budgets.values()]
    
    def get_transactions(self, 
                       transaction_type: Optional[str] = None,
                       category: Optional[str] = None,
                       days: Optional[int] = None) -> List[Transaction]:
        
        filtered = self.transactions
        
        if transaction_type:
            filtered = [t for t in filtered if t.get_type() == transaction_type]
        
        if category:
            filtered = [t for t in filtered if t.category.lower() == category.lower()]
        
        if days:
            cutoff_date = datetime.now() - timedelta(days=days)
            filtered = [t for t in filtered if datetime.strptime(t.date, "%Y-%m-%d %H:%M:%S") >= cutoff_date]
        
        return filtered
    
    def export_to_csv(self, filename: str = "transactions_export.csv"):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['type', 'amount', 'category', 'description', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction.to_dict())
    
    def generate_monthly_report(self, year: int, month: int) -> Dict:
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year+1, 1, 1)
        else:
            end_date = datetime(year, month+1, 1)
        
        monthly_transactions = [
            t for t in self.transactions
            if start_date <= datetime.strptime(t.date, "%Y-%m-%d %H:%M:%S") < end_date
        ]
        
        income = sum(t.amount for t in monthly_transactions if isinstance(t, Income))
        expenses = sum(t.amount for t in monthly_transactions if isinstance(t, Expense))
        balance = income - expenses
        
        return {
            "year": year,
            "month": month,
            "total_income": income,
            "total_expenses": expenses,
            "balance": balance,
            "transactions": len(monthly_transactions),
            "categories": {
                t.category for t in monthly_transactions
            }
        }
    
    def get_balance(self) -> float:
        total_income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        total_expense = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        return total_income - total_expense
    
    def get_summary(self) -> Dict:
        income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        expenses = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        balance = income - expenses
        
        return {
            "total_income": income,
            "total_expenses": expenses,
            "balance": balance
        }
    
    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=2)
    
    def save_budgets(self):
        with open(self.budget_file, "w") as f:
            json.dump([b.to_dict() for b in self.budgets.values()], f, indent=2)
    
    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for item in data:
                    if item["type"] == "income":
                        self.transactions.append(Income(
                            amount=item["amount"],
                            category=item["category"],
                            description=item["description"]
                        ))
                    else:
                        self.transactions.append(Expense(
                            amount=item["amount"],
                            category=item["category"],
                            description=item["description"]
                        ))
        except FileNotFoundError:
            self.transactions = []
        
        try:
            with open(self.budget_file, "r") as f:
                data = json.load(f)
                for item in data:
                    budget = Budget(
                        category=item["category"],
                        limit=item["limit"]
                    )
                    budget.spent = item["spent"]
                    self.budgets[item["category"]] = budget
        except FileNotFoundError:
            self.budgets = {}

class FinanceCLI:
    """Command Line Interface for the Finance Tracker"""
    def __init__(self):
        self.manager = FinanceManager()
        self.theme = {
            "header": Fore.CYAN + Style.BRIGHT,
            "option": Fore.YELLOW,
            "input": Fore.GREEN,
            "success": Fore.GREEN + Style.BRIGHT,
            "error": Fore.RED + Style.BRIGHT,
            "warning": Fore.YELLOW + Style.BRIGHT,
            "income": Fore.LIGHTGREEN_EX,
            "expense": Fore.LIGHTRED_EX,
            "summary": Fore.LIGHTBLUE_EX,
            "transaction": Fore.LIGHTWHITE_EX,
            "positive": Fore.LIGHTGREEN_EX,
            "negative": Fore.LIGHTRED_EX,
            "neutral": Fore.LIGHTWHITE_EX,
            "budget_safe": Fore.GREEN,
            "budget_warning": Fore.YELLOW,
            "budget_danger": Fore.RED
        }
    
    def clear_screen(self):
        """Clear the console screen"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def press_enter_to_continue(self):
        """Wait for user to press Enter"""
        input(f"\n{self.theme['input']}Press Enter to continue...{Style.RESET_ALL}")
    
    def print_header(self, text):
        """Print a formatted header"""
        print(f"\n{self.theme['header']}{'=' * 50}")
        print(f"{text.center(50)}")
        print(f"{'=' * 50}{Style.RESET_ALL}\n")
    
    def run(self):
        while True:
            self.clear_screen()
            self.print_header("Personal Finance Tracker")
            
            print(f"{self.theme['option']}1. Add Income")
            print(f"{self.theme['option']}2. Add Expense")
            print(f"{self.theme['option']}3. View Transactions")
            print(f"{self.theme['option']}4. View Summary")
            print(f"{self.theme['option']}5. Budget Management")
            print(f"{self.theme['option']}6. Generate Reports")
            print(f"{self.theme['option']}7. Export Data")
            print(f"{self.theme['option']}8. Exit")
            
            choice = input(f"\n{self.theme['input']}Enter your choice: {Style.RESET_ALL}")
            
            try:
                if choice == "1":
                    self.add_income()
                elif choice == "2":
                    self.add_expense()
                elif choice == "3":
                    self.view_transactions_menu()
                elif choice == "4":
                    self.view_summary()
                elif choice == "5":
                    self.budget_management()
                elif choice == "6":
                    self.reports_menu()
                elif choice == "7":
                    self.export_data()
                elif choice == "8":
                    print(f"\n{self.theme['success']}Exiting...")
                    break
                else:
                    print(f"\n{self.theme['error']}Invalid choice. Please try again.")
                    self.press_enter_to_continue()
            except Exception as e:
                print(f"\n{self.theme['error']}An error occurred: {e}")
                self.press_enter_to_continue()
    
    def add_income(self):
        self.clear_screen()
        self.print_header("Add New Income")
        
        try:
            amount = float(input(f"{self.theme['input']}Amount: {Style.RESET_ALL}"))
            category = input(f"{self.theme['input']}Category: {Style.RESET_ALL}")
            description = input(f"{self.theme['input']}Description (optional): {Style.RESET_ALL}")
            
            income = Income(amount, category, description)
            self.manager.add_transaction(income)
            print(f"\n{self.theme['success']}Income added successfully!")
        except ValueError:
            print(f"\n{self.theme['error']}Invalid amount. Please enter a valid number.")
        except Exception as e:
            print(f"\n{self.theme['error']}Error: {e}")
        
        self.press_enter_to_continue()
    
    def add_expense(self):
        self.clear_screen()
        self.print_header("Add New Expense")
        
        try:
            amount = float(input(f"{self.theme['input']}Amount: {Style.RESET_ALL}"))
            category = input(f"{self.theme['input']}Category: {Style.RESET_ALL}")
            description = input(f"{self.theme['input']}Description (optional): {Style.RESET_ALL}")
            
            expense = Expense(amount, category, description)
            self.manager.add_transaction(expense)
            print(f"\n{self.theme['success']}Expense added successfully!")
        except ValueError:
            print(f"\n{self.theme['error']}Invalid amount. Please enter a valid number.")
        except Exception as e:
            print(f"\n{self.theme['error']}Error: {e}")
        
        self.press_enter_to_continue()
    
    def view_transactions(self, transaction_type: Optional[str] = None):
        self.clear_screen()
        title = "Transaction History"
        if transaction_type:
            title = f"{transaction_type.capitalize()} Transactions"
        self.print_header(title)
        
        transactions = self.manager.get_transactions(transaction_type=transaction_type)
        if not transactions:
            print(f"{self.theme['warning']}No transactions found.")
            self.press_enter_to_continue()
            return
        
        for idx, t in enumerate(transactions, 1):
            color = self.theme['income'] if isinstance(t, Income) else self.theme['expense']
            print(f"{self.theme['transaction']}{idx}. [{color}{t.get_type().upper()}{Style.RESET_ALL}] {t.date} - {t.category}: {color}${t.amount:.2f}")
            if t.description:
                print(f"   {self.theme['transaction']}Description: {t.description}")
        
        self.press_enter_to_continue()
    
    def view_summary(self):
        self.clear_screen()
        self.print_header("Financial Summary")
        
        summary = self.manager.get_summary()
        balance_color = self.theme['positive'] if summary['balance'] >= 0 else self.theme['negative']
        
        print(f"{self.theme['summary']}Total Income: {self.theme['income']}${summary['total_income']:.2f}")
        print(f"{self.theme['summary']}Total Expenses: {self.theme['expense']}${summary['total_expenses']:.2f}")
        print(f"{self.theme['summary']}Balance: {balance_color}${summary['balance']:.2f}")
        
        self.press_enter_to_continue()
    
    def budget_management(self):
        while True:
            self.clear_screen()
            self.print_header("Budget Management")
            
            print(f"{self.theme['option']}1. Add New Budget")
            print(f"{self.theme['option']}2. View Budgets")
            print(f"{self.theme['option']}3. Check Budget Status")
            print(f"{self.theme['option']}4. Back to Main Menu")
            
            choice = input(f"\n{self.theme['input']}Enter your choice: {Style.RESET_ALL}")
            
            if choice == "1":
                self.add_budget()
            elif choice == "2":
                self.view_budgets()
            elif choice == "3":
                self.check_budget_status()
            elif choice == "4":
                break
            else:
                print(f"\n{self.theme['error']}Invalid choice. Please try again.")
                self.press_enter_to_continue()
    
    def add_budget(self):
        self.clear_screen()
        self.print_header("Add New Budget")
        
        category = input(f"{self.theme['input']}Category: {Style.RESET_ALL}")
        try:
            limit = float(input(f"{self.theme['input']}Budget Limit: {Style.RESET_ALL}"))
            self.manager.add_budget(category, limit)
            print(f"\n{self.theme['success']}Budget added successfully!")
        except ValueError as e:
            print(f"\n{self.theme['error']}{e}")
        except Exception as e:
            print(f"\n{self.theme['error']}Error: {e}")
        
        self.press_enter_to_continue()
    
    def view_budgets(self):
        self.clear_screen()
        self.print_header("Current Budgets")
        
        budgets = self.manager.get_all_budgets()
        if not budgets:
            print(f"{self.theme['warning']}No budgets set up yet.")
            self.press_enter_to_continue()
            return
        
        for budget in budgets:
            remaining = budget['limit'] - budget['spent']
            percentage = (budget['spent'] / budget['limit']) * 100 if budget['limit'] > 0 else 0
            
            if percentage < 70:
                color = self.theme['budget_safe']
            elif percentage < 90:
                color = self.theme['budget_warning']
            else:
                color = self.theme['budget_danger']
            
            print(f"\n{self.theme['summary']}Category: {budget['category']}")
            print(f"{self.theme['summary']}Limit: ${budget['limit']:.2f}")
            print(f"{self.theme['summary']}Spent: ${budget['spent']:.2f}")
            print(f"{color}Remaining: ${remaining:.2f} ({percentage:.1f}% used)")
        
        self.press_enter_to_continue()
    
    def check_budget_status(self):
        self.clear_screen()
        self.print_header("Check Budget Status")
        
        category = input(f"{self.theme['input']}Enter category to check: {Style.RESET_ALL}")
        status = self.manager.get_budget_status(category)
        
        if status:
            remaining = status['remaining']
            percentage = status['percentage']
            
            if percentage < 70:
                color = self.theme['budget_safe']
            elif percentage < 90:
                color = self.theme['budget_warning']
            else:
                color = self.theme['budget_danger']
            
            print(f"\n{self.theme['summary']}Budget Status for '{category}':")
            print(f"{self.theme['summary']}Limit: ${status['limit']:.2f}")
            print(f"{self.theme['summary']}Spent: ${status['spent']:.2f}")
            print(f"{color}Remaining: ${remaining:.2f} ({percentage:.1f}% used)")
            
            if percentage >= 100:
                print(f"{self.theme['error']}Warning: You have exceeded your budget!")
            elif percentage >= 90:
                print(f"{self.theme['warning']}Warning: You're close to exceeding your budget!")
        else:
            print(f"\n{self.theme['error']}No budget found for category '{category}'")
        
        self.press_enter_to_continue()
    
    def reports_menu(self):
        while True:
            self.clear_screen()
            self.print_header("Reports Menu")
            
            print(f"{self.theme['option']}1. Generate Monthly Report")
            print(f"{self.theme['option']}2. View Recent Transactions (Last 7 days)")
            print(f"{self.theme['option']}3. Back to Main Menu")
            
            choice = input(f"\n{self.theme['input']}Enter your choice: {Style.RESET_ALL}")
            
            if choice == "1":
                self.generate_monthly_report()
            elif choice == "2":
                self.view_recent_transactions()
            elif choice == "3":
                break
            else:
                print(f"\n{self.theme['error']}Invalid choice. Please try again.")
                self.press_enter_to_continue()
    
    def generate_monthly_report(self):
        self.clear_screen()
        self.print_header("Monthly Report")
        
        try:
            year = int(input(f"{self.theme['input']}Enter year (YYYY): {Style.RESET_ALL}"))
            month = int(input(f"{self.theme['input']}Enter month (1-12): {Style.RESET_ALL}"))
            
            report = self.manager.generate_monthly_report(year, month)
            
            print(f"\n{self.theme['header']}Monthly Report for {month}/{year}:")
            print(f"{self.theme['summary']}Total Income: {self.theme['income']}${report['total_income']:.2f}")
            print(f"{self.theme['summary']}Total Expenses: {self.theme['expense']}${report['total_expenses']:.2f}")
            
            balance_color = self.theme['positive'] if report['balance'] >= 0 else self.theme['negative']
            print(f"{self.theme['summary']}Balance: {balance_color}${report['balance']:.2f}")
            
            print(f"\n{self.theme['summary']}Transaction Categories:")
            for category in report['categories']:
                print(f"- {category}")
            
        except ValueError:
            print(f"\n{self.theme['error']}Invalid year or month entered.")
        except Exception as e:
            print(f"\n{self.theme['error']}Error generating report: {e}")
        
        self.press_enter_to_continue()
    
    def view_recent_transactions(self):
        self.clear_screen()
        self.print_header("Recent Transactions (Last 7 days)")
        
        recent = self.manager.get_transactions(days=7)
        if not recent:
            print(f"{self.theme['warning']}No transactions in the last 7 days.")
            self.press_enter_to_continue()
            return
        
        for idx, t in enumerate(recent, 1):
            color = self.theme['income'] if isinstance(t, Income) else self.theme['expense']
            print(f"{self.theme['transaction']}{idx}. [{color}{t.get_type().upper()}{Style.RESET_ALL}] {t.date} - {t.category}: {color}${t.amount:.2f}")
            if t.description:
                print(f"   {self.theme['transaction']}Description: {t.description}")
        
        self.press_enter_to_continue()
    
    def export_data(self):
        self.clear_screen()
        self.print_header("Export Data")
        
        filename = input(f"{self.theme['input']}Enter filename (default: transactions_export.csv): {Style.RESET_ALL}") or "transactions_export.csv"
        
        try:
            self.manager.export_to_csv(filename)
            print(f"\n{self.theme['success']}Data successfully exported to {filename}")
        except Exception as e:
            print(f"\n{self.theme['error']}Error exporting data: {e}")
        
        self.press_enter_to_continue()
    
    def view_transactions_menu(self):
        while True:
            self.clear_screen()
            self.print_header("View Transactions")
            
            print(f"{self.theme['option']}1. View All Transactions")
            print(f"{self.theme['option']}2. View Income Only")
            print(f"{self.theme['option']}3. View Expenses Only")
            print(f"{self.theme['option']}4. Filter by Category")
            print(f"{self.theme['option']}5. Back to Main Menu")
            
            choice = input(f"\n{self.theme['input']}Enter your choice: {Style.RESET_ALL}")
            
            if choice == "1":
                self.view_transactions()
            elif choice == "2":
                self.view_transactions(transaction_type="income")
            elif choice == "3":
                self.view_transactions(transaction_type="expense")
            elif choice == "4":
                self.filter_by_category()
            elif choice == "5":
                break
            else:
                print(f"\n{self.theme['error']}Invalid choice. Please try again.")
                self.press_enter_to_continue()
    
    def filter_by_category(self):
        self.clear_screen()
        self.print_header("Filter by Category")
        
        category = input(f"{self.theme['input']}Enter category to filter: {Style.RESET_ALL}")
        filtered = self.manager.get_transactions(category=category)
        
        if not filtered:
            print(f"\n{self.theme['warning']}No transactions found for category '{category}'")
            self.press_enter_to_continue()
            return
        
        self.clear_screen()
        self.print_header(f"Transactions for Category: {category}")
        
        for idx, t in enumerate(filtered, 1):
            color = self.theme['income'] if isinstance(t, Income) else self.theme['expense']
            print(f"{self.theme['transaction']}{idx}. [{color}{t.get_type().upper()}{Style.RESET_ALL}] {t.date} - {t.category}: {color}${t.amount:.2f}")
            if t.description:
                print(f"   {self.theme['transaction']}Description: {t.description}")
        
        self.press_enter_to_continue()

if __name__ == "__main__":
    try:
        cli = FinanceCLI()
        cli.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program terminated by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}A critical error occurred: {e}{Style.RESET_ALL}")



        