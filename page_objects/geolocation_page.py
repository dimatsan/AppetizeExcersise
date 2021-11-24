from seleniumbase import BaseCase

class GeolocationPage(BaseCase):
    get_coordinates_button = "button"
    latitude = "#lat-value"
    longitude = "#long-value"

    gps_latitude = "#latitude"
    gps_longitude = "#longitude"
    gps_get_address_btn = '''button[onclick="codeLatLng(1)"]'''
    gps_location = "#iwtitle"


    def open_geolocation_page(self):
        self.open("https://the-internet.herokuapp.com/geolocation")

    # helper method that determines your location based on provided latitude and longitude and prints it to the console
    def get_my_location(self, lat, long):
        self.open_new_window()
        self.open("https://www.gps-coordinates.net/")
        self.set_value(self.gps_latitude, lat)
        self.set_value(self.gps_longitude, long)
        self.click(self.gps_get_address_btn)
        self.wait_for_element_present(self.gps_location)
        myLocation = self.get_text(self.gps_location)
        print("\nYour current location is: " + myLocation)