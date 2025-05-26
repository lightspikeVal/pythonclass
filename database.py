# This is only for educational purposes only and this does not save any user info and will not work like Firebase or etc.
import re
import os
# Start of library
def author():
    print("Made by Smart Bob")
    
# Start of working library
def read(filename=""):
    """Reads the entire content of a file and returns it as a string.

    Parameters:

        filename (str): The path to the file you want to read. If not provided or left empty, the function will print an error message and return 0.
    Returns:

        Returns the content of the file as a string if the file is found and readable.
        Returns 0 if the filename is not provided or is empty."""
    if filename=="":
        print("Unable to find the filename or is it empty?")
        return 0
    else:
        f = open(filename)
        info = f.read()
        return info

def register(filename="", userdata=""):
    """Appends a new user's data to a file, ensuring that the username does not already exist.
    The userdata string must be formatted as username@password.
    """
    if filename == "" or userdata == "":
        raise ValueError("Unable to read file or get userdata, one of the fields are missing.")
    split = userdata.split("@")
    if len(split) != 2:
        print("Invalid userdata format. Use username@password.")
        return False
    username = split[0]
    with open(filename, "r") as f:
        filedata = f.readlines()
    for line in filedata:
        iof = line.strip().split("@")
        if iof[0] == username:
            print("Username already exists.")
            return False
    with open(filename, "a") as f:
        f.write(userdata + "\n")
    print("Registration successful!")
    return True

#Login

def login(filename="", userdata=""):
    """Checks if the provided username and password exist in the file.
    The userdata string must be formatted as username@password.

    If login fails, prompts the user to register.

    Returns:
        True if login is successful, False otherwise.
    """
    if filename == "" or userdata == "":
        raise ValueError("Unable to read file or get userdata, one of the fields are missing.")
    split = userdata.split("@")
    if len(split) != 2:
        print("Invalid userdata format. Use username@password.")
        return False
    username, password = split
    try:
        with open(filename, "r") as f:
            filedata = f.readlines()
    except FileNotFoundError:
        print("File not found.")
        return False
    for line in filedata:
        iof = line.strip().split("@")
        if len(iof) == 2 and iof[0] == username and iof[1] == password:
            print("Login successful!")
            return True
    print("Login failed: Incorrect username or password.")
    choice = input("No login details found. Would you like to register? (y/n): ").strip().lower()
    if choice == "y":
        register(filename, userdata)
    return False

def format(filename=""):
    """Erases all data in the specified file, like a factory reset."""
    if filename == "":
        print("No filename provided.")
        return False
    try:
        with open(filename, "w") as f:
            pass  # Opening in write mode with no content erases the file
        print("All data erased. File has been reset.")
        f.close()
        return True
    except Exception as e:
        print(f"Error erasing file: {e}")
        return False
def valid(filename=""):
    """Checks whether if given file is in valid format or need to change.
        Parameters:
        filename = str(Required filename path)
        Return:
            Returns in Incorrect,Correct"""
    
    f = open(filename)
    correct=0
    incor=0
    lines = f.readlines()
    for line in len(lines):
        info = line.split("@")
        if len(info) == 1:
            incor+=1
        else:
            correct+=1
    f.close()
    return incor,correct

def userpath(metadata_path="", userdata_path=""):
    """
    Asks the user for username and password, and stores additional data in userdata_path.
    Programmer must provide the file paths for metadata (credentials) and userdata.
    Raises ValueError if any path or input is empty.
    If the username exists in metadata, checks userdata for an entry.
    Stores in userdata as: username@password#data
    Prints only the user data (not username or password) if found in userdata.
    """
    if not metadata_path or not userdata_path:
        raise ValueError("Both metadata_path and userdata_path must be provided by the developer.")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    data = input("Enter additional user data: ").strip()

    if not username or not password or not data:
        raise ValueError("Username, password, and data cannot be empty.")

    # Check if user exists in metadata
    try:
        with open(metadata_path, "r") as meta_file:
            found = False
            for line in meta_file:
                parts = line.strip().split("@")
                if len(parts) >= 2 and parts[0] == username and parts[1] == password:
                    found = True
                    break
            if not found:
                print("User does not exist in metadata (credentials).")
                return False
    except FileNotFoundError:
        print("Metadata file not found.")
        return False

    # Check if user entry already exists in userdata and print only the user data if found
    try:
        with open(userdata_path, "r") as user_file:
            for line in user_file:
                if line.startswith(f"{username}@{password}#"):
                    # Extract and print only the user data part
                    parts = line.strip().split("#", 1)
                    if len(parts) == 2:
                        print("User data found:", parts[1])
                    else:
                        print("User data found, but could not parse data section.")
                    return True
    except FileNotFoundError:
        pass  # File will be created

    # Store new user data
    with open(userdata_path, "a") as user_file:
        user_file.write(f"{username}@{password}#{data}\n")
    print("User data stored successfully!")
    return True



def file_exists(filepath):
    """
    Checks whether the specified file exists.

    Parameters:
        filepath (str): The path to the file.

    Returns:
        True if the file exists, False otherwise.
    """
    return os.path.isfile(filepath)








