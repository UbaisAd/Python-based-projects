import imaplib
import email
import os
import json
from email.header import decode_header

CONFIG_FILE = "credentials.json"


# ==============================
# LOAD OR SAVE CREDENTIALS
# ==============================

def load_credentials():

    if os.path.exists(CONFIG_FILE):

        with open(CONFIG_FILE, "r") as file:
            data = json.load(file)

        print("Saved credentials loaded.\n")

        return data["email"], data["password"]

    else:

        user_email = input("Enter Gmail Address: ")
        app_password = input("Enter Gmail App Password: ")

        save = input("Save credentials for next time? (yes/no): ").lower()

        if save == "yes":

            data = {
                "email": user_email,
                "password": app_password
            }

            with open(CONFIG_FILE, "w") as file:
                json.dump(data, file, indent=4)

            print("Credentials saved.\n")

        return user_email, app_password


# ==============================
# LOGIN
# ==============================

your_mail, your_app_password = load_credentials()

try:

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(your_mail, your_app_password)

    print("Login Successful.\n")

except Exception as e:

    print("Login Failed.")
    print(e)
    exit()


# ==============================
# MAIN LOOP
# ==============================

while True:

    print("\n==============================")
    print(" Gmail Cleaner Menu ")
    print("==============================")

    # ==============================
    # MAILBOX SELECTION
    # ==============================

    print("\nSelect mailbox to clean:")
    print("1. Inbox")
    print("2. Spam")
    print("3. Both Inbox and Spam")
    print("0. Exit")

    mb_choice = input("Enter option number: ")

    if mb_choice == "0":

        print("\nExiting program...")
        break

    mailboxes = []

    if mb_choice == "1":
        mailboxes = ["inbox"]

    elif mb_choice == "2":
        mailboxes = ["[Gmail]/Spam"]

    elif mb_choice == "3":
        mailboxes = ["inbox", "[Gmail]/Spam"]

    else:
        print("\nInvalid mailbox option.")
        continue

    # ==============================
    # FILTER SELECTION
    # ==============================

    print("\nChoose filter to delete emails:")
    print("1. All emails")
    print("2. Unread emails")
    print("3. Emails from specific sender")
    print("4. Emails with specific subject")
    print("5. Emails before specific date")
    print("6. Emails containing OTP")
    print("0. Back to Main Menu")

    choice = input("Enter option number: ")

    if choice == "0":
        continue

    if choice == "3":
        sender = input("Enter sender email: ")

    elif choice == "4":
        subject = input("Enter subject text: ")

    elif choice == "5":
        date = input("Enter date (DD-Mon-YYYY): ")

    elif choice not in ["1", "2", "3", "4", "5", "6"]:
        print("\nInvalid filter option.")
        continue

    # ==============================
    # SEARCH + DELETE
    # ==============================

    for box in mailboxes:

        print(f"\nSearching in: {box}")

        mail.select(box)

        if choice == "1":
            result, mail_ids = mail.search(None, "ALL")

        elif choice == "2":
            result, mail_ids = mail.search(None, "UNSEEN")

        elif choice == "3":
            result, mail_ids = mail.search(None, 'FROM', f'"{sender}"')

        elif choice == "4":
            result, mail_ids = mail.search(None, f'SUBJECT "{subject}"')

        elif choice == "5":
            result, mail_ids = mail.search(None, f'BEFORE {date}')

        elif choice == "6":
            result, mail_ids = mail.search(None, "ALL")

        email_ids = mail_ids[0].split()

        print(f"Found {len(email_ids)} emails")

        # ==============================
        # OTP FILTER
        # ==============================

        if choice == "6":

            otp_ids = []

            for eid in email_ids:

                res, msg_data = mail.fetch(eid, "(RFC822)")

                raw_email = msg_data[0][1]

                msg = email.message_from_bytes(raw_email)

                subject, encoding = decode_header(
                    msg["Subject"]
                )[0]

                if isinstance(subject, bytes):

                    subject = subject.decode(
                        encoding or "utf-8",
                        errors="ignore"
                    )

                body_text = ""

                if msg.is_multipart():

                    for part in msg.walk():

                        if part.get_content_type() == "text/plain":

                            try:

                                body_text += part.get_payload(
                                    decode=True
                                ).decode(errors="ignore")

                            except:
                                continue

                else:

                    body_text = msg.get_payload(
                        decode=True
                    ).decode(errors="ignore")

                if "otp" in (subject + body_text).lower():

                    otp_ids.append(eid)

            email_ids = otp_ids

            print(f"Filtered OTP emails: {len(email_ids)}")

        # ==============================
        # NO EMAIL FOUND
        # ==============================

        if not email_ids:

            print("No emails found.")
            continue

        # ==============================
        # DELETE CONFIRMATION
        # ==============================

        confirm = input(
            "Delete these emails? (yes/no): "
        ).lower()

        if confirm != "yes":

            print("Skipped deletion.")
            continue

        all_ids = b','.join(email_ids)

        mail.store(all_ids, '+FLAGS', '\\Deleted')

        mail.expunge()

        print(f"Deleted {len(email_ids)} emails from {box}")

    # ==============================
    # CONTINUE OPTION
    # ==============================

    again = input(
        "\nDo you want to perform another operation? (yes/no): "
    ).lower()

    if again != "yes":

        print("\nExiting program...")
        break


# ==============================
# LOGOUT
# ==============================

mail.logout()

print("\nFinished.")