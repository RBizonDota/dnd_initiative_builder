document.querySelector("button").onclick = function () {
    eel.get_chars()(function (chars) {
        var old_tbl = document.getElementsByTagName("table"), index;

        for (index = old_tbl.length - 1; index >= 0; index--) {
            old_tbl[index].parentNode.removeChild(old_tbl[index]);
        }

        const body = document.body,
            tbl = document.createElement('table');
        tbl.style.width = '600px'
        tbl.style.border = '2px solid black';
        tbl.style.margin = '2% auto';
        tbl.style.font = '25px Arial';
        tbl.style.color =  '#ffffff';
        tbl.style.background =  '#b15124';
        tbl.style.borderCollapse = "collapse";
        const names = [ 'Имя персонажа', 'Игрок', 'Инициатива','Бонус','Статус','Ходов статуса'];
        const tr = tbl.insertRow();
        for (let j = 0; j < names.length; j++) {
            console.log(names[j]);
            const td = tr.insertCell();
            td.appendChild(document.createTextNode(names[j]));
            td.style.border = '3px solid black';
        }
        
        for (let i = 0; i < chars.length; i++) {
            const tr = tbl.insertRow();
            for (let j = 0; j < chars[0].length; j++) {
                console.log(chars[i][j]);
                const td = tr.insertCell();
                td.appendChild(document.createTextNode(chars[i][j]));
                td.style.border = '2px solid black';
            }
            const td = tr.insertCell();
            td.appendChild(document.createTextNode(' '));
            td.style.border = '2px solid black';
            const td2 = tr.insertCell();
            td2.appendChild(document.createTextNode(' '));
            td2.style.border = '2px solid black';
        }
        body.appendChild(tbl);
    })
}