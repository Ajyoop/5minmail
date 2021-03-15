$(document).ready(function(){

    $(function () {
        $('[data-toggle="popover"]').popover()
      })


    // sending a connect request to the server.
    var socket = io.connect('http://0445d1639b8a.ngrok.io/');
    $(".refresh").click( function(){
        socket.emit('mailrefresh')

    });

    socket.on('connect', function(){
        socket.emit('join')
        socket.emit('mailrefresh')
    });

    socket.on('getnewmails', function(){
        socket.emit('mailrefresh')
    });


    socket.on('mailrefresh', function(data){
        let mails = JSON.parse(data);

        let s = ""
        for (let i = 0; i < Object.keys(mails).length; i++){
            s+= '<tr class="mail">' +
                '<td style="padding-left:10px;">'+mails[i].sender+'</td>'+
                '<td>'+mails[i].subject+'</td>'+
                '<td>'+mails[i].subject+'</td>'+
                '</tr><tr class="hideablecontent"><td>'+mails[i].body+'</td></tr>'
        }
        
        $("#tbl").empty();
        
        $("#tbl").append(s).hide().show('slow');
        $(".hideablecontent").hide()

        $(".mail").off("click");
        $(".mail").click( function(){
            $(this).next().stop(false).slideToggle(500, "swing");
        });

    });

    $(".alert").delay(3000).slideUp(300);

    $("#copybutton").click(function(element) {
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($("#mailtext").text()).select();
        document.execCommand("copy");
        $temp.remove();
      });

    


   });

