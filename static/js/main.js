
  function makeRequest(url , callback) {
    if (window.XMLHttpRequest) { // Mozilla, Safari, ...
      httpRequest = new XMLHttpRequest();
    } else if (window.ActiveXObject) { // IE
      try {
        httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
      } 
      catch (e) {
        try {
          httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
        } 
        catch (e) {}
      }
    }

    if (!httpRequest) {
      alert('Giving up :( Cannot create an XMLHTTP instance');
      return false;
    }
    httpRequest.onreadystatechange = callback;
    httpRequest.open('GET' , url);
    httpRequest.send();
  }


  
   function handleCallback() {
    if (httpRequest.readyState === 4) {
      if (httpRequest.status === 200) {
//		console.log(httpRequest.responseText);	
	  } else {
        alert('There was a problem with the request.');
      }
    }
  }
  