# Gmail Cleaner Automation

A Python-based Gmail cleanup automation tool using IMAP.

This project helps automatically delete Gmail emails from:

- Inbox
- Spam
- Both Inbox and Spam

using multiple filters such as:

- All emails
- Unread emails
- Emails from specific sender
- Emails with specific subject
- Emails before a specific date
- OTP emails

---

# Features

- Gmail IMAP integration
- Secure Gmail App Password login
- Save credentials locally
- Bulk email deletion
- OTP email filtering
- Multi-mailbox support
- Interactive CLI menu
- Loop-based menu system
- JSON credential storage
- Virtual Environment (`venv`) support

---

# Project Structure

```text
gmail-cleaner/
│
├── gmail_cleaner.py
├── credentials.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── venv/
│
└── __pycache__/
```

---

# Requirements

- Python 3.10+
- Gmail account
- Gmail App Password enabled

---

# Setup Project

## 1. Clone Repository

```bash
gh repo clone UbaisAd/Python-based-projects
```

Move into project folder:

```bash
cd gmail-cleaner
```

---

# Create Virtual Environment (venv)

## Linux / Mac

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python3 gmail_cleaner.py
```

---

# Gmail Setup

Normal Gmail password will NOT work.

You must create a Gmail App Password.

---

# Step 1 — Enable 2-Step Verification

Open:

https://myaccount.google.com/security

Enable:

- 2-Step Verification

---

# Step 2 — Generate App Password

Open:

https://myaccount.google.com/apppasswords

Choose:

- App → Mail
- Device → Other

Generate password and use it in the project.

---

# Example credentials.json

```json
{
    "email": "yourmail@gmail.com",
    "password": "your-app-password"
}
```

> **Note**
>
> Replace:
>
> - `yourmail@gmail.com` → with your actual Gmail address
> - `your-app-password` → with your Google App Password
>
> Normal Gmail password will NOT work.

---

# Example Usage

```text
==============================
 Gmail Cleaner Menu
==============================

Select mailbox to clean:
1. Inbox
2. Spam
3. Both Inbox and Spam
0. Exit
```

---

# Available Filters

```text
1. All emails
2. Unread emails
3. Emails from specific sender
4. Emails with specific subject
5. Emails before specific date
6. Emails containing OTP
```

---

# Security

Create `.gitignore` file:

```gitignore
venv/
credentials.json
__pycache__/
```

Never upload:

- credentials.json
- Gmail App Password
- personal credentials
- venv files

to GitHub.

---

# Create requirements.txt

Run:

```bash
pip freeze > requirements.txt
```

---

# Recommended GitHub Upload Files

Upload:

```text
gmail_cleaner.py
README.md
requirements.txt
.gitignore
```

Do NOT upload:

```text
venv/
credentials.json
__pycache__/
```

---

# Future Improvements

- Password masking
- Credential encryption
- GUI version
- Email preview before delete
- Logging system
- Multi-account support
- Scheduled cleanup
- Export deleted email report

---

# Technologies Used

- Python
- IMAP
- JSON
- Gmail
- CLI Automation

---

# Author

Ubais Ahamed

---

# License

This project is for educational and automation purposes.
