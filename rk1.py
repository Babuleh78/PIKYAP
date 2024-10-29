class CD:
    def __init__(self, cd_id, title, artist, genre, minutes):
        self.cd_id = cd_id  
        self.title = title   
        self.artist = artist 
        self.genre = genre   
        self.duration = minutes
    def __repr__(self):
        return f"CD(ID: {self.cd_id}, Title: '{self.title}', Artist: '{self.artist}', Genre: '{self.genre}', Minutes: '{self.duration}') \n"

class Shop:
    def __init__(self, library_id, name):
        self.library_id = library_id 
        self.name = name              
        self.cds = []                 
    def add_cd(self, cd):
        self.cds.append(cd)
    def __repr__(self):
        return f"Library(ID: {self.library_id}, Name: '{self.name}', CDs: {self.cds}) \n "

class CDLibrary:
    def __init__(self):
        self.relationships = []
    def add_relationship(self, cd, library):
        self.relationships.append((cd, library))
        library.add_cd(cd)  
    def __repr__(self):
        return f"CDLibrary(Relationships: {len(self.relationships)}) \n"
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


if __name__ == "__main__":
    cd1 = CD(1, "Thriller", "Michael Jackson", "Pop", 40)
    cd2 = CD(2, "Back in Black", "AC/DC", "Rock", 35)
    cd3 = CD(3, "The Dark Side of the Moon", "Pink Floyd", "Rock", 123)
    cd4 = CD(4, "Kiss Of Death", "Motorhead", "Metal", 51)
    cd5= CD(5, "Alison Hell", "Annihilator", "Metal", 44)
    cd6 = CD(6, "The Number Of The Beast", "Iron Maiden", "Metal", 55)
    library1 = Shop(1, "Pop mania")
    library2 = Shop(2, "Rock House")
    library3 = Shop(3,  "Metall Invaders")

    cd_library = CDLibrary()
    
    cd_library.add_relationship(cd1, library1)
    cd_library.add_relationship(cd2, library1)
    cd_library.add_relationship(cd3, library2)
    cd_library.add_relationship(cd4, library3)
    cd_library.add_relationship(cd5, library3)
    cd_library.add_relationship(cd6, library3)
    cd_library.add_relationship(cd6, library2)
    cd_library.add_relationship(cd4, library1)
    cd_library.add_relationship(cd1, library2)
    cd_library.add_relationship(cd3, library3)

    # Вывод всех связанных дисков и магазинов
    print("CDs in Shops:")
    for library_name, cds in cd_library.list_cds_in_libraries().items():
        print(f"{library_name}: {cds}")

    # Подсчет длительности дисков в каждом магазине и вывод
    print("Count of Rock CDs in Shops:")
    for library_name, count in cd_library.count_total_duration_per_library():
        print(f"{library_name}: {count} minutes")

    # Вывод магазинов, в названии которых присутствует слово 'House' и их содержимого
    print("Shops containing 'House' and their names:")
    for library_name, cds in cd_library.list_libraries_with_cd_in_name('House').items():
        print(f"{library_name}: {cds}")
