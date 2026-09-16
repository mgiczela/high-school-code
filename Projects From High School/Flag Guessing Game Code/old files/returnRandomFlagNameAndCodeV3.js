const countries = [
    { code: "af", name: "Afghanistan" },
    { code: "ax", name: "Aland Islands" },
    { code: "al", name: "Albania" },
    { code: "dz", name: "Algeria" },
    { code: "as", name: "American Samoa" },
    { code: "ad", name: "Andorra" },
    { code: "ao", name: "Angola" },
    { code: "ai", name: "Anguilla" },
    { code: "aq", name: "Antarctica" },
    { code: "ag", name: "Antigua and Barbuda" },
    { code: "ar", name: "Argentina" },
    { code: "am", name: "Armenia" },
    { code: "aw", name: "Aruba" },
    { code: "au", name: "Australia" },
    { code: "at", name: "Austria" },
    { code: "az", name: "Azerbaijan" },
    { code: "bs", name: "Bahamas" },
    { code: "bh", name: "Bahrain" },
    { code: "bd", name: "Bangladesh" },
    { code: "bb", name: "Barbados" },
    { code: "by", name: "Belarus" },
    { code: "be", name: "Belgium" },
    { code: "bz", name: "Belize" },
    { code: "bj", name: "Benin" },
    { code: "bm", name: "Bermuda" },
    { code: "bt", name: "Bhutan" },
    { code: "bo", name: "Bolivia" },
    { code: "bq", name: "Bonaire" },
    { code: "ba", name: "Bosnia and Herzegovina" },
    { code: "bw", name: "Botswana" },
    { code: "br", name: "Brazil" },
    { code: "io", name: "British Indian Ocean Territory" },
    { code: "bn", name: "Brunei" },
    { code: "bg", name: "Bulgaria" },
    { code: "bf", name: "Burkina Faso" },
    { code: "bi", name: "Burundi" },
    { code: "kh", name: "Cambodia" },
    { code: "cm", name: "Cameroon" },
    { code: "ca", name: "Canada" },
    { code: "cv", name: "Cape Verde" },
    { code: "ky", name: "Cayman Islands" },
    { code: "cf", name: "Central African Republic" },
    { code: "td", name: "Chad" },
    { code: "cl", name: "Chile" },
    { code: "cn", name: "China" },
    { code: "cx", name: "Christmas Island" },
    { code: "cc", name: "Cocos Islands" },
    { code: "co", name: "Colombia" },
    { code: "km", name: "Comoros" },
    { code: "ck", name: "Cook Islands" },
    { code: "cr", name: "Costa Rica" },
    { code: "hr", name: "Croatia" },
    { code: "cu", name: "Cuba" },
    { code: "cw", name: "Curacao" },
    { code: "cz", name: "Czech Republic" },
    { code: "cd", name: "Democratic Republic of the Congo" },
    { code: "dk", name: "Denmark" },
    { code: "dj", name: "Djibouti" },
    { code: "dm", name: "Dominica" },
    { code: "do", name: "Dominican Republic" },
    { code: "ec", name: "Ecuador" },
    { code: "eg", name: "Egypt" },
    { code: "sv", name: "El Salvador" },
    { code: "gq", name: "Equatorial Guinea" },
    { code: "er", name: "Eritrea" },
    { code: "ee", name: "Estonia" },
    { code: "sz", name: "Eswatini" },
    { code: "et", name: "Ethiopia" },
    { code: "fk", name: "Falkland Islands" },
    { code: "fo", name: "Faroe Islands" },
    { code: "fj", name: "Fiji" },
    { code: "fi", name: "Finland" },
    { code: "fr", name: "France" },
    { code: "gf", name: "French Guiana" },
    { code: "pf", name: "French Polynesia" },
    { code: "tf", name: "French Southern Territories" },
    { code: "ga", name: "Gabon" },
    { code: "gm", name: "Gambia" },
    { code: "ge", name: "Georgia" },
    { code: "de", name: "Germany" },
    { code: "gh", name: "Ghana" },
    { code: "gi", name: "Gibraltar" },
    { code: "gr", name: "Greece" },
    { code: "gl", name: "Greenland" },
    { code: "gd", name: "Grenada" },
    { code: "gp", name: "Guadeloupe" },
    { code: "gu", name: "Guam" },
    { code: "gt", name: "Guatemala" },
    { code: "gg", name: "Guernsey" },
    { code: "gn", name: "Guinea" },
    { code: "gw", name: "Guinea-Bissau" },
    { code: "gy", name: "Guyana" },
    { code: "ht", name: "Haiti" },
    { code: "hk", name: "Hong Kong" },
    { code: "hn", name: "Honduras" },
    { code: "hu", name: "Hungary" },
    { code: "is", name: "Iceland" },
    { code: "in", name: "India" },
    { code: "id", name: "Indonesia" },
    { code: "ir", name: "Iran" },
    { code: "iq", name: "Iraq" },
    { code: "ie", name: "Ireland" },
    { code: "im", name: "Isle of Man" },
    { code: "il", name: "Israel" },
    { code: "it", name: "Italy" },
    { code: "ci", name: "Ivory Coast" },
    { code: "jm", name: "Jamaica" },
    { code: "jp", name: "Japan" },
    { code: "je", name: "Jersey" },
    { code: "jo", name: "Jordan" },
    { code: "kz", name: "Kazakhstan" },
    { code: "ke", name: "Kenya" },
    { code: "ki", name: "Kiribati" },
    { code: "kw", name: "Kuwait" },
    { code: "kg", name: "Kyrgyzstan" },
    { code: "la", name: "Laos" },
    { code: "lv", name: "Latvia" },
    { code: "lb", name: "Lebanon" },
    { code: "ls", name: "Lesotho" },
    { code: "lr", name: "Liberia" },
    { code: "ly", name: "Libya" },
    { code: "li", name: "Liechtenstein" },
    { code: "lt", name: "Lithuania" },
    { code: "lu", name: "Luxembourg" },
    { code: "mo", name: "Macao" },
    { code: "mg", name: "Madagascar" },
    { code: "mw", name: "Malawi" },
    { code: "my", name: "Malaysia" },
    { code: "mv", name: "Maldives" },
    { code: "ml", name: "Mali" },
    { code: "mt", name: "Malta" },
    { code: "mh", name: "Marshall Islands" },
    { code: "mq", name: "Martinique" },
    { code: "mr", name: "Mauritania" },
    { code: "mu", name: "Mauritius" },
    { code: "yt", name: "Mayotte" },
    { code: "mx", name: "Mexico" },
    { code: "fm", name: "Micronesia" },
    { code: "md", name: "Moldova" },
    { code: "mc", name: "Monaco" },
    { code: "mn", name: "Mongolia" },
    { code: "me", name: "Montenegro" },
    { code: "ms", name: "Montserrat" },
    { code: "ma", name: "Morocco" },
    { code: "mz", name: "Mozambique" },
    { code: "mm", name: "Myanmar" },
    { code: "na", name: "Namibia" },
    { code: "nr", name: "Nauru" },
    { code: "np", name: "Nepal" },
    { code: "nl", name: "Netherlands" },
    { code: "nc", name: "New Caledonia" },
    { code: "nz", name: "New Zealand" },
    { code: "ni", name: "Nicaragua" },
    { code: "ne", name: "Niger" },
    { code: "ng", name: "Nigeria" },
    { code: "nu", name: "Niue" },
    { code: "nf", name: "Norfolk Island" },
    { code: "kp", name: "North Korea" },
    { code: "mk", name: "North Macedonia" },
    { code: "mp", name: "Northern Mariana Islands" },
    { code: "no", name: "Norway" },
    { code: "om", name: "Oman" },
    { code: "pk", name: "Pakistan" },
    { code: "pw", name: "Palau" },
    { code: "ps", name: "Palestine" },
    { code: "pa", name: "Panama" },
    { code: "pg", name: "Papua New Guinea" },
    { code: "py", name: "Paraguay" },
    { code: "pe", name: "Peru" },
    { code: "ph", name: "Philippines" },
    { code: "pn", name: "Pitcairn" },
    { code: "pl", name: "Poland" },
    { code: "pt", name: "Portugal" },
    { code: "pr", name: "Puerto Rico" },
    { code: "qa", name: "Qatar" },
    { code: "cg", name: "Republic of the Congo" },
    { code: "re", name: "Reunion" },
    { code: "ro", name: "Romania" },
    { code: "ru", name: "Russia" },
    { code: "rw", name: "Rwanda" },
    { code: "bl", name: "Saint Barthelemy" },
    { code: "sh", name: "Saint Helena" },
    { code: "kn", name: "Saint Kitts and Nevis" },
    { code: "lc", name: "Saint Lucia" },
    { code: "pm", name: "Saint Pierre and Miquelon" },
    { code: "vc", name: "Saint Vincent and the Grenadines" },
    { code: "ws", name: "Samoa" },
    { code: "sm", name: "San Marino" },
    { code: "st", name: "Sao Tome and Principe" },
    { code: "sa", name: "Saudi Arabia" },
    { code: "sn", name: "Senegal" },
    { code: "rs", name: "Serbia" },
    { code: "sc", name: "Seychelles" },
    { code: "sl", name: "Sierra Leone" },
    { code: "sg", name: "Singapore" },
    { code: "sx", name: "Sint Maarten" },
    { code: "sk", name: "Slovakia" },
    { code: "si", name: "Slovenia" },
    { code: "sb", name: "Solomon Islands" },
    { code: "so", name: "Somalia" },
    { code: "za", name: "South Africa" },
    { code: "gs", name: "South Georgia and the South Sandwich Islands" },
    { code: "kr", name: "South Korea" },
    { code: "ss", name: "South Sudan" },
    { code: "es", name: "Spain" },
    { code: "lk", name: "Sri Lanka" },
    { code: "sd", name: "Sudan" },
    { code: "sr", name: "Suriname" },
    { code: "se", name: "Sweden" },
    { code: "ch", name: "Switzerland" },
    { code: "sy", name: "Syria" },
    { code: "tw", name: "Taiwan" },
    { code: "tj", name: "Tajikistan" },
    { code: "tz", name: "Tanzania" },
    { code: "th", name: "Thailand" },
    { code: "tl", name: "Timor-Leste" },
    { code: "tg", name: "Togo" },
    { code: "tk", name: "Tokelau" },
    { code: "to", name: "Tonga" },
    { code: "tt", name: "Trinidad and Tobago" },
    { code: "tn", name: "Tunisia" },
    { code: "tr", name: "Turkey" },
    { code: "tm", name: "Turkmenistan" },
    { code: "tc", name: "Turks and Caicos Islands" },
    { code: "tv", name: "Tuvalu" },
    { code: "ug", name: "Uganda" },
    { code: "ua", name: "Ukraine" },
    { code: "ae", name: "United Arab Emirates" },
    { code: "gb", name: "United Kingdom" },
    { code: "us", name: "United States" },
    { code: "uy", name: "Uruguay" },
    { code: "uz", name: "Uzbekistan" },
    { code: "vu", name: "Vanuatu" },
    { code: "va", name: "Vatican City" },
    { code: "ve", name: "Venezuela" },
    { code: "vn", name: "Vietnam" },
    { code: "vg", name: "British Virgin Islands" },
    { code: "vi", name: "U.S. Virgin Islands" },
    { code: "wf", name: "Wallis and Futuna" },
    { code: "eh", name: "Western Sahara" },
    { code: "ye", name: "Yemen" },
    { code: "zm", name: "Zambia" },
    { code: "zw", name: "Zimbabwe" }
];
// that thing above
// is a list of objects, each one has 2 atributes, teh code and name
// javascript allows you to just add it into list and it will know
//each object seperated by {}, has a code and a name




