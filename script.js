var level = 0;
var max = 10;

$(function() {

    $('#image').append(level);
    $('#maks').append(max);
    $( "#progressbar" ).progressbar({
      value: 0
    })
    .data("value","0");

    //Informations about buttons

    $("#but").hover(function() {
        $('#info').html('With an each step you will gain 1 point of experience.');
    }, function(){
        $('#info').empty();
    });

    //Progressbar
    
    $("#but").click(function() {

        $( "#progressbar" ).progressbar({
            max: max
        });

        currValue = $( "#progressbar" ).data("value");
        currValue = parseInt(currValue) ? parseInt(currValue) : 0;
        if(currValue <= max-1) {
            $( "#progressbar" ).progressbar({
              value: currValue+1
            }).data("value",currValue+1);
            $("#exper").html((currValue)+" exp");
        }else {
            level += 1;
            max = parseInt(max*1.5);
            $( "#progressbar" ).progressbar({
              value: 0
            }).data("value",0);
            console.log('next lvl. Level: ' + level + ' Max: ' + max + ' CurrValue: ' + currValue);
            $("#exper").html("0 exp");
            $('#image').html(level);
            $('#maks').html(max);
        }
    });
});