let utilisateur = [

]


const getUsers = () => {
    fetch('http://192.168.99.100:5000/api/users').then(resp => resp.json()).then(users => renderUsers(users))
}

const renderUsers = (users) => {
    for (user of users) {
        utilisateur.push({ name: user['nom'], lastname: user['prenom'], email: user['email'] })
    }
    let table = document.querySelector("table")
    let tbody = document.querySelector("tbody")
    let data = Object.keys(utilisateur[0]);
    generateTableHead(table, data);
    generateTable(tbody, utilisateur);
}

const generateTableHead = (table, data) => {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data) {
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

const generateTable = (table, data) => {

    for (let element of data) {
        let row = table.insertRow()
        for (key in element) {
            let cell = row.insertCell()
            let text = document.createTextNode(element[key])
            cell.appendChild(text);
        }
    }
}

function myFunction() {
    name(visible)
    var input, filter, table, tr, td, i, txtValue;
    input = document.querySelector("#myInput");
    filter = input.value.toUpperCase();
    table = document.querySelector("#myTable");
    tr = table.getElementsByTagName("tr");


    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

getUsers()

document.querySelector("#myInput").addEventListener("keyup", myFunction);

