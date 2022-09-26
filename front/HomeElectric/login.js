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

        fetch(url, fetchData)
        .then(response => response.json()) 
        .then(json => console.log(json))
        .catch(err => console.log(err))
    })
})