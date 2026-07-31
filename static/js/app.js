// ======================================
// File Selection
// ======================================

document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("fileInput");
    const fileName = document.getElementById("fileName");

    if (input && fileName) {

        input.addEventListener("change", () => {

            if (input.files.length > 0) {

                fileName.innerHTML = "✅ " + input.files[0].name;

            } else {

                fileName.innerHTML = "No file selected";

            }

        });

    }

});


// ======================================
// Copy Corrected Code
// ======================================

function copyCode() {

    const codeBlock = document.getElementById("codeblock");

    if (!codeBlock) return;

    navigator.clipboard.writeText(codeBlock.innerText);

    const btn = document.querySelector(".copy-btn");

    if (!btn) return;

    btn.innerHTML = "✅ Copied!";

    setTimeout(() => {

        btn.innerHTML = "📋 Copy Code";

    }, 2000);

}


// ======================================
// AI Loading Screen
// ======================================

document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    if (!form) return;

    const overlay = document.getElementById("loadingOverlay");

    const message = document.getElementById("loadingMessage");

    const messages = [

        "⚙ Running Icarus Verilog...",

        "🔍 Detecting compiler errors...",

        "🤖 Contacting Gemini AI...",

        "🧠 Understanding your RTL...",

        "🛠 Generating corrected code...",

        "✨ Preparing dashboard..."

    ];

    let index = 0;

    let interval;

    form.addEventListener("submit", () => {

        overlay.style.display = "flex";

        message.innerHTML = messages[0];

        interval = setInterval(() => {

            index++;

            message.innerHTML = messages[index % messages.length];

        }, 1800);

    });

});


// ======================================
// Auto Scroll to Error Line
// ======================================

window.addEventListener("load", () => {

    const errorLine = document.querySelector(".error-row");

    if (errorLine) {

        errorLine.scrollIntoView({

            behavior: "smooth",

            block: "center"

        });

    }

});