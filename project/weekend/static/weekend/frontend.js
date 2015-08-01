var map, pointarray, heatmap, coordinateObjects;

function initialize() {
    $.getJSON("/weekend/instagram", function(data) {
        var all_posts = data['all_post_info'];
        // var coordinates = [];
        // for (i in all_posts) {
        //     coordinates.push([all_posts[i].latitude, all_posts[i].longitude])
        // };
        // console.log(coordinates)
        coordinateObjects = []
        for (i in all_posts) {
          coordinateObjects.push(new google.maps.LatLng(all_posts[i].latitude, all_posts[i].longitude))
        }
        var mapOptions = {
        zoom: 15,
        center: new google.maps.LatLng(40.733661, -74.011023),
        mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        map = new google.maps.Map(document.getElementById('map-canvas'),
          mapOptions);

        var pointArray = new google.maps.MVCArray(coordinateObjects);
        
        heatmap = new google.maps.visualization.HeatmapLayer({
        data: pointArray
        });
        var flag = "flag"

        var marker_objects = []
        for (var i in coordinateObjects) {
            var marker = new google.maps.Marker({
                position: coordinateObjects[i],
                map: map,
                icon: flag,
                title: "Hello World" + i
            })
            
            marker_objects.push(marker)
        }
        var infowindows = []
        for (var i in marker_objects) {
            infowindows[i] = "infowindows" + i 
        }
        console.log(infowindows)
        for (var i in marker_objects) {

            var contentString = '<div id="content">'+
                  '<div id="siteNotice">'+
                  '</div>'+
                  '<h1 id="firstHeading" class="firstHeading"><img src=' + all_posts[i].thumbnail_url + '>' + marker_objects[i].title + '</h1>'+
                  '<div id="bodyContent">'+
                  '<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large ' +
                  'sandstone rock formation in the southern part of the '+
                  'Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) '+
                  'south west of the nearest large town, Alice Springs; 450&#160;km '+
                  '(280&#160;mi) by road. Kata Tjuta and Uluru are the two major '+
                  'features of the Uluru - Kata Tjuta National Park. Uluru is '+
                  'sacred to the Pitjantjatjara and Yankunytjatjara, the '+
                  'Aboriginal people of the area. It has many springs, waterholes, '+
                  'rock caves and ancient paintings. Uluru is listed as a World '+
                  'Heritage Site.</p>'+
                  '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">'+
                  'https://en.wikipedia.org/w/index.php?title=Uluru</a> '+
                  '(last visited June 22, 2009).</p>'+
                  '</div>'+
                  '</div>';

            infowindows[i] = new google.maps.InfoWindow({
                content: contentString
            });
            
            google.maps.event.addListener(marker_objects[i], 'click', function() {
                infowindows[i].open(map, this);
                infowindows[i].setContent(all_posts[i].thumbnail_url)
            });
            console.log(infowindows[i])
        }    

        heatmap.setMap(map);
    })
}

google.maps.event.addDomListener(window, 'load', initialize);

