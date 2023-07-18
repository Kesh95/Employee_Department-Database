from fastapi import FastAPI
import database
import uvicorn
from basemodel import Item
app = FastAPI()

@app.get("/",tags=["API"])
async def index():
    l = "CALL get_emp_rit()"
    k = database.call(l)
    values = []
    for i in k:
        detail_dict = {"e_id": i[0],
                       "e_name": i[1],
                       "d_id": i[2],
                       "salary": i[3]
                       }
        values.append(detail_dict)
    return values



@app.put( "/", tags= ["API"])
async def index( e_id:int ,item:Item):
    l = "CALL update_emp_rit  ('{}','{}','{}','{}')".format(e_id, item.e_name,item.d_id,item.salary)
    k=database.call(l)
    values = []
    for i in k:
        detail_dict = {"e_id": i[0],
                       "e_name": i[1],
                       "d_id": i[2],
                       "salary": i[3]}

        values.append(detail_dict)
    return values
@app.post( "/", tags= ["API"])
async def index( e_id :int,item:Item):
    l = "CALL create_emp_rit('{}','{}','{}','{}')".format(e_id, item.e_name,item.d_id,item.salary)
    k = database.call(l)
    values = []
    for i in k:
        detail_dict = {"e_id": i[0],
                       "e_name": i[1],
                       "d_id": i[2],
                       "salary": i[3]
                       }
        values.append(detail_dict)
    return values

@app.delete( "/", tags= ["API"])
async def index( ID:int,item:Item):
    l = "CALL delete_emp_rit('{}')".format(ID)
    k = database.call(l)
    values = []
    for i in k:
        detail_dict = {"e_id": i[0],
                       "e_name": i[1],
                       "d_id": i[2],
                       "salary": i[3]
                       }
        values.append(detail_dict)
    return values





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

