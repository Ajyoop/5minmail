$(document).ready(function(){
    // sending a connect request to the server.
    var socket = io.connect('http://285ad64a624c.ngrok.io');
    $(".refresh").click( function(){
        socket.emit('mailrefresh')
        console.log("click!")

    });

    socket.on('connect', function(){
        socket.emit('mailrefresh')
    });


    socket.on('mailrefresh', function(data){
        let mails = JSON.parse(data);
        console.log(mails)
        let s = ""
        for (let i = 0; i < Object.keys(mails).length; i++){
            s+= '<tr class="mail">' +
                '<td style="padding-left:10px;">'+mails[i].sender+'</td>'+
                '<td>'+mails[i].subject+'</td>'+
                '<td>'+mails[i].subject+'</td>'+
                '</tr>'+'<tr class="hideablecontent">'+'<td>'+mails[i].body+'</td>' +'</r>'

        }
        console.log(s)
        $("#tbl").empty();
        //$(".hideablecontent").hide()
        $("#tbl").append(s).hide().show('slow');

        $(".mail").off("click");
        $(".mail").click( function(){
            console.log("nigger")
            $(".hideablecontent").show("slow");
        });

    });

   });

