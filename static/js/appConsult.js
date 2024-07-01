function consult_client_id(){
    
    let dni_client = document.getElementById("dni").value
    
    let obj_client = {
        "dni": dni_client
    }
    
    fetch("/consultClientId" , {
        "method":"post",
        "headers": {"Content-Type":"application/json"},
        "body": JSON.stringify(obj_client)
    })
}