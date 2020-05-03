function initMap() {
    // Map options
    var options = {
      zoom: 13,
      center: {
        lat: 53.350140,
        lng: -6.266155
      }
    }
  
    var map = new google.maps.Map(document.getElementById('map'), options);
  
    var marker = new google.maps.Marker({
        position:{lat:53.345139,lng:-6.264115},
        map:map
    })
   
}