"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Adjusts account balance for withdrawal.

        Script that verifies withdrawal amount is valid and adjusts account balance.
        To be valid: must be positive but not greater than account balance

        Arg:
            account(dict): contains pin and balance for account

        Return:
            account(dict): returns account with balance adjusted for withdrawal

    """

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.
    amount = questionary.text("How much would you like to withdrawal?").ask()
    amount = float(amount)

    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if amount <= 0.0:
        sys.exit(f"This is not a valid withdrawal amount. Please try again.")

    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        print(f"Your withdrawal was successful.")
        return account
    else:
        sys.exit(f"There are not sufficient funds to withdraw this amount. Please try again.")