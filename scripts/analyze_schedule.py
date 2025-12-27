import pandas as pd
import os
from datetime import datetime

def analyze_schedule():
    """Analyze the 2026 schedule and provide insights"""
    
    if not os.path.exists("schedule_2026.csv"):
        print("❌ schedule_2026.csv not found!")
        print("   Run: python scripts/generate_full_csv.py")
        return
    
    df = pd.read_csv("schedule_2026.csv")
    
    print("\n" + "="*60)
    print("📊 2026 CONTENT SCHEDULE ANALYSIS")
    print("="*60 + "\n")
    
    # Overall statistics
    print("📋 OVERALL STATISTICS")
    print("-" * 60)
    total_activities = len(df)
    published = len(df[df["Published"] == "Yes"])
    content_ready = len(df[df["Content_Ready"] == "Yes"])
    prep_complete = len(df[df["Prep_Status"] == "Complete"])
    
    print(f"   Total Activities: {total_activities}")
    print(f"   Published: {published} ({published/total_activities*100:.1f}%)")
    print(f"   Content Ready: {content_ready} ({content_ready/total_activities*100:.1f}%)")
    print(f"   Prep Complete: {prep_complete} ({prep_complete/total_activities*100:.1f}%)")
    
    # By activity type
    print(f"\n📺 BY ACTIVITY TYPE")
    print("-" * 60)
    activity_counts = df.groupby("Activity").size().sort_values(ascending=False)
    for activity, count in activity_counts.items():
        published_count = len(df[(df["Activity"] == activity) & (df["Published"] == "Yes")])
        print(f"   {activity[:35]:<35} {count:>3} total | {published_count:>3} published")
    
    # By day of week
    print(f"\n📅 BY DAY OF WEEK")
    print("-" * 60)
    day_counts = df.groupby("Day").size()
    day_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in day_order:
        if day in day_counts:
            print(f"   {day:<12} {day_counts[day]:>3} activities")
    
    # By priority
    print(f"\n⭐ BY PRIORITY")
    print("-" * 60)
    priority_counts = df.groupby("Priority").size()
    for priority in ["High", "Normal", "Low"]:
        if priority in priority_counts:
            print(f"   {priority:<12} {priority_counts[priority]:>3} activities")
    
    # By platform
    print(f"\n🌐 BY PLATFORM")
    print("-" * 60)
    platform_counts = df.groupby("Platform").size().sort_values(ascending=False)
    for platform, count in platform_counts.items():
        print(f"   {platform[:35]:<35} {count:>3} activities")
    
    # Upcoming this week
    print(f"\n📆 UPCOMING THIS WEEK")
    print("-" * 60)
    df['Date_dt'] = pd.to_datetime(df['Date'])
    today = datetime.now()
    this_week = df[(df['Date_dt'] >= today) & (df['Date_dt'] <= today + pd.Timedelta(days=7))]
    
    if len(this_week) > 0:
        for _, row in this_week.iterrows():
            status = "✅" if row["Published"] == "Yes" else "🔄" if row["Content_Ready"] == "Yes" else "📝"
            print(f"   {status} {row['Date']} ({row['Day']}) - {row['Activity']}")
    else:
        print("   No activities scheduled for this week")
    
    # Prep status summary
    print(f"\n🔧 PREP STATUS SUMMARY")
    print("-" * 60)
    prep_counts = df.groupby("Prep_Status").size()
    for status in ["Not Started", "In Progress", "Complete"]:
        if status in prep_counts:
            print(f"   {status:<15} {prep_counts[status]:>3} activities")
    
    print("\n" + "="*60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")

if __name__ == "__main__":
    analyze_schedule()
