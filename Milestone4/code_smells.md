Tasks:

Research common code smells and how they impact code quality:

Magic Numbers & Strings – Using hardcoded values instead of constants.
let discountPrice = price * 0.85;
let role = "admin";
if (userRole === "admin") {
grantAccess();
}
Refactor:

const DISCOUNT_RATE = 0.15;
const ADMIN_ROLE = "admin";

let discountPrice = price * (1 - DISCOUNT_RATE);
if (userRole === ADMIN_ROLE) {
grantAccess();
}

Long Functions – Functions that do too much and should be broken into smaller parts.
function handleOrder(order) {
console.log("Validating...");
// many steps
console.log("Calculating...");
// more steps
console.log("Sending email...");
// even more steps
}

Refactor:
function handleOrder(order) {
validate(order);
calculate(order);
sendEmail(order);
}

Duplicate Code – Copy-pasting logic instead of reusing functions.
let fullName1 = firstName1 + " " + lastName1;
let fullName2 = firstName2 + " " + lastName2;

Refactor:
function getFullName(first, last) {
return ${first} ${last};
}
let fullName1 = getFullName(firstName1, lastName1);
let fullName2 = getFullName(firstName2, lastName2);

Large Classes (God Objects) – Classes that handle too many responsibilities.
class UserManager {
registerUser() {}
sendEmail() {}
validateInput() {}
resetPassword() {}
logActivity() {}
}

Refactor:
class UserService {
registerUser() {}
resetPassword() {}
}

class EmailService {
sendEmail() {}
}

class Logger {
logActivity() {}
}

Deeply Nested Conditionals – Complex if/else trees that make code harder to follow.
if (user) {
if (user.loggedIn) {
if (user.role === "admin") {
deletePost();
}
}
}

Refactor:
if (!user || !user.loggedIn || user.role !== "admin") return;
deletePost();

Commented-Out Code – Unused code that clutters the codebase.
// let oldFunction = () => console.log("Old Code");
// oldFunction();
let newFunction = () => console.log("New Code");
newFunction();

Refactor:
let newFunction = () => console.log("New Code");
newFunction();

Inconsistent Naming – Variable names that don't clearly describe their purpose.
let x = 10;
let user1 = getData();
let user_data_count = 5;

Refactor:
let itemLimit = 10;
let user = getData();
let userCount = 5;

Avoiding code smells make future debugging easier?
i) Code is easier to understand.
ii) Smaller functions and well-named variables.
iii) Clean and organized structure.