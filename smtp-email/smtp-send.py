import smtplib

# store test email/password to variable
my_email = "testemail.ksg.data@gmail.com"
app_password = "tjfe xxdk yojh xpuc"
my_password = "^K8QWdbRjF49Ehq5"

# recipient test email
to_email = "testemailksg.data@yahoo.com"

# So you don't have to close
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    # call tls - transport layer security - encrypts connection
    connection.starttls()
    # then login with credentials
    connection.login(user=my_email, password=app_password)
    # now send email - to, from, msg all required
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg="Subject: yee yee praise be\n\nSkeeiieee"
    )

#---------------------------------------------#
# without with keyword - must manually close
# create SMTP object, takes smtp server as input
connection = smtplib.SMTP("smtp.gmail.com", port=587)
# call tls - transport layer security - encrypts connection
connection.starttls()
# then login with credentials
connection.login(user=my_email, password=app_password)
# now send email - to, from, msg all required
connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject: yee yee praise be\n\nSkeeiieee")
# close connection
connection.close()





