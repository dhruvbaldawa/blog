$(document).ready(function() {
    $(document).foundation();
    jQuery(".colorbox").colorbox({maxWidth: "100%"});
    jQuery(function($) {
        $(".easydate").easydate();
    });

    if (document.referrer.indexOf(window.location.host) < 0) {
        // some issue with jQuery not selecting all the instances, or
        // maybe I am missing something, this seems to work anyways.
        jQuery(document.querySelectorAll('#back-button')).hide();
    }
});
