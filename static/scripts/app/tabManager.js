$ = require('jquery')

export function manageTabs(){
    $(function () {
        $('.panel .panel-tabs a').click(function () {
            let tab = $(this)
            let tabIndex = tab.index()

            $('.panel .panel-tabs a').removeClass('is-active')
            $(this).addClass('is-active')

            $.each($('.panel .tab-content'), function (index, el) {
                if(!$(el).hasClass('is-hidden')){
                    $(el).addClass('is-hidden')
                }
            })

            $('.tab-content:eq('+tabIndex+')').removeClass('is-hidden')

        })
    });
}

export function goToTab(TabIndex){
    $('.tabs ul li').removeClass('is-active')
    $(`.tabs ul li:eq('${TabIndex}') `).addClass('is-active')


    $.each($('.tab-content-container .tab-content'), function (index, el) {
        if(!$(el).hasClass('is-hidden')){
            $(el).addClass('is-hidden')
        }
    })

    $(`.tab-content-container .tab-content:eq('${TabIndex}')`).removeClass('is-hidden')
}

export function activeAllTabs(){
    $(function () {
        $.each($('.tabs ul li a'), (i, tab)=>{
            $(tab).click((event) => {
                console.log("On clique "+i)
                goToTab(i)
            })
        })
    })
}