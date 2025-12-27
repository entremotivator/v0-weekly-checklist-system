import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os

# Page config
st.set_page_config(
    page_title="2026 Content Schedule Tracker",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stExpander {
        background-color: #f8f9fa;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .activity-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin-bottom: 10px;
    }
    .priority-high {
        border-left-color: #f44336 !important;
    }
    .priority-normal {
        border-left-color: #2196F3 !important;
    }
    .priority-low {
        border-left-color: #9E9E9E !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize CSV file
CSV_FILE = "schedule_2026.csv"

def load_schedule():
    """Load schedule from CSV"""
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        st.error("⚠️ Schedule file not found! Please run: `python scripts/generate_2026_schedule.py`")
        st.stop()

def save_schedule(df):
    """Save schedule to CSV"""
    df.to_csv(CSV_FILE, index=False)

def get_week_status(week_df):
    """Calculate completion status for a week"""
    total = len(week_df)
    published = len(week_df[week_df["Published"] == "Yes"])
    content_ready = len(week_df[week_df["Content_Ready"] == "Yes"])
    prep_complete = len(week_df[week_df["Prep_Status"] == "Complete"])
    
    return {
        "total": total,
        "published": published,
        "content_ready": content_ready,
        "prep_complete": prep_complete
    }

# Load data
df = load_schedule()

# App header
st.title("📅 2026 Weekly Content Schedule Tracker")
st.markdown("**52-Week Checklist & Prep Execution System**")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Date range filter
min_date = pd.to_datetime(df["Date"]).min()
max_date = pd.to_datetime(df["Date"]).max()
current_date = datetime.now()

date_filter_option = st.sidebar.radio(
    "Date Range",
    ["Current Week", "Next 4 Weeks", "Custom Range", "All"]
)

if date_filter_option == "Current Week":
    week_num = ((current_date - min_date).days // 7) + 1
    selected_weeks = [week_num] if 1 <= week_num <= 52 else [1]
elif date_filter_option == "Next 4 Weeks":
    week_num = ((current_date - min_date).days // 7) + 1
    selected_weeks = [w for w in range(week_num, min(week_num + 4, 53))]
elif date_filter_option == "Custom Range":
    weeks = sorted(df["Week"].unique())
    selected_weeks = st.sidebar.multiselect(
        "Select Weeks",
        options=weeks,
        default=[1, 2, 3, 4]
    )
else:
    selected_weeks = sorted(df["Week"].unique())

# Activity filter
activities = ["All"] + sorted(df["Activity"].unique().tolist())
selected_activity = st.sidebar.selectbox("Filter by Activity", activities)

# Status filter
status_filter = st.sidebar.multiselect(
    "Status",
    ["Not Started", "In Progress", "Complete"],
    default=["Not Started", "In Progress", "Complete"]
)

# Priority filter
priority_filter = st.sidebar.multiselect(
    "Priority",
    ["High", "Normal", "Low"],
    default=["High", "Normal", "Low"]
)

# Apply filters
filtered_df = df.copy()

if selected_weeks:
    filtered_df = filtered_df[filtered_df["Week"].isin(selected_weeks)]

if selected_activity != "All":
    filtered_df = filtered_df[filtered_df["Activity"] == selected_activity]

if status_filter:
    filtered_df = filtered_df[filtered_df["Prep_Status"].isin(status_filter)]

if priority_filter:
    filtered_df = filtered_df[filtered_df["Priority"].isin(priority_filter)]

# Statistics
st.sidebar.header("📊 Overall Statistics")
total_tasks = len(df)
published_tasks = len(df[df["Published"] == "Yes"])
content_ready_tasks = len(df[df["Content_Ready"] == "Yes"])
completion_rate = (published_tasks / total_tasks * 100) if total_tasks > 0 else 0

col1, col2 = st.sidebar.columns(2)
col1.metric("Total", total_tasks)
col2.metric("Published", published_tasks)

col3, col4 = st.sidebar.columns(2)
col3.metric("Content Ready", content_ready_tasks)
col4.metric("Progress", f"{completion_rate:.0f}%")

st.sidebar.progress(completion_rate / 100)

# Weekly breakdown
st.sidebar.subheader("By Activity")
activity_stats = df.groupby("Activity")["Published"].apply(lambda x: (x == "Yes").sum()).sort_values(ascending=False)
for activity, count in activity_stats.items():
    st.sidebar.write(f"**{activity[:20]}**: {count}")

# Main content area
if len(filtered_df) == 0:
    st.warning("No activities found for the selected filters.")
else:
    # Summary cards
    st.subheader("📋 Filtered View Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    filtered_total = len(filtered_df)
    filtered_published = len(filtered_df[filtered_df["Published"] == "Yes"])
    filtered_ready = len(filtered_df[filtered_df["Content_Ready"] == "Yes"])
    filtered_prep = len(filtered_df[filtered_df["Prep_Status"] == "Complete"])
    
    col1.metric("Total Activities", filtered_total)
    col2.metric("Published", filtered_published, f"{(filtered_published/filtered_total*100):.0f}%" if filtered_total > 0 else "0%")
    col3.metric("Content Ready", filtered_ready, f"{(filtered_ready/filtered_total*100):.0f}%" if filtered_total > 0 else "0%")
    col4.metric("Prep Complete", filtered_prep, f"{(filtered_prep/filtered_total*100):.0f}%" if filtered_total > 0 else "0%")
    
    st.markdown("---")
    
    # Group by week
    for week in sorted(filtered_df["Week"].unique()):
        week_df = filtered_df[filtered_df["Week"] == week]
        week_stats = get_week_status(week_df)
        
        # Week header
        week_start = week_df.iloc[0]["Date"]
        week_end_date = pd.to_datetime(week_start) + timedelta(days=6)
        
        with st.expander(
            f"📆 Week {week} | {week_start} to {week_end_date.strftime('%Y-%m-%d')} | "
            f"Published: {week_stats['published']}/{week_stats['total']} | "
            f"Ready: {week_stats['content_ready']}/{week_stats['total']} | "
            f"Prepped: {week_stats['prep_complete']}/{week_stats['total']}",
            expanded=(week in (selected_weeks[:2] if isinstance(selected_weeks, list) else []))
        ):
            # Display each activity
            for idx, row in week_df.iterrows():
                # Activity card with priority styling
                priority_class = f"priority-{row['Priority'].lower()}"
                
                col1, col2, col3, col4, col5 = st.columns([1, 2.5, 1.5, 1.5, 2])
                
                with col1:
                    # Priority selector
                    priority = st.selectbox(
                        "Priority",
                        ["High", "Normal", "Low"],
                        index=["High", "Normal", "Low"].index(row["Priority"]),
                        key=f"priority_{idx}",
                        label_visibility="collapsed"
                    )
                    if priority != row["Priority"]:
                        df.at[idx, "Priority"] = priority
                        save_schedule(df)
                        st.rerun()
                
                with col2:
                    status_icon = "✅" if row["Published"] == "Yes" else "🔄" if row["Content_Ready"] == "Yes" else "📝"
                    st.markdown(f"**{status_icon} {row['Activity']}**")
                    st.caption(f"{row['Day']}, {row['Date']} | {row['Time']}")
                    st.caption(f"📍 {row['Platform']} | 📄 {row['Format']}")
                
                with col3:
                    # Prep Status
                    prep_status = st.selectbox(
                        "Prep",
                        ["Not Started", "In Progress", "Complete"],
                        index=["Not Started", "In Progress", "Complete"].index(row["Prep_Status"]),
                        key=f"prep_{idx}",
                        label_visibility="visible"
                    )
                    if prep_status != row["Prep_Status"]:
                        df.at[idx, "Prep_Status"] = prep_status
                        save_schedule(df)
                        st.rerun()
                
                with col4:
                    # Content Ready Checkbox
                    content_ready = st.checkbox(
                        "Content Ready",
                        value=(row["Content_Ready"] == "Yes"),
                        key=f"ready_{idx}"
                    )
                    if content_ready != (row["Content_Ready"] == "Yes"):
                        df.at[idx, "Content_Ready"] = "Yes" if content_ready else "No"
                        save_schedule(df)
                        st.rerun()
                    
                    # Published Checkbox
                    published = st.checkbox(
                        "Published",
                        value=(row["Published"] == "Yes"),
                        key=f"pub_{idx}"
                    )
                    if published != (row["Published"] == "Yes"):
                        df.at[idx, "Published"] = "Yes" if published else "No"
                        save_schedule(df)
                        st.rerun()
                
                with col5:
                    # Notes field
                    notes = st.text_area(
                        "Notes",
                        value=row["Notes"],
                        key=f"notes_{idx}",
                        placeholder="Add prep notes, links, ideas...",
                        height=80,
                        label_visibility="collapsed"
                    )
                    if notes != row["Notes"]:
                        df.at[idx, "Notes"] = notes
                        save_schedule(df)
                
                st.divider()

# Footer actions
st.markdown("---")
st.subheader("⚙️ Actions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔄 Reset All", type="secondary"):
        df["Prep_Status"] = "Not Started"
        df["Content_Ready"] = "No"
        df["Published"] = "No"
        df["Notes"] = ""
        save_schedule(df)
        st.success("✅ All data reset!")
        st.rerun()

with col2:
    if st.button("📥 Download CSV", type="primary"):
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="💾 Download Full Schedule",
            data=csv_data,
            file_name=f"content_schedule_2026_backup_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv"
        )

with col3:
    if st.button("📊 Export Report", type="secondary"):
        report = df.groupby("Activity").agg({
            "Published": lambda x: (x == "Yes").sum(),
            "Content_Ready": lambda x: (x == "Yes").sum(),
            "Week": "count"
        }).reset_index()
        report.columns = ["Activity", "Published", "Content Ready", "Total Scheduled"]
        report_csv = report.to_csv(index=False)
        st.download_button(
            label="📈 Download Activity Report",
            data=report_csv,
            file_name=f"activity_report_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

with col4:
    st.markdown(f"**Last Sync:** {datetime.now().strftime('%H:%M:%S')}")
    if st.button("♻️ Refresh"):
        st.rerun()
