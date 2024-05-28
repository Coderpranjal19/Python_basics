def main():
    print("Welcome to the slicer")
    print("")

    email_input = input("please enter your email: ")

    (username,domain) = (email_input.split("@"))
    (domain, extension) = (domain.split("."))

    print("username :", username)
    print("domain :", domain) 
    print("extension :", extension)

main()