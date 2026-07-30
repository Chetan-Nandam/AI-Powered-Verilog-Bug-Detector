/* ==========================================
   AI Verilog Bug Detector
   app.js
========================================== */

const fileInput = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");
const uploadArea = document.querySelector(".upload-area");
const form = document.querySelector("form");
const analyseButton = document.getElementById("analyseButton");

/* ===========================
   FILE SELECTION
=========================== */

fileInput.addEventListener("change", function () {

    if (this.files.length > 0) {

        fileName.innerHTML = "📄 " + this.files[0].name;

        fileName.style.color = "#22c55e";

    } else {

        fileName.innerHTML = "No file selected";

        fileName.style.color = "#94a3b8";

    }

});

/* ===========================
   DRAG & DROP
=========================== */

["dragenter", "dragover"].forEach(eventName => {

    uploadArea.addEventListener(eventName, e => {

        e.preventDefault();
        e.stopPropagation();

        uploadArea.style.borderColor = "#7c5cff";
        uploadArea.style.background = "#1b2638";

    });

});

["dragleave", "drop"].forEach(eventName => {

    uploadArea.addEventListener(eventName, e => {

        e.preventDefault();
        e.stopPropagation();

        uploadArea.style.borderColor = "#4f8cff";
        uploadArea.style.background = "transparent";

    });

});

uploadArea.addEventListener("drop", function (e) {

    const files = e.dataTransfer.files;

    if (files.length > 0) {

        fileInput.files = files;

        fileName.innerHTML = "📄 " + files[0].name;

        fileName.style.color = "#22c55e";

    }

});

/* ===========================
   FORM SUBMIT
=========================== */

form.addEventListener("submit", function () {

    analyseButton.disabled = true;

    analyseButton.innerHTML = "⏳ Analysing Verilog...";

});

/* ===========================
   CARD ANIMATION
=========================== */

document.querySelectorAll(".feature-card").forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-8px) scale(1.02)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px) scale(1)";

    });

});

/* ===========================
   PAGE FADE-IN
=========================== */

window.addEventListener("load", () => {

    document.body.style.opacity = "0";

    requestAnimationFrame(() => {

        document.body.style.transition = "opacity 0.5s ease";

        document.body.style.opacity = "1";

    });

});