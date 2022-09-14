# Warmup

def sleep_in(weekday, vacation):
  return  not weekday or vacation
  
##

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

##

def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return a + b
