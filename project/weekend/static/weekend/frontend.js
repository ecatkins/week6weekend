var map, pointarray, heatmap, eddyData;

function initialize() {
    $.getJSON("/weekend/instagram", function(data) {
        console.log(data['all_post_info']);
        var all_posts = data['all_post_info'];
        var coordinates = [];
        for (i in all_posts) {
            coordinates.push([all_posts[i].latitude, all_posts[i].longitude])
        };
        console.log(coordinates)
        eddyData = []
        for (i in coordinates) {
          eddyData.push(new google.maps.LatLng(coordinates[i][0], coordinates[i][1]))
        }

        var mapOptions = {
        zoom: 15,
        center: new google.maps.LatLng(40.733661, -74.011023),
        mapTypeId: google.maps.MapTypeId.SATELLITE
        };

        map = new google.maps.Map(document.getElementById('map-canvas'),
          mapOptions);

        var pointArray = new google.maps.MVCArray(eddyData);
        console.log(eddyData);
        
        heatmap = new google.maps.visualization.HeatmapLayer({
        data: pointArray
        });
        var flag = "{% static 'weekend/rainbow_brick.jpg' %}"

        for (i in eddyData) {
            new google.maps.Marker({
                position: eddyData[i],
                map: map,
                icon: flag,
                title: "Hello World"
            })
        }

        heatmap.setMap(map);
    })
}

google.maps.event.addDomListener(window, 'load', initialize);

