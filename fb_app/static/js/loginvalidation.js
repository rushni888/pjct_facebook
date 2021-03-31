function validation(){
    //Get the username and password from the form and store them in variables
        var username=document.getElementById("uname");
        var password=document.getElementById("pass");
    
    //Get the error message dispalying elements and store them in variables
        var err_username=document.getElementById("err_username");
        var err_pass=document.getElementById("err_pass"); 
    
    // Creating a variable status
       var status=1;
       
    
    //validating username
        var emailformat = /^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;
        if(username.value.trim()==""){
            err_username.innerHTML="Please enter your username";
            username.style.border="1px solid red";
            status=0;}
        else if(username.value.match(emailformat)==null){
            err_username.innerHTML="Please enter a valid email";
            username.style.border="1px solid red";
            status=0;}
        else{
            username.style.border="none";
            err_username.style.visibility="hidden";
        }
    
    //validating password 
        if(password.value.trim()=="" ){
           err_pass.innerHTML="Please enter your password"
           password.style.border="1px solid red";
           status=0;}
        else if(password.value.trim().length<5){
            err_pass.innerHTML="Password must be minimum 5 characters"
            password.style.border="1px solid red";
            status=0;}
        else{
            password.style.border="none";
            err_pass.style.visibility="hidden";
        }      
   
    
    if(status==1){
        return true;
    }
    else{
        return false;
    }
    }
        
   