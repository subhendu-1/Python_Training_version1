import oracledb
 
# Connection setup
try:
    conn = oracledb.connect(
        user="system",
        password="12345",
        dsn=oracledb.makedsn("localhost", 1521, service_name="xe")
    )
    cursor = conn.cursor()
except oracledb.Error as e:
    print("Database connection failed:", e)
    exit()
 
# CREATE: Add new user
def create_user(email, gender, name, password, role):
    try:
        cursor.execute("""
            INSERT INTO tbl_users (USER_EMAIL, USER_GENDER, USER_NAME, USER_PASSWORD, USER_ROLE)
            VALUES (:1, :2, :3, :4, :5)
        """, [email, gender, name, password, role])
        conn.commit()
        print("User created successfully.")
    except oracledb.Error as e:
        print("Error creating user:", e)
 
# READ: Get all users
def get_users():
    try:
        cursor.execute("SELECT * FROM tbl_users")
        users = cursor.fetchall()
        for user in users:
            print(user)
    except oracledb.Error as e:
        print("Error retrieving users:", e)
 
# UPDATE: Update a user's role or password by USER_ID
def update_user(user_id, new_password=None, new_role=None):
    try:
        if new_password:
            cursor.execute("UPDATE tbl_users SET USER_PASSWORD = :1 WHERE USER_ID = :2", [new_password, user_id])
        if new_role:
            cursor.execute("UPDATE tbl_users SET USER_ROLE = :1 WHERE USER_ID = :2", [new_role, user_id])
        conn.commit()
        print("User updated.")
    except oracledb.Error as e:
        print("Error updating user:", e)
 
# DELETE: Delete a user by ID
def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM tbl_users WHERE USER_ID = :1", [user_id])
        conn.commit()
        print("User deleted.")
    except oracledb.Error as e:
        print("Error deleting user:", e)
 
# Close connection
def close_connection():
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Connection closed.")
    except oracledb.Error as e:
        print("Error closing connection:", e)
 
# Main test sequence
if __name__ == "__main__":
    create_user("alice@example.com", "Female", "Alice", "secure123", "admin")
    get_users()
    update_user(user_id=1, new_password="newpass123", new_role="user")
    delete_user(user_id=1)
    close_connection()