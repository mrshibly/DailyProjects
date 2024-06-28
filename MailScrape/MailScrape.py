import re

def extract_emails(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_addresses = re.findall(email_pattern, content)
    
    return email_addresses

def main():
    print("Welcome to MailScrape - Email Address Extractor")
    file_path = input("Please enter the path to the text file: ").strip()
    
    emails = extract_emails(file_path)
    
    if emails:
        print("\nExtracted Email Addresses:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")

if __name__ == "__main__":
    main()
