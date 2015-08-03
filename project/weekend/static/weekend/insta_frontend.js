var map, pointarray, heatmap, coordinateObjects;



function initialize(event, search, interval) {
    $.getJSON(window.location.pathname+ "/info", function(data) {
        var event_name = data['event']
        var icon = data['icon']
        var latitude = data['latitude']
        var longitude = data['longitude']
        var zoom = parseInt(data['zoom'])
        var suggested_search = data['suggested_search']
        console.log(suggested_search)
        
        ///adding suggest search terms
        $("#search_term").attr("placeholder","e.g. " + suggested_search)


        search = search || "none"
        interval = interval || "all"
        $.getJSON("/weekend/instagram/" + event_name + "/" + search + "/" + interval, function(data) {
            var all_posts = data['all_post_info'];
            coordinateObjects = []
            for (i in all_posts) {
              coordinateObjects.push(new google.maps.LatLng(all_posts[i].latitude, all_posts[i].longitude))
            }
            var mapOptions = {
            zoom: zoom,
            center: new google.maps.LatLng(latitude, longitude),
            mapTypeId: google.maps.MapTypeId.ROADMAP
            };

            map = new google.maps.Map(document.getElementById('map-canvas'),
              mapOptions);

            var pointArray = new google.maps.MVCArray(coordinateObjects);
            
          
            var icon_link = icon

            var marker_objects = []
            for (var i in coordinateObjects) {
                var marker = new google.maps.Marker({
                    position: coordinateObjects[i],
                    map: map,
                    icon: icon_link,
                    id: i
                })
                
                marker_objects.push(marker)
            }
           
            for (var i in marker_objects) {
                
                google.maps.event.addListener(marker_objects[i], 'click', function() {
                    var id = this.id
                    // infowindows[id].open(map, this);
                    $("#post").html('<div id="content">'+
                      '<div id="siteNotice">'+
                      '</div>'+
                      '<h1 id="firstHeading" class="firstHeading"> <a href="https://instagram.com/' + all_posts[id].user + '"">' + all_posts[id].user + '</a></h1>'+
                      '<div id="bodyContent">' + 
                      '<img src='+ all_posts[id].thumbnail_url +'> ' + 
                      '<p id="time_created">' + all_posts[id].created_time + '</p>' +
                      '<p id="caption">Caption: ' + all_posts[id].caption + '</p>' +
                      '</div>'+
                      '</div>')
      
                });
            }    

        
        })
    })

}

google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(function(event) {
    $("form").on("submit", function(event){
        event.preventDefault()
        var search = $('[name=search_field]').val();
        var interval = $('[name=time_interval]').val();
        initialize(event, search, interval);
    })
})