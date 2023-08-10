function restructure(){
    var is = document.getElementById("initial-struct");
    var ns = document.createElement("div");
    ns.setAttribute("id", "new-struct")
    
    nca = {};
    for (let j = 0; j < columns; j++) {
        nca[j] = document.createElement("div");
        nca[j].classList.add("column");
    }
    console.log(nca);
    
    i = 0
    chl = Array.from(is.children);
    for (let ch of chl) {
        is.removeChild(ch);
        nca[i%columns].appendChild(ch);
        console.log(ch);
        i+=1;
    }   

    for (let j = 0; j < columns; j++) {
        ns.appendChild(nca[j]);
    }

    document.getElementById("content").appendChild(ns);
}

function fn1(pid){
    p = pid;
    //window.alert(p);
}

function fn2(cid){
    c = cid;
    //window.alert(p);
}

function del_prod(){
    var url = "/del_prod";
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var ret = JSON.parse(xhttp.responseText);
            if(ret.stat == "success"){
                location.reload();
            }
            else{
                window.alert("Something went wrong!");
            }
        }
    };
    
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    var data = { pid: p };
    xhttp.send(JSON.stringify(data));
}

function del_cat(){
    var url = "/del_cat";
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var ret = JSON.parse(xhttp.responseText);
            if(ret.stat == "success"){
                location.reload();
            }
            else{
                window.alert("Something went wrong!");
            }
        }
    };
    
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    var data = { cid: c };
    xhttp.send(JSON.stringify(data));
}

function filter_ip(){
    var v = document.getElementById("filter-select").value
    if(v == 1){
        document.getElementById("filter-ip").type = "text" 
        document.getElementById("filter-ip").style.display = ""
        document.getElementById("filter-btn").disabled = ""
        document.getElementById("range-val").innerHTML =""
        document.getElementById("filter-ip").removeEventListener('input', val);    
    }
    else if(v == 2){
        document.getElementById("filter-ip").type = "text"
        document.getElementById("filter-ip").style.display = ""
        document.getElementById("filter-btn").disabled = ""
        document.getElementById("range-val").innerHTML =""
        document.getElementById("filter-ip").removeEventListener('input', val);    
    }
    else if(v == 3){
        document.getElementById("filter-ip").type = "range"
        document.getElementById("filter-ip").min = "0"
        document.getElementById("filter-ip").max = "1000"
        document.getElementById("filter-ip").step = "0.5"
        document.getElementById("filter-ip").style.display = ""
        document.getElementById("filter-btn").disabled = ""
        document.getElementById("filter-ip").addEventListener('input', val);
    }
    else{
        document.getElementById("filter-ip").style.display = "none"
        document.getElementById("filter-btn").disabled = "disabled"
        document.getElementById("filter-ip").removeEventListener('input', val);
        document.getElementById("range-val").innerHTML =""
        filter();    
    }
}

function val(){
    document.getElementById("range-val").innerHTML="\<\= Rs "+document.getElementById("filter-ip").value;
}

function filter(){
    var v = document.getElementById("filter-select").value
    var lines = document.getElementsByClassName("cat");
    var value = document.getElementById("filter-ip").value;
    
    for(var i = 0; i < lines.length; i++){
        const parent = lines[i];
        const children = parent.querySelectorAll('.card-body-prod');
        children.forEach((child) => {
            //window.alert(child.id)
            child.style.display = ""
        });
        parent.style.display = ""
    }  

    if(v==1){
        value = value.toLowerCase();
        
        for(var i = 0; i < lines.length; i++){
            //window.alert(lines[i].id)
            var classlist = Array.from(lines[i].classList)
            var name = classlist[classlist.length-1];
            if(name.toLowerCase().indexOf(value) != -1){
                lines[i].style.display = ""
            }
            else{
                lines[i].style.display = "none"
            }
        }  
    }
    else if(v==2){
        value = value.toLowerCase();
        for(var i = 0; i < lines.length; i++){
            var flag = 0;

            const parent = lines[i];
            const children = parent.querySelectorAll('.card-body-prod');
            children.forEach((child) => {
                if(child.id.toLowerCase().indexOf(value) != -1){
                    flag = 1;
                    child.style.display = ""
                }
                else{
                    child.style.display = "none"
                }
            });

            if(flag == 1){
                parent.style.display = ""
            }
            else{
                parent.style.display = "none"
            }

        }  
    }
    else if(v==3){
        value = parseFloat(value);
        for(var i = 0; i < lines.length; i++){
            var flag = 0;
            //window.alert(lines[i].id)
            const parent = lines[i];

            const children = parent.querySelectorAll('.card-body-prod');
            children.forEach((child) => {
                var child_price = child.querySelectorAll('.price');
                //window.alert(child.id+" "+child_price[0].innerHTML+" || ")
                if(parseFloat(child_price[0].innerHTML) <= value){
                    //window.alert("yes");
                    flag = 1;
                    child.style.display = ""
                }
                else{
                    //window.alert("no");
                    child.style.display = "none"
                }
            });

            if(flag == 1){
                parent.style.display = ""
            }
            else{
                parent.style.display = "none"
            }

        }  
    }
    else{
        for(var i = 0; i < lines.length; i++){
            const parent = lines[i];
            const children = parent.querySelectorAll('.card-body-prod');
            children.forEach((child) => {
                //window.alert(child.id)
                child.style.display = ""
            });
            parent.style.display = ""
        }  
    } 
}