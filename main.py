from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    n: int

@app.post("/")
def ret_square1(num: Number):
	N = num.n
	return N*N
	
@app.get("/{num}")
def ret_square2(num):
	number = int(num)
	return number*number
