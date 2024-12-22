from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Analysis API</title>
    </head>
    <body>
        <h1>환영한다.</h1>
        <p>각기 다른 결과를 확인해보세요</p>
        <button onclick="window.location.href='/statistics'">json으로 보기</button>
        <button onclick="window.location.href='/distribution-plot'">확인하기</button>
        <button onclick="window.location.href='/pca-plot'">확인하기</button>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/statistics")
def get_statistics():
    statistics = {
        "mean": {"feature1": 5.5, "feature2": 3.2},
        "std_dev": {"feature1": 1.2, "feature2": 0.8},
    }
    return JSONResponse(content=statistics)

@app.get("/distribution-plot")
def get_distribution_plot():
    return FileResponse("static/data_distribution.png")

@app.get("/pca-plot")
def get_pca_plot():
    return FileResponse("static/data_distribution.png")