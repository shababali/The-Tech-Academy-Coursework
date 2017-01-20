/*1. Write a JavaScript program to display the current day and time in 
the following format:
Sample Output : Today is : Friday. 
Current time is : 4 PM : 50 : 22 
*/

function Question1 () {

var today = new Date();  
var daysOfWeek = 
	["Sunday",
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday"]; // Array of days of the week (from 0-6).
var day = daysOfWeek[today.getDay()]; //Array output
  
var hours = today.getHours(); // Returns the hour (from 0-23). 
var minutes = today.getMinutes(); // Returns the minutes (from 0-59).
var seconds = today.getSeconds(); // Returns the seconds (from 0-59).
var meridiem = (hours >= 12)? " PM ":" AM ";
   
		hours = (hours >= 13)? hours - 13: hours; // Adjusting display to correct syntax. Javascript hour is 0-23. Code corrects hours to 1-12 digit format.  
		minutes = minutes < 10 ? '0'+minutes : minutes; // Adjusting display to correct output format. Javascript minutes is 0-59, and 0-9 expressed as single digit.  
		seconds = seconds < 10 ? '0'+seconds : seconds; // Adjusting display to correct output format. Javascript seconds is 0-59, and 0-9 expressed as single digit. 

if (hours===0 && minutes===0 && seconds===0)
meridiem=' Midnight'; 	
	
if (hours===12 && minutes===0 && seconds===0)
meridiem=' Noon';

var currentTime = (hours +' : ' + meridiem + ' : ' + minutes + ' : ' + seconds);

document.getElementById("Q1Day").textContent = day;
document.getElementById("Q1CurrentTime").textContent = currentTime;
}



/* 2. Write a JavaScript program to print the contents of the current window.
*/

function Question2 () {  
window.print(); // JavaScript method to print the contents of the current window. 
}  
 
 
 
/* 3. Write a JavaScript program to get the current date. Expected Output : 
mm-dd-yyyy, mm/dd/yyyy or dd-mm-yyyy, dd/mm/yyyy:
*/

function Question3 () {  
var today = new Date();  
var dd = today.getDate(); // Returns the day of the month (from 1-31). 
var mm = today.getMonth()+1; // Returns the month (from 0-11). Code corrects months to 1-12 digit format. 
var yyyy = today.getFullYear(); // Returns the year. 

	mm = mm < 10 ? '0'+mm : mm; // Adjusting display to correct syntax, 0-9 expressed as single digit. 
	dd = dd < 10 ? '0'+dd : dd; 

var today1 = mm+'-'+dd+'-'+yyyy;  
var today2 = mm+'/'+dd+'/'+yyyy;  
var today3 = dd+'-'+mm+'-'+yyyy;  
var today4 = dd+'/'+mm+'/'+yyyy;

document.getElementById("Q3CurrentDate").textContent = (today1 +"  ,  "+ today2 +"  ,  "+ today3 +"  ,  "+ today4);
}



/*4. Write a JavaScript program to find the area of a triangle where lengths of the 
three of its sides are 5, 6, 7. 
*/

function Question4 () {
var sideA = 5 
var sideB = 6
var sideC = 7
var semiPerimeter = (sideA + sideB + sideC)/2; 
var triangleArea =  Math.sqrt(semiPerimeter*((semiPerimeter-sideA)*(semiPerimeter-sideB)*(semiPerimeter-sideC)));  
//Heron's formula gives the area of a triangle by requiring no arbitrary choice of side as base or vertex as origin. 

document.getElementById("Q4AreaTriangle").textContent = (triangleArea);
}



/*5. Write a JavaScript program to rotate the string 'w3resource' in right direction by 
periodically removing one letter from the end of the string and attaching it to the front.
Great Solution by Dylan Dykes*/


function Question5(arg) {
    if (arg == 1) {
        startMarquee = setInterval( function() {
            var str = document.getElementById("Q5String").textContent;
            var arr = str.split('');
			 console.log(arr);
            var letter = arr.pop();
			 console.log(arr);
            arr.unshift(letter);
			 console.log(arr);
            document.getElementById("Q5String").textContent = "";
            for (var i = 0; i < str.length; i++) {
                document.getElementById("Q5String").textContent += arr[i];
            }
        }, 100)
    } else {
        clearInterval(startMarquee);
    }
}



/* 6. Write a JavaScript program to determine whether a given year is a leap year in the 
Gregorian calendar.*/

function Question6 () {
    var userInputYear = document.getElementById("Q6InputYear").value;
    if (userInputYear % 4 == 0 && userInputYear % 100 != 0) {
        document.getElementById("Q6YearResult").textContent = userInputYear + " is a Leap Year";
    } else if (userInputYear % 400 == 0 && userInputYear % 100 == 0) {
        document.getElementById("Q6YearResult").textContent = userInputYear + " is a Leap Year";
    } else {
        document.getElementById("Q6YearResult").textContent = userInputYear + " is not a Leap Year";
    }
}



//7. Write a JavaScript program to find which 1st January is being a Sunday between 2014 and 2050.

function Question7() {
	var span7 =[];
    for (var year = 2014; year <= 2050; year++) {
        var date = new Date(year, 0, 1);
        console.log(date.getDay());
        if (date.getDay() == 0) {
            span7.push(year);
            }
	}
	 document.getElementById("Q7Span").textContent = (span7 +" have 1st January being a Sunday");
}



/*8. Write a JavaScript program where the program takes a random integer between 1 to 10, the user is then prompted to 
input a guess number. If the user input matches with guess number, the program will display a message "Good Work" 
otherwise display a message "Not matched". 
*/

function Question8 () {
    var randomSystemNumber = Math.ceil((Math.random() * 10 )); 
	
	/* Math.random is a function used to get a floating-point, 
	pseudo-random number in the range [0,1) that is, 
	from 0 (inclusive) up to but not including (exclusive) 1.
	
	/Math.ceil - The Math.ceil() function returns the smallest 
	integer greater than or equal to a given number.
	
	/Math.floor - he Math.floor() function returns the largest 
	integer less than or equal to a given number. */
    
	var userGuess = document.getElementById("UserNumber").value;
    if (randomSystemNumber == userGuess) {
        document.getElementById("Q8NumberComparison").textContent = "Good Work";
    } else {
        document.getElementById("Q8NumberComparison").textContent = "Not matched. The random integer is "+ randomSystemNumber;
    }
}



/*9. Write a JavaScript program to calculate days left until next Christmas.*/

function Question9() {
    var today = new Date();
    var christmas = new Date(today.getFullYear(), 11, 25);
	todaySTD = today.getTime();
	christmasSTD = christmas.getTime();
    var diff = christmasSTD - todaySTD;
    if (diff < 0) { //For dates that are after between Christmas and New Years, the date difference results in negative day count.
        christmas = new Date(today.getFullYear() + 1, 11, 25);
		christmasSTD = christmas.getTime();
        diff = christmasSTD - todaySTD;
    }
	var oneday=1000*60*60*24; 
	//day = milliseconds*seconds*minutes*hours 
    var daysTillChristmas = Math.ceil((diff/oneday));
    document.getElementById("Q9DaysTillChristmasAnswer").textContent = (daysTillChristmas) + " days";
}
	

	
/* 10. Write a JavaScript program to calculate multiplication and division of two numbers (input from user). */
			
function Question10(operator) {
    var operand1 = document.getElementById("Operand1").value;
    var operand2 = document.getElementById("Operand2").value;
    if (operator == 1)
    {
        var result = operand1 * operand2;
        document.getElementById("Q10FunctionResult").textContent = result;
    } else if (operator == 2) {
        var result = operand1 / operand2;
        document.getElementById("Q10FunctionResult").textContent = result;
    } else { //redundant code because JavaScript returns NaN result.
		document.getElementById("Q10FunctionResult").textContent = "Incorrect input.";
	}
}




/* 11. Write a JavaScript program to convert temperatures to and from celsius, fahrenheit. 
[Formula : C/5 = (F-32)/9 [ where C = temperature in celsius and F = temperature in fahrenheit ] 
Expected Output : 
60°C is 140 °F 
45°F is 7.222222222222222°C 
*/

function Question11() {
    var C = document.getElementById("CTemp").checked;
    var F = document.getElementById("FTemp").checked;
    var degree = String.fromCharCode(parseInt("00B0", 16));
	var tempNew;
	if (C) {
		var tempC = document.getElementById("Temp").value;
        var tempF = tempC * (9 / 5) + 32;
        tempNew = tempF + degree + "F";
		document.getElementById("Q11Conversion").textContent = document.getElementById("Temp").value + degree + "C" + " = " + tempNew;
	} else if (F) {
        var tempF = document.getElementById("Temp").value;
        var tempC = (tempF - 32) * 5 / 9;
        tempNew = tempC + degree + "C";
		 document.getElementById("Q11Conversion").textContent = document.getElementById("Temp").value + degree + "F" + " = " + tempNew;
    } else {
        var tempNew = "Incorrect input.";
    }

   
}



/* 12. Write a JavaScript program to get the website URL (loading page). */

function Question12() {
    var url = window.location.protocol;
    url += window.location.host;
    url += window.location.pathname;
    document.getElementById("Q12WebsiteValue").textContent = url;
}














