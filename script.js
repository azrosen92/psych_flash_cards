window.onload = function() {

	document.getElementById('word-div').onclick = getDefinition;

};

function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
  	console.log("with credentials");

    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, true);

  } else if (typeof XDomainRequest != "undefined") {
  	console.log("without credentials");

    // Otherwise, check if XDomainRequest.
    // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    xhr = new XDomainRequest();
    xhr.open(method, url);

  } else {

    // Otherwise, CORS is not supported by the browser.
    xhr = null;

  }
  return xhr;
}

function onRequestLoad() {
	console.log(this.responseText);
}

function getDefinition(term) {
	var baseURL = "http://psychologydictionary.org/";
	// Build url for request
	var requestURL = "http://psychologydictionary.org/deindividuation";

	var request = new XMLHttpRequest();
	request.open('get', requestURL, true);
	request.send();
	
	// $.ajax({
	// 	type: "GET",
	// 	url: requestURL,
	// 	datatype: "jsonp",
	// 	crossDomain: true,
	// 	contentType: "application/json;charset-uf8",
	// 	xhrFields: {
	// 		withCredentials: true
	// 	},
	// 	success: onRequestLoad
	// });
}