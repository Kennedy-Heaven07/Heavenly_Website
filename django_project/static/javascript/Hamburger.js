$(document).ready(function() {
  $('#hamburger').on('click', function() {
      $('#navContainer').toggleClass('open');
  });
});
   function checkingUserName() {
      var Username = document.forms["register"]["Username"].value;
      if (Username == null || Username == "") {
         alert("Username field cannot  be empty. Please, fill it.");
         return false;
        }
     
   }