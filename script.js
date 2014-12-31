var level = 0;
var max = 10;

$(function() {

    $('#image').append(level);
    $('#maks').append(max);
    $( '#progressbar').progressbar({
      value: 0
    })
    .data("value","0");

    //Progressbar
    
    $('#but').click(function() {

        $( '#progressbar' ).progressbar({
            max: max
        });

        currValue = $( '#progressbar' ).data('value');
        currValue = parseInt(currValue) ? parseInt(currValue) : 0;

        if(currValue <= max-1) {
            $( '#progressbar' ).progressbar({
              value: currValue+1
            }).data('value',currValue+1);
            $('#exper').html((currValue)+' exp');
        }else {
            level += 1;
            max = parseInt(max*1.5);
            $( '#progressbar' ).progressbar({
                value: 0
            }).data('value',0);

            //Test
            console.log('next lvl. Level: ' + level + ' Max: ' + max + ' CurrValue: ' + currValue);

            //Set
            $('#exper').html('0 exp');
            $('#image').html(level);
            $('#maks').html(max);

            //Time
            var d = new Date();
            var time = '</br>' + d.toLocaleString() + ' - ';

            var levelUP = 'LEVEL UP to level:  ' + level;

            //Logs
            $('#logs').prepend(time + levelUP);
        }
    });

    //Informations about buttons

    $('#but').hover(function() {
        $('#info').html('With an each step you will gain 1 point of experience.');
    }, function(){
        $('#info').empty();
    });

});