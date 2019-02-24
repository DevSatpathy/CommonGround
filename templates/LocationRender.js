var latitude = document.getElementById("latitude");

var longitude = document.getElementById("longitude");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(displayPos, reqRejected);
    } else {
        latitude.innerHTML = "Geolocation is not supported by this browser/";
        longitude.innerHTML = "Geolocation is not supported by this browser/";
    }
}

function displayPos(position) {
    latitude.innerHTML = "Your current latitude is: " + position.coords.latitude;
    longitude.innerHTML = "Your current longitude is: " + position.coords.longitude;
    x_user = position.coords.latitude;
    y_user = position.coords.longitude;
    document.getElementById('xcoord').value = position.coords.latitude;
    document.getElementById('ycoord').value = position.coords.longitude;
    // document.getElementById('form').submit();
}

function reqRejected(error) {
    var addressinput = document.getElementById("addressinput");
    var box = document.createElement("input");
    box.type = "text";
    var button = document.createElement("BUTTON")
    button.type = "submit";
    button.value = "Submit";
    button.onclick = "submitAddr()"
    addressinput.appendChild(box);
    addressinput.appendChild(button);
    var errormsg = document.getElementById("errormsg");

    switch (error.code) {
        case error.PERMISSION_DENIED:
            errormsg.innerHTML = "User denied the request for Geolocation."
            break;
        case error.POSITION_UNAVAILABLE:
            errormsg.innerHTML = "Location information is unavailable."
            break;
        case error.TIMEOUT:
            errormsg.innerHTML = "The request to get user location timed out."
            break;
        case error.UNKNOWN_ERROR:
            errormsg.innerHTML = "An unknown error occurred."
            break;
    }
}

function submitAddr(){
    var addr = document.getElementById("input").value;
}
