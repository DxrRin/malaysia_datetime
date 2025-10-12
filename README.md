# malaysia_datetime

A small Python module to retrieve the current date and time in Malaysia (Kuala Lumpur) timezone. 

## Features

- Get the current Malaysia time as HH:MM.
- Get the current Malaysia date in full month format (e.g., 03 October 2025).
- Get the current Malaysia date in short month format (e.g., 03 Oct 2025).
- Get the current Malaysia date in numeric format (e.g., 03/10/2025).

## Installation

Clone the repository:

```bash
git clone https://github.com/DxrRin/malaysia_datetime.git
```

Install dependencies:

```bash
pip install pytz
```

## Usage

Import the functions from setting_time.py:

```python
from setting_time import (
    get_malaysia_time,
    get_malaysia_date_full,
    get_malaysia_date_short,
    get_malaysia_date_numeric
)

print("Malaysia Time:", get_malaysia_time())
print("Malaysia Date (Full Month):", get_malaysia_date_full())
print("Malaysia Date (Short Month):", get_malaysia_date_short())
print("Malaysia Date (Numeric):", get_malaysia_date_numeric())
```

## File Structure

```
malaysia_datetime/
├── setting_time.py
├── README.md
├── LICENSE
└── .gitignore

```
