let map;
function monumentoPosicion(monumentoLocalizacion){
    $.ajax(
        {
        url: 'https://maps.googleapis.com/maps/api/geocode/json?address=' + monumentoLocalizacion + '&key=AIzaSyDuqyO6rP6S_609rthhZt0dbi_uAHgpM8s',
        type: 'GET',
        dataType: 'text',
        success: function (data) {
            datos = JSON.parse(data);
            map = new google.maps.Map(document.getElementById("mapa"), {
                center: {lat: parseFloat(datos.results[0].geometry.location.lat) , lng: parseFloat(datos.results[0].geometry.location.lng)},
                zoom: 18,
            });
        },
        error: function () {
            alert("No hemos podido encontrar resultados");
        },
    });
}