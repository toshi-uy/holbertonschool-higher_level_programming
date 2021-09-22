$('DIV#red_header').click(function () { 
  $(this).parent().find('header').toggleClass('red green');
});
