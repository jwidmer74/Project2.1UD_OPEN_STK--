from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup2 import Category, Base, Item

engine = create_engine('sqlite:///catalog.db')
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

category1 = Category(name="Soccer")

session.add(category1)
session.commit()

Item2 = Item(name="net", description="standard size",
                     title="net", category=category1)

session.add(Item2)
session.commit()


Item1 = Item(name="backboard", description="plastic and wooden",
                     title="backboard", category=category1)

session.add(Item1)
session.commit()



category2 = Category(name="Basketball")
session.add(category2)
session.commit()

Item2 = Item(name="Stick", description="long piece of wood",
                     title="stick", category=category2)

session.add(Item2)
session.commit()


Item1 = Item(name="Googles", description="put over your eyes",
                     title="Googles", category=category2)

session.add(Item1)
session.commit()

category3 = Category(name="Baseball")

session.add(category3)
session.commit()

Item2 = Item(name="bat", description="wooden or aluminum",
                     title="bat", category=category3)

session.add(Item2)
session.commit()


Item1 = Item(name="glove", description="right and left handed",
                     title="glove", category=category3)

session.add(Item1)
session.commit()

category4 = Category(name="Frisbee")

session.add(category4)
session.commit()

Item2 = Item(name="Frisbee Net", description="iron chain",
                     title="Frisbee Net", category=category4)

session.add(Item2)
session.commit()


Item1 = Item(name="Signed Frisbee", description="Frisbee signed by legions of the game",
                     title="Signed", category=category4)

session.add(Item1)
session.commit()

category5 = Category(name="Snowboarding")

session.add(category5)
session.commit()

Item2 = Item(name="Snow Board gooogles", description="plastic",
                     title="Snow Board gooogles", category=category5)

session.add(Item2)
session.commit()


Item1 = Item(name="Snowboards", description="Fiberglass",
                     title="Snowboards", category=category5)

session.add(Item1)
session.commit()

print "added items!"