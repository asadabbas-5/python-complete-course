# Lesson 19: DateTime Module

"""
This lesson covers:
- Working with dates and times
- Date and time formatting
- Timezone handling
- Date arithmetic and comparisons
- Parsing dates from strings
- Timedelta operations
- Calendar operations
- Practical date/time applications
"""

# 1. Basic Date and Time Operations
print("=== Basic Date and Time Operations ===")

from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
today = date.today()
current_time = datetime.now().time()

print(f"Current datetime: {now}")
print(f"Today's date: {today}")
print(f"Current time: {current_time}")

# Creating specific dates and times
specific_date = date(2024, 1, 15)
specific_time = time(14, 30, 0)  # 2:30 PM
specific_datetime = datetime(2024, 1, 15, 14, 30, 0)

print(f"Specific date: {specific_date}")
print(f"Specific time: {specific_time}")
print(f"Specific datetime: {specific_datetime}")

# 2. Date and Time Formatting
print("\n=== Date and Time Formatting ===")

# Format datetime objects
now = datetime.now()

# Common format codes
formats = {
    "Year": "%Y",           # 2024
    "Month": "%m",          # 01
    "Day": "%d",            # 15
    "Hour": "%H",           # 14 (24-hour)
    "Minute": "%M",         # 30
    "Second": "%S",         # 45
    "Weekday": "%A",        # Monday
    "Month name": "%B",     # January
    "AM/PM": "%p"          # AM/PM
}

print("Format examples:")
for desc, fmt in formats.items():
    print(f"{desc}: {now.strftime(fmt)}")

# Common date formats
common_formats = {
    "ISO format": "%Y-%m-%d",
    "US format": "%m/%d/%Y",
    "European format": "%d/%m/%Y",
    "Full datetime": "%Y-%m-%d %H:%M:%S",
    "Readable format": "%B %d, %Y at %I:%M %p"
}

print("\nCommon formats:")
for desc, fmt in common_formats.items():
    print(f"{desc}: {now.strftime(fmt)}")

# 3. Parsing Dates from Strings
print("\n=== Parsing Dates from Strings ===")

# Parse dates from strings
date_strings = [
    "2024-01-15",
    "01/15/2024",
    "15/01/2024",
    "January 15, 2024",
    "2024-01-15 14:30:00"
]

formats_to_try = [
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%d/%m/%Y",
    "%B %d, %Y",
    "%Y-%m-%d %H:%M:%S"
]

print("Parsing dates:")
for date_str in date_strings:
    for fmt in formats_to_try:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            print(f"'{date_str}' -> {parsed_date} (format: {fmt})")
            break
        except ValueError:
            continue

# 4. Date Arithmetic and Comparisons
print("\n=== Date Arithmetic and Comparisons ===")

# Date arithmetic
today = date.today()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
next_month = today + timedelta(days=30)

print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")
print(f"Next month: {next_month}")

# Date comparisons
dates = [date(2024, 1, 15), date(2024, 1, 20), date(2024, 1, 10)]
sorted_dates = sorted(dates)
print(f"Sorted dates: {sorted_dates}")

# Check if date is in range
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)
test_date = date(2024, 6, 15)

is_in_range = start_date <= test_date <= end_date
print(f"Is {test_date} in range {start_date} to {end_date}? {is_in_range}")

# 5. Timedelta Operations
print("\n=== Timedelta Operations ===")

# Creating timedelta objects
delta1 = timedelta(days=5, hours=3, minutes=30)
delta2 = timedelta(weeks=2, days=1)
delta3 = timedelta(hours=24)

print(f"Delta 1: {delta1}")
print(f"Delta 2: {delta2}")
print(f"Delta 3: {delta3}")

# Timedelta arithmetic
start_time = datetime(2024, 1, 15, 9, 0, 0)
end_time = start_time + delta1

print(f"Start time: {start_time}")
print(f"End time: {end_time}")

# Calculate difference
time_diff = end_time - start_time
print(f"Time difference: {time_diff}")
print(f"Total seconds: {time_diff.total_seconds()}")

