import csv

def read_csv(filename):
    emails = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            first_name = row[0].strip().title()
            last_name = row[1].strip().title()
            email = row[2].strip().lower()
            emails.append((first_name, email))
    return emails

def create_emails(emails, template):
    for first_name, email in emails:
        email_content = template.format(email=email, first_name=first_name)
        print("================================================================")
        print(f"To: {email}\nFrom: noreply@deals.com\nSubject: Deals!\n")
        print(email_content)

def main():
    email_template = ""
    with open("email_template.txt", 'r') as template_file:
        email_template = template_file.read().strip()

    emails = read_csv("email.csv")
    create_emails(emails, email_template)

if __name__ == "__main__":
    main()
