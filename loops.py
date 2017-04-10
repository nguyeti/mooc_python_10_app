print("*** FOR LOOP ***")
emails = ["me@gmail.com","you@hotmail.com","he@gmail.com"]

for e in emails:
    if "@gmail.com" in e:
        print(e)

emails.append("we@gmail.com")
# print("*** WHILE LOOP ***")
#
# password = ''
# while password != 'python123':
#     password = input("Enter password: ")
#     if password == "python123":
#         print("You are logged in.")
#     else:
#         print("Sorry, try again")
