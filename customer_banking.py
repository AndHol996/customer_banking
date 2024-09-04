# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance=float(input("How much are you wanting to put into saving?"))
    savings_interest=float(input("What is the APR of the savings account?"))
    savings_maturity=int(input("How amany months will it stay in this account?"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, s_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account ba1lance with interest earned for the given months.
    print(f"""After {savings_maturity} months, the interest earned will be  
          ${s_interest_earned:.2f} with a total of ${updated_savings_balance:.2f} in the account
          """)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance=float(input("How much are you wanting to put into a CD?" ))
    cd_interest=float(input("What is the APR of the CD account?" ))
    cd_maturity=int(input("How amany months will it stay in this account?" ))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, c_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"""After {cd_maturity} months, the interest earned will be 
          ${c_interest_earned:.2f} with a total of ${updated_cd_balance:.2f} in the account
          """)
if __name__ == "__main__":
    # Call the main function.
    main()