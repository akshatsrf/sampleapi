from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ret_square1(num: int):
	return num*num
	
@app.get("/{num}")
def ret_square2(num):
	number = int(num)
	return number*number
