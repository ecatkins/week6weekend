var map, pointarray, heatmap, coordinateObjects;

function initialize() {
    $.getJSON("/weekend/instagram/6gay", function(data) {
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
                title: "Hello World" + i,
                id: i
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
                  '<h1 id="firstHeading" class="firstHeading">' + all_posts[i].user + '</h1>'+
                  '<div id="bodyContent">' + 
                  '<img src='+ all_posts[i].thumbnail_url +'> ' + 
                  '<p>' + all_posts[i].created_time + '</p>' +
                  '<p>Likes: ' + all_posts[i].likes + '</p>' +
                  '<p>Caption: ' + all_posts[i].caption + '</p>' +
                  '</div>'+
                  '</div>';

              

            infowindows[i] = new google.maps.InfoWindow({
                content: contentString
            });
            
            google.maps.event.addListener(marker_objects[i], 'click', function() {
                var id = this.id
                infowindows[id].open(map, this);
  
            });
            console.log(infowindows[i])
        }    

        heatmap.setMap(map);
    })
}

google.maps.event.addDomListener(window, 'load', initialize);

