// Global variable to track the open modal
var isModalOpen = false;

// Function to create a Bootstrap modal
function createBootstrapModal(title, content, buttonColor, buttonText, position) {
    // Check if a modal is already open
    if (isModalOpen) {
        return;
    }

    // Set the flag to true since we now have an open modal
    isModalOpen = true;

    // Generate a unique ID for the modal
    var modalId = "customModal" + new Date().getTime();
    console.log("Modal UUID: " + modalId);

    // Create the modal elements
    var modalContainer = document.createElement("div");
    modalContainer.className = "modal fade";
    modalContainer.id = modalId;

    var modalDialog = document.createElement("div");
    modalDialog.className = "modal-dialog " + getModalPositionClass(position);

    var modalContent = document.createElement("div");
    modalContent.className = "modal-content";

    // Create the modal header
    var modalHeader = document.createElement("div");
    modalHeader.className = "modal-header";
    modalHeader.innerHTML = '<h5 class="modal-title">' + (title || "Modal Title") + '</h5>' +
        '<button type="button" class="close" data-dismiss="modal" aria-label="Close">' +
        '<span aria-hidden="true">&times;</span></button>';

    // Create the modal body
    var modalBody = document.createElement("div");
    modalBody.className = "modal-body";
    modalBody.innerHTML = content || "Modal content goes here.";

    // Create the modal footer
    var modalFooter = document.createElement("div");
    modalFooter.className = "modal-footer";
    modalFooter.innerHTML = '<small class="text-muted small" style="float: left;">UUID: ' + modalId + '</small>' +
        '<button type="button" class="btn btn-' + (buttonColor || "primary") + '" data-dismiss="modal" onclick="closeModal(\'' + modalId + '\')">' + (buttonText || "I Understand") + '</button>';

    // Append elements to the modal
    modalContent.appendChild(modalHeader);
    modalContent.appendChild(modalBody);
    modalContent.appendChild(modalFooter);

    modalDialog.appendChild(modalContent);
    modalContainer.appendChild(modalDialog);

    // Append the modal to the body
    document.body.appendChild(modalContainer);

    // Show the modal
    $('#' + modalId).modal('show');
}

// Function to close the modal
function closeModal(modalId) {
    isModalOpen = false;
    $('#' + modalId).modal('hide');
}

// Helper function to get the class for the modal position
function getModalPositionClass(position) {
    switch (position) {
        case "top":
            return "modal-dialog-top";
        case "left":
            return "modal-dialog-left";
        case "right":
            return "modal-dialog-right";
        case "bottom":
            return "modal-dialog-bottom";
        default:
            return "modal-dialog-centered";
    }
}
