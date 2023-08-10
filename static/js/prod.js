function create(user, cat_id){
    var pname = "";
    var punit = "";
    var prate = "";
    var pqt = "";
    var url = "/add_prod_val";
    pname = document.getElementById("prod-name").value;
    punit = document.getElementById("prod-unit").value;
    prate = document.getElementById("prod-rate").value;
    pqt = document.getElementById("prod-qt").value;                

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    
        if (this.readyState == 4 && this.status == 200) {
            var ret = JSON.parse(xhttp.responseText);
            //window.alert(data.prate+1);
            //window.alert(ret.stat);
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
    var data = { pname: pname, punit: punit, prate: prate, pqt: pqt, cat_id: cat_id};
    xhttp.send(JSON.stringify(data));
}

function update(user, cat_id, prod_id){
    var pname = "";
    var punit = "";
    var prate = "";
    var pqt = "";
    var url = "/update_prod_val";
    pname = document.getElementById("prod-name").value;
    punit = document.getElementById("prod-unit").value;
    prate = document.getElementById("prod-rate").value;
    pqt = document.getElementById("prod-qt").value;  
    

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    
        if (this.readyState == 4 && this.status == 200) {
            var ret = JSON.parse(xhttp.responseText);
            //window.alert(data.prate+1);
            //window.alert(ret.stat);
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
    var data = { pid: prod_id, pname: pname, punit: punit, prate: prate, pqt: pqt, cat_id: cat_id};
    xhttp.send(JSON.stringify(data));
}