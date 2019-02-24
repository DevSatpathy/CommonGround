var x = 40;
var y = -88;
var uni = L.map('mapid').setView([40.1164, -88.2434], 13);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYmoxOSIsImEiOiJjanNoeHF6dTQwd2VrNGF0N3VpYjBhNmVlIn0.DkwEg5jiRyQFqZ-Xe98o-Q', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
      '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox.streets'
  }).addTo(uni);

// function myFunction() {
//   var node = document.createElement("LI");
//   var textnode = document.createTextNode("Water");
//   node.appendChild(textnode);
//   document.getElementById("myList").appendChild(node);
// }

var user = JSON.parse("users.json");
var x_coord = parseFloat(user.x);
var y_coord = parseFloat(user.y);
L.marker([x_coord, y_coord]).addTo(uni)
    .bindPopup("Meeting Placeholder").openPopup();
L.marker([x, y]).addTo(uni)
  .bindPopup("Best place to meet");

  // Users sample user list variable
  var user = {x:"40.1201", y:"-88.2090", name:"Ben John"};
  
 for (var i = 0; i < user.length; i++) { 
   L.marker([user.x, user.y]).addTo(uni)
   .bindPopup(user.name +  "is here").openPopup();
 }