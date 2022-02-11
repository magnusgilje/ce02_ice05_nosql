from pickle import TRUE
from typing import Optional
from fastapi import FastAPI
from pythoncircle import Circle
import re
import uuid
from azure.cosmos import CosmosClient

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/area/{radius}")
def read_area(radius: float):
    myC = Circle(float(radius))
    return {"area": myC.area()}

@app.get("/circumference/{radius}")
def read_circumference(radius: float):
    myC = Circle(float(radius))
    return {"circumference": myC.perimeter()}

@app.get("/range/{range}")
def read_range(range: str):

    match = re.match('(\d*)-(\d*)',range)
    if match:
        areas = []
        lower = int(match.group(1))
        higher = int(match.group(2))
        x=lower
        while x <= higher:
            myC = Circle(float(x))
            x += 1
            area =         myC.area()
            areas.append(area)
        return {"areas:" : areas }

    else:
        return {"error:" : "No range found"}    

def check_if_exists(range: str):

    query = ("SELECT * from c where c.radius={0}".format(range))
    url="https://pea02.documents.azure.com:443/"
    key="" 

    client = CosmosClient(url, credential=key)

    database_name = 'ce02_pea02'
    database = client.get_database_client(database_name)
    container_name = 'container_circles'
    container = database.get_container_client(container_name)
    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))

    return len(items)

@app.get("/cosmos-range/{range}")
def read_cosmos_range(range: str):

    match = re.match('(\d*)-(\d*)',range)
    if match:
        areas = {}
        lower = int(match.group(1))
        higher = int(match.group(2))
        x=lower
        while x <= higher:
            radius = float(x)
            myC = Circle(radius)
            x += 1
            areas[radius]=(myC.area())

            if check_if_exists(radius) > 0:
                print("already added {0} to database".format(radius))
            else:
                cosmos_add({    
                    'id': str(uuid.uuid4()),
                    'radius' : radius,
                    'area' :(myC.area()),
                    'perimeter' :(myC.perimeter()),
                    'extra': "test"
                    }
                )

        return areas
    else:
        return {"error:" : "No range found"}   


def add_circle_info(conn, radius: float, area: float, perimeter: float):
    cursor = conn.cursor()
    cursor.execute("""
    insert into Circles (cohort,radius,area,perimeter)
    values (?,?,?,?) """ , 'pea', radius, area, perimeter)

    # Commit and close
    conn.commit()

def cosmos_add(summary):

    url="https://pea02.documents.azure.com:443/"
    key="" 

    client = CosmosClient(url, credential=key)

    database_name = 'ce02_pea02'
    database = client.get_database_client(database_name)
    container_name = 'container_circles'
    container = database.get_container_client(container_name)
    container.upsert_item(summary)
