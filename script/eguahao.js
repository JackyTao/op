// Javascript fragment inserted into article page of health channel,
// to add guahao entrance in 2 positon: below tile, right after share button
//
function countUpLink() {
    $('body').append('<img src="http://smart.sohu.com/count/eguahao/uplink" style="display:none;">');
}

function countBottomButton() {
    $('body').append('<img src="http://smart.sohu.com/count/eguahao/bottombutton" style="display:none;">');
}

function countBingLiBang() {
    $('body').append('<img src="http://smart.sohu.com/count/binglibang/bottom" style="display:none;">');
}

(function(){
    setTimeout(function(){
        if (/CN(33[0123]|51[0123]|43[0123]|440|37[01]|15[012]).{3}/.test(sohu_IP_Loc)) {
            // right below title
            $('.news-info .state a:last').before('<a href="http://laiguahao.cn/sohu?locid=' + sohu_IP_Loc + '&catenames=' + encodeURIComponent(cateNames) + '" style="margin-right:1em;" target="_blank" onclick="countUpLink();">Ô¤Ô¼¹ÒºÅ</a>');
            // after share button
            $('#big-share .like-boring').append('<dd><a style="background-color:#5CACEE" onclick="countBottomButton();" target="_blank" href="http://laiguahao.cn/sohu?locid=' + sohu_IP_Loc + '&catenames=' + encodeURIComponent(cateNames) + '">Ô¤Ô¼¹ÒºÅ</a></dd>');
        } else if (/Ö×Áö/.test(cateNames)) {
            $('#big-share .like-boring').append('<dd><a style="background-color:#5CACEE" onclick="countBingLiBang();" target="_blank" href="http://smart.sohu.com">ÕÒ²¡ÓÑ</a></dd>');
        }
    }, 1500);
})();
// It's a gbk file, keep the following line
// vim: set fileencoding=gbk:
