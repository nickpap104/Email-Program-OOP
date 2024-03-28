### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails.

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False # this is added as a default to all emails

    # Initialise the instance variables for emails.
    # email_instance_var = Email(email_address="nickp@gmail.com", subject_line="Last week's notes", email_content="blah blah")
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# This is the methods that has the other methids for my program.

def populate_inbox(inbox):
    # Create 3 sample emails and add it to the Inbox list.
    inbox.append(Email(email_address="sample1@gmail.com", subject_line="Catching up", email_content="something"))
    inbox.append(Email(email_address="sample2@gmail.com", subject_line="Following up", email_content="another thing"))
    inbox.append(Email(email_address="sample3@gmail.com", subject_line="Company Party", email_content="other thing"))


def list_emails():
    # This method prints the email’s subject_line, along with a corresponding number.
    for i, email in enumerate(inbox, start=1):
        print(f"\n{i}. Email Address: {email.email_address}, Subject Line: {email.subject_line}")

def read_email():
    list_emails()
    index = int(input("\nEnter the index of the email you want to read: "))

    # Here we check if the index is valid, we take from outside
    # 0,1,2 numbers we set earlier
    if index < 1 or index > len(inbox):
        print("Invalid index. Please try again.")
        return

    email = inbox[index -1]

    # Print the right emails according to index from user
    print("Email From:", email.email_address)
    print("Subject Line:", email.subject_line)
    print("Email Content:", email.email_content)

    # The variable has_been_read is set to true
    email.has_been_read = True


populate_inbox(inbox)
# This is the method to populate the inbox with email addresses.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    
        1. Read an email
        2. View unread emails
        3. Quit application

    Enter selection (1,2,3): '''))
       
    if user_choice == 1:
        read_email()
        
    elif user_choice == 2:
        print("\nUnread Emails:")
        for i, email in enumerate(inbox, start=1):
            if email.has_been_read == False:
                print(f"{i}. Email Address: {email.email_address}, Subject Line: {email.subject_line}")
            
    elif user_choice == 3:
        print("\nBye bye!")
        exit()


else:
    print("Oops - incorrect input.")

