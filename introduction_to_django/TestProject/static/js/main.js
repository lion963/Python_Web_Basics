alert('It works')
function highlight() {
    if(this.className.includes('highlight')){
        this.className = this.className.replace('highlight', '')
    } else {
        this.className += 'highlight'
    }
}

window.onload = function () {
[...document.getElementsByClassName('highlight')]
    .forEach(element => {
        element.addEventListener('mouseenter', highlight)
        element.addEventListener('mouseout', highlight)
    })
}
