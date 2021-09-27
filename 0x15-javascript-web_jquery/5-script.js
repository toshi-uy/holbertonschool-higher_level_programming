$('DIV#add_item').click(function () {
  $(this).parent().find('UL.my_list').append('<li>Item</li>');
});
