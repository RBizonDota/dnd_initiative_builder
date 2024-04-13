document.querySelector("button").onclick = function () {
    eel.get_chars()(function (chars) {
        var old_tbl = document.getElementsByTagName("table"), index;

        for (index = old_tbl.length - 1; index >= 0; index--) {
            old_tbl[index].parentNode.removeChild(old_tbl[index]);
        }

        const body = document.body,
            tbl = document.createElement('table');
        tbl.style.width = '100px';
        tbl.style.border = '1px solid black';
        console.log(chars);
        for (let i = 0; i < chars.length; i++) {
            const tr = tbl.insertRow();
            for (let j = 0; j < chars[0].length; j++) {
                console.log(chars[i][j]);
                const td = tr.insertCell();
                td.appendChild(document.createTextNode(chars[i][j]));
                td.style.border = '1px solid black';
            }
        }
        body.appendChild(tbl);
    })
}