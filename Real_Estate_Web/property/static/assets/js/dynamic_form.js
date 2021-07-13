$(function(){
    $('#property-type').change(function(){
        $('#dynamic-form').submit();
        $('#dynamic-form').css('display','none');;
    });
});


//$("#property-type").change(function () {
//  var url = $("#dynamic-form").attr("action");  // get the url of the `load_cities` view
//  var property_type = $(this).val();  // get the selected country ID from the HTML input
//
//  $.ajax({                       // initialize an AJAX request
//    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
//    data: {
//      'form_type': property_type      // add the country id to the GET parameters
//    },
//    success: function (data) {   // `data` is the return of the `load_cities` view function
//      alert(property_type) // replace the contents of the city input with the data that came from the server
//    }
//  });
//
//});