#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails


def check_localhost():
  localhost=socket.gethostbyname("localhost")
  return localhost=="127.0.0.1"

def cpu_usage():
  usage=psutil.cpu_percent(1)
  return usage > 80

def disk_space():
  total,free=shutil.disk_usage("/")
  result=free*100/total
  return result < 20

def memory_usage():
  usage=psutil.virtual_memory().available
  usage_in_mbs=usage/(1024.0*2)
  return usage_in_mbs < 500

def email_sending(subject):
  email = emails.generate_email("automation@example.com", "yourEmail.com",subject, "Please check your system and resolve the issue as soon as possible.", "")
  emails.send_email(email)

if cpu_usage():
  subject="Error - CPU usage is over 80%"
  email_sending(subject)

if disk_space():
  subject="Error - Available disk space is less than 20%"
  email_sending(subject)

if memory_usage():
  subject="Error - Available memory is less than 500MB"
  email_sending(subject)

if not check_localhost():
  subject="Error - localhost cannot be resolved to 127.0.0.1"
  email_sending(subject)
