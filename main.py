from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def ret_square1(num: int):
	return num*num
	
@app.post("/{num}")
def ret_square2(num):
	number = int(num)
	return number*number
