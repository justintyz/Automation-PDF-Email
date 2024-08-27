#!/usr/bin/env python3


import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  # Your Hotmail credentials
  sender_email = "tyzjustin@hotmail.com"
  sender_password = "tyz7099E!"

  # Recipient Gmail address
  receiver_email = "tyzjustin@gmail.com"
  
  # Create SMTP session
  parameters = smtplib.SMTP("smtp.office365.com", 587)
  with parameters.connect("smtp.office365.com", 587) as server:
      server.starttls()  # Enable TLS encryption
      server.login(sender_email, sender_password)
      server.send_message(message, sender_email, receiver_email)
      # server.quit()
  # try:
  #   with parameters.connect("smtp.office365.com", 587) as server:
  #       server.starttls()  # Enable TLS encryption
  #       server.login(sender_email, sender_password)
  #       server.send_message(message, sender_email, receiver_email)
  #       # server.quit()
  #   print("Email sent successfully!")
  # except Exception as e:
  #   print(f"An error occurred: {e}")
  