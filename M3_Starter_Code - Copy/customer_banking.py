# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
   # Prompt the user to set the savings balance, interest rate, and months for the savings account
savings_balance = float(input("Enter the savings balance: "))
interest_rate = float(input("Enter the interest rate: "))
months = int(input("Enter the number of months: "))

    # Call the create_savings_account function and pass the variables from the user.
updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
class SavingsAccount:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate

    def calculate_interest(self, months):
        interest_rate = self.int_rate / 100
        interest_earned = self.balance * interest_rate * (months / 12)
        new_balance = self.balance + interest_earned
        return interest_earned, new_balance

# Create a SavingsAccount instance with initial balance and interest rate
savings = SavingsAccount(1000, 2.5)

# Get user input for the number of months
months = int(input("Enter the number of months: "))

# Calculate interest earned and update balance for the given months
interest_earned, new_balance = savings.calculate_interest(months)

# Print out the interest earned and updated balance
print(f"Interest earned: ${interest_earned:.2f}")
print(f"Updated balance: ${new_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
cd_balance = float(input("Enter the CD balance: "))
cd_interest_rate = float(input("Enter the CD interest rate: "))
cd_months = int(input("Enter the number of months for the CD: "))

# Create a CD instance with user input values
cd_account = CD(cd_balance, cd_interest_rate, cd_months)

    # Call the create_cd_account function and pass the variables from the user.
Assuming cd_balance, cd_interest, and cd_months are the variables from the user input
updated_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(f"Interest earned on CD account: ${interest_earned:.2f}")
print(f"Updated CD account balance with interest earned: ${updated_balance:.2f}")

    # Call the main function.
    if __name__ == "__main__":
    main()