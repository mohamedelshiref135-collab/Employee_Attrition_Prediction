import pickle
import pandas as pd
import streamlit as st

data = pickle.load(open("employee_churn_data.sav", "rb"))
# st.title("Attertion of Employee")
# st.sidebar.header("feature selection")

st.set_page_config(page_title="Employee Attrition", layout="wide")

st.title("Employee Attrition Prediction")
st.subheader("Predict if an employee will leave the company")

st.write("Enter employee information below to get prediction.")

department = st.selectbox(
    "Choose Department",
    [ "sales","admin","engineering","finance","logistics","marketing","operations","retail","support"]
)

review=st.text_input("review")
projects=st.text_input("projects")

salary = st.selectbox(
    "Choose Salary",
    ["low", "medium", "high"])

tenure=st.text_input("tenure")
satisfaction=st.text_input("satisfaction")
bonus=st.text_input("bonus")
avg_hrs_month=st.text_input("avg_hrs_month")

df=pd.DataFrame({"department":[department],
                 
                 "review":[review],
                 "projects":[projects],
                 "salary":[salary],
                 "tenure":[tenure],
                 "satisfaction":[satisfaction],
                 "bonus":[bonus],
                 "avg_hrs_month":[avg_hrs_month]},index=[0])

con=st.button("confirm")

if con:
    result=data.predict(df)
    if result== 0:
         st.write("The Employee will be stay")
    else:
         st.write("The Employee will be leave")
        
    
        
   
#engineering	0	0.62561547511694	3	medium	7	0.5009926017746082	1	186.322470915312	yes
5
#sales	0	0.8622333627251975	4	medium	5	0.2843037148031055	0	180.51676862425472	yes

