var reloadTime = 5000;

$("#form").hide();

function toggleCat(id, num)
{
    array = Array.apply(null, Array(num)).map(function (_, i) {return i;});
    for(i=0; i<array.length; i++)
    {
        if(i != id && id>-1)
            $(".cat-" + i).hide();
        else
            $(".cat-" + i).show();
    }
}

function toggleForm(name)
{
    $('#form-' + name).show();
    $('.display-' + name).hide();
}

function showTweets(data)
{
    var length = data.result.length;
    var t;
    $("#tweets-list").html("");
    for(var i=length-1; i>=0; i--)
    {
        t = data.result[i];
        $("#tweets-list").html($("#tweets-list").html() +
            '<div class=" mdl-card mdl-shadow--2dp mdl-cell mdl-cell--4-col mdl-cell--4-col-tablet mdl-cell--12-col-desktop cat-' + t.cat.id +'">'+
                '<div class="mdl-card__title mdl-card--expand" style="background-color: ' + t.cat.color + '">'+
                    '<div class="head-boxes">'+
                        '<h2 class="mdl-card__title-text">'+
                            '<span class="user-badge">' + t.author + ' <small>(@' + t.author_id + ')</small></span>'+
                        '</h2>'+
                    '</div>'+
                    '<div class="head-boxes cat-header">'+
                        '<span class="badge">' + t.cat.name + '</span>'+
                    '</div>'+

                '</div>'+
                '<div class="mdl-card__supporting-text mdl-color-text--grey-600">'+
                    t.text +
                '</div>'+
                '<div class="mdl-card__actions mdl-card--border">'+
                    '<a href="http://twitter.com/' + t.author_id + '/status/' + t.id + '" class="mdl-button mdl-js-button mdl-js-ripple-effect">See</a>'+
                '</div>'+
            '</div>')
    }
}

function showCategories(data)
{
    var length = data.result.length;
    var c;

    $("#cat-list").html("");
    for(var i=length-1; i>=0; i--)
    {
        c = data.result[i];
        $("#cat-list").html($("#cat-list").html() +
        '<a class="mdl-navigation__link cat-main-'+ c.id + ' cat-item" href="#" onclick="toggleCat('+ c.id + ', '+ length + ')">'+
            '<i class="dot mdl-color-text--blue-grey-400 material-icons" style="background-color: '+ c.color + ';"></i>'+
            '<span class="list-item">'+ c.name + '</span>'+
        '</a>')
    }
}

window.setInterval( function(){$("#refresh-tweets").click();} , reloadTime);
window.setInterval( function(){$("#refresh-cat").click();} , reloadTime);

$('a#refresh-tweets').bind('click', function(){
    $.getJSON('./update_tweets',
    {json:true},
    function(data) {
        if(data.result.length > 0)
            $('#refresh-tweets').hide();
        showTweets(data);
    });

    return false;
});

$('a#refresh-cat').bind('click', function(){
    $.getJSON('./update_categories',
    {json:true},
    function(data) {
        if(data.result.length > 0)
            $('#refresh-cat').hide();
        showCategories(data);
    });

    return false;
});
