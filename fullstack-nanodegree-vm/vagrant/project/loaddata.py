from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import zoo, Base, animal

engine = create_engine('sqlite:///zoomenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Zoo for Cleveland
zoo1 = Zoo(zoo_name="Cleveland ")

session.add(zoo1)
session.commit()

animal2 = Animal(name="Donkey", species="Equus africanus asinus",
                     diet="hay", description="", zoo=zoo1)

session.add(animal2)
session.commit()


animal1 = Animal(name="sloth", species="Pilosa",
                     diet="leaves", description="", zoo=zoo1)

session.add(animal1)
session.commit()

animal2 = Animal(name="sea horse", species="Hippocampus",
                     diet="plankton", description="", zoo=zoo1)

session.add(animal2)
session.commit()

animal3 = Animal(name="parrot fish", species="Chordate",
                     diet="fish", description="", zoo=zoo1)

session.add(animal3)
session.commit()

animal4 = Animal(name="nuteria", species="Myocastor coypus",
                     diet="anything", description="", zoo=zoo1)

session.add(animal4)
session.commit()

animal5 = Animal(name="wood duck", species="Aix sponsa",
                     diet="duck weed", description="", zoo=zoo1)

session.add(animal5)
session.commit()

animal6 = Animal(name="giraffe", species="Giraffa camelopardalis",
                     diet="tree leaves", description="", zoo=zoo1)

session.add(animal6)
session.commit()

animal7 = Animal(name="chimpanzee", species="Pan troglodytes",
                     diet="bananas", description="", zoo=zoo1)

session.add(animal7)
session.commit()

animal8 = Animal(name="falcon", species="Falco peregrinus",
                     diet="rodents", description="", zoo=zoo1)

session.add(animal8)
session.commit()




# Zoo for Columbus
zoo1 = Zoo(zoo_name="Columbus ")

session.add(zoo1)
session.commit()


animal1 = Animal(name="reindeer", species="Rangifer tarandus",
                     diet="Santas Cookies", description="", zoo=zoo1)

session.add(animal1)
session.commit()

animal2 = Animal(name="alligator turtle", species=" Macrochelys temminckii",
                     diet="lettus", description="", zoo=zoo1)

session.add(animal2)
session.commit()

animal3 = Animal(name="grizzly bear", species=" Ursus arctos horribilis",
                     diet="Just about anything", description="", zoo=zoo1)

session.add(animal3)
session.commit()

animal4 = Animal(name="stork", species="Ciconiidae",
                     diet="fish", description="", zoo=zoo1)

session.add(animal4)
session.commit()

animal2 = Animal(name="snapping turtle", species=" Chelydra serpentina",
                     diet="leaves", description="", zoo=zoo1)

session.add(animal2)
session.commit()


# Zoo for Cincinnati
zoo1 = Zoo(zoo_name="Cincinnati ")

session.add(zoo1)
session.commit()


animal1 = Animal(name="anteater", species="Vermilingua",
                     diet="ants", description="", zoo=zoo1)

session.add(animal1)
session.commit()

animal2 = Animal(name="black bear", species="Ursus americanus",
                     diet="picnic baskets", description="", zoo=zoo1)

session.add(animal2)
session.commit()

animal3 = Animal(name="african elephant", species=" Elephantidae",
                     diet="leaves and bark", description="", zoo=zoo1)

session.add(animal3)
session.commit()

animal4 = Animal(name="porcupine", species="Rodent",
                     diet="pizza", description="", zoo=zoo1)

session.add(animal4)
session.commit()

animal5 = Animal(name="flamingo", species="Phoenicopterus",
                     diet="shimp", description="", zoo=zoo1)

session.add(animal5)
session.commit()

animal6 = Animal(name="camel", species="Camelus",
                     diet="hay", description="", zoo=zoo1)

session.add(animal6)
session.commit()

animal7 = Animal(name="alpaca", species="Camelus",
                     diet="hay", description="", zoo=zoo1)

session.add(animal7)
session.commit()





print "added menu items!"
