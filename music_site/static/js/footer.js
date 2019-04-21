require.config({
    paths: {
        "jquery": "jquery.min",
        "com": "common.min"
    }
});

require(['jquery', 'com'], function($, com){
    function footerPosition(){
        $("footer").removeClass("footer-bottom");
        var contentHeight = document.body.scrollHeight,     // 网页正文高度
            winHeight = window.innerHeight;     // 可视窗口高度
        if(!(contentHeight > winHeight)) {
            //当网页正文高度小于可视窗口高度时，为footer添加style
            $("footer").addClass("footer-bottom");
        } else {
            $("footer").removeClass("footer-bottom");
        }
    }
    footerPosition();
    $(window).resize(footerPosition);
});
