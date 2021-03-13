$(document).ready(function(){
    // sending a connect request to the server.
    var socket = io.connect('localhost:8000');
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
                '</tr><div class="hideablecontent"><tr><td>'+mails[i].body+'</td></tr></div>'

        }-
        console.log(s)
        $("#tbl").empty();
        $(".hideablecontent").hide()
        $("#tbl").append(s).hide().show('slow');
        $(".hideablecontent").hide()

        $(".mail").off("click");
        $(".mail").click( function(){
            console.log('yeeeeet')
            $(".hideablecontent").slideToggle()
        });

    });
    $(".alert").delay(3000).slideUp(300);

    function copyToClipboard(element) {
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($(element).text()).select();
        document.execCommand("copy");
        $temp.remove();
      }

   });