# 6. Timezone Handling
print("\n=== Timezone Handling ===")

from datetime import timezone, timedelta

# UTC timezone
utc_now = datetime.now(timezone.utc)
print(f"UTC time: {utc_now}")

# Local timezone
local_now = datetime.now()
print(f"Local time: {local_now}")

# Custom timezone
custom_tz = timezone(timedelta(hours=5, minutes=30))  # UTC+5:30
custom_time = datetime.now(custom_tz)
print(f"Custom timezone (UTC+5:30): {custom_time}")

# Convert between timezones
utc_time = datetime.now(timezone.utc)
local_time = utc_time.astimezone()
print(f"UTC to local: {utc_time} -> {local_time}")

# 7. Calendar Operations
print("\n=== Calendar Operations ===")

import calendar

# Calendar information
year = 2024
month = 1

print(f"Calendar for {calendar.month_name[month]} {year}:")
print(calendar.month(year, month))

print(f"\nYear calendar for {year}:")
print(calendar.calendar(year))

# Calendar functions
print(f"Is {year} a leap year? {calendar.isleap(year)}")
print(f"Number of leap years between 2000 and 2024: {calendar.leapdays(2000, 2024)}")
print(f"Weekday of January 1, {year}: {calendar.weekday(year, 1, 1)}")

# 8. Working with Timestamps
print("\n=== Working with Timestamps ===")

import time

# Current timestamp
current_timestamp = time.time()
print(f"Current timestamp: {current_timestamp}")

# Convert timestamp to datetime
timestamp_datetime = datetime.fromtimestamp(current_timestamp)
print(f"Timestamp as datetime: {timestamp_datetime}")

# Convert datetime to timestamp
datetime_timestamp = timestamp_datetime.timestamp()
print(f"Datetime as timestamp: {datetime_timestamp}")

# Format timestamp
formatted_timestamp = datetime.fromtimestamp(current_timestamp).strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted timestamp: {formatted_timestamp}")

# 9. Date Range Generation
print("\n=== Date Range Generation ===")

def date_range(start_date, end_date, step=timedelta(days=1)):
    """Generate a range of dates"""
    current = start_date
    while current <= end_date:
        yield current
        current += step

# Generate dates for a week
start = date(2024, 1, 15)
end = date(2024, 1, 21)

print("Dates in range:")
for d in date_range(start, end):
    print(f"  {d} ({d.strftime('%A')})")

# Generate dates with custom step
print("\nEvery 3 days:")
for d in date_range(start, end, timedelta(days=3)):
    print(f"  {d}")

# 10. Business Days Calculation
print("\n=== Business Days Calculation ===")

def business_days_between(start_date, end_date):
    """Calculate business days between two dates"""
    current = start_date
    business_days = 0
    
    while current <= end_date:
        if current.weekday() < 5:  # Monday = 0, Sunday = 6
            business_days += 1
        current += timedelta(days=1)
    
    return business_days

def add_business_days(start_date, days):
    """Add business days to a date"""
    current = start_date
    added_days = 0
    
    while added_days < days:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Monday = 0, Sunday = 6
            added_days += 1
    
    return current

# Test business days
start = date(2024, 1, 15)  # Monday
end = date(2024, 1, 26)    # Friday

business_days = business_days_between(start, end)
print(f"Business days between {start} and {end}: {business_days}")

new_date = add_business_days(start, 5)
print(f"5 business days after {start}: {new_date}")

# 11. Age Calculation
print("\n=== Age Calculation ===")

def calculate_age(birth_date):
    """Calculate age from birth date"""
    today = date.today()
    age = today.year - birth_date.year
    
    # Adjust if birthday hasn't occurred this year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    return age

def days_until_birthday(birth_date):
    """Calculate days until next birthday"""
    today = date.today()
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    
    return (next_birthday - today).days

# Test age calculation
birth_date = date(1990, 5, 15)
age = calculate_age(birth_date)
days_until = days_until_birthday(birth_date)

print(f"Birth date: {birth_date}")
print(f"Current age: {age}")
print(f"Days until next birthday: {days_until}")

