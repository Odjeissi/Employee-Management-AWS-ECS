from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    job_title = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f"<Employee {self.full_name}>"
