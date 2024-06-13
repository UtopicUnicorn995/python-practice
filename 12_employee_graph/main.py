import plotly.express as px
import pandas as pd

employees_df = pd.read_csv('employees.csv')


sorted_employee_df = employees_df.groupby(["Department"])['Salary'].mean().reset_index()


fig = px.bar(sorted_employee_df, x="Department", y="Salary",
             title="Average Salary by Department")
fig.show()
