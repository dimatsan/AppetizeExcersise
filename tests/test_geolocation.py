from page_objects.geolocation_page import GeolocationPage

class GeolocationTest(GeolocationPage):
    # should provide latitude and longitude upon clicking "Where am I?" button
    def test_geolocation(self):
        self.open("https://the-internet.herokuapp.com/geolocation")
        self.get_coordinates()


