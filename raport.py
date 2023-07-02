import os
from month_data import generate_dates_records
from openpyxl import load_workbook

def load_template():
    return load_workbook(filename="template_raport.xlsx")

def fill_template(output_file_path: str, year: int, month_nr: int,
                  out_days: [],
                  project_name: str, contractor_name: str, nip:str,
                  position: str, client_name: str):
    workbook = load_template()

    time_records = generate_dates_records(year, month_nr, out_days)
    sheet = workbook.active

    sheet["B2"] = contractor_name
    sheet["B3"] = year
    sheet["B4"] = month_nr
    sheet["E2"] = nip
    sheet["H2"] = position
    sheet["H3"] = client_name

    target_file = output_file_path
    raport_details = {"working_hours": 0, "raport_file": target_file, "time_records": time_records}

    start_tmpl_row = 15
    for index, day_record in enumerate(time_records):
        row = str(start_tmpl_row + index)
        date = day_record["date"]

        is_workday = day_record["workday"]
        is_ooo = day_record["ooo"]
        is_holiday = day_record["holiday"]

        # date
        sheet["A" + row] = date.strftime("%d.%m.%Y")

        # day of week
        sheet["B" + row] = date.strftime("%A")

        # project name
        if is_workday:
            sheet["C" + row] = project_name
        else:
            sheet["C" + row] = ""

        # OOO or holiday bank
        if is_workday:
            if is_ooo:
                sheet["D" + row] = "out of office"
            elif is_holiday:
                sheet["D" + row] = "holiday bank"

        # hours
        if is_workday and not is_ooo and not is_holiday:
            raport_details["working_hours"] += 8
            sheet["F" + row] = 8
        else:
            sheet["F" + row] = 0

    workbook.save(filename=target_file)

    raport_details["raport_file_path"] = os.path.abspath(target_file)

    return raport_details