var $button         = $('#one'),
    $modalContainer = $('#modal-container'),
    $closebtn       = $('#close'),
    $body           = $('body'),
    $content        = $('.content'),
    btnId;

$button.on('click', function () {
  btnId = $(this).attr('id');
  
  $modalContainer
      .removeAttr('class')
      .addClass(btnId);
  $content
      .removeAttr('class')
      .addClass('content');
  
  $body.addClass('modal-active');
  
  if (btnId == 'two' || btnId == 'three'|| btnId == 'four') {
    $content.addClass(btnId);
  }
  
});

$closebtn.on('click', function () {
  $modalContainer.addClass('out');
  $body.removeClass('modal-active');
  if ($modalContainer.hasClass(btnId)) {
    
    $content.addClass('out');
    
  }
});