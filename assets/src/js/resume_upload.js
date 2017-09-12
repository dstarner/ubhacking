// Add the file name to the label anytime a new file is selected
(function() {
  var elements = document.querySelectorAll("input[type=file]");
  for (var i = 0; i < elements.length; ++i) {
    elements[i].addEventListener("change", function () {
      var labels = this.labels;
      if (typeof labels !== "undefined" && labels.length > 0) {
        labels[0].innerText = "Upload Résumé: " + this.files[0].name;
      }
    });
  }
})();
