let email = prompt("Email: ");

if (email.includes("@") && email.split("@")[1].includes(".") && !email.includes(" ")) {
    console.log("Email manzili to`gri");
} else {
    console.log("Email manzili notug`ri");
}
