$(document).ready(function () {
  function translate () {
    const lang_code = $('INPUT#language_code').val();
    $('INPUT#btn_translate').click(function () {
      $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang_code, function (data) {
        $('DIV#hello').text(data.hello);
      });
    });
  }
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (e) {
	  if (e.which == 13) {
		  translate();
	  }
  });
});
