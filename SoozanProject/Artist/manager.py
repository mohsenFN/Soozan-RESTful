from Artist.models import DerivedArtist
from Utils.selectors import Selector

class NewArtist:

    def __init__(self, user_id, full_name,
                        art_name, location):

        self.user_id = user_id
        self.full_name = full_name
        self.art_name = art_name
        self.location = location


    def save(self):
        # Data Should be validated in API views (for this case Artist.viewes)
        new_artist = DerivedArtist(user = Selector.user_instance(self.user_id), full_name = self.full_name,
                                    art_name = self.art_name, location = self.location)

        new_artist.save()
