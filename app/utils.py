from datetime import datetime


def is_past_date(input_date):
    current_date = datetime.now().date()

    if isinstance(input_date, str):
        input_date = datetime.strptime(input_date, "%Y-%m-%d").date()  # Adjust the format as needed

    if input_date < current_date:
        return True
    else:
        return False
