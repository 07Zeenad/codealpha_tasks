
import re

input_file = "emails.txt"
output_file = "extracted_emails.txt"

try:
    # Read text from the input file
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Find email addresses using a regular expression
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)

    # Remove duplicate email addresses
    emails = sorted(set(emails))

    # Save extracted emails to a new file
    with open(output_file, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    print("Email extraction completed!")
    print("Total unique emails found:", len(emails))
    print("Emails:", emails)
    print("Saved to:", output_file)

except FileNotFoundError:
    print("Error: emails.txt was not found.")
    print("Please create emails.txt in the same folder.")

