$(document).ready(function () {
    $('.incrementbtn').click(function (e) { 
        e.preventDefault();
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value=parseInt(inc_value,10);
        value = isNaN(value) ? 0 : value;
        if (value < 10)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
});

$(document).ready(function () {
    $('.decrementbtn').click(function (e) { 
        e.preventDefault();
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value=parseInt(dec_value,10);
        value = isNaN(value) ? 0 : value;
        if (value > 1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
});



