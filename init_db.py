# init_db.py
from app_rest import app,Book,db
from faker import Faker


# Create a Faker instance
fake = Faker()

with app.app_context():
    # Create the database tables
    db.create_all()

    # Generate 100 fake books
    for _ in range(100):
        book = Book(
            title=fake.catch_phrase(),
            poster=fake.image_url(),
            summary=fake.text(),
            is_available=fake.boolean(),
            author_name=fake.name(),
            author_country=fake.country()
        )
        db.session.add(book)

    # Commit the session to save the books
    db.session.commit()