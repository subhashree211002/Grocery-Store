function create(user){
    var u = "";
    var url = "/add_cat_val";
    u = document.getElementById("cat-name").value;
    

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var ret = JSON.parse(xhttp.responseText);
            //window.alert(ret.stat)
            if(ret.stat == "success"){
                window.location.replace("/"+user+"/manager_dashboard");
            }
            else{
                document.getElementById("feedback").innerHTML=ret.stat; 
            }
            
        }
    };
    
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    var data = { name: u };
    xhttp.send(JSON.stringify(data));
}

function update(user, cat_id){
    var u = "";
    var url = "/update_cat_val";
    u = document.getElementById("cat-name").value;
    

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var ret = JSON.parse(xhttp.responseText);
            //window.alert(ret.stat)
            if(ret.stat == "success"){
                window.location.replace("/"+user+"/manager_dashboard");
            }
            else{
                document.getElementById("feedback").innerHTML=ret.stat; 
            }
            
        }
        else if(this.readyState == 4){
            
        }
    };
    
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    var data = { name: u, cid: cat_id };
    xhttp.send(JSON.stringify(data));
}