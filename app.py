from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return "<html><body><b>Hello,World</b></body></html>"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
