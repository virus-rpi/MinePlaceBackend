from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.178.53:8080",
    "http://192.168.178.53"
    "http://dev_mineplace.virusrpi.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

shops = []
with open("database.txt", "r") as file:
    shops_string = file.readline()
    shops = eval(shops_string)


@app.get("/")
async def root():
    return {"message": "Hello World! This is the backend for the MinePlace"}


@app.get("/texture/{name}")
async def get_textures(name: str):
    return FileResponse("item_textures/" + name + ".png")


@app.get("/shops/get_all")
async def get_all_shops():
    global shops
    return {"shops": shops}


@app.get("/shops/create/{name}/{owner}/{location}/{items}")
async def create_shop(name, owner, location, items):
    rating: float = -1.0
    print(name, owner, location, [items])
    global shops
    shops.append({"name": name, "owner": owner, "location": location, "rating": rating, "items": [items]})
    with open("database.txt", "w") as file:
        file.write(str(shops))
    return {"id": {}}
