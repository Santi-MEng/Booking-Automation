import json
import os

def save_report(hotel_info):
    report_file = "data/hotel_report.json"

    if os.path.exists(report_file) and os.path.getsize(report_file) > 0:
        with open(report_file, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("Invalid JSON found in the report file. Starting a new report.")
                data = []
    else:
        data = []


    data.append(hotel_info)


    with open(report_file, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Report saved to {report_file}")