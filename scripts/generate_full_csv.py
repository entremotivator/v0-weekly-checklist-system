import csv
from datetime import datetime, timedelta
import random

# Define the weekly schedule with full details
weekly_schedule = [
    {"day": "Sunday", "time": "6:00 AM", "activity": "AIVACEO Podcast", "format": "Audio / Recorded", "platform": "Podcast Platforms"},
    {"day": "Sunday", "time": "2:00 PM", "activity": "Promptology Tip", "format": "Video", "platform": "Social Media"},
    {"day": "Monday", "time": "9:00-11:00 AM", "activity": "Real Estate & AI", "format": "Clubhouse", "platform": "Clubhouse"},
    {"day": "Tuesday", "time": "6:00-8:00 PM", "activity": "Community: AI Superheroes Class", "format": "Live Class", "platform": "Community Platform"},
    {"day": "Wednesday", "time": "Flexible", "activity": "AI Whiteboard Wednesday", "format": "YouTube Educational", "platform": "YouTube"},
    {"day": "Thursday", "time": "9:00-10:00 AM", "activity": "Sales Team Training", "format": "Training", "platform": "Internal"},
    {"day": "Friday", "time": "12:00 PM", "activity": "Futuristic Fridays", "format": "Live Stream", "platform": "Multiple Platforms"},
    {"day": "Saturday", "time": "Flexible", "activity": "System Saturdays", "format": "Short Video Tip", "platform": "All Social Platforms"},
]

# Sample notes for variety
sample_notes = [
    "Guest interview scheduled",
    "Need to prepare slides",
    "Topic: AI automation",
    "Follow up on last week's discussion",
    "Record ahead of time",
    "Live Q&A session",
    "",  # Empty notes are common
    "Schedule promotional posts",
]

# Start date: First Sunday of 2026
start_date = datetime(2026, 1, 4)  # January 4, 2026 is a Sunday

# Generate 52 weeks of schedule
schedule_data = []

print("🔄 Generating comprehensive 2026 schedule...")

for week in range(52):
    week_start = start_date + timedelta(weeks=week)
    
    for item in weekly_schedule:
        # Calculate the date for this activity
        day_offset = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].index(item["day"])
        activity_date = week_start + timedelta(days=day_offset)
        
        # For demo purposes, mark some past activities as complete
        is_past = activity_date < datetime.now()
        
        # Randomly assign status for past dates (to show variety in demo)
        if is_past and week < 3:  # Only first 3 weeks for demo
            prep_options = ["Complete", "In Progress", "Complete"]
            content_ready = random.choice(["Yes", "Yes", "No"])
            published = "Yes" if content_ready == "Yes" and random.random() > 0.3 else "No"
            prep_status = "Complete" if published == "Yes" else random.choice(prep_options)
            notes = random.choice(sample_notes)
            priority = random.choice(["High", "High", "Normal", "Normal", "Normal", "Low"])
        else:
            prep_status = "Not Started"
            content_ready = "No"
            published = "No"
            notes = ""
            priority = "Normal"
        
        schedule_data.append({
            "Week": week + 1,
            "Date": activity_date.strftime("%Y-%m-%d"),
            "Day": item["day"],
            "Time": item["time"],
            "Activity": item["activity"],
            "Format": item["format"],
            "Platform": item["platform"],
            "Prep_Status": prep_status,
            "Content_Ready": content_ready,
            "Published": published,
            "Notes": notes,
            "Priority": priority
        })
    
    if (week + 1) % 10 == 0:
        print(f"   ✓ Generated weeks 1-{week + 1}")

# Write to CSV
with open("schedule_2026.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Week", "Date", "Day", "Time", "Activity", "Format", "Platform", 
        "Prep_Status", "Content_Ready", "Published", "Notes", "Priority"
    ])
    writer.writeheader()
    writer.writerows(schedule_data)

print(f"\n✅ Successfully generated schedule_2026.csv!")
print(f"📅 Total activities: {len(schedule_data)}")
print(f"📆 Date range: {schedule_data[0]['Date']} to {schedule_data[-1]['Date']}")
print(f"📊 Activities per week: {len(weekly_schedule)}")
print(f"🗓️  Total weeks: 52")
print(f"\n💡 Run 'streamlit run app.py' to start tracking!")
