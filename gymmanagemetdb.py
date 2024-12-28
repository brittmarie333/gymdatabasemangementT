import mysql.connector
from mysql.connector import Error

#establishing the connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='dougfunny',  
            database='gym_database'  # name of the database
        )
        if connection.is_connected():
            print("Connection to the database established.")
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Task 1: add member with information needed in one query
def add_member(id, name, age):
    connection = create_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, age))
        connection.commit()
        print("Member added successfully.")
    except Error as e:
        print(f"Error adding member: {e}")
    finally:
        cursor.close()
        connection.close()

# Task 2: add a workout session with information needed in one query
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    connection = create_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        # First, check if the member exists
        query = "SELECT id FROM Members WHERE id = %s"
        cursor.execute(query, (member_id,))
        result = cursor.fetchone()
        if result is None:
            print(f"No member found with ID {member_id}.")
            return
        
#if member exists, add the workout session
        query = """INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        connection.commit()
        print("Workout session added successfully.")
    except Error as e:
        print(f"Error adding workout session: {e}")
    finally:
        cursor.close()
        connection.close()

#Task 3: Updating Member Information (age from task example)
def update_member_age(member_id, new_age):
    connection = create_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        # Check if the member exists
        query = "SELECT id FROM Members WHERE id = %s"
        cursor.execute(query, (member_id,))
        result = cursor.fetchone()
        if result is None:
            print(f"No member found with ID {member_id}.")
            return

#update member age
        query = "UPDATE Members SET age = %s WHERE id = %s"
        cursor.execute(query, (new_age, member_id))
        connection.commit()
        print("Member's age updated successfully.")
    except Error as e:
        print(f"Error updating member age: {e}")
    finally:
        cursor.close()
        connection.close()
        
#Task 4: delete a Workout Session
def delete_workout_session(session_id):
    connection = create_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
#check if workout session exists
        query = "SELECT session_id FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query, (session_id,))
        result = cursor.fetchone()
        if result is None:
            print(f"No workout session found with ID {session_id}.")
            return

#delete workout sessio
        query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query, (session_id,))
        connection.commit()
        print("Workout session deleted successfully.")
    except Error as e:
        print(f"Error deleting workout session: {e}")
    finally:
        cursor.close()
        connection.close()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='dougfunny',   
            database='gym_database'
        )
        if connection.is_connected():
            print("Connection to the database established.")
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None


def get_members_in_age_range(start_age, end_age):
    connection = create_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
#MySQL query using BETWEEN to filter members by age range
        query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))
        members = cursor.fetchall()
        
       
        if members:
            print(f"Members between ages {start_age} and {end_age}:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        else:
            print(f"No members found in the age range {start_age} to {end_age}.")
    except Error as e:
        print(f"Error fetching members: {e}")
    finally:
        cursor.close()
        connection.close()        

#usage:
if __name__ == "__main__":
#adding a member
    add_member(1, 'John Doe', 25)
    
#adding a workout session for the member
    add_workout_session(1, '2023-08-16', 45, 300)
    
#updating a member's age
    update_member_age(1, 26)
    
#deleting a workout session by session ID
    delete_workout_session(1)

if __name__ == "__main__":
#get members whose age is between 21 and 31
    get_members_in_age_range(21, 31)