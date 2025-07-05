import smtplib

try:
    # Use Gmail's SMTP over TLS on port 587
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS encryption
    server.login('obserawebsite@gmail.com', 'cski yysw kdar ')  # Use your Gmail email and app password

    # Send a test email
    server.sendmail('obserawebsite@gmail.com', 'info@obsera.ca', 'Subject: Test\n\nHello from test script.')

    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
