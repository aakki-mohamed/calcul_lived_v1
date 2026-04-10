age = int(input('what\'s your age : '))
months = age *12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60 
seconds = minutes * 60
print(f'''You Lived For :
      {months} Months 
      {weeks:,} Weeks 
      {days:,} Days
      {hours:,} Hours 
      {minutes:,} Minutes 
      {seconds:,} Seconds''')