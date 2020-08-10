
let utilisateur = {

}

const send = (event) => {
    event.preventDefault()
    for (let i = 0; i <= 5; i++) {
        utilisateur[event.target[i].name] = event.target[i].value

    }
    fetch('http://127.0.0.1:5000/api/users/', {
        method: 'POST',
        body: JSON.stringify(utilisateur),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(res => res.json())
        .then(res => console.log(res));


}

document.querySelector('#MonForm').addEventListener
    ('submit', send)




