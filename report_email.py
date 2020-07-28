#!/usr/bin/env python3

import os
import datetime
import reports
import emails


def pdf_body():
    data=""
    dir="./supplier-data/descriptions/"

    for files in os.listdir(dir):
        with open(dir+files) as file:
            line = file.readlines()
            data+="name: "+line[0].strip()+"<br />"+"weight: "+line[1].strip()+"<br /><br /><br />"
    return data

if __name__=="__main__":
  title="Processed Update on "+str(datetime.date.today().strftime("%B %d, %Y"))
  pdf_data = pdf_body()
  reports.generate_report("/tmp/processed.pdf", title,pdf_data)
  message=emails.generate_email("automation@example.py", "Yourgmail@gmail.com","Upload Completed - Online Fruit Store","All fruits are uploaded to our website successfully. A detailed list is attached to this email.","/tmp/processed.pdf")
  emails.send_email(message)

