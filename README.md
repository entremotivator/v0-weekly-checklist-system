# 2026 Weekly Content Schedule Tracker

A comprehensive Streamlit-based checkbox system for tracking your 52-week content schedule throughout 2026 with full preparation and execution workflow management.

## Features

- ✅ **52-Week Complete Schedule**: All 416 activities mapped to specific 2026 dates
- 📅 **Smart Date Tracking**: Automatic calendar integration from Jan 4 - Dec 26, 2026
- 🔄 **Three-Stage Workflow**: Track Prep → Content Ready → Published
- ☑️ **Interactive Checkboxes**: Persistent state with auto-save to CSV
- 📝 **Rich Notes System**: Add prep notes, links, guest names, and ideas
- ⭐ **Priority Management**: Mark activities as High, Normal, or Low priority
- 🔍 **Advanced Filtering**: Filter by week, activity, status, priority, and date range
- 📊 **Real-Time Analytics**: Track completion rates and progress statistics
- 💾 **CSV Export**: Download schedule and activity reports
- 📈 **Analysis Tools**: Comprehensive schedule analysis script included

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Your 2026 Schedule

```bash
python scripts/generate_full_csv.py
```

This creates `schedule_2026.csv` with all 416 activities across 52 weeks.

### 3. Launch the Tracker

```bash
streamlit run app.py
```

Your browser will open at `http://localhost:8501`

## Weekly Schedule Overview

Your content repeats weekly throughout 2026:

- **Sunday**: AIVACEO Podcast (6 AM) + Promptology Tip (2 PM)
- **Monday**: Real Estate & AI on Clubhouse (9-11 AM)
- **Tuesday**: AI Superheroes Class (6-8 PM)
- **Wednesday**: AI Whiteboard Wednesday (YouTube - Flexible)
- **Thursday**: Sales Team Training (9-10 AM)
- **Friday**: Futuristic Fridays Live Stream (12 PM)
- **Saturday**: System Saturdays Video Tips (Flexible)

**Total**: 8 activities per week × 52 weeks = 416 total activities

## How to Use

### Track Your Progress

Each activity has three tracking stages:

1. **Prep Status**: Not Started → In Progress → Complete
2. **Content Ready**: Check when content is finalized
3. **Published**: Check when content goes live

### Set Priorities

Use the priority dropdown to organize your work:
- **High**: Time-sensitive, important deadlines
- **Normal**: Regular weekly schedule
- **Low**: Flexible, can be rescheduled

### Add Notes

Click in the notes field to document:
- Guest names and contact info
- Topic ideas and talking points
- Links to resources or documents
- Follow-up reminders

### Filter Your View

Use the sidebar to focus on what matters:
- **Current Week**: Jump to this week's activities
- **Next 4 Weeks**: Plan ahead
- **Custom Range**: Select specific weeks
- **By Activity**: Focus on one content type
- **By Status**: Show only pending or completed items

## Additional Tools

### Analyze Your Schedule

Get detailed insights anytime:

```bash
python scripts/analyze_schedule.py
```

This provides:
- Overall completion statistics
- Activity-by-activity breakdown
- Upcoming activities for the week
- Platform distribution
- Priority summary
- Prep status overview

### Example CSV

An example CSV (`schedule_2026_example.csv`) is included showing:
- Properly formatted entries
- Sample notes and priorities
- Different workflow stages
- How to structure your data

## Data Management

### Automatic Saving

All changes are automatically saved to `schedule_2026.csv` in real-time.

### Backups

Download CSV backups regularly:
1. Click "Download CSV" in the app
2. Saves as `content_schedule_2026_backup_YYYYMMDD_HHMM.csv`

### Reset Options

- **Reset All**: Clear all progress (use carefully!)
- **Export Report**: Download activity summary by type

## File Structure

```
.
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── QUICKSTART.md                   # 3-minute setup guide
├── schedule_2026.csv              # Your schedule data (generated)
├── schedule_2026_example.csv      # Example with sample data
└── scripts/
    ├── generate_2026_schedule.py  # Basic schedule generator
    ├── generate_full_csv.py       # Full schedule with demo data
    └── analyze_schedule.py        # Analysis and reporting tool
```

## Tips for Success

1. **Check Daily**: Review your week every Monday morning
2. **Prep Ahead**: Mark prep status 1-2 weeks in advance
3. **Use Priorities**: Focus on high-priority items first
4. **Document Everything**: Use notes for continuity
5. **Export Weekly**: Download backups every Friday
6. **Analyze Monthly**: Run analysis script at month-end

## Troubleshooting

**CSV not found?**
- Run: `python scripts/generate_full_csv.py`

**App won't start?**
- Check: `pip install -r requirements.txt`

**Changes not saving?**
- Verify `schedule_2026.csv` exists and is writable

**Need fresh start?**
- Delete `schedule_2026.csv` and regenerate

## Customization

### Modify Schedule

Edit `scripts/generate_full_csv.py` to change:
- Activity times
- Content formats
- Platform names
- Weekly structure

Then regenerate: `python scripts/generate_full_csv.py`

### Add More Activities

Add entries to the `weekly_schedule` list in the generator script.

### Change Start Date

Modify the `start_date` variable if you want a different first week.

## License

Free to use for your content scheduling needs!

---

**Ready to conquer 2026 content creation!** 🚀
