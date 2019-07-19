from datetime import datetime
from pytz import timezone
from os import path


def __get_current_date():
    central = timezone("America/Chicago")
    return central.localize(datetime.now())


def __get_date_as_string():
    date = __get_current_date()
    return date.strftime("%B %d, %Y")


def get_title():
    date_str = __get_date_as_string()
    return f"Free Talk Friday: {date_str}"


def get_body():
    filepath = path.join(path.dirname(path.abspath(__file__)), "post_body.md")
    infile = None
    try:
        infile = open(filepath, mode="r")
        return infile.read()
    except:
        return None
    finally:
        if infile is not None:
            infile.close()
