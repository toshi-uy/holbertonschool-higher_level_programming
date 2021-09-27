document.addEventListener('DOMContentLoaded', function remove () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $(document).ready(
    $('DIV#remove_item').click(function () {
      $('UL.my_list li:last-child').remove();
    })
  );
  $(document).ready(
    $('DIV#clear_list').click(function () {
      $('UL.my_list').empty();
    })
  );
});
