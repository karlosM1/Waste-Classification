// script.js

document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');

    fileInput.addEventListener('change', function(event) {
        handleFiles(event.target.files);
    });

    document.getElementById('uploadArea').addEventListener('dragover', function(event) {
        event.preventDefault();
    });

    document.getElementById('uploadArea').addEventListener('drop', function(event) {
        event.preventDefault();
        handleFiles(event.dataTransfer.files);
    });

    function handleFiles(files) {
        fileList.innerHTML = ''; // Clear the file list
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const listItem = document.createElement('li');
            const fileIcon = document.createElement('img');
            const fileName = document.createElement('span');
            const deleteIcon = document.createElement('span');

            fileIcon.src = 'file_icon.png'; // Replace with actual icon path
            fileIcon.alt = 'File Icon';
            fileIcon.style.width = '30px';
            fileIcon.style.height = '30px';

            fileName.className = 'file-name';
            fileName.textContent = file.name;

            deleteIcon.className = 'delete';
            deleteIcon.textContent = 'Delete';
            deleteIcon.onclick = function() {
                listItem.remove();
                fileInput.value = ''; // Clear the file input
            };

            listItem.appendChild(fileIcon);
            listItem.appendChild(fileName);
            listItem.appendChild(deleteIcon);

            fileList.appendChild(listItem);
        }
    }
});
