$("#buttonGroup button").click(function () {
    var selectedOption = $(this).text();
    $("#buttonGroup button").removeClass("active");
    $(this).addClass("active");
    $("#userInput").val(selectedOption);
});

$('#userInput').on('input', function () {
    this.style.height = 'auto'; // Reset the textarea height to auto
    this.style.height = this.scrollHeight + 'px'; // Set the height based on the content
});

const toggleSwitch = document.querySelector('#darkModeToggle');
toggleSwitch.addEventListener('change', switchTheme);

function switchTheme(event) {
    if (event.target.checked) {
        document.body.classList.add('dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
    }
}

var firstButtonHeight = $('#buttonGroup .list-group-item:first-child').outerHeight();
var secondButtonHeight = $('#buttonGroup .list-group-item:nth-child(2)').outerHeight();
// var scrollableHeight = firstButtonHeight + secondButtonHeight;
// $('#buttonGroup').css('height', scrollableHeight + 'px');
console.log(firstButtonHeight);
console.log(secondButtonHeight);

const chatbox = $("#chatbox");
const userInput = $("#userInput");
const sendButton = $("#sendButton");
let messages = [];

function clearContent() {
    // document.getElementById('chatbox').innerHTML = '';
    // messages = [];
    location.reload(); // Reload lại trang
}

userInput.on("input", function () {
    var inputText = $(this).val();

    if (inputText.trim() === "") {
        $("#buttonGroup button").removeClass("active");
    }
});

sendButton.click(function () {
    $("#buttonGroup button").removeClass("active");
});

const messageForm = document.querySelector('.message-form');
$('#sendButton').on("click", () => {
    var actionUrl = $('form').attr('action');
    console.log(actionUrl);

    const message = userInput.val().trim();
    if (message.length === 0) {
        return;
    } else {
        messages.push({
            "role": "user",
            "content": message
        });

        const displaytext = window.markdownit().render(message);
        let userMessageHtml = '<pre><div class="message right-side "  >' + displaytext + '</div></pre>';
        chatbox.append(userMessageHtml);
        chatbox.animate({ scrollTop: 20000000 }, "slow");
        userInput.val("");
        sendButton.val("Generating Response...");
        sendButton.prop("disabled", true);
        fetchMessages(actionUrl);
    }
});

userInput.on("keydown", (event) => {
    if (event.keyCode === 13 && !event.ctrlKey && !event.shiftKey) {
        event.preventDefault();
        $("#buttonGroup button").removeClass("active");
        sendButton.click();
    } else if (event.keyCode === 13 && (event.ctrlKey || event.shiftKey)) {
        event.preventDefault();
        const cursorPosition = userInput.prop("selectionStart");
        const currentValue = userInput.val();
        userInput.val(
            currentValue.slice(0, cursorPosition) +
            "\n" +
            currentValue.slice(cursorPosition)
        );
        userInput.prop("selectionStart", cursorPosition + 1);
        userInput.prop("selectionEnd", cursorPosition + 1);
    }
});

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

function fetchMessages(url) {
    var settings = {
        url: url,
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': getCookie('csrftoken')
        },
        data: JSON.stringify({
            messages: messages
        })
    };

    $.ajax(settings).done(function (response) {
        const message = response.message;
        messages.push({
            "role": message.role,
            "content": message.content
        });

        const htmlText = window.markdownit().render(message.content);
        const botMessageHtml = '<pre><div class="message left-side" id="' + CryptoJS.MD5(htmlText) + '">'
            + htmlText + '</div><i class="far fa-clipboard ml-1 btn btn-outline-dark" id="'
            + CryptoJS.MD5(htmlText) + '-copy"></i></pre>';
        chatbox.append(botMessageHtml);

        // Add event listener to the copy icon 
        var copyIcon = document.getElementById(CryptoJS.MD5(htmlText) + '-copy');
        var copyText = document.getElementById(CryptoJS.MD5(htmlText));

        copyIcon.addEventListener("click", function () {
            var tempTextarea = document.createElement("textarea");
            tempTextarea.value = copyText.textContent;
            document.body.appendChild(tempTextarea);
            tempTextarea.select();
            document.execCommand("copy");
            document.body.removeChild(tempTextarea);

            // Display "Copied!" popup
            var copyPopup = document.getElementById("copy-popup");
            copyPopup.style.display = "block";
            setTimeout(function () {
                copyPopup.style.display = "none";
            }, 1000); // Display for 1 second
        });

        chatbox.animate({ scrollTop: 20000000 }, "slow");
        sendButton.val("SUBMIT");
        sendButton.prop("disabled", false);
    }).catch(error => {
        sendButton.val("Error");
        let errorText = "Error: " + 'Message not found.';
        let errorMessage = '<pre><div class="message left-side  text-danger" >' + errorText + '</div></pre>';
        chatbox.append(errorMessage);
        chatbox.animate({ scrollTop: 20000000 }, "slow");
    });
}