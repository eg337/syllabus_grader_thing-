from openpyxl import Workbook
from tempfile import NamedTemporaryFile
from django.http import HttpResponse

def write_calc(grade_dict, deadline_dict, title):
    
    count_var = 0
    for key in grade_dict:
        print(str(count_var)+": "+str(key) + "\n")
        if key in deadline_dict:
            print("YEP")
        count_var += 1


    for key in grade_dict:
        print(str(key) + "\n")
        if grade_dict[key]['number'] == 0 or grade_dict[key]['number'] is None:
            grade_dict[key]['number'] = 1
        if key not in deadline_dict or len(deadline_dict[key]) == 0:
            print("CHECK KEY\n")
            print(key)
            print("\n")
            deadline_dict[key] = []
            for i in range(grade_dict[key]['number']):
                deadline_dict[key].append(dict())
                deadline_dict[key][-1]["deadline"] = "Nope"
        elif grade_dict[key]['number'] != len(deadline_dict[key]):
            grade_dict[key]['number'] = len(deadline_dict[key])
        
        
        
    COLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    row = 2
    categories = set()

    # Create a new workbook
    workbook = Workbook()

    # Get the active worksheet
    worksheet = workbook.active

    # Add data to cells
    worksheet['A1'] = 'Course'
    worksheet['B1'] = 'Name'
    worksheet['C1'] = 'Deadline'
    worksheet['D1'] = 'Category'
    worksheet['E1'] = 'Weight'
    worksheet['F1'] = 'Score'



    worksheet['H1'] = "Course"
    worksheet['I1'] = "Grade"

    print(deadline_dict)
    print(grade_dict)
    # grade_dict = grade_dict['grade weights']
    deadline = "PLACEHOLDER"
    for cat in grade_dict:
        percentage = ""
        count = 0
        if type(grade_dict[cat]['weight']) == type(" "):
            while grade_dict[cat]['weight'][count].isnumeric() or grade_dict[cat]['weight'][count].isnumeric() == ".":
                percentage += grade_dict[cat]['weight'][count]
                count += 1
                
        
            percentage = float(percentage)
            each = percentage/grade_dict[cat]['number']
            print(str(type(percentage) ) + "\n")
            print(str(type(grade_dict[cat]['number'])))
        else:
            each = grade_dict[cat]['weight']/grade_dict[cat]['number']
        
        print(cat)
        print(deadline_dict[cat])
        print("CHECK2")
        print(grade_dict[cat]['number'])
        print("CHECK3")
        for i in range(grade_dict[cat]['number']):
            worksheet['A' + str(row)] = title
            worksheet['B' + str(row)] = cat + " " + str(i)
            # print(deadline_dict[cat])
            print(i)
            print("len: " + str(len(deadline_dict[cat])))
            worksheet['C' + str(row)] = deadline_dict[cat][i]['deadline']
            worksheet['D' + str(row)] = cat
            worksheet['E' + str(row)] = each
            row += 1
        
    
    for i in range(2, row):
        worksheet["G" + str(i)] = "=E" + str(i) + "*F" + str(i)



    new_row = 2
    while worksheet["H"+str(new_row)].value is not None:
        print(worksheet["H"+str(new_row)])
        new_row += 1

    worksheet["H" + str(new_row)] = title

    worksheet["I" + str(new_row)] = "=SUM(G2:G" + str(row) + ")"




    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data.xlsx"'


    # with NamedTemporaryFile() as tmp:
    #         workbook.save(tmp.name)
    #         tmp.seek(0)
    #         stream = tmp.read()
        
    # return stream

    workbook.save(response)
    return response


