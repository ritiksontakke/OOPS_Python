# PILLAR: Encapsulation
# PROGRAM 5: Password Manager
# ============================================================
#
# PROBLEM:
# Create a PasswordManager class that hides the password.
# - Password is stored privately (never shown as plain text).
# - set_password(new_pass): set password only if it has:
#     * at least 8 characters
#     * at least one digit
#   Otherwise print why it failed.
# - check_password(attempt): return True if correct, False otherwise.
# - is_set(): return True if a password has been set.
#
# HINT: Use a simple hash (e.g., Python's built-in hash()) to store
# the password instead of plain text.
#
# EXAMPLE USAGE:
#   pm = PasswordManager()
#   pm.set_password("abc")        # "Too short! Minimum 8 characters."
#   pm.set_password("abcdefgh")   # "Must contain at least one digit."
#   pm.set_password("secure123")  # Password set successfully!
#   print(pm.check_password("wrong"))     # False
#   print(pm.check_password("secure123")) # True
# ============================================================


class PasswordManager:
    def __init__(self):
        self.__password_hash = None
    
    def set_password(self, new_pass):
        if len(new_pass) < 8:
            print("to short password")
        
        if not any(char.isdigit() for char in new_pass):
            print("must contain at least one digit")
            return
        
        self.__password_hash = hash(new_pass)
        print("password set succefully")

    def check_password(self, attempt):
        if self.__password_hash is None:
            return False
        return hash(attempt) == self.__password_hash
    def is_set(self):
        return self.__password_hash is not None
    
pm = PasswordManager()

pm.set_password("abc")
# Too short! Minimum 8 characters.

pm.set_password("abcdefgh")
# Must contain at least one digit.

pm.set_password("secure123")
# Password set successfully!

print(pm.check_password("wrong"))     
# False

print(pm.check_password("secure123")) 
# True