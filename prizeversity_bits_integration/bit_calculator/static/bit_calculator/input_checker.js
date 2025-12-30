// this file contains a bunch of functions that can be used for
// individually checking whether the generate button can be enabled
function enableSubmit(){
    // NOT WORKING CURRENTLY
    let inputs = document.getElementsByClassName('required');
    let btn = document.getElementById('generate_btn');
    let isValid = true;
    
    for (var i = 0; i < inputs.length; i++){
        let changedInput = inputs[i];
        if (changedInput.value.trim() === "" || changedInput.value === null){
            isValid = false;break;}
    }
    
    btn.disabled = !isValid;
    }