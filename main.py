# An Email slicer is a very useful program for separating the username and domain name of an email address.

# our task is to write a program that can retrieve the username and the domain name of the email.

# So we need to divide the email into two strings using ‘@’ as the separator. Let’s see how to separate the email and domain name

email = input("Enter Your Email: ").strip()
print(email)
userName = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{userName}' and your domain is '{domain_name}'")
print(format_)
