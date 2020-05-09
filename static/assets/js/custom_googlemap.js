/** 
 * It outputs a styled (back and white) map on the given dom element id
 * 
 * @param {string}  dom_el_id the id of the html dom element to mount the map on
 * @param {float}   lat the lattidue of the place
 * @param {float}   lng the longitude of the place
 * @param {string}   marker_icon the path to map marker icon
 * 
 * @return void
 * */ 

function initMap(dom_el_id, lat, lng, marker_icon) {
    // add the fallback, we could use default parameterr but IE does not support default parameters
    if (typeof dom_el_id === 'undefined') {
        dom_el_id = 'map';
    }
    if (typeof lat === 'undefined') {
        lat = 40.712776;
    }
    if (typeof lng === 'undefined') {
        lng = -74.005974;
    }
    if (typeof marker_icon === 'undefined') {
        marker_icon = 'assets/images/map-marker.png';
    }



    let lat_lng = {
        lat: lat,
        lng: lng
    }; // lattitude and longitude of your place
    let element_to_mount_map = document.getElementById(dom_el_id); // get the dom element using the given ID
    let map = new google.maps.Map(
        element_to_mount_map, {
            zoom: 13,
            center: lat_lng,
            styles: [{
                "featureType": "water",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#e9e9e9"
                }, {
                    "lightness": 17
                }]
            },
            {
                "featureType": "landscape",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#f5f5f5"
                },
                {
                    "lightness": 20
                }
                ]
            },
            {
                "featureType": "road.highway",
                "elementType": "geometry.fill",
                "stylers": [{
                    "color": "#ffffff"
                },
                {
                    "lightness": 17
                }
                ]
            },
            {
                "featureType": "road.highway",
                "elementType": "geometry.stroke",
                "stylers": [{
                    "color": "#ffffff"
                },
                {
                    "lightness": 29
                }, {
                    "weight": 0.2
                }
                ]
            },
            {
                "featureType": "road.arterial",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#ffffff"
                },
                {
                    "lightness": 18
                }
                ]
            },
            {
                "featureType": "road.local",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#ffffff"
                },
                {
                    "lightness": 16
                }
                ]
            },
            {
                "featureType": "poi",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#f5f5f5"
                },
                {
                    "lightness": 21
                }
                ]
            },
            {
                "featureType": "poi.park",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#dedede"
                },
                {
                    "lightness": 21
                }
                ]
            }, {
                "elementType": "labels.text.stroke",
                "stylers": [{
                    "visibility": "on"
                }, {
                    "color": "#ffffff"
                }, {
                    "lightness": 16
                }]
            }, {
                "elementType": "labels.text.fill",
                "stylers": [{
                    "saturation": 36
                }, {
                    "color": "#333333"
                }, {
                    "lightness": 40
                }]
            }, {
                "elementType": "labels.icon",
                "stylers": [{
                    "visibility": "off"
                }]
            }, {
                "featureType": "transit",
                "elementType": "geometry",
                "stylers": [{
                    "color": "#f2f2f2"
                }, {
                    "lightness": 19
                }]
            }, {
                "featureType": "administrative",
                "elementType": "geometry.fill",
                "stylers": [{
                    "color": "#fefefe"
                }, {
                    "lightness": 20
                }]
            }, {
                "featureType": "administrative",
                "elementType": "geometry.stroke",
                "stylers": [{
                    "color": "#fefefe"
                }, {
                    "lightness": 17
                }, {
                    "weight": 1.2
                }]
            }
            ]
        });


    new google.maps.Marker({
        position: lat_lng,
        map: map,
        icon: marker_icon,
        animation: google.maps.Animation.BOUNCE
    });
}

jQuery(document).ready(function ($) {

    /*** =====================================
     * Google Maps
     * =====================================***/
    initMap('map', 40.712776, -74.005974, 'assets/images/map-marker.png');
});