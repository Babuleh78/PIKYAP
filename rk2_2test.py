import unittest
#проверка взаимодействия классов
class CD:
    def __init__(self, cd_id, title, artist, genre, minutes):
        self.cd_id = cd_id  
        self.title = title   
        self.artist = artist 
        self.genre = genre   
        self.duration = minutes

    def __repr__(self):
        return f"CD(ID: {self.cd_id}, Title: '{self.title}', Artist: '{self.artist}', Genre: '{self.genre}', Minutes: '{self.duration}')"

class Shop:
    def __init__(self, library_id, name):
        self.library_id = library_id 
        self.name = name              
        self.cds = []                 

    def add_cd(self, cd):
        self.cds.append(cd)

    def __repr__(self):
        return f"Library(ID: {self.library_id}, Name: '{self.name}', CDs: {self.cds})"

class CDLibrary:
    def __init__(self):
        self.relationships = []

    def add_relationship(self, cd, library):
        self.relationships.append((cd, library))
        library.add_cd(cd)

    def __repr__(self):
        return f"CDLibrary(Relationships: {len(self.relationships)})"

    def list_cds_in_libraries(self):
        result = {}
        for cd, library in self.relationships:
            if library.name not in result:
                result[library.name] = []
            result[library.name].append(cd)
        return result

    def count_total_duration_per_library(self):
        duration_count = {}
        for cd, library in self.relationships:
            if library.name not in duration_count:
                duration_count[library.name] = 0
            duration_count[library.name] += cd.duration  
        return sorted(duration_count.items(), key=lambda x: x[1], reverse=True)

    def list_libraries_with_cd_in_name(self, name_part):
        result = {}
        for cd, library in self.relationships:
            if name_part in library.name:
                if library.name not in result:
                    result[library.name] = []
                result[library.name].append(cd)
        return result

class TestCDLibraryAdditional(unittest.TestCase):
    
    def setUp(self):
        self.cd1 = CD(1, "Thriller", "Michael Jackson", "Pop", 40)
        self.cd2 = CD(2, "Back in Black", "AC/DC", "Rock", 35)
        self.cd3 = CD(3, "The Dark Side of the Moon", "Pink Floyd", "Rock", 123)
        self.cd4 = CD(4, "Kiss Of Death", "Motorhead", "Metal", 51)
        self.cd5 = CD(5, "Alison Hell", "Annihilator", "Metal", 44)
        self.cd6 = CD(6, "The Number Of The Beast", "Iron Maiden", "Metal", 55)
        
        self.library1 = Shop(1, "Pop mania")
        self.library2 = Shop(2, "Rock House")
        self.library3 = Shop(3, "Metall Invaders")

        self.cd_library = CDLibrary()
        self.cd_library.add_relationship(self.cd1, self.library1)
        self.cd_library.add_relationship(self.cd2, self.library1)
        self.cd_library.add_relationship(self.cd3, self.library2)
        self.cd_library.add_relationship(self.cd4, self.library3)
        self.cd_library.add_relationship(self.cd5, self.library3)
        self.cd_library.add_relationship(self.cd6, self.library3)
        self.cd_library.add_relationship(self.cd6, self.library2)
        self.cd_library.add_relationship(self.cd4, self.library1)
        self.cd_library.add_relationship(self.cd1, self.library2)
        self.cd_library.add_relationship(self.cd3, self.library3)

    def test_add_relationship(self):
        new_cd = CD(7, "New Album", "New Artist", "New Genre", 60)
        new_library = Shop(4, "New Library")
        
        self.cd_library.add_relationship(new_cd, new_library)
        self.assertIn(new_cd, new_library.cds)
        self.assertIn((new_cd, new_library), self.cd_library.relationships)

    def test_count_total_duration_empty_library(self):
        empty_library = Shop(5, "Empty Library")
        empty_cd_library = CDLibrary()
        result = empty_cd_library.count_total_duration_per_library()
        expected = []  
        self.assertEqual(result, expected)

  
    
if __name__ == "__main__":
    unittest.main()
