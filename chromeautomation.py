import webbrowser as wb 

def webauto():
    chrome_path = '/usr/bin/google-chrome'
    URLS = (
        "gmail.com",
        "google.com",
        "youtube.com",
        "github.com"
    )
    for url in URLS:
        print("Opening: " + url)
        wb.get(chrome_path).open(url)

webauto()