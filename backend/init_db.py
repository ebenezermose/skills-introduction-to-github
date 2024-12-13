from project_alpha.app import create_app, db

# Create the app instance
app = create_app()

# Use the app context to initialize the database
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")