let map;
function initMap(localizacionCiudad) {
    $.ajax(
        {
            url: 'https://maps.googleapis.com/maps/api/geocode/json?address=' + localizacionCiudad + '&key=AIzaSyDuqyO6rP6S_609rthhZt0dbi_uAHgpM8s',
            type: 'GET',
            dataType: 'text',
            success: function (data) {
                datos = JSON.parse(data);

                map = new google.maps.Map(document.getElementById("mapa"), {
                    center: {
                        lat: parseFloat(datos.results[0].geometry.location.lat),
                        lng: parseFloat(datos.results[0].geometry.location.lng)
                    },
                    zoom: 15,
                });
            },
            error: function () {
                alert("No hemos podido encontrar resultados");
            },
        });
}

function getMarkers(localizacionMonumentos){
    $.ajax(
        {
        url: 'https://maps.googleapis.com/maps/api/geocode/json?address=' + localizacionMonumentos + '&key=AIzaSyDuqyO6rP6S_609rthhZt0dbi_uAHgpM8s',
        type: 'GET',
        dataType: 'text',
        success: function (data) {
            datos = JSON.parse(data);
            const marker = new google.maps.Marker({
            position: {lat: parseFloat(datos.results[0].geometry.location.lat) , lng: parseFloat(datos.results[0].geometry.location.lng)},
            map: map,
          });
        },
        error: function () {
            alert("No hemos podido encontrar resultados");
        },
    });
}