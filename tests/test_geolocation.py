from page_objects.geolocation_page import GeolocationPage

class GeolocationTest(GeolocationPage):
    # should provide latitude and longitude upon clicking "Where am I?" button
    def test_geolocation(self):
        self.open("https://the-internet.herokuapp.com/geolocation")
        self.click(GeolocationPage.get_coordinates_button)
        myLat = self.get_text(GeolocationPage.latitude)
        myLong = self.get_text(GeolocationPage.longitude)
        print("\nYour latitude is: " + myLat + "\nYour longitude is: " + myLong)

        # quick extra step that prints your location based on provided latitude and longitude to the console
        self.get_my_location(myLat, myLong)


