let map;
function initMap(localizacionCiudad){
    $.ajax({
        url: 'https://maps.googleapis.com/maps/api/geocode/json?address=' + localizacionCiudad + '&key=AIzaSyDuqyO6rP6S_609rthhZt0dbi_uAHgpM8s',
        type: 'GET',
        dataType: 'text',
        success: function (data) {
            datos = JSON.parse(data);
            map = new google.maps.Map(document.getElementById("mapa"), {
                center: {lat: parseFloat(datos.results[0].geometry.location.lat) , lng: parseFloat(datos.results[0].geometry.location.lng)},
                types: ["lodging"],
                zoom: 15,
                styles: [
                    {"featureType": "poi",
                    "stylers": [{"visibility": "off"}]},
                    {"featureType": "poi.business.lodging",
                    "stylers": [{"visibility": "on"}]},
                    {"featureType": "poi.business.lodging",
                        "elementType": "labels.icon",
                    "stylers": [{"color": "#003cf7"}]},
                    {"featureType": "poi.business.lodging",
                        "elementType": "labels.text.fill",
                    "stylers": [{"color": "#fbe005"}]},
                    {"featureType": "poi.business.lodging",
                        "elementType": "labels.text.stroke",
                    "stylers": [{"color": "#3b3bcc"}]},
                    {"featureType": "transit",
                    "stylers": [{"visibility": "off"}]},
                ]
            });
        },
        error: function () {
            alert("No hemos podido encontrar resultados");
        },
    });
}

function getMarkers(localizacionAlojamiento){
      $.ajax({
        url: 'https://maps.googleapis.com/maps/api/geocode/json?address='+ localizacionAlojamiento+'&key=AIzaSyDuqyO6rP6S_609rthhZt0dbi_uAHgpM8s',
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

function getBarrio(localizacionBarrio){
        $.ajax({
        url: 'https://maps.googleapis.com/maps/api/geocode/json?address='+ localizacionBarrio +'&key=AIzaSyDuqyO6rP6S_609rthhZt0dbi_uAHgpM8s',
        type: 'GET',
        dataType: 'text',
        success: function (data) {
            datos = JSON.parse(data);
            console.log("modif 1")
            map = new google.maps.Map(document.getElementById("mapa"), {
                center: {lat: parseFloat(datos.results[0].geometry.location.lat) , lng: parseFloat(datos.results[0].geometry.location.lng)},
                types: ["lodging"],
                zoom: 15,
                styles: [
                    {"featureType": "poi",
                    "stylers": [{"visibility": "off"}]},
                    {"featureType": "poi.business.lodging",
                    "stylers": [{"visibility": "on"}]},
                    {"featureType": "poi.business.lodging",
                        "elementType": "labels.icon",
                    "stylers": [{"color": "#003cf7"}]},
                    {"featureType": "poi.business.lodging",
                        "elementType": "labels.text.fill",
                    "stylers": [{"color": "#b5d9e2"}]},
                    {"featureType": "poi.business.lodging",
                        "elementType": "labels.text.stroke",
                    "stylers": [{"color": "#3b3bcc"}]},
                    {"featureType": "transit",
                    "stylers": [{"visibility": "off"}]},
                ]
            });
        },
        error: function () {
            alert("No hemos podido encontrar resultados");
        },
    });
}