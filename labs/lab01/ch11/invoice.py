# Starting file for Lab 1 Chapter 11 invoice.py program
# natan quirino 10/14/2026 dev128

from datetime import datetime, timedelta, date

def get_invoice_date():
    while True:

        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")
        try:
            dt = datetime.strptime(invoice_date_str, "%m/%d/%Y")

        except ValueError:
            print("invalid date format. Please enter the date as MM/DD/YYYY format. Try again! ")
            continue

        invoice_date = date(dt.year, dt.month, dt.day)
        # validating invoive to be today date or earlier. No future date
        if invoice_date > date.today():
            print("Invoice date must be before today's date or earlier. Try again!")
        else:
            return invoice_date

    invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")
    return invoice_date

def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
