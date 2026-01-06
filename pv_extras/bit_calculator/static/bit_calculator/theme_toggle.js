function toggleTheme(){
    // toggles daisyui theme between light and dark, dark is default
    // if on dark -> light, if on light -> dark
    const mainBody = document.body;

    if (mainBody.getAttribute('data-theme') == 'dark'){
        mainBody.setAttribute('data-theme', 'light');
    }
    else {
        mainBody.setAttribute('data-theme', 'dark');
    }
}

document.addEventListener('DOMContentLoaded', (event) => {toggleTheme()});

var elem = document.getElementById('themeChbx');

if (elem){
    elem.addEventListener('click', toggleTheme);
}