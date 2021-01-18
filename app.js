function getAge() {
    var age = parseInt(document.getElementById("age").value);
    return age;
}


function getBmi() {
    var bmi = parseFloat(document.getElementById("bmi").value);
    return bmi;
}


function getChildren() {
    var children = parseInt(document.getElementById("children").value);
    return children;
}


function getGender() {
    var gender;
    var ele = document.getElementsByName("gender");
    for(var i=0; i<ele.length; i++) {
        if(ele[i].checked)
            gender = ele[i].value;
    }
    return gender;
}


function getSmoker() {
    var is_smoker;
    var ele = document.getElementsByName("is_smoker");
    for(var i=0; i<ele.length; i++) {
        if(ele[i].checked)
            is_smoker = ele[i].value;
    }
    return is_smoker;
}


function getLocation() {
    var loc = document.getElementById("location").value;
    return loc;
}


function onClickedEstimateCharge() {
    console.log("Estimate Charge button clicked.");
    var age = getAge();
    var bmi = getBmi();
    var children = getChildren();
    var gender = getGender();
    var is_smoker = getSmoker();
    var loc = getLocation();
    var estCharge = document.getElementById("result");
    
    var url = "http://127.0.0.1:5000/predict_insurance_cost";
    
    console.log("url called");
    
    $.post(url, {
        age: age,
        bmi: bmi,
        children: children,
        gender: gender,
        is_smoker: is_smoker,
        loc: loc
    }, function(data, status) {
        console.log(data.estimated_charges);
        estCharge.innerHTML = "<h3>Your estimated Insurance charge is: Rs</h3>" + "<h1>" + data.estimated_charges.toString() + "</h1>";
        console.log(status);
    });
}