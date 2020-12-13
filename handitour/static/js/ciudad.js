function initMap() {
  var coord =  { lat: -34.397, lng: 150.644 }
  var map = new google.maps.Map(document.getElementById("mapa"), {
    zoom: 8,
    center: coord
  });
}

