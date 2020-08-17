let utilisateur = [

]
const getUsers = () => {
    fetch('http://127.0.0.1:5000/api/users').then(resp => resp.json()).then(users => renderUsers(users))
}

const renderUsers = (users) => {
    for (user of users) {
        utilisateur.push({ id: user['id'], name: user['nom'], lastname: user['prenom'], email: user['email'] })
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
        //Add Button cell.
        cell = row.insertCell(-1);
        var btnRemove = document.createElement("INPUT");
        btnRemove.type = "button";
        btnRemove.value = "Remove";
        btnRemove.setAttribute("onclick", "Remove(this);");
        cell.appendChild(btnRemove);


    }
}


function Remove(button) {
    //Determine the reference of the Row using the Button.
    var row = button.parentNode.parentNode;
    var tag = row.getElementsByTagName("TD")[0].innerHTML;
    if (confirm("Do you want to delete: " + tag)) {

        //Get the reference of the Table.
        var table = document.getElementById("myTable");

        //Delete the Table row using it's Index.
        table.deleteRow(row.rowIndex);

        //Delete row in object
        fetch('http://192.168.99.100:5000/api/users' + tag,
            { method: 'DELETE', })
            .then(
                res => this.setState({ jsonReturnedValue: json })
            )

    }
}



getUsers()