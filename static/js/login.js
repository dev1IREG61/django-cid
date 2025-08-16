$(document).on("click", "#login_submit", function () {
  let data = {
    email: $(".email").val(),
    password: $(".password").val(),
  };

  $.ajax({
    type: "post",
    url: "/world/login/validate/",
    data: data,
    success: function (result) {
      if (result.success) {
        window.location.href = "/";
      } else {
        alert(result.message);
      }
    },
    error: function () {
      alert("Login failed. Please try again.");
    },
  });
});
