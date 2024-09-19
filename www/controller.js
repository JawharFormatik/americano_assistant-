$(document).ready(function () {
  //display speak message
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    $(".siri-message").text(message);
    $(".siri-message").textillate("start");
  }

  //display hood
  eel.expose(ShowHood);
  function ShowHood() {
    $("#Oval").attr("hidden", false);
    $("#SiriWave").attr("hidden", true);
  }

  eel.expose(senderText);
  function senderText(message) {
    var chatBox = document.getElementById("offcanvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-end mb-4">
        <div class="width-size">
        <div class="sender_message">${message}</div>`;
      //scroll to the bottom of chatbox
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
  eel.expose(recieverText);
  function recieverText(message) {
    var chatBox = document.getElementById("offcanvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-start mb-4">
        <div class="width-size">
        <div class="reciever_message">${message}</div>`;
      //scroll to the bottom of chatbox
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }

  eel.expose(hideLoader)
  function hideLoader() {

      $("#Loader").attr("hidden", true);
      $("#FaceAuth").attr("hidden", false);

  }
  // Hide Face auth and display Face Auth success animation
  eel.expose(hideFaceAuth)
  function hideFaceAuth() {

      $("#FaceAuth").attr("hidden", true);
      $("#FaceAuthSuccess").attr("hidden", false);

  }
  // Hide success and display 
  eel.expose(hideFaceAuthSuccess)
  function hideFaceAuthSuccess() {

      $("#FaceAuthSuccess").attr("hidden", true);
      $("#HelloGreet").attr("hidden", false);

  }


  // Hide Start Page and display blob
  eel.expose(hideStart)
  function hideStart() {

      $("#Start").attr("hidden", true);

      setTimeout(function () {
          $("#Oval").addClass("animate__animated animate__zoomIn");

      }, 1000)
      setTimeout(function () {
          $("#Oval").attr("hidden", false);
      }, 1000)
  }
});
