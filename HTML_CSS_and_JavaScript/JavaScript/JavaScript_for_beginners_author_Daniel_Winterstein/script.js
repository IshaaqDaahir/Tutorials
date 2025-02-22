function view_new_logo_1() {
    win_width = 500;
    win_height = 600;

    win_left = (screen.availWidth) - (win_width/2);
    win_top = (screen.availHeight) - (win_height/2);

    objNewLogo = window.open("RocolLogo", "logo", "width=500,height=600,left="+win_left+"top="+win_top);
    RocolLogo = "rocollogo.jpg";
    objNewLogo.onfocus() = view_new_logo();
}

function view_new_logo_2() {
    win_width = 500;
    win_height = 600;

    win_left_old = (screen.availWidth/3) - (win_width);
    win_top_old = (screen.availHeight/3) - (win_height);

    objOldLogo = window.open("oldRocolLogo", "oldlogo", "width=500,height=600,left="+win_left_old+"top="+win_top_old);
    oldRocolLogo = "oldRocolLogo.jpg";
    objOldLogo.onfocus() = view_new_logo();
}

function view_new_logo_3() {
    objNewHTML = window.open("", "newHTML", "width=400,height=400");
    newHTML = "newHTML.jpg";

    objNewHTML.document.write("<html><head>");
    objNewHTML.document.write("<title>Rocol Art</title>");
    objNewHTML.document.write("</head><body>");
    objNewHTML.document.write("<h1>Welcome!</h1><p>Please decide which logo you would like to choose.</p>");
    objNewHTML.document.write("<p><a href='oldRocolLogo.jpg' onclick='view_new_logo_2();'>The Old Logo</a></p>");
    objNewHTML.document.write("<p><a href='rocollogo.jpg' onclick='view_new_logo_1();'>The New Logo</a></p>");
    objNewHTML.document.write("</body></html>");

    objNewHTML.onfocus() = view_new_logo();

    /* objNewHTML.close();
    onclick="opener.objNewHTML.close();" */
}