#!/usr/bin/env python3

import configargparse as argparse
import smtplib
import datetime
from email.mime.text import MIMEText

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def get_args():
    parser = argparse.ArgumentParser(
        description='Send an email.',
        default_config_files=[dir_path + '/config/main.yaml']
    )
    parser.add_argument('--sender', type=str, default='sender@gmx.de')
    parser.add_argument('--password', type=str, default=None)
    parser.add_argument('--to', type=str, default='recipient@email.de')
    parser.add_argument('--subject', type=str, default='NOTIFICATION')
    parser.add_argument('--text', type=str, default='')
    parser.add_argument('--smtp_server', type=str, default='mail.gmx.net')
    parser.add_argument('--smtp_port', type=int, default=587)
    parser.add_argument('--add_timestamp_to_subject', type=bool, default=True)
    args = parser.parse_args()
    return args


def send_email(args):
    sender = args.sender
    receiver = args.to

    msg = MIMEText(args.text)
    msg['From'] = sender
    msg['To'] = receiver

    subject = args.subject
    if args.add_timestamp_to_subject:
        subject = '{} // {}'.format(get_formatted_timestamp(), subject)

    msg['Subject'] = subject

    server = smtplib.SMTP(args.smtp_server, args.smtp_port)
    server.starttls()
    server.login(sender, args.password)
    server.send_message(msg)
    server.quit()

def get_formatted_timestamp():
    return '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

def print_args(args):
    args = vars(args)
    print('Program arguments:')
    for k, v in sorted(args.items(), key=lambda x: x[0]):
        if 'password' in k:
            v = '*********'
        print('\t{:40} {}'.format(k, v))
    print('')


def main():
    args = get_args()
    print_args(args)

    try:
        send_email(args)
        print('Mail successfully sent!')
    except Exception as e:
        print('Error sending email:', e)


if __name__ == '__main__':
    main()
