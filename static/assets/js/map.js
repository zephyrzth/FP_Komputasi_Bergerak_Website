// Creating map options
var mapOptions = {
center: [-7.250445, 112.768845],
zoom: 10
}

// Creating a map object
var map = new L.map('map', mapOptions);

// Creating a Layer object
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Adding layer to the map
map.addLayer(layer);

// function myMap(map, mapOptions){
//     var myData = '{% url "data"%}';
//     $.getJSON(myData, function(data){
//         L.geoJson(data).addTo(map);
//     })
// }