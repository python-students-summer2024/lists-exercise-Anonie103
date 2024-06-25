import os
from datetime import date, timedelta
from pathlib import Path

def get_mood_value(mood):
    mood_values = {
        "happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1,
        "angry": -2
    }
    return mood_values.get(mood.lower(), None)

def get_mood_diary_path():
    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "mood_diary.txt"

def assess_mood(mood_input=None):
    mood_diary_path = get_mood_diary_path()
    today = date.today()

    # Check if a mood has already been entered for today
    with open(mood_diary_path, "r") as f:
        for line in f:
            entry_date = date.fromisoformat(line.split(",")[0])
            if entry_date == today:
                print("You have already entered your mood for today.")
                return

    # Get mood input (or use provided input for testing)
    if mood_input is None:
        while True:
            mood = input("Enter your current mood (happy, relaxed, apathetic, sad, angry): ").lower()
            mood_value = get_mood_value(mood)
            if mood_value is not None:
                break
            print("Invalid mood. Please try again.")
    else:
        mood_value = get_mood_value(mood_input)
        if mood_value is None:
            raise ValueError(f"Invalid mood: {mood_input}")

    # Store the mood entry in the mood diary file
    with open(mood_diary_path, "a") as f:
        f.write(f"{today.isoformat()},{mood_value}\n")

    # Analyze the last 7 days of mood entries
    mood_entries = []
    with open(mood_diary_path, "r") as f:
        for line in f:
            entry_date, entry_value = line.strip().split(",")
            entry_date = date.fromisoformat(entry_date)
            if entry_date >= today - timedelta(days=7):
                mood_entries.append(int(entry_value))

    # Diagnose mood disorder based on the last 7 days of entries
    num_happy = mood_entries.count(2)
    num_sad = mood_entries.count(-1)
    num_apathetic = mood_entries.count(0)

    if num_sad >= 4:
        print("Based on your recent mood entries, you may be experiencing depression.")
    elif num_happy >= 5:
        print("Based on your recent mood entries, you may be experiencing mania.")
    elif num_apathetic >= 6:
        print("Based on your recent mood entries, you may be experiencing a schizoid disorder.")
    else:
        average_mood = sum(mood_entries) / len(mood_entries)
        if average_mood >= 1:
            print("Based on your recent mood entries, your average mood is relaxed.")
        elif average_mood == 0:
            print("Based on your recent mood entries, your average mood is apathetic.")
        else:
            print("Based on your recent mood entries, your average mood is sad or angry.")
