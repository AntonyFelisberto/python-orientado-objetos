from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sql_alchemy import Entity, base
from sqlalchemy.orm import relationship

class Inventory(Entity,base):
    __tablename__ = 'inventory'

    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    avaiable = Column(Boolean)
    color = Column(String)

    def __init__(self,make,model,year,avaiable,color):
        Entity.__init__(self)
        self.make = make
        self.model = model
        self.year = year
        self.avaiable = avaiable
        self.color = color

class History(Entity, base):
    __tablename__ = 'history'
    history_type = Column(String)
    inventory_id = Column(Integer,ForeignKey('inventory.id'))

    def __init__(self,history_type):
        Entity.__init__(self)
        self.history_type = history_type

    inventory = relationship("Inventory",back_populates="history")

Inventory.history = relationship(
    "History",order_by=History.id,back_populates="inventory"
)