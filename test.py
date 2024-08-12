import streamlit as st

# HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html>
  <body>
    <h3>Click the button to get your current position:</h3>
    <button onclick="getLocation()">Get Location</button>

    <p id="location">Your location will be displayed here.</p>

    <script>
      const options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0,
      };

      function success(pos) {
        const crd = pos.coords;

        document.getElementById("location").innerHTML = `
          Latitude: ${crd.latitude} <br>
          Longitude: ${crd.longitude} <br>
          Accuracy: ${crd.accuracy} meters
        `;
      }

      function error(err) {
        document.getElementById("location").innerHTML = `
          ERROR(${err.code}): ${err.message}
        `;
      }

      function getLocation() {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(success, error, options);
        } else {
          document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
        }
      }
    </script>
  </body>
</html>
"""

# Display the HTML and JavaScript in the Streamlit app
st.components.v1.html(html_code)
