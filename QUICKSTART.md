# Quick Start Guide

Get your 2026 Content Schedule Tracker up and running in 3 minutes!

## Step 1: Generate Your Schedule (30 seconds)

Run the generation script to create your complete 52-week schedule:

```bash
python scripts/generate_full_csv.py
```

This creates `schedule_2026.csv` with:
- 416 total activities (8 per week × 52 weeks)
- All dates mapped to 2026 calendar
- Ready-to-track format

## Step 2: Launch the Tracker (10 seconds)

Start the Streamlit app:

```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501`

## Step 3: Start Tracking! (2 minutes)

### Quick Actions:

1. **Mark Progress**: Use the checkboxes to track:
   - Prep Status: Not Started → In Progress → Complete
   - Content Ready: Check when content is finished
   - Published: Check when live

2. **Add Notes**: Click in the notes field to add:
   - Guest names
   - Topic ideas
   - Links to documents
   - Reminders

3. **Set Priorities**: Use the dropdown to mark:
   - High: Time-sensitive or important
   - Normal: Regular schedule
   - Low: Flexible timing

4. **Filter View**: Use sidebar to:
   - Jump to current week
   - View next 4 weeks
   - Filter by activity type
   - Show only pending items

## Your Weekly Schedule

| Day | Time | Activity | Format |
|-----|------|----------|--------|
| **Sunday** | 6:00 AM | AIVACEO Podcast | Audio Recording |
| **Sunday** | 2:00 PM | Promptology Tip | Video |
| **Monday** | 9-11 AM | Real Estate & AI | Clubhouse |
| **Tuesday** | 6-8 PM | AI Superheroes Class | Live Class |
| **Wednesday** | Flexible | AI Whiteboard | YouTube |
| **Thursday** | 9-10 AM | Sales Training | Internal |
| **Friday** | 12:00 PM | Futuristic Fridays | Live Stream |
| **Saturday** | Flexible | System Saturdays | Short Video |

## Pro Tips

- **Check daily**: Review upcoming week every Monday
- **Prep ahead**: Mark prep status 1 week in advance
- **Export often**: Download CSV backups weekly
- **Use notes**: Document guest names, topics, and links
- **Filter smart**: Use "Next 4 Weeks" view for planning

## Analyze Your Progress

Run the analysis script anytime:

```bash
python scripts/analyze_schedule.py
```

This shows:
- Completion statistics
- Activity breakdowns
- Upcoming schedule
- Priority distribution

## Need Help?

- CSV not found? Run `python scripts/generate_full_csv.py`
- App won't start? Check `pip install -r requirements.txt`
- Lost changes? Check for `schedule_2026.csv` backup files

---

**Ready to dominate 2026!** 🚀
