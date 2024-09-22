# Music Database Project

## Overview

This project is a **Music Database** built using **SQLAlchemy** ORM to manage relationships between **Bands**, **Concerts**, and **Venues**. The database stores information about bands, their concerts, and the venues they perform at. The models are designed to allow easy querying of data such as the most frequent band at a venue, whether a concert is in the band’s hometown, and more.

## Technologies Used

- **Python 3.10**
- **SQLAlchemy ORM**
- **SQLite** (Database)
- **Alembic** (for database migrations)

## Project Structure

```plaintext
├── lib
│   ├── alembic.ini
│   ├── migrations
│   │   ├── env.py
│   │   ├── __pycache__
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   ├── models.py  # SQLAlchemy models (Band, Venue, Concert)
│   ├── musicdata.db  # SQLite database file
│   ├── __pycache__
│   └── runfile.py  # Script to interact with the models
└── README.md  # This file


## Models

### Band
The **Band** model represents a musical band with the following attributes:

- `name`: Name of the band
- `hometown`: Hometown of the band

### Key Methods

- `play_in_venue(venue, date)`: Adds a concert at a specific venue on a given date.
- `all_introductions()`: Returns a list of all concert introductions.
- `most_performance()`: Returns the band with the most concerts.


### Concert
The **Concert** model represents a musical concert and links a band with a venue. It includes the following attributes:

- `name`: Name of the concert
- `date`: Date of the concert
- `band_id`: Foreign key to the band performing
- `venue_id`: Foreign key to the venue hosting

### Key Methods

- `hometown_show()`: Returns `True` if the concert is in the band's hometown, `False` otherwise.
- `introduction()`: Returns a string introduction for the band (e.g., "Hello, [city]! We are [band name] from [band hometown]").


### Venue
The **Venue** model represents a concert venue with the following attributes:

- `title`: Name of the venue
- `city`: City where the venue is located

### Key Methods

- `concert_on(date)`: Finds and returns the first concert on a given date at the venue.
- `most_frequent_band()`: Returns the band that has performed most frequently at the venue.


