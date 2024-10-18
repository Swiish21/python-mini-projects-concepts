# Define a dictionary with currency conversion rates
conversion_rates = {
    'ksh': {'usd': 0.0076, 'euro': 0.0070, 'yen': 1.16, 'yuan': 0.055},
    'usd': {'ksh': 131.00, 'euro': 0.92, 'yen': 151.52, 'yuan': 7.22},
    'euro': {'ksh': 141.93, 'usd': 1.09, 'yen': 164.16, 'yuan': 7.82},
    'yen': {'ksh': 0.86, 'usd': 0.0066, 'euro': 0.0061, 'yuan': 0.048},
    'yuan': {'ksh': 18.15, 'usd': 0.14, 'euro': 0.13, 'yen': 20.99}
}

def convert_currency(amount, from_currency, to_currency):
    """
    Convert a given amount from one currency to another.

    Args:
        amount (float): The amount to convert.
        from_currency (str): The currency to convert from.
        to_currency (str): The currency to convert to.

    Returns:
        float: The converted amount.
    """
    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        raise ValueError("Invalid currency")

    return amount * conversion_rates[from_currency][to_currency]

def main():
    from_currency = input("Enter currency you have (Ksh/Usd/Euro/Yen/Yuan):\n").lower()
    to_currency = input("Enter currency to convert to (Ksh/Usd/Euro/Yen/Yuan):\n").lower()
    amount = int(input(f"What amount of {from_currency} do you have exactly:\n"))

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"Your currency is worth {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()