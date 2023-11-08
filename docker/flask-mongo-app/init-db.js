db = db.getSiblingsDB("animal_db");
db.animal_tb.drop()

db.animal_tb.insertMany([
    {
        "id": 1,
        "name" : "Lion",
        "type" :"Wild"
    },
    {
        "id": 2,
        "name": "Goat",
        "type": "Messi"
    } ,
    {
        "id":3,
        "name":"Tiger",
        "type":"wild"
    }

]);