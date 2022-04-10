/*jshint esversion: 6 */
// A script for timeout of the messages

setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

/// When you click everywhere in the document
$(document).click(function(event) {

    /// If *navbar-collapse* is not among targets of event
    if (!$(event.target).is('.navbar-collapse *')) {

        /// Collapse every *navbar-collapse*
        $('.navbar-collapse').removeClass('show');

    }
});