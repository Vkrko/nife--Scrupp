# nife--Scrupp
copying data under specific column
import gspread
gc = gspread.service_account(filename=r"C:\Users\91887\Downloads\task-1.json")
source_sheet= gc.open("hr mum").sheet1
dest_sheet= gc.open("demo2").sheet2
source_sheet= gc.open("hr mum").sheet1
dest_sheet= gc.open("demo2").get_worksheet(1)

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


source_data = source_sheet.get_all_values()
dest_data = dest_sheet.get_all_values()

for row in range():
    
    
    name_cell = source_sheet.acell(name+str(row)).value
    linked_in_cell = source_sheet.acell(linked_in+str(row)).value
    indust_cell = source_sheet.acell(indust+str(row)).value
    educ_cell = source_sheet.acell(educ+str(row)).value
    curr_pos_cell = source_sheet.acell(curr_pos+str(row)).value
    email_cell = source_sheet.acell(email+str(row)).value
    pers_email_cell = source_sheet.acell(pers_email+str(row)).value
    num_of_conn_cell = source_sheet.acell(num_of_conn+str(row)).value
    location_cell = source_sheet.acell(location+str(row)).value
    website_cell = source_sheet.acell(website+str(row)).value
    phone_no_cell = source_sheet.acell(phone_no+str(row)).value
    company_name_cell = source_sheet.acell(company_name+str(row)).value
    company_link_cell = source_sheet.acell(company_link+str(row)).value
    company_found_cell = source_sheet.acell(company_found+str(row)).value
    company_size_cell = source_sheet.acell(company_size+str(row)).value
    company_loc_cell = source_sheet.acell(company_loc+str(row)).value
    company_ind_cell = source_sheet.acell(company_ind+str(row)).value
    annual_rev_cell = source_sheet.acell(annual_rev+str(row)).value
    tech_cell = source_sheet.acell(tech+str(row)).value
    total_fun_cell = source_sheet.acell(total_fun+str(row)).value
    
    dest_array_org = [ company_name_cell,'','','','','',website_cell,company_link_cell,'','',company_loc_cell,indust_cell,
                      company_size_cell,annual_rev_cell,company_found_cell,'',tech_cell,'',total_fun_cell,pers_email_cell,company_ind_cell]
   
    print(dest_array_org)
    
    for row in range():
    
    dest_array_cont = [name_cell,company_name_cell,'','','',curr_pos_cell,linked_in_cell,educ_cell,email_cell,phone_no_cell,
                       num_of_conn_cell,location_cell]


    dest_sheet.append_rows([dest_array_org])
    dest_sheet.append_rows([dest_array_cont])
