document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');
});

function addTag(tagName) {
    let tagInput = document.getElementById("id_tags");
    let currentTags = tagInput.value.split(",").map(t => t.trim()).filter(Boolean);

    if (!currentTags.includes(tagName)) {
        currentTags.push(tagName);
        tagInput.value = currentTags.join(", ");
    }
}