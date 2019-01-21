$(document).ready(()=>{
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
})