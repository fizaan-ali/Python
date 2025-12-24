# dictionary comprehension -> create dictionary using an expression
#                   can replace for loops and certain lambda expression

# dictionary = {key : expression for (key,value) in iterable}

cities_in_F = {'Gujranwala' : 52, 'Lahore' : 21, 'Sialkot' : 56, 'Multan' : 45}

cities_in_C = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

print(cities_in_C)

# dictionary = {key : expression for (key,value) in iterable if conditional}

weatherr = {'Gujranwala' : 'snowing', 'Lahore' : 'drizzling', 'Sialkot' : 'sunny', 'Faisalabad' : 'snowing'}

#               key :  expression for key, value in {iterable} if value == '{some}'
sunny_weather = {city : weather for city, weather in weatherr.items() if weather == 'snowing'}
#sunny_weather = {key : value for (key,value) in weatherr.items if value == 'snowing'} # we can also write like this
print(sunny_weather)
# it's not mandatory to write only key, value you can write anything but it's suggestive

# dictionary = {key : (if/else) for (key,value) in iterable }

citiestemp = {'Gujranwala' : 52, 'Lahore' : 21, 'Sialkot' : 56, 'Multan' : 45}

cities = {key : ('WARM' if value > 50 else 'COLD') for key,value in citiestemp.items()}

print(cities)

# dictionary = {key : function(value) for (key,value) in iterable}

citiestemp = {'Gujranwala' : 52, 'Lahore' : 21, 'Sialkot' : 56, 'Multan' : 45}

def check_temp(value):
    return "Warm" if value >= 50 else "Cold"

check_tmp = lambda value : "Warm" if value >= 50 else "Cold"

cities = {key : check_temp(value) for (key,value) in citiestemp.items()} # using function 
cities = {key : check_tmp(value) for (key, value) in citiestemp.items()} # using lambda expression
print(cities)

# we can use either function or lambda 