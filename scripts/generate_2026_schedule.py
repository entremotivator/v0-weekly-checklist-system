import csv
from datetime import datetime, timedelta

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

# Start date: First Sunday of 2026
start_date = datetime(2026, 1, 4)  # January 4, 2026 is a Sunday

# Generate 52 weeks of schedule
schedule_data = []

for week in range(52):
    week_start = start_date + timedelta(weeks=week)
    
    for item in weekly_schedule:
        # Calculate the date for this activity
        day_offset = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].index(item["day"])
        activity_date = week_start + timedelta(days=day_offset)
        
        schedule_data.append({
            "Week": week + 1,
            "Date": activity_date.strftime("%Y-%m-%d"),
            "Day": item["day"],
            "Time": item["time"],
            "Activity": item["activity"],
            "Format": item["format"],
            "Platform": item["platform"],
            "Prep_Status": "Not Started",
            "Content_Ready": "No",
            "Published": "No",
            "Notes": "",
            "Priority": "Normal"
        })

# Write to CSV
with open("schedule_2026.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Week", "Date", "Day", "Time", "Activity", "Format", "Platform", 
        "Prep_Status", "Content_Ready", "Published", "Notes", "Priority"
    ])
    writer.writeheader()
    writer.writerows(schedule_data)

print("✅ Generated schedule_2026.csv with 52 weeks of content!")
print(f"📅 Total activities: {len(schedule_data)}")
print(f"📆 Date range: {schedule_data[0]['Date']} to {schedule_data[-1]['Date']}")
print(f"📊 Activities per week: {len(weekly_schedule)}")
