$(document).ready(function() {
    $(document).foundation();
    jQuery(".colorbox").colorbox({maxWidth: "100%"});
    jQuery(function($) {
        $(".easydate").easydate();
    });

    if (!document.referrer.indexOf(window.location.host) > 0) {
        jQuery('#back-btn').hide();
    }
});
