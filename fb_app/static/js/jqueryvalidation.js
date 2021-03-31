$(function(){

    status=0

    $('#uname').blur(function(){
        checkusername()  
    })

    $('#logform').submit(function(){
        checkusername()  
        if(status==0){
            alert("not submitted")
            return false;            
        }
        else{
            alert("submitted")
            return true;         
        }
    })
})

function checkusername(){
    username=$('#uname');
        if(username.val()==""){
            username.css("border", "1px solid red");
            $('#err_username').text("Enter the username")
           
        }
        else if(IsEmail(username.val())==false)
            {
            username.css("border", "1px solid red");
            $('#err_username').text("Enter a valid email")
                      
        }  
        else{
            username.css("border", "none");
            status=1
        } 
}

function IsEmail(email){
    var emailregex=/^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;
    if(!emailregex.test(email)){
        return false;
    }
    else{
        return true;
    }
}


        
   