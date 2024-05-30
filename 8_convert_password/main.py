import random

class Passwords:
    def __init__(self, length):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        self.generated_password = ''.join(random.choice(characters) for i in range(length))
        
    
    def check_password_strength(self):
         # Define criteria for a strong password
        criteria = {
            'length': len(self.generated_password) >= 8,
            'lowercase': any(char.islower() for char in self.generated_password),
            'uppercase': any(char.isupper() for char in self.generated_password),
            'digit': any(char.isdigit() for char in self.generated_password),
            'special': any(char in "!@#$%^&*()" for char in self.generated_password)
        }
        strength = sum(criteria.values())
        
        return strength
    
password = Passwords(12)
print("Generated password:", password.generated_password)

print("Password strength:", password.check_password_strength())