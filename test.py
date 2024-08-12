import streamlit as st

# HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html>
  <body>
    <h3>Click the button to get your current position:</h3>
    <button onclick="getLocation()">Get Location</button>

    <script>
      const options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0,
      };

      function success(pos) {
        const crd = pos.coords;

        console.log("Your current position is:");
        console.log(`Latitude : ${crd.latitude}`);
        console.log(`Longitude: ${crd.longitude}`);
        console.log(`More or less ${crd.accuracy} meters.`);
      }

      function error(err) {
        console.warn(`ERROR(${err.code}): ${err.message}`);
      }

      function getLocation() {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(success, error, options);
        } else {
          console.warn("Geolocation is not supported by this browser.");
        }
      }
    </script>
  </body>
</html>
"""

# Display the HTML and JavaScript in the Streamlit app
st.components.v1.html(html_code)
