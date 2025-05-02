import re
def calendar_check(check_in,check_out):
    in_month_number=None
    out_month_number=None
    months={
        1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul",
        8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"
    }

    for month in range(1,13):
        if months[month] in check_in:
            in_month_number=str(month)

        if months[month] in check_out:
            out_month_number=str(month)

    in_day=int(re.search(r'\d+', check_in).group())
    check_in= f"{in_month_number}-{str(in_day).zfill(2)}"  #function to format the day in two digits

    out_day=int(re.search(r'\d+', check_out).group())
    check_out=f"{out_month_number}-{str(out_day).zfill(2)}"

    return check_in, check_out


