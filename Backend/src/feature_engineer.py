import pandas as pd

def featured_data():
    df=pd.read_csv('../database/Org_data/data.csv')
    df['text'] = (
    "Employee ID: " + df['employee_id'].astype(str) +
    ", Name: " + df['name'].astype(str) +
    ", Email: " + df['email'].astype(str) +
    ", Phone: " + df['phone'].astype(str) +
    ", Department: " + df['department'].astype(str) +
    ", Designation: " + df['designation'].astype(str) +
    ", Manager: " + df['manager'].astype(str) +
    ", Joining Date: " + df['joining_date'].astype(str) +
    ", Salary: " + df['salary'].astype(str) +
    ", Location: " + df['location'].astype(str) +
    ", Status: " + df['status'].astype(str) +
    ", Department Head: " + df['department_head'].astype(str) +
    ", Department Floor: " + df['department_floor'].astype(str) +
    ", Cabin Number: " + df['cabin_no'].astype(str) +
    ", Desk Number: " + df['desk_no'].astype(str) +
    ", Extension Number: " + df['extension_number'].astype(str) +
    ", Project Name: " + df['project_name'].astype(str) +
    ", Skills: " + df['skill_set'].astype(str) +
    ", Leave Balance: " + df['leave_balance'].astype(str) +
    ", Attendance Percentage: " + df['attendance_percentage'].astype(str) +
    ", Employment Type: " + df['employment_type'].astype(str) +
    ", Office Timing: " + df['office_timing'].astype(str) +
    ", Casual Leave: " + df['casual_leave'].astype(str) +
    ", Sick Leave: " + df['sick_leave'].astype(str) +
    ", Earned Leave: " + df['earned_leave'].astype(str) +
    ", Work From Home Policy: " + df['wfh_policy'].astype(str) +
    ", Salary Credit Date: " + df['salary_credit_date'].astype(str)
    )
    df = df.astype(str)
    return df,df['text']