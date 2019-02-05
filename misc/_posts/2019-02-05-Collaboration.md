---
layout: misc
title: Collaboration
---

<div id="map" style="width:125%;height:600px"></div>

<script>

function make_marker(map, loc, name) {
  var marker = new google.maps.Marker({
    position:loc,
    title: name
  });
  marker.setMap(map);
  return marker;
}

function myMap() {

	var siteArray = [
		[ "PVAMU", 30.0954723, -95.9775204, "Prairie View A&M University" ], 
		[ "BRI", 32.7921971, -96.7867213, "Baylor Scotts & White Research Institute" ],
		[ "MDACC", 29.7085575, -95.4397136, "M.D. Anderson Cancer Center" ],
		[ "TAMU", 30.618615, -96.336577, "Texas A&M University" ], 
		[ "BCM", 29.710529, -95.396241, "Baylor College of Medicine" ], 
		[ "UPMC", 40.4422013, -79.9631745, "University of Pittsburgh School of Medicine" ],
		[ "UNC", 35.9049122, -79.0491021, "University of North Carolina (Chapel Hill)" ],
		[ "TGEN", 33.4530114, -112.0681182, "Translational Genomics Research Institue" ],
		[ "SALK", 32.886991, -117.2461476, "Salk Institute for Biological Studies" ],
		[ "UCSD", 32.8800604, -117.2362075, "University of California (San Diego)" ],
		[ "JHMI", 39.2969505, -76.6029355, "Johns Hopkins Medical Institute" ],
		[ "STANFORD", 37.428660999999984, -122.16992099999999, "Stanford University"],
		[ "GEGR", 42.82715560000002, -73.8780481, "GE Global Research (US)" ],
		[ "NIH", 34.9522699, -112.6614746, "National Institutes of Health" ],
		[ "EINSTEIN", 40.8521491, -73.8465878, "Einstein College of Medicine (NY)" ],
		[ "CAMBRIDGE", 52.2016155, 0.1156954, "University of Cambridge (UK)" ], 
		[ "UNIV. QUEENSLAND", -27.4954306, 153.0120301, "University of Queensland (Australia)" ],
		[ "UFRJ", -22.9541412, -43.1753638, "Universidade Federal do Rio de Janeiro (Brazil)" ],
		[ "FUTBILISI", 41.805463, 44.767108, "Free University of Tbilisi (Georgia)" ], 
		[ "BIP GERMANY", 48.1451738, 5.3171299, "Boehringer Ingelheim Pharma - Biberach an der Riss (Germany)" ], 
		[ "FSC_ROMANIA", 44.4379268, 26.0244262, "Fundatia Stop Cancer - Bucharest (Romania)" ]
	]

  	var centerLoc = new google.maps.LatLng(28,-96);

 	var mapCanvas = document.getElementById("map");
 	var mapOptions = {center: centerLoc, zoom: 2};
  	var map = new google.maps.Map(mapCanvas,mapOptions);

	var locArray = []
	var markerArray = []
	var windowArray = []
	var pathArray = []
	var pvamu

	for (ii = 0, len = siteArray.length; ii < len; ii++) {
		var aLoc = new google.maps.LatLng(siteArray[ii][1], siteArray[ii][2])
		locArray.push(aLoc)
		// var aMarker = make_marker(map, aLoc, siteArray[ii][3])
	    var aMarker = new google.maps.Marker({
	      position: aLoc,
	      title: siteArray[ii][3]
	    });
	    aMarker.setMap(map);
		markerArray.push(aMarker)
		
		var aWindow = new google.maps.InfoWindow({
			content: siteArray[ii][0],
			zIndex: 1
		});
		if (ii == 0) {
			aWindow.open(map, aMarker)
		} 
		// else {
		//	aMarker.addListener('mouseover', function() {
		//		aWindow.open(map, this)
		//	})
		//	aMarker.addListener('mouseout', function() {
		//		aWindow.close(map, this)
		//	})
		// }
		windowArray.push(aWindow)
	}

	for (ii = 1, len = siteArray.length; ii < len; ii++) {
		var aPath = new google.maps.Polyline({
    		path: [locArray[0], locArray[ii]],
   	 		geodesic: true,
  	  		strokeColor: "#0000FF",
    		strokeOpacity: 0.5,
    		strokeWeight: 3
    	});	
    	aPath.setMap(map)		
	}

}
</script>

<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAiRB4xTWRrBgj1aZ9pcLVo8NfsEsMsdsk&callback=myMap"></script>

<!--
To use this code on your website, get a free API key from Google.
Read more at: https://www.w3schools.com/graphics/google_maps_basic.asp
-->

</body>


