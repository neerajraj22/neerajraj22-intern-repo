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