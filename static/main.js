let request_methods = document.querySelector("#methods");

request_methods.addEventListener("change", function () {
    const r_method = this.value;
    let request_data = document.querySelector("#data");
    let req_form = document.querySelector("#reqForm");
    let method = document.querySelector("#hid")
    method.value = this.value;
    const btn = document.querySelector("#btn");
    btn.textContent = this.value;
    
    switch (r_method) {
        case "GET":
            btn.style.background = "blue";
            request_data.style.display = "none";
            break;
        case "POST":
            btn.style.background = "green";
            request_data.style.display = "inline-block";
            break;
        case "PUT":
        case "PATCH":
            btn.style.background = "orange";
            request_data.style.display = "inline-block";
            break;
        case "DELETE":
            btn.style.background = "red";
            request_data.style.display = "none";
            break;
        case "OPTIONS":
            btn.style.background = "#27282c";
            request_data.style.display = "none";
            break;
        case "HEAD":
            btn.style.background = "brown";
            request_data.style.display = "none";
            break;
    }
})