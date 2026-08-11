from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Employee
from app.forms import EmployeeForm

main = Blueprint("main", __name__)

@main.route("/")
def index():
    employee_count = Employee.query.count()
    return render_template("index.html", employee_count=employee_count)

@main.route("/health")
def health():
    return {"status": "healthy"}, 200

@main.route("/employees")
def employees():
    all_employees = Employee.query.order_by(Employee.full_name).all()
    return render_template("employees.html", employees=all_employees)

@main.route("/employees/add", methods=["GET", "POST"])
def add_employee():
    form = EmployeeForm()

    if form.validate_on_submit():
        employee = Employee(
            full_name=form.full_name.data,
            job_title=form.job_title.data,
            department=form.department.data,
            email=form.email.data,
            location=form.location.data,
        )

        db.session.add(employee)
        db.session.commit()

        flash("Employee added successfully.", "success")
        return redirect(url_for("main.employees"))

    return render_template("add_employee.html", form=form)

@main.route("/employees/<int:employee_id>/edit", methods=["GET", "POST"])
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    form = EmployeeForm(obj=employee)

    if form.validate_on_submit():
        employee.full_name = form.full_name.data
        employee.job_title = form.job_title.data
        employee.department = form.department.data
        employee.email = form.email.data
        employee.location = form.location.data

        db.session.commit()

        flash("Employee updated successfully.", "success")
        return redirect(url_for("main.employees"))

    return render_template("edit_employee.html", form=form, employee=employee)

@main.route("/employees/<int:employee_id>/delete", methods=["POST"])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)

    db.session.delete(employee)
    db.session.commit()

    flash("Employee deleted successfully.", "success")
    return redirect(url_for("main.employees"))
