$(document).ready(function language () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
});
