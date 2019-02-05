$(document).ready(()=>{

    // $('.scrollbar-dynamic').scrollbar();

    function showSlidebar(){
        $('.right-slidebar').removeClass('animated slideOutRight');
        $('.right-slidebar').css('right', '0px');
        $('.right-slidebar').addClass('animated slideInRight');
    }

    function hideSlidebar(){
        $('.right-slidebar').removeClass('animated slideInRight');
        $('.right-slidebar').css('right', '0vh');
        $('.right-slidebar').addClass('animated slideOutRight');
    }

    $('.support-card').on('click', (e)=>{
        e.preventDefault();
        console.log("support card has been clicked");
        showSlidebar();
    })

    $('#close-slidebar').on('click', (e)=>{
        e.preventDefault();
        hideSlidebar();
    })

    $('.right-slidebar').each('div', new SimpleBar);

    $(".next_btn").click(function() { // Function Runs On NEXT Button Click
        $(this).parent().next().fadeIn('slow');
        $(this).parent().css({
        'display': 'none'
        });
        // Adding Class Active To Show Steps Forward;
        $('.active').next().addClass('active');
        });
        $(".pre_btn").click(function() { // Function Runs On PREVIOUS Button Click
        $(this).parent().prev().fadeIn('slow');
        $(this).parent().css({
        'display': 'none'
        });
        // Removing Class Active To Show Steps Backward;
        $('.active:last').removeClass('active');
    });
})