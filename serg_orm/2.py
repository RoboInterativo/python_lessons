    from sqlalchemy.orm import sessionmaker

    # Create tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new user
    new_user = User(name="Alice", email="alice@example.com")
    session.add(new_user)
    session.commit()

    # Query users
    users = session.query(User).all()
    for user in users:
        print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")

    session.close()
