function copyToClipboard(text) {
    const textField = document.createElement('textarea');
    textField.innerText = text;
    document.body.appendChild(textField);
    textField.select();
    document.execCommand('copy');
    document.body.removeChild(textField);
}

function copyTextElement(id, text) {
    const TextId = document.getElementById(id);
    TextId.addEventListener('click', function () {
        const textToCopy = TextId.innerText;
        copyToClipboard(textToCopy);
        alert(text)
    });
}

copyTextElement("ip", "IP copied to clipboard")
copyTextElement("isp", "Internet provider copied to clipboard")
copyTextElement("country", "Country copied to clipboard")