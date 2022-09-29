$(document).ready(function() {
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
            window.location.href ="#"; // Dirección del home
        }
        document.getElementById("logged").appendChild(btn);
    }
})