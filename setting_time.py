# setting_time.py
"""
setting_time.py

Get the current Malaysia date and time in various formats.

Dependencies:
- pytz
"""

from datetime import datetime
from pytz import timezone

def get_malaysia_datetime():
    """Return the current Malaysia datetime object"""
    tz = timezone("Asia/Kuala_Lumpur")
    return datetime.now(tz)

def get_malaysia_time():
    """Return the current Malaysia time as HH:MM"""
    now = get_malaysia_datetime()
    return now.strftime("%H:%M")

def get_malaysia_date_full():
    """Return the current Malaysia date with full month name, e.g., 03 October 2025"""
    now = get_malaysia_datetime()
    return now.strftime("%d %B %Y")

def get_malaysia_date_short():
    """Return the current Malaysia date with short month name, e.g., 03 Oct 2025"""
    now = get_malaysia_datetime()
    return now.strftime("%d %b %Y")

def get_malaysia_date_numeric():
    """Return the current Malaysia date in numeric format, e.g., 03/10/2025"""
    now = get_malaysia_datetime()
    return now.strftime("%d/%m/%Y")

def get_malaysia_now():
    """Return the current Malaysia datetime as a string"""
    time = get_malaysia_time()
    date = get_malaysia_date_short()
    return f"{time}, {date}"

# Optional: quick test if run directly
# You can remove or comment out this block if you just want to use the module in your projects
if __name__ == "__main__":
    print("Malaysia Time:", get_malaysia_time())
    print("Malaysia Date (Full Month):", get_malaysia_date_full())
    print("Malaysia Date (Short Month):", get_malaysia_date_short())
    print("Malaysia Date (Numeric):", get_malaysia_date_numeric())
    print("Malaysia Now:", get_malaysia_now())
