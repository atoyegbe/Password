$(document).ready( function () {
    $(".btn").click( function () {
        $.ajax({
            url: '',
            type: 'GET',
            data: {
                generate_button: $(this).text()
            },
            success: function(response) {
                $("#password").text(response.password)
            }

            
        })
    })
})