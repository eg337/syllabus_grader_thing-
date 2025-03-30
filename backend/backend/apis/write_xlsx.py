from openpyxl import Workbook
from tempfile import NamedTemporaryFile

def write_calc(grade_dict, deadline_dict):
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

    title = grade_dict['course title']
    grade_dict = grade_dict['grade weights']
    deadline = "PLACEHOLDER"
    for cat in grade_dict:
        percentage = ""
        count = 0
        while grade_dict[cat]['weight'][count].isnumeric() or grade_dict[cat]['weight'][count].isnumeric() == ".":
            percentage.append(grade_dict[cat]['weight'][count])
            count += 1
        
        percentage = float(percentage)
        each = percentage/grade_dict[cat]['number']
        for i in range(grade_dict[cat]['number']):
            worksheet['A' + str(row)] = title
            worksheet['B' + str(row)] = cat + " " + str(i)
            worksheet['C' + str(row)] = deadline_dict[cat][i]['deadline']
            worksheet['D' + str(row)] = cat
            worksheet['E' + str(row)] = each
        
    

    with NamedTemporaryFile() as tmp:
            workbook.save(tmp.name)
            tmp.seek(0)
            stream = tmp.read()
        
    return stream


write_calc(0)