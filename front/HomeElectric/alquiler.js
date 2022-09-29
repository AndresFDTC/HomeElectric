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

    $("#alquilar").click(function(){
        var herramienta = $("#herramienta").val()
        var inicio = $("#inicio").val();
        var fin = $("#fin").val();
        var usuario = window.localStorage.getItem("user_id");
        
        const url = "http://localhost:8000/alquiler/reg_rent/"

        var data = {
            "inicio": inicio,
            "fin": fin,
            "usuario": usuario,
            "herramienta": herramienta
        }

        var fetchData = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-Type': 'application/json'
                }
        }

        fetch(url, fetchData)
        .then(response => response.json()) 
        .then(json => {
            alert("Alquiler registrado exitosamente")
            window.location.href = "confirmacion.html"
        })
        .catch(err => console.log(err))
        .catch(err => alert("Hubo problemas al registar su alquiler"))
    })
})