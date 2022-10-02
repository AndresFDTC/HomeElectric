$(document).ready(function() {
    $("#login").click(function(){
        var nomUs = $("#username").val();
        var pass = $("#password").val();

        
        const url = "http://127.0.0.1:8000/perfil/login/"

        var data = {
            "username": nomUs,
            "password": pass,
        }

        var fetchData = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-Type': 'application/json'
                }
        }

        // Solicitud para iniciar sesión
        fetch(url, fetchData)
        .then(response => response.json()) 
        .then(json => console.log(json))
        .catch(err => console.log(err))

        // Solicitud para obtener el id y nombre del usuario para almacenarlo en el localstorage
        fetch(`http://localhost:8000/perfil/username/${nomUs}`)
        .then(response => response.json()) 
        .then(json => {
            //console.log(json)
            var user_id = json["id"];
            //console.log(`El id del usuario es ${user_id}`)
            var user_name =json["first_name"];
            //console.log(`El nombre del usuario es ${user_name}`)
            window.localStorage.setItem('name', user_name)
            window.localStorage.setItem("user_id", user_id)
            window.location.href ="tienda.html";
        })
        .catch(err => console.log(err))
    })
})