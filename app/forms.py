from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class EmployeeForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired(), Length(max=120)])
    job_title = StringField("Job Title", validators=[DataRequired(), Length(max=120)])
    department = StringField("Department", validators=[DataRequired(), Length(max=120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    location = StringField("Location", validators=[Length(max=120)])
    submit = SubmitField("Save Employee")
