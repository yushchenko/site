$(function() {
    
    function selectElement(jq) {
        $('.selectable').removeClass('selected');
        jq.addClass('selected');        
    }

    function addNewElement(jqContainer) {

        var markup = '<div class="selectable"></div>',
            jq = $(markup);

        jq.appendTo(jqContainer);
        selectElement(jq);
    }

    function removeElement(jq) {

        if (jq.attr('id') === 'root') {
            return;
        }

        selectElement(jq.parent());
        jq.remove();
    }

    // Events

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