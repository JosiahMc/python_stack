function letterCount(string, letter) {
    var count = 0;
        string = string.toUpperCase();
        letter = letter.toUpperCase();
    for (var i=0, l=string.length; i<string.length; i += 1) {
        if (string[i] === letter) {
            count += 1;
        }
    }
    return count;
}

letterCount("Yellow WhaLes","l")