// google says that server is needed to read from txt file
// for javascript so i feel liek this is better


//countries[random #] gives us a random country


//make a randNum function cuz its annoying and not as intuitive(like in java)
function randNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let recentCountriesQueue = [];//make an array w q funcitonality cuz not built in one
const HOW_MANY_RECENTS_TO_AVOID = 5;

function addToRecentsQueue(country)
{
    recentCountriesQueue.push(country)
    if (recentCountriesQueue.length > HOW_MANY_RECENTS_TO_AVOID)
    {
        recentCountriesQueue.shift(); //shift removes from front (like Q), but also 
        // since in js the whole issue w removing leaves holes of undefined, q autoshifts.
        //so like a normal remove like a normal programing language would

    }
}
function isRecent(country)//check if a country is in the queue, makes easier to check
{
    for (let i = 0; i < recentCountriesQueue.length; i++){
        if (recentCountriesQueue[i].code === country.code)
        {
            return true;
        }
    }
    return false;
}

function generateNewQuestion() {
    //get a random flag (the one we guess)
    
    rand1 = randNumber(0, countries.length - 1);
    correct = countries[rand1];


    rand2 = randNumber(0, countries.length - 1);
    rand3 = randNumber(0, countries.length - 1);
    rand4 = randNumber(0, countries.length - 1);

    
    while (isRecent(countries[rand1]))
    {
        rand1 = randNumber(0, countries.length - 1);
    }
    while (rand2 == rand1 || countries[rand2] == undefined || isRecent(countries[rand2])) {
        rand2 = randNumber(0, countries.length - 1);
    }
    while (rand3 == rand2 || rand3 == rand1 || countries[rand3] == undefined || isRecent(countries[rand3])) {
        rand3 = randNumber(0, countries.length - 1);
    }
    while (rand4 == rand3 || rand4 == rand2 || rand4 == rand1 || countries[rand4] == undefined || isRecent(countries[rand4])) {
        rand4 = randNumber(0, countries.length - 1);
    }


    currentQuestionOptions = [correct, countries[rand2], countries[rand3], countries[rand4]];


    console.log(`the correct flag is ${correct.name}`);
    flagLink.src = `https://flagcdn.com/${correct.code}.svg`;


    // BUTTON 1
    randButton1 = randNumber(0, 3);
    txtForButton1 = currentQuestionOptions[randButton1];
    delete currentQuestionOptions[randButton1];
    button1.innerHTML = txtForButton1.name;
    if (txtForButton1.name.length > 14) //this makes it so we can shrink the text only if rlly long name in html part
    {
        button1.classList.add("longText");
    }
    else {
        button1.classList.remove("longText");
    }


    // BUTTON 2
    randButton2 = randNumber(0, 3);
    while (randButton2 == randButton1) {
        randButton2 = randNumber(0, 3);
    }
    txtForButton2 = currentQuestionOptions[randButton2];
    delete currentQuestionOptions[randButton2];
    button2.innerHTML = txtForButton2.name;
    if (txtForButton2.name.length > 14) //this makes it so we can shrink the text only if rlly long name in html part
    {
        button2.classList.add("longText");
    }
    else {
        button2.classList.remove("longText");
    }


    // BUTTON 3
    randButton3 = randNumber(0, 3);
    while (randButton3 == randButton1 || randButton3 == randButton2) {
        randButton3 = randNumber(0, 3);
    }
    txtForButton3 = currentQuestionOptions[randButton3];
    delete currentQuestionOptions[randButton3];
    button3.innerHTML = txtForButton3.name;
    if (txtForButton3.name.length > 14) //this makes it so we can shrink the text only if rlly long name in html part
    {
        button3.classList.add("longText");
    }
    else {
        button3.classList.remove("longText");
    }
    // BUTTON 4
    randButton4 = randNumber(0, 3);
    while (randButton4 == randButton1 || randButton4 == randButton2 || randButton4 == randButton3) {
        randButton4 = randNumber(0, 3);
    }
    txtForButton4 = currentQuestionOptions[randButton4];
    delete currentQuestionOptions[randButton4];
    button4.innerHTML = txtForButton4.name;
    if (txtForButton4.name.length > 14) //this makes it so we can shrink the text only if rlly long name in html part
    {
        button4.classList.add("longText");
    }
    else {
        button4.classList.remove("longText");
    }


    buttonTextArray = [txtForButton1, txtForButton2, txtForButton3, txtForButton4];


    correctButtonNum = -1;
    for (let i = 0; i < 4; i++) {
        if (buttonTextArray[i].name === correct.name) {
            correctButtonNum = i + 1;
        }
    }
    

    console.log(`The correct button is button ${correctButtonNum}`);


    const correctButton = document.getElementById(`button${correctButtonNum}WholeThing`);
    correctButton.classList.add("correct");
    addToRecentsQueue(correct);
    console.log(recentCountriesQueue.map(c => c.name));//print to consle so i can see its working
    //map makes a duplicate array (since we using q to immitate array, not built in to js),
    //  c=>c.name tels it only get the name of country

}


