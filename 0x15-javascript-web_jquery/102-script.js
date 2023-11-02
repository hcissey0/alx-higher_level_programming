$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang_code = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang_code, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
