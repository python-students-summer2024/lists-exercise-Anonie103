import os
import datetime

def get_today_date():
    return str(datetime.date.today())

def read_mood_diary(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return file.readlines()

def write_mood_diary(file_path, date_today, mood_value):
    with open(file_path, 'a') as file:
        file.write(f"{date_today},{mood_value}\n")

def validate_mood(mood):
    valid_moods = ["happy", "relaxed", "apathetic", "sad", "angry"]
    return mood in valid_moods

def mood_to_value(mood):
    mood_values = {
        "happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1,
        "angry": -2
    }
    return mood_values[mood]

def assess_mood():
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, "mood_diary.txt")

    date_today = get_today_date()
    mood_entries = read_mood_diary(file_path)

    if any(date_today in entry for entry in mood_entries):
        print("Sorry, you have already entered your mood today.")
        return

    while True:
        mood = input("Enter your current mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if validate_mood(mood):
            break
        print("Invalid mood. Please enter a valid mood.")

    mood_value = mood_to_value(mood)
    write_mood_diary(file_path, date_today, mood_value)

    if len(mood_entries) >= 6:
        recent_entries = mood_entries[-6:] + [f"{date_today},{mood_value}\n"]
        mood_values = [int(entry.strip().split(',')[1]) for entry in recent_entries]

        diagnosis = diagnose_mood(mood_values)
        print(f"Your diagnosis: {diagnosis}!")

def diagnose_mood(mood_values):
    mood_count = {"happy": 0, "relaxed": 0, "apathetic": 0, "sad": 0, "angry": 0}
    for value in mood_values:
        if value == 2:
            mood_count["happy"] += 1
        elif value == 1:
            mood_count["relaxed"] += 1
        elif value == 0:
            mood_count["apathetic"] += 1
        elif value == -1:
            mood_count["sad"] += 1
        elif value == -2:
            mood_count["angry"] += 1

    if mood_count["happy"] >= 5:
        return "manic"
    if mood_count["sad"] >= 4:
        return "depressive"
    if mood_count["apathetic"] >= 6:
        return "schizoid"

    average_mood_value = round(sum(mood_values) / len(mood_values))
    mood_value_to_name = {
        2: "happy",
        1: "relaxed",
        0: "apathetic",
        -1: "sad",
        -2: "angry"
    }
    return mood_value_to_name.get(average_mood_value, "unknown")
