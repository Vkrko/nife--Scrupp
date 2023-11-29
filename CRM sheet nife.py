#!/usr/bin/env python
# coding: utf-8

# In[27]:


pip install --upgrade gspread


# In[2]:


pip install requests


# In[125]:


import gspread
import time


# In[12]:


gc = gspread.service_account(filename=r"C:\Users\91887\Downloads\task-1.json")


# In[130]:


spread_sheet = input("Enter the name of the spreadsheet:")
source_sheet= gc.open(spread_sheet)
sheet= source_sheet.sheet1


dest_sheet= gc.open("demo2").get_worksheet(0)
dest_sheet_1= gc.open("demo2").get_worksheet(1)

name = 'A'
linked_in = 'B'
indust = 'C'
educ = 'D'
curr_pos = 'E'
email = 'F'
pers_email = 'G'
num_of_conn = 'H'
location ='I'
website ='J'
phone_no ='K'
company_name = 'L'
company_link = 'M'
company_found = 'N'
company_size = 'O'
company_loc = 'P'
company_ind = 'Q'
annual_rev = 'R'
tech = 'S'
total_fun = 'T'


source_data = sheet.get_all_values()
dest_data = dest_sheet.get_all_values()

for row in range(2,len(source_data)):
    time.sleep(20)
    
    
    name_cell = sheet.acell(name+str(row)).value
    linked_in_cell = sheet.acell(linked_in+str(row)).value
    indust_cell = sheet.acell(indust+str(row)).value
    educ_cell = sheet.acell(educ+str(row)).value
    curr_pos_cell = sheet.acell(curr_pos+str(row)).value
    email_cell = sheet.acell(email+str(row)).value
    pers_email_cell = sheet.acell(pers_email+str(row)).value
    num_of_conn_cell = sheet.acell(num_of_conn+str(row)).value
    location_cell = sheet.acell(location+str(row)).value
    website_cell = sheet.acell(website+str(row)).value
    phone_no_cell = sheet.acell(phone_no+str(row)).value
    company_name_cell = sheet.acell(company_name+str(row)).value
    company_link_cell = sheet.acell(company_link+str(row)).value
    company_found_cell = sheet.acell(company_found+str(row)).value
    company_size_cell = sheet.acell(company_size+str(row)).value
    company_loc_cell = sheet.acell(company_loc+str(row)).value
    company_ind_cell = sheet.acell(company_ind+str(row)).value
    annual_rev_cell = sheet.acell(annual_rev+str(row)).value
    tech_cell = sheet.acell(tech+str(row)).value
    total_fun_cell = sheet.acell(total_fun+str(row)).value
    
    dest_array_org = [ company_name_cell,'','','','','',website_cell,company_link_cell,'','',company_loc_cell,indust_cell,
                      company_size_cell,annual_rev_cell,company_found_cell,'',tech_cell,'',total_fun_cell,pers_email_cell,company_ind_cell]
   
    print(dest_array_org)
    
    dest_array_cont = [name_cell,company_name_cell,'','','',curr_pos_cell,linked_in_cell,educ_cell,email_cell,phone_no_cell,
                       num_of_conn_cell,location_cell]


    dest_sheet.append_rows([dest_array_org])
    dest_sheet_1.append_rows([dest_array_cont])
    
   


# In[ ]:





# In[ ]:




