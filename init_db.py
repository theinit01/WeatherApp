from app import app, db

# Create application context
with app.app_context():
    # Create all tables
    db.create_all()