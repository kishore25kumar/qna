/**
 * Created with PyCharm.
 * User: Dinesh
 * Date: 9/13/14
 * Time: 10:17 PM
 * To change this template use File | Settings | File Templates.
 */

  function ajaxCall(accesstoken){
    $.ajax({
        url: "http://localhost:8000/qa/api",
        type: "post",
        datatype: "html",
        data: {
            accesstoken : accesstoken
        },
        success: function(response){
//            console.log("success");
        },
        error: function(response){
//            console.log("fail");
        }
    });
  }
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
        ajaxCall(response.authResponse.accessToken);
    });
  }

  window.fbAsyncInit = function() {
  FB.init({
    appId      : '575542489235692',
    cookie     : true,  // enable cookies to allow the server to access
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.1' // use version 2.1
  });

  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
