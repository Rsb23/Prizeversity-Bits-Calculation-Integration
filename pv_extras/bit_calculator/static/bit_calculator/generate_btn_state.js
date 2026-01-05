let genBtn = document.getElementById('generate_btn');

let file = document.getElementById('id_file');

let crn = document.getElementById('id_crn');

// will need to iterate through dynamic widget, this is placeholder
let bitRewards = document.getElementById('id_bitRewards');
    
// need checkbox references to know if we include those inputs
// FNSB = first n submissions bonus, naming convention
var FNSBChbx = document.getElementById("id_firstNSubmissionBonus");
var FNSBInput = document.getElementById("id_n");
// WS = weekly streak, naming convention
var WSChbx = document.getElementById("id_submissionStreak");
var WSInput = document.getElementById("id_streakWeeks");

var dualCompletion = document.getElementById('id_dualCompletion');

function setGenerateBtnState(){
    // start by disabling the btn because the form is presented unbound
    genBtn.disabled = true;

    var readyToSubmit = true;

    if (file.value == ""){
        readyToSubmit = false;
    }
    if (crn.value == ""){
        readyToSubmit = false;
    }
    if (bitRewards.value == ""){
        readyToSubmit = false;
    }
    if (FNSBChbx.checked){
        if (FNSBInput.value == ""){
            readyToSubmit = false;
        }
    }
    if (WSChbx.checked){
        if (WSInput.value == ""){
            readyToSubmit = false;
        }
    }

    if (readyToSubmit){
        genBtn.disabled = false;
    }
    else{
        genBtn.disabled = true;
    }
}

document.addEventListener('DOMContentLoaded', (event) => {setGenerateBtnState()});

if (file){
    file.addEventListener('change', setGenerateBtnState);
}
if (crn){
    crn.addEventListener('change', setGenerateBtnState);
}
if (bitRewards){
    bitRewards.addEventListener('change', setGenerateBtnState);
}
if (FNSBChbx){
    FNSBChbx.addEventListener('change', setGenerateBtnState);
}
if (FNSBInput){
    FNSBInput.addEventListener('change', setGenerateBtnState);
}
if (WSChbx){
    WSChbx.addEventListener('change', setGenerateBtnState);
}
if (WSInput){
    WSInput.addEventListener('change', setGenerateBtnState);
}
if (dualCompletion){
    dualCompletion.addEventListener('change', setGenerateBtnState);
}