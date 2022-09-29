$(document).ready(function() {

    // nombre del ususario y cerrar sesión
    var userSession = window.localStorage.getItem('name')
    if (userSession) {
        //Crea el saludo al usuario con nombre propio
        var p = document.createElement("p");
        p.innerHTML = `Hola ${userSession}`;
        document.getElementById("logged").appendChild(p)

        // Agrega el botón para cerrar la sesión
        let btn = document.createElement("button");
        btn.innerHTML = "Cerrar sesión";
        btn.class = "btn btn-secondary"
        btn.onclick = function () {
            window.localStorage.clear();
            window.location.href ="index.html";
        }
        document.getElementById("logged").appendChild(btn);
    }


    var user_id = "4";
    const url = `http://localhost:8000/alquiler/rents_user/${user_id}`
    fetch(url)
        .then(response => response.json()) 
        .then(json => {
            console.log(json)
            for (let i in json){
                let rent_id = json[i]["id"];
                let inicio = json[i]["inicio"];
                let fin = json[i]["fin"];
                let herramienta = json[i]["herramienta"];
                let usuario = window.localStorage.getItem('user_id');
                console.log(rent_id, inicio, fin, herramienta, usuario);

                let rent = document.createElement("li");
                rent.innerHTML = herramienta
                rent.class = "list-group-item"
                document.getElementById("list_reserva").appendChild(rent)
            }
        })
        .catch(err => console.log(err))
})