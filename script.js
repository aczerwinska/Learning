var level = 0;
var max = 10;

$(document).ready(function(){

	$('#image').append(level);
    $('#maks').append(max);

});

$(function() {
    $( "#progressbar" ).progressbar({
      value: 0
    })
    .data("value","0");
    
    
$("#but").click(function() {
        var currValue = $( "#progressbar" ).data("value");
        currValue = parseInt(currValue) ? parseInt(currValue) : 0;
        if(currValue < max) {
            $( "#progressbar" ).progressbar({
              value: currValue+1
            }).data("value",currValue+1);
            $("#exper").html((currValue+1)+" exp");
        }else {
            level += 1;
            max = parseInt(max*1.2);
            currValue = 0;
            console.log('next lvl. Level: ' + level + ' Max: ' + max + ' CurrValue: ' + currValue);
            $('#image').html(level);
            $('#maks').html(max);
        }
    });
});