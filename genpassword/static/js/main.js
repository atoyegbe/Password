$(document).ready(function () {
  $(document).on("click", "#generate", function (e) {
    e.preventDefault();
    $.ajax({
      url: "",
      type: "GET",
      data: $(this).text(),
      success: function (response) {
        $("#passwordsafe").val(response.password);
      },
    });
  });
});
$(document).ready(function () {
  $(document).submit( function (e) {
    $.ajax({
      type: "POST",
      url: "",
      data: $("#form_id").serializer(),
      success: function (json) {
        document.getElementById("form_id").reset();
      },
      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
      },
    });
  });
});
