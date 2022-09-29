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
            window.location.href ="#"; // Dirección del home
        }
        document.getElementById("logged").appendChild(btn);
    }

    var rent_id = 4; //Necesitamos que sea el id de renta correspondiente al id que hizo click en reserva aparezca aquí
    const url = `http://localhost:8000/alquiler/retrieve_rent/${rent_id}`
    fetch(url)
        .then(response => response.json()) 
        .then(json => {
            console.log(json)
            console.log(json["herramienta"])
            document.getElementById("herramienta").value = json["herramienta"];
            document.getElementById("inicio").value = json["inicio"];
            document.getElementById("fin").value = json["fin"];
        })
        .catch(err => console.log(err))
        
    // Update request
    $("#update").click(function(){
        var rent_id = 3;
        const url = `http://localhost:8000/alquiler/update_rent/${rent_id}`
        console.log("hola");
        
        var herramienta = $("#herramienta").val()
        var inicio = $("#inicio").val();
        var fin = $("#fin").val();
        var usuario = window.localStorage.getItem('user_id');
        
        var data = {
            "inicio": inicio,
            "fin": fin,
            "usuario": usuario,
            "herramienta": herramienta
        }

        var fetchData = {
            method: 'PUT',
            body: JSON.stringify(data),
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-Type': 'application/json'
                }
        }
        
        fetch(url, fetchData)
            .then(response => response.json()) 
            .then(json => {
                console.log(json)
                alert("Registro actualizado exitosamente")
            })
            .catch(err => {
                console.log(err)
                alert("Hubo un problema al actualizar su registro")
            })
        
    })
})