# 12. Practical Applications
print("\n=== Practical Applications ===")

# Application 1: Log File Analysis
class LogAnalyzer:
    """Analyze log files with timestamps"""
    
    def __init__(self):
        self.logs = []
    
    def add_log(self, timestamp_str, message):
        """Add a log entry"""
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            self.logs.append((timestamp, message))
        except ValueError:
            print(f"Invalid timestamp format: {timestamp_str}")
    
    def get_logs_by_date(self, target_date):
        """Get logs for a specific date"""
        return [log for log in self.logs if log[0].date() == target_date]
    
    def get_logs_in_range(self, start_time, end_time):
        """Get logs in a time range"""
        return [log for log in self.logs if start_time <= log[0] <= end_time]
    
    def get_recent_logs(self, hours=24):
        """Get logs from the last N hours"""
        cutoff = datetime.now() - timedelta(hours=hours)
        return [log for log in self.logs if log[0] >= cutoff]

# Test log analyzer
analyzer = LogAnalyzer()
analyzer.add_log("2024-01-15 10:00:00", "Application started")
analyzer.add_log("2024-01-15 10:05:00", "User logged in")
analyzer.add_log("2024-01-15 10:10:00", "Database connection established")
analyzer.add_log("2024-01-15 11:00:00", "User logged out")

target_date = date(2024, 1, 15)
logs_today = analyzer.get_logs_by_date(target_date)
print(f"Logs for {target_date}: {len(logs_today)}")

# Application 2: Event Scheduler
class EventScheduler:
    """Simple event scheduler"""
    
    def __init__(self):
        self.events = []
    
    def add_event(self, name, start_time, duration_hours=1):
        """Add an event"""
        end_time = start_time + timedelta(hours=duration_hours)
        self.events.append({
            'name': name,
            'start': start_time,
            'end': end_time,
            'duration': duration_hours
        })
    
    def get_events_on_date(self, target_date):
        """Get events on a specific date"""
        return [event for event in self.events if event['start'].date() == target_date]
    
    def get_conflicting_events(self, start_time, duration_hours):
        """Check for conflicting events"""
        end_time = start_time + timedelta(hours=duration_hours)
        conflicts = []
        
        for event in self.events:
            if (start_time < event['end'] and end_time > event['start']):
                conflicts.append(event)
        
        return conflicts
    
    def get_upcoming_events(self, days=7):
        """Get upcoming events in the next N days"""
        cutoff = datetime.now() + timedelta(days=days)
        return [event for event in self.events if event['start'] <= cutoff and event['start'] >= datetime.now()]

# Test event scheduler
scheduler = EventScheduler()
scheduler.add_event("Meeting", datetime(2024, 1, 15, 14, 0, 0), 2)
scheduler.add_event("Lunch", datetime(2024, 1, 15, 12, 0, 0), 1)
scheduler.add_event("Presentation", datetime(2024, 1, 16, 10, 0, 0), 3)

target_date = date(2024, 1, 15)
events_today = scheduler.get_events_on_date(target_date)
print(f"Events on {target_date}: {len(events_today)}")

# Application 3: Data Backup Scheduler
class BackupScheduler:
    """Schedule data backups"""
    
    def __init__(self):
        self.backups = []
    
    def schedule_backup(self, name, frequency_days=7):
        """Schedule a backup"""
        last_backup = datetime.now() - timedelta(days=frequency_days)
        next_backup = last_backup + timedelta(days=frequency_days)
        
        self.backups.append({
            'name': name,
            'frequency_days': frequency_days,
            'last_backup': last_backup,
            'next_backup': next_backup
        })
    
    def get_due_backups(self):
        """Get backups that are due"""
        now = datetime.now()
        return [backup for backup in self.backups if backup['next_backup'] <= now]
    
    def get_backup_schedule(self, days=30):
        """Get backup schedule for the next N days"""
        end_date = datetime.now() + timedelta(days=days)
        schedule = []
        
        for backup in self.backups:
            current = backup['next_backup']
            while current <= end_date:
                schedule.append({
                    'name': backup['name'],
                    'date': current
                })
                current += timedelta(days=backup['frequency_days'])
        
        return sorted(schedule, key=lambda x: x['date'])

