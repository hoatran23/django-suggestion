(function($) {
    $('#getSuggest').click(function(e) {
        console.log("ok")
    });

    $(document).on('formset:removed', function(event, $row, formsetName) {
        console.log("ok")
        // Row removed
    });
})(django.jQuery);