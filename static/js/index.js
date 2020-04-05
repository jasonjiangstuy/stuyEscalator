$(document).ready(function(){
    console.log('jquery working')
})

$('#submit').click(function (){
	var sendRequest = true;
    const target = $('#escalator').val();
    console.log(target);

    // checkboxes
    var radioButton = document.getElementsByName('status');

    const status = (function(){
      var temp = []
      for(i = 0; i < radioButton.length; i++) {
        if (radioButton[i].checked){
          temp.push(radioButton[i].value);
        }
      };
      return temp
    })();
    // ();
    
    // const curFirst = $('#cfirstname').val();

    // const newFirst = $('#firstname').val();
    // console.log(newFirst);
    // const curLast = $('#clastname').val()
    // const newLast = $('#lastname').val();
    // console.log(newLast);
    // const newprofilepic = $('#profilepic').prop('files')[0];
    // console.log(newprofilepic);

    var form = $('.accountForm')[0];
    var fd = new FormData(form);

    if (target != "" && target != undefined){
        console.log('form includes target');
        fd.append('newUsername', "true");
    }else {
        if (sendRequest){
            sendRequest = false;
        }
        fd.append('newUsername', "false");
    }

    if (newFirst != curFirst && newFirst != "" && newFirst != undefined){
        console.log('form includes first');
        if (sendRequest){
            sendRequest = false;
        }

        fd.append('newFirst', "true");
    }else {
        fd.append('newFirst', "false");
    }
    if (newLast != curLast && newLast != "" && newLast != undefined){
        console.log('form includes last');
        if (sendRequest){
            sendRequest = false;
        }
        fd.append('newLast', "true");
    }else {
        fd.append('newLast', "false");
    }
    if (newprofilepic != undefined){
        console.log('form includes pic 2,0');
        if (sendRequest){
            sendRequest = false;
        }
        fd.append('newPFP', "true");
    }else {
        fd.append('newPFP', "false");
    }


    if (sendRequest){
        $.ajax({
    type : 'POST',
    url : '/myAccount',
    data: fd,
    processData: false,  // tell jQuery not to process the data
    contentType: false,   // tell jQuery not to set contentType
    success: function(data) {
        if (data == "success"){
        alert("edits successful");
                    window.location.reload(true);
        }else {
        alert(data);
                    window.location.reload(true);
        }
    },
    error: function(e) {
        console.log(e);
    }
    });
    }
    else {
        alert("Not all forms are filled canceling request");
    }




  });
