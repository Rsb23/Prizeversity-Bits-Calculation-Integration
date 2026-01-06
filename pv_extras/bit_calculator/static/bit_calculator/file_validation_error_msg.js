function hideAfterTimeout(){
    let elem = document.getElementById('file_error_msg');
    let elem2 = document.getElementById('file_card');

    if (elem){
        elem.remove();
    }

    if (elem2){
        elem2.classList.toggle('border-1');
        elem2.classList.toggle('border-error');
    }
}
setTimeout(() => {hideAfterTimeout()}, 3000);