/*
//get a random flag (the one we guess)
let rand1 = randNumber(0, countries.length);
let correct = countries[rand1];


let rand2 = randNumber(0, countries.length - 1);
let rand3 = randNumber(0, countries.length - 1);
let rand4 = randNumber(0, countries.length - 1);


//get 3 more rand #'s for hte other answer choices
while(rand2 == rand1 || countries[rand2] == undefined)
{
   rand2 = randNumber(0, countries.length - 1);
}
while (rand3 == rand2 || rand3 == rand1 || countries[rand3] == undefined) 
{
   rand3 = randNumber(0, countries.length - 1);
}
while(rand4 == rand3 || rand4 == rand2 || rand4 == rand1 || countries[rand4] == undefined)
{
   rand4 = randNumber(0, countries.length - 1);
}
//put em in list, so we can retrive and remove in random order
//so right answer isnt always in same spot
let currentQuestionOptions = [correct, countries[rand2], countries[rand3], countries[rand4]];
const flagLink = document.getElementById("flagLink");
// for p and div its .innerHTML, for img its .scr and links (a) its .href
// ALSO HUGE THING: whats below is basically fstring in python
//but 2 differences:
// its ${} not {}
//and its ` not ' or " so the backtick thats to left of 1 key very top left
console.log(`the correct flag is ${correct.name}`);
flagLink.src = `https://flagcdn.com/${correct.code}.svg`;




// ok massive news: the flags show up, the correct one shows up
//now its getting buttons to show the text




//use delete countries[i], make sure to check that its not undefined
//cuz annoyingly, a removed element just stays in the array as an undefined element
//so just check if its not one and pick again if it is, keep goin till we're not undefined
//fine cuz its 4 elements so yea
const button1 = document.getElementById("button1");
let randButton1 = randNumber(0, 3);
let txtForButton1 = currentQuestionOptions[randButton1];
delete currentQuestionOptions[randButton1]; // since we do this, must always check for next oens that we're nto picking the spot where we removed thing
button1.innerHTML = txtForButton1.name;


const button2 = document.getElementById("button2");
let randButton2 = randNumber(0, 3);
while (randButton2 == randButton1)
{
   randButton2 = randNumber(0, 3); // cant pick same # as button 1
}
let txtForButton2 = currentQuestionOptions[randButton2];
delete currentQuestionOptions[randButton2];
button2.innerHTML = txtForButton2.name;
//alr button2 works now repeat for 3 and 4, just add that they cannot be == to all previous buttons weve already made
const button3 = document.getElementById("button3");
let randButton3 = randNumber(0, 3);
while (randButton3 == randButton1 || randButton3 == randButton2)
{
   randButton3 = randNumber(0, 3); // cant pick same # as button 1
}
let txtForButton3 = currentQuestionOptions[randButton3];
delete currentQuestionOptions[randButton3];
button3.innerHTML = txtForButton3.name;


//now for the fourth
const button4 = document.getElementById("button4");
let randButton4 = randNumber(0, 3);
while (randButton4 == randButton1 || randButton4 == randButton2 || randButton4 == randButton3)
{
   randButton4 = randNumber(0, 3); // cant pick same # as button 1
}
let txtForButton4 = currentQuestionOptions[randButton4];
delete currentQuestionOptions[randButton4];
button4.innerHTML = txtForButton4.name;


let buttonTextArray = [txtForButton1, txtForButton2, txtForButton3, txtForButton4];
let correctButtonNum = -1;
for (let i = 0; i < 4; i++)
{
   if (buttonTextArray[i].name === correct.name)
   {
       correctButtonNum = i+1; // this gets us which button stores correct answer
     
   }
}


console.log(`The correct button is button ${correctButtonNum}`);
const correctButton = document.getElementById(`button${correctButtonNum}WholeThing`);
correctButton.classList.add("correct"); //add a tag to correct button
*/


