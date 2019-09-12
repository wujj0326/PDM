#get

check=input("Do you want to ask for a person's contact?")
contact_list={
    "mostafa mesgari":4475,
    "linda leon":7634,
    "kala seal":2741,
    "sijun wang":1787,
    "dayle smith":5187
}
while check=="yes":
    contact=input("Who do you want to contact?")
    print("The extention you are looking for is",contact_list.get(contact)) #use get to show NONE for an error
    check=input("Do you want to ask for another person's contact?")
print("Thanks for using our LMU directory. Feel free to come back at any time.")