$(document).ready(function() {
    $('.notice-para').hide();
    $('.notice-heading').append(
        $('<a class="toggle-notice">explain</span>').click(function() {
            $(this).closest('.notice').find('.notice-para').toggle();
        })
    );

    function highlightReferences() {
        var ids = $(this).find('[data-ref-to]').map(function() {
            return $(this).attr('data-ref-to');
        }).get().join(', ');
        $(ids).addClass('highlight');
    }
    function clearHighlight() {
        $('.highlight').removeClass('highlight');
    }
    $('.notice').hover(highlightReferences, clearHighlight);
});
