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


    var marker = [

		  {
		      coordinates: {lat:37.7695, lng:-122.4460},
		      content: '<h3> All Saints\' Episcopal Church: </h3><p><b>Address</b>:1350 Waller St., San Francisco, CA 94117</p><p><b>Offering</b>: Brunch [10:30 - 11:30am] on <b>Saturdays</b> </p><p><b>Note</b>:Vegetarian option, sometimes Vegan!. Meat; potatoes or pasta or rice; fresh vegetables, salad, fruit salad, pastry, coffee & bread.</p><p><b>Phone Number</b>: 415-621-1862</p>'
		  },

		  {
		      coordinates: {lat:37.7800, lng:-122.4078},
		      content: '<h3> Church Without Walls </h3><p><b>Address</b>: 164 6th Street, San Francisco, CA 94103</p><p><b>Offering</b>: Cafe [10 - 11am] & Dinner [6 - 7pm] on <b> M-F </b></p><p><b>Note</b>: Cafe: cofee & toast, Dinner: A hot meal.</p><p><b>Phone Number</b>: 415-861-8688</p>'

		  },
	  ]


    for(var i = 0; i < marker.length; i++){
	addMarker(marker[i]);
    };


    function addMarker(properties){
	var marker = new google.maps.Marker({
		position:properties.coordinates,
		map:map
	    });

	if (properties.icon){
	    marker.setIcon(properties.icon);
	}

	if (properties.content){
	    var infoWindow = new google.maps.InfoWindow({
		    content:properties.content
		});

	    marker.addListener('click', function(){
		    infoWindow.open(map, marker)
			});
	}
    }


    function  findlatlng(geocoder, map, infoWindow, address, properties){
	if (address){
	    geocoder.geocode({'address': address}, function(results, status) {
		    if (status === 'OK') {
			if (results[0]) {
			    var marker = new google.maps.Marker({
				    map: map,
				    position: results[0].geometry.location
				});

			    if (properties.icon){
				marker.setIcon(properties.icon);
			    }

			    if (properties.content){
				var infoWindow = new google.maps.InfoWindow({
					content:properties.content
				    });

				marker.addListener('click', function(){
					infoWindow.open(map, marker)
					    });
			    }
			}
		    }
		});
	}
    }
}


    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
	infoWindow.setPosition(pos);
	infoWindow.setContent(browserHasGeolocation ?
			      'Error: The Geolocation service failed.' :
			      'Error: Your browser doesn\'t support geolocation.');
	infoWindow.open(map);
    }