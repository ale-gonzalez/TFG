$(function (){

    function getCoords(posicion){
        var lat = posicion.coords.latitude;
        var lng = posicion.coords.longitude;
        initialize(lat, lng);
    }

    function initialize (lat, lng){
        var latlng = new google.maps.LatLng(lat, lng)
        var mapSetting = {
            center: latlng,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        map = google.maps.Map($('#mapa').get(0), mapSetting)
    }
});