def add_time(start, duration, day=None):
  #returns the new day by adding a certain amount of days to another day
  #takes start day as text and the days to add as a number
  def dayconverter(day, daynumber):
    weekdays = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
    }
    for k,v in weekdays.items():
      #finds what number is associated with given day
      if v.lower() == day.lower():
        #adds days that have to be added to starting day
        daynumber += k
    #makes sure the number is between 0-6 even when weeks have passed
    if daynumber > 6:
      daynumber = (daynumber % 6) - ((daynumber-(daynumber%6))/6)
    return(weekdays[daynumber])
  #convert 24hour time to 12hour time
  def timeconverter(time):
    if time == 0:
      return(12, 'AM')
    elif time < 12:
      return(time, 'AM')
    elif time == 12:
      return(time, 'PM')
    elif time > 12:
      time -= 12
      return(time, 'PM')
  #take out the hours and minutes from start and duration
  dhours = int(duration.split(':')[0])
  dminutes = int(duration.split(':')[1])
  shours = int(start.split(':')[0])
  sminutes = int(start.split(':')[1][0:2])
  #converts 12hour time to 24hour time
  if start[-2:].lower() == 'pm':
    shours += 12
  ehours = shours + dhours
  eminutes = sminutes + dminutes
  #calculates if there's any excess minutes to convert to hours
  if eminutes >= 60:
    ehours += 1
    eminutes -= 60
  #calculate if there's any excess hours to convert to days
  if ehours >= 24:
    dayslater = (ehours-(ehours%24))/24
    ehours = ehours%24
  else:
    dayslater = 0
  if eminutes < 10:
    eminutes = f'0{eminutes}'
  time  = f'{timeconverter(ehours)[0]}:{eminutes} {timeconverter(ehours)[1]}'
  if day != None:
    time += f', {dayconverter(day, dayslater)}'
  if dayslater == 1:
    time += ' (next day)'
  elif dayslater > 1:
    time += f' ({int(dayslater)} days later)'
  return(time)