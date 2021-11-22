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
    #print(mail_numbers)

    subject_en = 'SUBJECT "Secure Login Gateway E-Mail Verification Code"'
    subject_tr = 'SUBJECT "Güvenli Giriş Kapısı E-Posta Doğrulama Kodu"'
    #subject_tr = 'SUBJECT "Secure Login Gateway E-Mail Verification Code"'


    search_s = '(OR (%s) (%s))'%(subject_en, subject_tr)

    #print(search_s)
    data = imap.search('utf-8', search_s.encode("utf-8"))[1][0].decode("utf-8").split()
    #print(data)
    res, msg = imap.fetch(str(data[-1]), "(RFC822)")

    mes = msg[0][1].decode("utf-8")

    words = email.message_from_string(mes).get_payload().split()
    #print(words)

    if(words[1] == "kodlu"):
        return  (words[0],words[-1])
    elif words[0] == "Verification":
        return (words[-1][:-1], words[2])

    return words[2]


