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

   $('#next_btn').on('click', function(){
       $('#tab1').removeClass('active');
       $('#tab2').addClass('active');
       $("#trans_btn").attr("disabled", "disabled");
       
   });

   $('#prev_btn').on('click', function(){
       $('#tab2').removeClass('active');
       $('#tab1').addClass('active');
       $("#trans_btn").attr("disabled", "disabled");
   })

   $('#pro_btn').on('click', function(){
       $('#process').removeClass('trans-blur');
       $('.tab-content').addClass('trans-blur');
   })

   $('#pro_btn').on('click', function(){
       $('#process').removeClass('trans-blur');
       $('.tab-content').addClass('trans-blur');
       $("button,input[type=text]").attr("disabled", "disabled");
   })

    $('.left_btn').on('click', function(){
       $('.tab-content').removeClass('trans-blur');
       $('#tab1').addClass('active');
       $('#tab2').removeClass('active');
       $('#process').addClass('trans-blur');
       $("button,input[type=text]").removeAttr("disabled", "disabled");
   })
})