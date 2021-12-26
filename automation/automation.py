import re

# Given document potential contacts, find all email and phone numbers.
# Save email and phone numbers in separate documents. Sorted ascending. No duplicates.

def find_phone_numbers(str):
    """
    Finds phone numbers in the given string and returns a set of phone numbers found. The phone numbers will be formatted into the following format: "123-456-7890". 206 area code is assumed if area code is not found.
    """
    phone_numbers_uncleaned = re.findall(r"\D?(\d{3})?\D{0,2}(\d{3})\D?(\d{4})\D?", str)
    phone_numbers_cleaned = set([ \
                                        "206" + "-".join(groups) if len(list(filter(None, groups))) == 2 \
                                        else "-".join(list(filter(None, groups))) \
                                        for groups in phone_numbers_uncleaned \
                                    ])
    return phone_numbers_cleaned

def find_emails(str):
    """
    Finds email addresses in the given string and returns a set of emails found.
    """
    emails = set(re.findall(r"[a-zA-Z0-9\-_\.]+@[a-zA-Z0-9\-_\.]+\.[a-zA-Z]{2,5}", str))
    return emails

def write_phone_numbers_to_file(phone_numbers_cleaned):
    """
    Accepts an interable containing phone numbers and writes them to automation/phone_numbers.txt". File is created if it does not exist. Contents of file will be overwritten.
    """
    with open("automation/phone_numbers.txt", 'w+') as f:
        f.writelines(sorted([line + "\n" for line in phone_numbers_cleaned]))

def write_emails_to_file(emails):
    """
    Accepts an interable containing email addresses and writes them to automation/emails.txt". File is created if it does not exist. Contents of file will be overwritten.
    """
    with open("automation/emails.txt", 'w+') as f:
        f.writelines(sorted([line + "\n" for line in emails]))


if __name__ == "__main__":
    with open("automation/potential-contacts.txt") as f:
        file = f.read()

    write_phone_numbers_to_file(find_phone_numbers(file))
    write_emails_to_file(find_emails(file))
