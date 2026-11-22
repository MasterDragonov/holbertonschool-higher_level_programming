# app.py
from database import engine, Base, SessionLocal
from models import Project

def init_db():
    print("Creating tables in MySQL...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

def main():
    init_db()
    
    session = SessionLocal()
    
    try:
        print("\n--- Adding projects ---")
        proj1 = Project(title="Learn SQLAlchemy", status="In Progress")
        proj2 = Project(title="Build a Flask App", status="Not Started")
        
        session.add(proj1)
        session.add(proj2)
        
        session.commit()
        print("Successfully saved projects to MySQL!")
        
        print("\n--- Reading projects back out ---")
        all_projects = session.query(Project).all()
        for project in all_projects:
            print(project)
            
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()