function statusList(){
    $.get('/user/status').then(res =>{
        $('#status').html(res);
    })
}

function favoriteList(){
    $.get('/user/favorite').then(res => {
        $('#favourite').html(res);
    })
}

function documentList(){
    $.get('/user/document').then(res => {
        $('#document').html(res);
    })
}

function contactsList(){
    $.get('user/contacts').then(res => {
        $('#contact-list').html(res);
    })
}

function settingList(){
    $.get('/user/settings').then(res => {
        $('#settings').html(res);
    })
}

function notificationList(){
    $.get('/notification').then(res =>{
        $('#notification').html(res);
    })
}

function toDoList(){
    $.get('/user/to-do').then(res => {
        $('#todo').html(res);
    })
}

function filesList(){
    $.get('/user/files').then(res => {
        $('#files').html(res);
    })
}

function noteList(){
    $.get('/user/note').then(res => {
        $('#notes').html(res);
    })
}

function reminderList(){
    $.get('/user/reminder').then(res => {
        $('#reminder').html(res);
    })
}

function goChat(id){
    $.get('/chat/' + id).then(res => {
        $('#chat-view').html(res);
    })
}

function popUpVideoCall(){
    $.get('/call/video-call').then(res => {
        $('#videocall').html(res);
    })
}