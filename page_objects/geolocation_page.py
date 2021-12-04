from seleniumbase import BaseCase

class GeolocationPage(BaseCase):
    get_coordinates_button = "button"
    latitude = "#lat-value"
    longitude = "#long-value"

    gps_latitude = "#latitude"
    gps_longitude = "#longitude"
    gps_get_address_btn = '''button[onclick="codeLatLng(1)"]'''
    gps_location = "#iwtitle"

    def get_coordinates(self):
        self.click(GeolocationPage.get_coordinates_button)
        myLat = self.get_text(GeolocationPage.latitude)
        myLong = self.get_text(GeolocationPage.longitude)
        print("\nYour latitude is: " + myLat + "\nYour longitude is: " + myLong)


