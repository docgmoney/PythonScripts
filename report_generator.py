import datetime
import time
import os

def get_input(prompt):
    return input(prompt + ": ")

def get_multiline_input(prompt, end_sentinel='.'):
    print(f"{prompt} (Enter '{end_sentinel}' on a new line to finish):")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == end_sentinel:
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def create_report():
    report_name = get_input("Enter Report Name")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{report_name.replace(' ', '_')}_{timestamp.replace(':', '-').replace(' ', '_')}.txt"

    report_data = {
        "Executive Summary": get_multiline_input("Enter Executive Summary"),
        "Methodology": get_multiline_input("Enter Methodology"),
        "Findings": get_multiline_input("Enter Findings"),
        "Recommendations": get_multiline_input("Enter Recommendations"),
        "Appendices": get_multiline_input("Enter Appendices")
    }

    report = f"""
{report_name} - Penetration Testing Report
{'='* (len(report_name) + 29)}

Date: {timestamp}

Executive Summary:
{'-'*18}
{report_data['Executive Summary']}

Methodology:
{'-'*11}
{report_data['Methodology']}

Findings:
{'-'*8}
{report_data['Findings']}

Recommendations:
{'-'*15}
{report_data['Recommendations']}

Appendices:
{'-'*10}
{report_data['Appendices']}

"""

    with open(filename, 'w') as file:
        file.write(report)

    print(f"Report saved as {filename}")
    time.sleep(5)
    full_path = os.path.abspath(filename)
    print(f"The report was saved to: {full_path}")

if __name__ == "__main__":
    create_report()
