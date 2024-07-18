# 📧 Email Automation using Flask

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repo](#clone-the-repo)
  - [Customize the Script](#customize-the-script)
  - [Create an App Password](#create-an-app-password)
  - [Run the Script](#run-the-script)
- [Limitations](#limitations)
- [Note](#note)

## Description
Email Automation using Flask is a Python script that uses Flask and Flask-Mail to automate the process of sending emails with attachments and embedded images. This can be useful for automating email notifications or sending batch emails with attachments.

## Features
- Send emails with attachments (PDF, images, etc.)
- Embed images within the email body
- Customize email recipients, CC, subject, and body

## Prerequisites
- Python 3.x
- Flask (`pip install Flask`)
- Flask-Mail (`pip install Flask-Mail`)

## Getting Started

### Clone the Repo
```sh
git clone https://github.com/JayshreeMishra/Email-Automation-using-Flask.git
cd Email-Automation-using-Flask
```

### Customize the Script
Edit `main.py` to customize the email details:
- Update the `MAIL_USERNAME` and `MAIL_PASSWORD` in the app configuration with your email and password.
- Update the email subject, sender, recipients, and CC fields.
- Customize the email body and attachments.

### Create an App Password
To be able to send emails, you will require an app password:
1. Go to your Google Account settings.
2. Navigate to [App Passwords](https://myaccount.google.com/apppasswords).
3. Generate a new app password and use it in place of your regular email password in the script.

### How to Use It
Go to the settings for your Google Account in the application or device you are trying to set up. Replace your password with the 16-character app password shown above. Just like your normal password, this app password grants complete access to your Google Account. Don't share it with anyone.

### Run the Script
To run the script, execute the following command:
```sh
python main.py
```
Follow the local host link displayed in the terminal. The "Message sent!" message will be displayed there, indicating that the email has been sent successfully.

## Limitations
- The script is currently configured for Gmail; if you are using a different email provider, make the necessary changes in the code accordingly.

```
