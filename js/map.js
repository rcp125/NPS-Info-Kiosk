function individual(){

mapboxgl.accessToken = 'pk.eyJ1IjoicmNwMTI1IiwiYSI6ImNqeDIwMXB3aDAxYmM0NHFxZjk2eWhiMGIifQ.pyb7HzsOHKziL0ge0KZviA';

var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/light-v10',
  center: [-96, 37.8],
  zoom: 3
});

$.getJSON('https://cors-anywhere.herokuapp.com/https://www.nps.gov/lib/npmap.js/4.0.0/examples/data/national-parks.geojson', function (geojson) {
    geojson.features.forEach(function (marker) {
        var el = document.createElement('div');
  		el.className = 'marker';

  // make a marker for each feature and add to the map
  new mapboxgl.Marker(el)
    .setLngLat(marker.geometry.coordinates)
    .setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
    .setHTML('<h3>' + marker.properties.Name + '</h3><p>' + marker.properties.Code + '</p>'))
    .addTo(map);
    });
});

map.addControl(new mapboxgl.NavigationControl());

}

function cluster(){

	mapboxgl.accessToken = 'pk.eyJ1IjoicmNwMTI1IiwiYSI6ImNqeDIwMXB3aDAxYmM0NHFxZjk2eWhiMGIifQ.pyb7HzsOHKziL0ge0KZviA';
	var map = new mapboxgl.Map({
	container: 'map',
	style: 'mapbox://styles/mapbox/dark-v10',
	center: [-103.59179687498357, 40.66995747013945],
	zoom: 3
	});
	 
	map.on('load', function() {
	// Add a new source from our GeoJSON data and set the
	// 'cluster' option to true. GL-JS will add the point_count property to your source data.
	map.addSource("parks", {
	type: "geojson",
	data: "https://cors-anywhere.herokuapp.com/https://www.nps.gov/lib/npmap.js/4.0.0/examples/data/national-parks.geojson",
	cluster: true,
	clusterMaxZoom: 14, // Max zoom to cluster points on
	clusterRadius: 50 // Radius of each cluster when clustering points (defaults to 50)
	});
	 
	map.addLayer({
	id: "clusters",
	type: "circle",
	source: "parks",
	filter: ["has", "point_count"],
	paint: {
	//   * Blue, 15px circles when point count is less than 10
	//   * Yellow, 20px circles when point count is between 10 and 50
	//   * Pink, 30px circles when point count is greater than or equal to 50
	"circle-color": [
	"step",
	["get", "point_count"],
	"#51bbd6",
	10,
	"#f1f075",
	50,
	"#f28cb1"
	],
	"circle-radius": [
	"step",
	["get", "point_count"],
	15,
	10,
	20,
	50,
	30
	]
	}
	});
	 
	map.addLayer({
	id: "cluster-count",
	type: "symbol",
	source: "parks",
	filter: ["has", "point_count"],
	layout: {
	"text-field": "{point_count_abbreviated}",
	"text-font": ["DIN Offc Pro Medium", "Arial Unicode MS Bold"],
	"text-size": 12
	}
	});
	 
	// map.addLayer({
	// id: "unclustered-point",
	// type: "circle",
	// source: "parks",
	// filter: ["!", ["has", "point_count"]],
	// paint: {
	// "circle-color": "#11b4da",
	// "circle-radius": 6,
	// "circle-stroke-width": 2,
	// "circle-stroke-color": "#fff"
	// }
	// });

	map.loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Map_marker.svg/512px-Map_marker.svg.png', function(error, image){
		if(error) throw error;
		map.addImage('marker-map', image);

		map.addLayer({
			'id': "unclustered-point",
			'type': "symbol",
			'source': "parks",
			'filter': ["!", ["has", "point_count"]],
			'layout': {
				'visibility': 'visible',
			    'icon-image': 'marker-map',
			    'icon-size': 0.03
			}
	});
	});



	 
	// inspect a cluster on click
	map.on('click', 'clusters', function (e) {
	var features = map.queryRenderedFeatures(e.point, { layers: ['clusters'] });
	var clusterId = features[0].properties.cluster_id;
	map.getSource('parks').getClusterExpansionZoom(clusterId, function (err, zoom) {
	if (err)
	return;
	 
	map.easeTo({
	center: features[0].geometry.coordinates,
	zoom: zoom
	});
	});
	});
	 
	map.on('mouseenter', 'clusters', function () {
	map.getCanvas().style.cursor = 'pointer';
	});
	map.on('mouseleave', 'clusters', function () {
	map.getCanvas().style.cursor = '';
	});

	map.on('click', 'unclustered-point', function (e) {
	var coordinates = e.features[0].geometry.coordinates.slice();
	var description = e.features[0].properties.Name;
	 
	// Ensure that if the map is zoomed out such that multiple
	// copies of the feature are visible, the popup appears
	// over the copy being pointed to.
	while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
	coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
	}
	 
	new mapboxgl.Popup()
	.setLngLat(coordinates)
	.setHTML(description)
	.addTo(map);
	});
	 
	map.on('mouseenter', 'unclustered-point', function () {
	map.getCanvas().style.cursor = 'pointer';
	});
	 
	map.on('mouseleave', 'unclustered-point', function () {
	map.getCanvas().style.cursor = '';
	});


	});

	map.addControl(new mapboxgl.NavigationControl());

}