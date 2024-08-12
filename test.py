import streamlit as st
import streamlit.components.v1 as components

# HTML and JavaScript code to embed
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Store User Info Locally</title>
</head>
<body>

    <p id="user-info"></p>
    <p id="browser-info"></p>
    <p id="os-info"></p>

    <script>
        class DetectOS {
            constructor() {
                this.browser = this.searchString(this.dataBrowser())
                this.version = this.searchVersion(navigator.userAgent) || this.searchVersion(navigator.appVersion)
                this.OS = this.searchString(this.dataOS())
            }

            searchString(data) {
                for (let i = 0; i < data.length; i++) {
                    let
                        dataString = data[i].string,
                        dataProp = data[i].prop
                    this.versionSearchString = data[i].versionSearch || data[i].identity
                    if (dataString) {
                        if (dataString.indexOf(data[i].subString) !== -1) {
                            return data[i].identity
                        }
                    } else if (dataProp) {
                        return data[i].identity
                    }
                }
            }

            searchVersion(dataString) {
                let index = dataString.indexOf(this.versionSearchString)
                if (index === -1) return
                return parseFloat(dataString.substring(index+this.versionSearchString.length + 1))
            }

            dataBrowser() {
                return [
                    // Browser detection code here...
                    {
                        string: navigator.userAgent,
                        subString: "Chrome",
                        identity: "Chrome"
                    },
                    {
                        string: navigator.vendor,
                        subString: "Apple",
                        identity: "Safari",
                        versionSearch: "Version"
                    },
                    {
                        prop: window.opera,
                        identity: "Opera",
                        versionSearch: "Version"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "MSIE",
                        identity: "IE10",
                        versionSearch: "MSIE"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "Trident",
                        identity: "IE11",
                        versionSearch: "rv"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "Edge",
                        identity: "Edge",
                        versionSearch: "Edge"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "Firefox",
                        identity: "Firefox"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "Gecko",
                        identity: "Mozilla",
                        versionSearch: "rv"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "Mozilla",
                        identity: "Netscape",
                        versionSearch: "Mozilla"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "Netscape",
                        identity: "Netscape"
                    },
                    {
                        string: navigator.userAgent,
                        subString: "OmniWeb",
                        versionSearch: "OmniWeb/",
                        identity: "OmniWeb"
                    },
                    {
                        string: navigator.vendor,
                        subString: "iCab",
                        identity: "iCab"
                    },
                    {
                        string: navigator.vendor,
                        subString: "KDE",
                        identity: "Konqueror"
                    },
                    {
                        string: navigator.vendor,
                        subString: "Camino",
                        identity: "Camino"
                    }
                ]
            }

            dataOS() {
                return [
                    {
                        string: navigator.platform,
                        subString: 'Win',
                        identity: 'Windows'
                    },
                    {
                        string: navigator.platform,
                        subString: 'Mac',
                        identity: 'macOS'
                    },
                    {
                        string: navigator.userAgent,
                        subString: 'iPhone',
                        identity: 'iOS'
                    },
                    {
                        string: navigator.userAgent,
                        subString: 'iPad',
                        identity: 'iOS'
                    },
                    {
                        string: navigator.userAgent,
                        subString: 'iPod',
                        identity: 'iOS'
                    },
                    {
                        string: navigator.userAgent,
                        subString: 'Android',
                        identity: 'Android'
                    },
                    {
                        string: navigator.platform,
                        subString: 'Linux',
                        identity: 'Linux'
                    }
                ]
            }
        }

        const Detect = new DetectOS()

        document.getElementById("browser-info").innerText = "Browser: " + Detect.browser + " " + Detect.version;
        document.getElementById("os-info").innerText = "Operating System: " + Detect.OS;

        // Function to prompt user for their name if not already stored
        function askForUserName() {
            let firstName = localStorage.getItem('firstName');
            let lastName = localStorage.getItem('lastName');

            if (!firstName || !lastName) {
                firstName = prompt("Please enter your first name:");
                lastName = prompt("Please enter your last name:");

                localStorage.setItem('firstName', firstName);
                localStorage.setItem('lastName', lastName);
            }

            document.getElementById("user-info").innerText = `User: ${firstName} ${lastName}`;
        }

        // Check if user information is already stored
        askForUserName();

    </script>
</body>
</html>
"""

# Embed the HTML and JavaScript code in Streamlit
components.html(html_code, height=400)
