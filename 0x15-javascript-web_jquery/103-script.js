$(document).ready(function languageEnter () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
  $(document).on('keypress', function (e) {
    if (e.which === 13) {
      const language = $('INPUT#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (response) {
        $('DIV#hello').text(response.hello);
      });
    }
  });
});
