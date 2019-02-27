# The get_login_name function accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name.

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the name is less than 3 characters, the
    # slice will return the entire first name.
    set1 = first[0 : 3]

    # Get the first three letters of the last name.
    # If the name is less than 3 characters, the
    # slice will return the entire first name.
    set2 = last[0 : 3]

    # Get the first three letters of the student ID.
    # If the name is less than 3 characters, the
    # slice will return the entire ID number.
    set3 = idnumber[-3 : 0]

    # Put the sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name
    return login_name


