const file = document.getElementById('file');
file.addEventListener("click"   , () => {
    file.innerHTML = "Loading...";
    window.pywebview.api.select_file().then ((result) => {
        file.innerHTML = result;
})});