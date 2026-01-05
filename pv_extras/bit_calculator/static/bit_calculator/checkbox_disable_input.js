function setFirstNSubmissionsBonusState() {
        // FNSB = first n submissions bonus, naming convention
        var FNSBChbx = document.getElementById("id_firstNSubmissionBonus");
        var FNSBInput = document.getElementById("id_n");

        // If the checkbox is unchecked (!checked), disable the input field
        // A disabled input field's data is not submitted with the form
        if (FNSBChbx.checked) {
            FNSBInput.disabled = false;
        } else {
            FNSBInput.disabled = true;
        }
}
function setWeeklyStreakState() {
        // WS = weekly streak, naming convention
        var WSChbx = document.getElementById("id_submissionStreak");
        var WSInput = document.getElementById("id_streakWeeks");

        // If the checkbox is unchecked (!checked), disable the input field
        // A disabled input field's data is not submitted with the form
        if (WSChbx.checked) {
            WSInput.disabled = false;
        } else {
            WSInput.disabled = true;
        }
}
function checkStates(){
    setFirstNSubmissionsBonusState();
    setWeeklyStreakState();
}

// Run the function on page load to set the initial state
document.addEventListener('DOMContentLoaded', (event) => {checkStates()});

if (document.getElementById("id_firstNSubmissionBonus")){
    document.getElementById("id_firstNSubmissionBonus").addEventListener('change', setFirstNSubmissionsBonusState);
}

if (document.getElementById("id_submissionStreak")){
    document.getElementById("id_submissionStreak").addEventListener('change', setWeeklyStreakState);
}