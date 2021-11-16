import imaplib
import email
from email.header import decode_header
import webbrowser
import os

def read_mails(u,p):
    # account credentials     
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("mail.bilkent.edu.tr")
    # authenticate
    imap.login(u, p)

    status, messages = imap.select("INBOX")


    mail_numbers = int(messages[0])
    #mailler = imap.search("starsmsg@bilkent.edu.tr")
    print(mail_numbers)
    i = 0
    res, msg = imap.fetch(str(1), "(RFC822)")

    print(msg)



read_mails("omer.olkun@ug.bilkent.edu.tr","*********")