let answeredAlready = false;


//make memory saved spots for num Correct and Answered


if (localStorage.getItem('numCorrect') === null) {
    // If not, initialize it
    localStorage.setItem('numCorrect', 0);
}
if (localStorage.getItem('numAnswered') === null) {
    // If not, initialize it
    localStorage.setItem('numAnswered', 0);
}




let numCorrect = Number((localStorage.getItem('numCorrect')));
let numAnswered = Number((localStorage.getItem('numAnswered')));


//make the next quesiton button not on the screen until after answered
document.getElementById("NextQuestionButton").style.display = "none";


//update the scoreboard so placeholder values dont show up on it
const scoreboard = document.getElementById("currentScore");
scoreboard.innerHTML = `${numCorrect}/${numAnswered} Correct`;



const answerButtons = document.querySelectorAll(".answerButton"); //all items with the class answerButtons
function colorButtons() {


    //const answerButtons = document.querySelectorAll(".answerButton"); //all items with the class answerButtons
    answerButtons.forEach((button, index) => {
        button.addEventListener("click", function () {
            if (answeredAlready) {
                return; //do nothing if we alr answered
            }

            answeredAlready = true;



            if (button.classList.contains("correct")) // if correct picked
            {
                const correctButtonImg = document.getElementById(`button${correctButtonNum}Img`);
                correctButtonImg.src = "pictures/greenButtonSmallBorder.png";
                numCorrect += 1;
                localStorage.setItem('numCorrect', `${numCorrect}`);
            }
            else //else if what we clicked wasnt the right one
            {
                //still make correct green
                const correctButtonImg = document.getElementById(`button${correctButtonNum}Img`);
                correctButtonImg.src = "pictures/greenButtonSmallBorder.png";

                //now get the wrong button and it's img so we can make it red
                let indexOfIncorrectlyPicked = index;
                const incorrectlyPickedButton = document.getElementById(`button${index + 1}WholeThing`);
                incorrectlyPickedButton.classList.add("incorrectlyPicked")
                const incorrectlyPickedButtonImg = document.getElementById(`button${index + 1}Img`);
                incorrectlyPickedButtonImg.src = "pictures/redButtonSmallBorder.png";
            }
            numAnswered += 1;
            localStorage.setItem('numAnswered', `${numAnswered}`);
            scoreboard.innerHTML = `${numCorrect}/${numAnswered} Correct`;

            //make anyting not clicked grey
            answerButtons.forEach((otherButton, i) => {
                if (!otherButton.classList.contains("correct") && !otherButton.classList.contains("incorrectlyPicked")) {
                    const otherButton = document.getElementById(`button${i + 1}Img`);
                    otherButton.src = "pictures/greyButtonSmallBorder.png";
                }
            });
            //after all that, make the next question button appear
            document.getElementById("NextQuestionButton").style.display = "flex"; //NOTE: updated to right display style
            //since w/ bootstrap i use flex not block style of display
        });
    });


}


generateNewQuestion();




colorButtons();
//reseting






let doReset = true; // make it so we only start reseting when we're done with a question not later not earlier
//so far, this resets and allows us to answer the question again
//buuut its the same one flag...
document.getElementById("NextQuestionButton").onclick = function () {
    answeredAlready = false;
    for (let i = 1; i <= 4; i++) {
        if (doReset) {
            const buttonTemp = document.getElementById(`button${i}Img`);
            buttonTemp.src = "pictures/blueButtonSmallBorder.png";
        }
    }


    //remove the tags on which button is right/clicked for new quesiton
    answerButtons.forEach((button) => {
        button.classList.remove("correct");
        button.classList.remove("incorrectlyPicked");
    });
    generateNewQuestion();
    document.getElementById("NextQuestionButton").style.display = "none";



};


//differnt from the doReset boolean
//this is to reset how many quetions it says youve answered
const resetButton = document.getElementById("resetButton");
resetButton.onclick = function () {
    numCorrect = 0;
    numAnswered = 0;
    localStorage.setItem('numCorrect', 0);
    localStorage.setItem('numAnswered', 0);
    scoreboard.innerHTML = `${numCorrect}/${numAnswered} Correct`;


}