var map, infoWindow;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
	    center: {lat: -34.397, lng: 150.644},
	    //center: {lat:37.7847, lng: -122.4145},
	    zoom: 15
	});

    infoWindow = new google.maps.InfoWindow;
    var geocoder = new google.maps.Geocoder;

    // Try HTML5 geolocation.
    if (navigator.geolocation) {
	navigator.geolocation.getCurrentPosition(function(position) {
		var pos = {
		    lat: position.coords.latitude,
		    lng: position.coords.longitude
		};
		addMarker({
			coordinates: pos,
			    content:'<h3>You Are Here</h3>',
			    icon: 'images/map/icon.png'
			    });
		infoWindow.open(map);
		map.setCenter(pos);
	    }, function() {
		handleLocationError(true, infoWindow, map.getCenter());
	    });
    } else {
	// Browser doesn't support Geolocation
	handleLocationError(false, infoWindow, map.getCenter());
    }