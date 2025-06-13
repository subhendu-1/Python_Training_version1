class User:
    user_count = 0

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        User.user_count += 1
    
    @staticmethod
    def is_valid_email(email):
        return '@' in email and email.endswith('.com')

# Example
u1 = User("Alice", "Premium")
u2 = User("Bob", "Free")
print(User.user_count)


print(User.is_valid_email("test@example.com"))  # True
print(User.is_valid_email("invalid@domain.org")) 


u1 = User("Alice", "Premium")
u2 = User("Bob", "Free")

print(f"User Count (class variable): {User.user_count}")
print(f"{u1.name}'s Membership: {u1.membership_type}")
print(f"{u2.name}'s Membership: {u2.membership_type}")
