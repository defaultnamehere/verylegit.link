
var ANIMATION_DURATION = 500;
    $('.slideable').each(function() {
        if ($(this).offset().left < 0) {
            $(this).css("left", "150%");
        } else if ($(this).offset().left > $('div.container').width()) {
            $(this).animate({
                left: '50%',
            }, 500 );
        } else {
            $(this).animate({
                left: '-150%',
            }, 500 );
        }
    });

function handleURL() {
    // Get the entered URL.
    var long_url = $('input.long-url').val();

    var $spinner = $('.spinner');
    var $submitBtn = $('button.btn-sketchify');

    // Show a spinner.
    // This doesn't use fadeOut, because that sets display: none on the element.
    // This makes the page layout jank.
    // By using fadeTo on the opacity property, the hidden element still
    // takes up space.
    $spinner.fadeTo('fast', 1);

    // Hide the button for #UX
    $submitBtn.hide();

    // TODO post a google analytics event
    $.post("/sketchify", {
        "long_url": long_url
    })
    .done(function(data) {

        // So we're using .html here, but feel free to try and XSS yourself if you must.
        $('p.result-long').html('<a href="' + long_url + '">' + long_url + '</a>');
        $('p.result-sketchy').html('<a href="' + data + '">' + data + '</a>');

        // Store the result in the page, ready to copy.
        $('div.example').slideUp(ANIMATION_DURATION);
        $('h2.slogan').slideUp(ANIMATION_DURATION);
        //$('div.result').show(ANIMATION_DURATION);
        $('div.result').slideDown(ANIMATION_DURATION);

        $('form.sketchify').removeClass("has-error")
        $('div.error').hide();

        $spinner.fadeTo('fast', 0);
        $submitBtn.show();
    })
    .fail(function(data) {
        console.log("failed");
        $('form.sketchify').addClass("has-error")
        $('div.error').show();
        $('div.result').hide(300);
        $spinner.fadeTo('fast', 0);
        $submitBtn.show();
    });
    return false;
};


// Also do the things when the user presses enter
$('form.sketchify-form').submit(function(e) {
    e.preventDefault();
    // Set loading spinner

    // Not actually disabling keyboard events but go ahead hack me if you dare.
    $('#main').addClass("disabled");
    handleURL();
    $('#main').removeClass("disabled");
    return false; 
});

$('button.btn-sketchify').click(function(e) {
    handleURL();
    return false;
});