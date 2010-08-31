$(function() { 
    
    function selectElement(jq) {
        $('.selectable').removeClass('selected');
        jq.addClass('selected');        
    }

    function addNewElement(jqContainer) {

        var markup = '<div class="selectable"></div>',
            jq = $(markup);

        jq.appendTo(jqContainer);
    }

    function removeElement(jq) {

        if (jq.attr('id') === 'root') {
            return;
        }

        selectElement(jq.parent());
        jq.remove();
    }

    // events

    $('.selectable').live('click', function() {
        selectElement($(this));
    });

    $('#addChild').click(function() {
        addNewElement($('.selected'));
    });


    $('#remove').click(function() {
        removeElement($('.selected'));
    });

});