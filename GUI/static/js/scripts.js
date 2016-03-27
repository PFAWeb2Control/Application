$("form").hide();

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
