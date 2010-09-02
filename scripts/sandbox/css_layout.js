$(function() { 
    
    function selectElement(jqElement) {

        $('.selectable').removeClass('selected');
        jqElement.addClass('selected');

        $('.property-editor').each(function() {

            if (this.id !== 'text') {
                $(this).val(jqElement.css(this.id)); // editor's id hardcoded as css propety name
            }
        });

        var isRoot = jqElement.attr('id') === 'root';

        (isRoot || jqElement.has('.selectable').length)
            ? $('#text').hide()
            : $('#text').show().val(jqElement.text());

        $('#remove')[isRoot ? 'hide' : 'show']();

        $('.child-only').each(function() {
            this.disabled = isRoot;
        });
    }

    function addNewElement(jqContainer) {

        var markup = '<div class="selectable"></div>',
            jq = $(markup);

        if (!jqContainer.has('.selectable').length) {
            jqContainer.text('');
        }

        jq.appendTo(jqContainer);

        selectElement(jqContainer);
    }

    function removeElement(jqElement) {

        if (jqElement.attr('id') === 'root') {
            return;
        }

        selectElement(jqElement.parent());

        jqElement.remove();
    }

    function setElementProperty(editor) {

        var target = $('.selected'),
            val = $(editor).val();

        (editor.id === 'text') ? target.text(val) : target.css(editor.id, val);
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

    $('.property-editor').change(function() {
        setElementProperty(this);
    });

    var hintIsHiddenCookie = 'hintIsHidden=1',
        hintIsNotHiddenCookie = 'hintIsHidden=0';

    $('#showHint,#hideHint').click(function() {

        var isHidden = this.id === 'hideHint';

        $('#hint').toggleClass('hidden', isHidden);

        document.cookie =  isHidden ? hintIsHiddenCookie : hintIsNotHiddenCookie;
    });

    // initialization

    selectElement($('#root'));

    $('#properties').removeClass('hidden');
    
    if (document.cookie.indexOf(hintIsNotHiddenCookie) !== -1) {
        $('#hint').removeClass('hidden');
    }

});