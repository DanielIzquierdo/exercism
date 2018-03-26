def is_isogram(string):
    string = [c.lower() for c in string if c.isalpha()] #removing non alphanumeric characters
    return len(string)-len(set(string)) == 0 #creating a set of unique chars to compare with the list of chars we create
