# Colorado Mountains API

A clean, modern Django REST Framework API for exploring and filtering Colorado mountain peaks, including fourteeners, elevation stats, routes, and geographic data. This project automatically seeds itself from a local CSV data catalog and offers a rich, searchable, and filterable endpoint.

## Features

- **Automated CSV Data Seeding**: Custom management command reads local mountain data and safely updates the SQLite database.
- **Dynamic Filter System**: Built-in interactive filters for matching ranges, difficulties, and elevation margins.
- **Fuzzy Name Search**: Quickly find peaks with partial text queries.
- **Sensible Elevation Defaults**: Automatically defaults to displaying high country peaks (13,000–15,000 ft) unless explicitly overridden.

---

## Technical Architecture & Flow

The API coordinates incoming HTTP client requests through Django REST Framework's router down to the serialized database objects:

```
[ Client Request ]
       │
       ▼
[ URL Router ] ───► [ MountainViewSet ] ───► [ MountainFilter ]
                              │                     │
                              ▼                     ▼
                    [ Mountain Model ] ◄──── [ Database (SQLite) ]
                              │
                              ▼
                    [ MountainSerializer ] ───► [ JSON Response ]
```

---

## Prerequisites

- Python 3.8+
- Git

## Getting Started

### 1. Clone & Set Up the Environment

First, clone this repository (or navigate to your root folder) and spin up a Python virtual environment:

```bash
# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install django djangorestframework django-filter
```

### 2. Run Database Migrations

Initialize your local database schema using Django's migration engine:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Seed Mountain Data from CSV

Ensure your source CSV is located at `data/mountains.csv`. Then, run the custom seeder command to import all the mountain rows into your database:

```bash
python manage.py load_mountains
```

### 4. Run the Development Server

Fire up the local server to start testing the endpoints:

```bash
python manage.py runserver
```

The interactive browsable API will now be available in your browser at:
`http://127.0.0.1:8000/api/mountains/`

## API Endpoints & Query Parameters

### Base URL

`GET /api/mountains/`

### Query Parameter Options

You can append standard query parameters to the URL to filter down your mountain listings precisely.

| Parameter           | Type      | Description                                                                    | Example                     |
| :------------------ | :-------- | :----------------------------------------------------------------------------- | :-------------------------- |
| **`is_fourteener`** | _Boolean_ | Filter by whether a peak is a 14er (`true` or `false`).                        | `?is_fourteener=true`       |
| **`range_name`**    | _String_  | Filter exactly by the specific name of a mountain range.                       | `?range_name=Sawatch Range` |
| **`difficulty`**    | _String_  | Filter exactly by the technical climbing route classification.                 | `?difficulty=Class 1`       |
| **`min_elevation`** | _Integer_ | Display peaks with an elevation greater than or equal to this value (in feet). | `?min_elevation=14000`      |
| **`max_elevation`** | _Integer_ | Display peaks with an elevation less than or equal to this value (in feet).    | `?max_elevation=14300`      |
| **`search`**        | _String_  | Performs a fuzzy text search on the mountain peak's name.                      | `?search=Elbert`            |

### Combined Query Example

To retrieve all **Class 1 Fourteeners** located in the **Sawatch Range**, you would chain the parameters together like this:

```http
GET [http://127.0.0.1:8000/api/mountains/?is_fourteener=true&difficulty=Class+1&range_name=Sawatch+Range](http://127.0.0.1:8000/api/mountains/?is_fourteener=true&difficulty=Class+1&range_name=Sawatch+Range)
```
