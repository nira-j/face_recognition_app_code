def mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_content = '''Hello,
    This is niraj, recognised by face recognier.
    Thank You
    '''
    
    sender = 'xyz@gmail.com'
    password = '**********'
    receiver = 'abc@gmail.com'
   
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    # body for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) # use gmail with port
    session.starttls() # enable security
    session.login(sender, password) # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent successfully!')