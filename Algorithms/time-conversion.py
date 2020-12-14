# Link: https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    hours = s.split(':')[0]
    if 'PM' in s:
        return s.replace("PM", "") if hours == '12' else (str(int(hours) + 12) + s[2:]).replace("PM", "")
    else:
        return (str(int(hours) - 12) + '0' + s[2:]).replace("AM", "") if hours == '12' else s.replace("AM", "")


print(timeConversion('07:05:45PM'))
print(timeConversion('01:00:00PM'))
print(timeConversion('09:30:00PM'))
print(timeConversion('11:59:59PM'))
print(timeConversion('12:30:30AM'))
print(timeConversion('01:45:00AM'))
print(timeConversion('07:45:45AM'))
print(timeConversion('12:45:54PM'))
