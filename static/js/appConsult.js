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
    .then(resp => resp.json())
    .then(data => {
        if (data.error) {
            displayNotFoundClient(data.error);
        } else {
            console.log(data)
            displayClientInfo(data);
        }
    })
    .catch(err => {
        alert("Error " + err);
    });
}

function displayClientInfo(client) {
    console.log(client)
    let clientInfoDiv = document.getElementById("cliente-info");
    
    let photoSrc = client.photo ? client.photo : "https://vetbucket1.s3.amazonaws.com/images/user-default.png";
    
    clientInfoDiv.innerHTML = `
    <img src="${photoSrc}" alt="image" width="50" height="50">
        <h3>Información del Cliente</h3>
        <p><strong>Nombre:</strong> ${client.name}</p>
        <p><strong>Apellido:</strong> ${client.lastname}</p>
        <p><strong>Email:</strong> ${client.email}</p>
        <p><strong>Telefono:</strong> ${client.phoneNumber}</p>
        
    `;
}

function displayNotFoundClient(msj) {
    let clientInfoDiv = document.getElementById("cliente-info");
    clientInfoDiv.innerHTML = `
        <h3>${msj}</h3>
    `;
}