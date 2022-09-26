$(document).ready(function() {
    $("#alquilar").click(function(){
        var herramienta = $("#herramienta").val()
        var inicio = $("#inicio").val();
        var fin = $("#fin").val();
        var usuario = "8";
        
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
        .then(json => console.log(json), alert("Alquiler registrado exitosamente"))
        .catch(err => console.log(err))
        .catch(err => alert("Hubo problemas al registar su alquiler"))
    })
})