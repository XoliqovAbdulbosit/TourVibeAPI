# TourVibeAPI

TourVibeAPI is a Django-based REST API for a tourism and hospitality platform that provides information about destinations, hotels, restaurants, and foods. The API allows users to browse travel-related content, view ratings and reviews, and manage user profiles.

## Features

- Browse destinations with descriptions, history, and images
- Explore hotels with pricing and location information
- Discover restaurants with calorie information and reviews
- View food items categorized by region
- User registration, login, and profile management
- Rating and commenting system for all entities
- Filtering by categories, states, and locations

## Technologies Used

- Python 3.9
- Django 5.0
- SQLite (default database)
- JSON API responses

## Prerequisites

- Python 3.9
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd TourVibeAPI
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`

## API Endpoints

### Destinations

- `GET /destinations/` - Get all destinations
- `GET /destinations/categories/` - Get all destination categories
- `GET /destinations/states/` - Get all destination states
- `GET /destinations/<category>` - Get destinations by category
- `GET /destinations/state/<state>` - Get destinations by state
- `GET /destination/<id>` - Get destination by ID

### Hotels

- `GET /hotels/` - Get all hotels
- `GET /hotels/categories/` - Get all hotel categories (by country)
- `GET /hotels/<category>` - Get hotels by category
- `GET /hotel/<id>` - Get hotel by ID

### Restaurants

- `GET /restaurants/` - Get all restaurants
- `GET /restaurant/<id>` - Get restaurant by ID

### Foods

- `GET /foods/` - Get all foods
- `GET /foods/categories/` - Get all food categories
- `GET /foods/<category>` - Get foods by category
- `GET /food/<id>` - Get food by ID

### User Management

- `GET /login/<email>/<password>` - Login user
- `GET /register/<email>/<password>/<name>/<country>` - Register new user
- `GET /edit/<user_id>/<email>/<password>/<name>/<country>/<number>` - Edit user profile

### Comments and Ratings

- `POST /comment/<address>/<id>/<user>/<rating>` - Add a comment and rating to an entity

## Data Models

The API includes the following main models:

- **Destination**: Tourism destinations with images, descriptions, history, and location
- **Hotel**: Accommodation options with pricing and location
- **Restaurant**: Dining establishments with pricing and calorie information
- **Food**: Food items with descriptions and categorization
- **Profile**: User accounts with personal information
- **Comment**: User-generated reviews and ratings
- **Image**: Media associated with entities

## Project Structure

```
TourVibeAPI/
├── manage.py
├── TourVibeAPI/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── main/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you have any questions or issues, please open an issue in the repository.