# Test backup scheduler
backup_scheduler = BackupScheduler()
backup_scheduler.schedule_backup("Database", 7)
backup_scheduler.schedule_backup("Files", 3)
backup_scheduler.schedule_backup("System", 14)

due_backups = backup_scheduler.get_due_backups()
print(f"Due backups: {len(due_backups)}")

schedule = backup_scheduler.get_backup_schedule(14)
print(f"Backup schedule (next 14 days): {len(schedule)}")

# 13. Best Practices
print("\n=== Best Practices ===")

# Best Practice 1: Always use timezone-aware datetime objects
utc_now = datetime.now(timezone.utc)
print(f"UTC time: {utc_now}")

# Best Practice 2: Use date objects for date-only operations
today = date.today()
print(f"Today: {today}")

# Best Practice 3: Use timedelta for date arithmetic
tomorrow = today + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# Best Practice 4: Handle timezone conversions properly
def convert_timezone(dt, target_tz):
    """Convert datetime to target timezone"""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(target_tz)

# Best Practice 5: Use appropriate date formats
def format_date_for_api(dt):
    """Format date for API consumption"""
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def format_date_for_display(dt):
    """Format date for user display"""
    return dt.strftime("%B %d, %Y at %I:%M %p")

# Exercises:
"""
1. Create a function that calculates the number of days between two dates
2. Write a function that finds the next occurrence of a specific weekday
3. Create a function that formats a datetime object in multiple formats
4. Write a function that calculates the age in years, months, and days
5. Create a function that generates a list of all Mondays in a given month
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Days between dates
print("Exercise 1: Days Between Dates")
def days_between(date1, date2):
    return abs((date2 - date1).days)

date1 = date(2024, 1, 15)
date2 = date(2024, 2, 15)
days = days_between(date1, date2)
print(f"Days between {date1} and {date2}: {days}")

# 2. Next occurrence of weekday
print("\nExercise 2: Next Weekday")
def next_weekday(target_date, weekday):
    """Find next occurrence of weekday (0=Monday, 6=Sunday)"""
    days_ahead = weekday - target_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return target_date + timedelta(days=days_ahead)

today = date.today()
next_monday = next_weekday(today, 0)
print(f"Next Monday after {today}: {next_monday}")

# 3. Multiple date formats
print("\nExercise 3: Multiple Date Formats")
def format_datetime_multiple(dt):
    formats = {
        "ISO": dt.strftime("%Y-%m-%dT%H:%M:%S"),
        "US": dt.strftime("%m/%d/%Y %I:%M %p"),
        "European": dt.strftime("%d/%m/%Y %H:%M"),
        "Readable": dt.strftime("%A, %B %d, %Y at %I:%M %p")
    }
    return formats

now = datetime.now()
formats = format_datetime_multiple(now)
for fmt_name, fmt_value in formats.items():
    print(f"{fmt_name}: {fmt_value}")

# 4. Age in years, months, days
print("\nExercise 4: Detailed Age Calculation")
def detailed_age(birth_date):
    today = date.today()
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        months -= 1
        days += 30  # Approximate
    
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

birth_date = date(1990, 5, 15)
years, months, days = detailed_age(birth_date)
print(f"Age: {years} years, {months} months, {days} days")

# 5. All Mondays in a month
print("\nExercise 5: All Mondays in a Month")
def mondays_in_month(year, month):
    mondays = []
    first_day = date(year, month, 1)
    
    # Find first Monday
    first_monday = next_weekday(first_day, 0)
    
    # Add all Mondays in the month
    current = first_monday
    while current.month == month:
        mondays.append(current)
        current += timedelta(days=7)
    
    return mondays

year = 2024
month = 1
mondays = mondays_in_month(year, month)
print(f"Mondays in {calendar.month_name[month]} {year}:")
for monday in mondays:
    print(f"  {monday}")

print("\n🎉 Congratulations! You've completed Lesson 19!")
print("Next: Lesson 20 - Regular Expressions")
