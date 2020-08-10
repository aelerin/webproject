// let Utilisateur = [
//     { id: 1, pseudo: "Michel", password: "Banane" },
//     { id: 2, pseudo: "Martine", password: "Jambon" },
//     { id: 3, pseudo: "Mariette", password: "Orange" },
//     { id: 4, pseudo: "Kiki", password: "crevette" }
// ]
utilisateur = {}
const connexion = (event) => {
    event.preventDefault()
    for (let i = 0; i <= 1; i++) {
        utilisateur[event.target[i].name] = event.target[i].value

    }
    // for (users of Utilisateur) {
    //     if (event.target[0].value == "root" && event.target[1].value == "root") {
    //         window.location.href = "../../src/admin/admin.html";
    //     }
    //     if (users.pseudo == event.target[0].value && users.password == event.target[1].value) {
    // if (confirm("Felicitations, vous êtes maintenant connecter")) {
    //     window.location.href = "../accueil.html";
    fetch('http://127.0.0.1:5000/api/users/login', {
        method: 'POST',
        body: JSON.stringify(utilisateur),
        headers: {
            'Content-Type': 'application/json'
        }

    })
        .then(res => res.json())
        .then(res => window.location.replace(res["url"]));

}
//         }
//     }
// }

document.querySelector("#MonForm").addEventListener('submit', connexion)

