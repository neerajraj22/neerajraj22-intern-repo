Tasks:

Clean Code Principles: Writing clean code is crucial to create software that is scalable and maintainable. The following priniciples helps to create clean code:

Simplicity: Write code that is clear, simple to understand and no complicated reasoning. Simple code is easier to test and expand.
Readability: Code that is easily comprehensible to another developer. Readability is influenced by descriptive labeling, a clear code organization, and consistent formatting.
Maintainability: Over time, it is simple to update, expand, or debug code that is maintained. Because of its organization, future developers can avoid creating new defects.
Consistency: Following style manuals, architectural patterns, and coding standards is a necessary part of consistency. The codebase has a consistent structure that facilitates collaboration and navigation.
Efficiency: Code that is efficient works well and isn't overly complicated. Try to make the code scalability better rather than over-optimization that adds unnecessary complexity to the design.
Messy code example:

var day = "monday";
var weather ="sunny";

let daytime = function(){
if(day == "monday"){
if(weather == "sunny"){
console.log(this is a good sunny monday);
}else if(weather == "cloud"){
console.log("this is a cloudy monday");
}else if(weather == "storm"){
console.log("this is a stormy monday")
}
}else if(day == "tuesday"){
if(weather == "sunny"){
console.log(this is a good sunny tuesday);
}else if(weather == "cloud"){
console.log("this is a cloudy tuesday");
}else if(weather == "storm"){
console.log("this is a stormy tuesday")
}
}else if(day == "wednesday"){
//other day of the week
}

}

daytime();

Cleanest code:

var day ;
var weather ;

weathers = {
sunny:"sunny",
cloud:"cloudy",
storm:"stormy"
}

let daytime = function(day, weather){
console.log(this is a good ${weathers[weather]} ${day} )
}

daytime("monday", "cloud");

Why it's difficult to read?

Poor naming.
Inconsistent formatting.
No proper comments.
Repetition.
Unclear logic flow.

Task 3:

Tasks:

Best practices for naming variables and functions:

Specific variable name.
Consistent naming conventions.
Functions which shows an action.
Avoid abbreviations.
Use Bollean prefixes.
Constants values should be clearly defined.
Clear name.
Code with unclear variable names:

for i in range(n):
for j in range(m):
for k in range(l):
temp_value = X[i][j][k] * 12.5
new_array[i][j][k] = temp_value + 150

Using clear variable names:

PIXEL_NORMALIZATION_FACTOR = 12.5
PIXEL_OFFSET_FACTOR = 150

for row_index in range(row_count):
for column_index in range(column_count):
for color_channel_index in range(color_channel_count):
normalized_pixel_value = (
original_pixel_array[row_index][column_index][color_channel_index]
* PIXEL_NORMALIZATION_FACTOR
)
transformed_pixel_array[row_index][column_index][color_channel_index] = (
normalized_pixel_value + PIXEL_OFFSET_FACTOR
)

Reflection:

Issues Can Arise from Poorly Named Variables:
Confusion, difficult to maintain, introduce errors and waste of time.

Refactoring Improve Code Readability:

By using clear function name, the code is more understandable.
Reduce the repetition of functions.
Better structure.

Small Focused functions:

Tasks:

Best practices for writing small, single-purpose functions: A descriptive name, single function use, short functions, comments and using parameters.

Why?

It brings clarity and makes it easy to understand.
It maintains the codebase and promotes design.
It is easy to debug the code and testing small functions.
An example of a long, complex function in an existing codebase:

def do_stuff(x, y):

return (lambda x, y: x * y)(x, y)
w = 5

h = 10

a = do_stuff(w, h)

print(f"The area is {a}")

Codebase using smaller functions:

def calculate_area_of_rectangle(width, height):

return width * height
area = calculate_area_of_rectangle(5, 10)

print(f"The area is {area}")

Refactoring improve the structure of the code:

Refactor makes the code more organized.
It improves the flexibility and scalability.
It avoids repetition.
It is easy to understand the code funciton calls.


Refactoring code for simplicity:

Tasks:

Refactoring techniques:

Use smaller functions and makes it more readable.
A purposeful name reflects readability.
Reduce unnecessary functions.
Splitting large functions inot small function.
Using combine related parameters.

Overly complicated code:

def get_host(self):
"""
Returns the HTTP Host header, with support for X-Forwarded-Host.
"""
try:
host = self.META['HTTP_X_FORWARDED_HOST']
if isinstance(host, str):
return host.split(',')[0]
except KeyError:
pass

try:
    host = self.META['HTTP_HOST']
    if isinstance(host, str):
        return host.split(':')[0]
except KeyError:
    raise DisallowedHost('Invalid HTTP_HOST header: %r' % self.META.get('HTTP_HOST'))

raise DisallowedHost('Invalid HTTP_HOST header: %r' % self.META.get('HTTP_HOST'))

Refactor:

def get_header_host(self, header_name):
"""
Helper function to extract the host from a header,
handling both X-Forwarded-Host and HTTP_HOST headers.
"""
host = self.META.get(header_name)
if host and isinstance(host, str):
return host.split(',')[0].split(':')[0]
return None

def get_host(self):
"""
Returns the HTTP Host header, with support for X-Forwarded-Host.
"""
host = self.get_header_host('HTTP_X_FORWARDED_HOST') or self.get_header_host('HTTP_HOST')

if host is None:
    raise DisallowedHost('Invalid HTTP_HOST header: %r' % self.META.get('HTTP_HOST'))

return host

The complex code used multiple try-except blocks which makes it harder to follow the flow of execution.
This function try-except is performing similar operations, which leads to code duplication.
The function used the DisallowedHost exception in two different places, which makes the error handling slightly harder to maintain.

Refactoring improved the code:

get_header_host is responsible for retrieving and processing the host header from META. get_host is now focused solely on combining the results of get_header_host and raising an exception.
The duplicated logic for processing HTTP_X_FORWARDED_HOST and HTTP_HOST has been moved into the helper function get_header_host.
The error handling (raising DisallowedHost) is now isolated in a single location, making it easier to manage.
