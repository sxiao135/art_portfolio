{% comment %} TESTING - NOT WORKING {% endcomment %}

var iframe = document.getElementById('if');
var oldSrc = iframe.src;
var newSrc = 'https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onmouseover_dom';

iframe.addEventListener('mouseover', function() {
    iframe.src = newSrc;
});

iframe.addEventListener('mouseout', function() {
    iframe.src = oldSrc;
});