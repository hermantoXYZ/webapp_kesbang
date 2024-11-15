
function toggleSection(sectionClass) {
    var inputDataSection = document.querySelector('.' + sectionClass);
    inputDataSection.style.display = inputDataSection.style.display === 'none' ? 'block' : 'none';
}
