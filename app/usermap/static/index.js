const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer] });
map.fitWorld();
const markers = JSON.parse(document.getElementById("markers-data").textContent);
let feature = L.geoJSON(markers)
  .bindPopup(function (layer) {
    return "<p>" + layer.feature.properties.username + "</p>"
        + "<p>" + layer.feature.properties.email + "</p>"
        + "<p>" + layer.feature.properties.home_address + "</p>"
        + "<p>" + layer.feature.properties.location + "</p>"
  })
  .addTo(map);
map.setView([0, 0], 2);