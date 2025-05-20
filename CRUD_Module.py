import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'DogsAreCool'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31018
        DB = 'ACC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

#Create method to implement C in CRUD
    def create(self, data):
        """
        Method inserts new data to the collection
        :param data: data to be inserted
        :return: True if inserted successfully
        """
        if data is not None:
            insert_data = self.database.animals.insert_one(data)
            if insert_data.acknowledged:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")


# Create method to implement the R in CRUD.
    def read(self, data_search):
        """
        Method to get data from the collection
        :param data_Search: data that isbeing searched for within collection
        :return: read_Data data being searched if found
        """
        if data_search is not None:
             read_data = self.database.animals.find(data_search)
             if read_data is not None:
                return read_data
             else:
                return "Data not Found"
        else:
            return "Search parameters are empty"

# Create method to implement the U in CRUD.
    def update(self, data_search, new_data):
        """
        Method to update data already within the collection
        :param data_Search:  data to be updated
        :param new_Data: new data to update dataSearch
        :return: number of items that were updated
        """
        if data_search is not None:
            updated_data = self.database.animals.update_one(data_search, new_data)
            return updated_data.modified_count
        else:
            return "Data not Found to Update"

# Create method to implement the D in CRUD.
    def delete(self, data):
        """
        Method to delete data from a collection
        :param data: attributes to delete
        :return: how many items were deleted
        """
        if data is not None:
            deleted_count = self.database.animals.delete_one(data)
            return deleted_count.deleted_count
        else:
            return "Data not Found to Delete"



