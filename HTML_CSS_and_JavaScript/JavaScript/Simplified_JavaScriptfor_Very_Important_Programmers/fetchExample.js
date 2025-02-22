/* let fetchRequest = fetch("data.json");

fetchRequest.then((response) => {
    return response.json();
}).then((data) => {
    let ul = document.createElement("ul");

    data.forEach((user) => {
        let li = document.createElement("li");
        li.textContent = `${user.name} is ${user.age}`;
        ul.appendChild(li);
    })
    document.body.appendChild(ul);
}); */

/* let fetchUsers = async () => {
    let response = await fetch("data.json");
    console.log(response);
}
fetchUsers(); */

/* async function fetchUsers() {
    let response = await fetch("data.json");
    let data = await response.json();

    let ul = document.createElement("ul");

    data.forEach((user) => {
        let li = document.createElement("li");
        li.textContent = `${user.name} is ${user.age}`;
        ul.appendChild(li);
    });
    document.body.appendChild(ul);
}
fetchUsers(); */

/* let fetchUsers = async () => {
    try {
        let response = await fetch("data.json");
        let data = await response.json();
        console.log(data);
    } catch (error) {
        //Handle the error
        console.log(error);
    }
}
fetchUsers(); */

// MAKING HTTP REQUEST TO THE GITHUB API.
let fetchUsers = async () => {
    try {
        // let response = await fetch("https://api.github.com/users/ebenezerdon");
        let response = await fetch("https://api.github.com/users/ishaaqdaahir");
        let data = await response.json();
        console.log(data);
    } catch (error) {
        //Handle the error
        console.log(error);
    }
}
fetchUsers();