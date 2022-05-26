import smtplib
import maskpass

send_add="a1999.12.09anjali@gmail.com"
rec_add='a1999.12.09anjali@gmail.com'


# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
# pwd = maskpass.askpass(mask="")
s.login(send_add, 'calculusS18')

# message to be sent
message = "Hello"

# sending the mail
s.sendmail(send_add, rec_add, message)

# terminating the session
s.quit()