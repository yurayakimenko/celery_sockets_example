var socket = io();
socket.on('notify', function() {
    $.notify({
        message: 'Таска выполнена'
    },{
        type: 'success'
    });
});

function createTask() {
    var delayVal = $('delay').val()
    $.ajax({
        method: "POST",
        url: '/create_task',
        data: {
            delay: delayVal
        },
        success: () => {
            $.notify({
                message: 'Таска принята в обработку'
            },{
                type: 'warning'
            });
        }
    });
}