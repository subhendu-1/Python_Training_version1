# 9️⃣ Greet Users with Custom Messages

def greet_users(**greetings):
    for user, message in greetings.items():
        print(f"Hello {user}, {message}")

greet_users(Alice="Good morning!", Bob="Happy Birthday!", Charlie="Welcome back!")
