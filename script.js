var level = '0';

$(document).ready(function(){

	$('#image').append(level);

});

$(function() {
    $( "#progressbar" ).progressbar({
      value: 0
    })
    .data("value","0");
    
    $("#but").click(function() {
        var currValue = $( "#progressbar" ).data("value");
        currValue = parseInt(currValue) ? parseInt(currValue) : 0;
        if(currValue < 100) {
            $( "#progressbar" ).progressbar({
              value: currValue+1
            }).data("value",currValue+1);
            $("#exper").html((currValue+1)+" exp");
        }    
    });


});