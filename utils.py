import random
import pandas as pd


def concat_arrays(arrays):
    concatenated = []
    for i in range(len(arrays[0])):
        for array in arrays:
            concatenated.append(array[i])
    return concatenated


def showProducts(n):
    values = []
    df = pd.read_csv("AIDB3.csv")
    products = df["Product Label"]
    sells2 = df["Sells"]
    stocks2 = df["Stock"]
    projectedR = df["Projected Restocking"]

    # print(len(sells2))
    # print(len(stocks2))
    # print(len(products))
    # print(len(projectedR))
    # x_axis = ["Product" + str(i) for i in range(n)]
    # for i in range(n):
    #     choices = [0.95, 0.97, 0.98, 0.99]
    #     sells = random.randint(10, 200)
    #     stock = random.randint(10, 200)
    #     value = [stock, sells, 0 if stock - sells > 0 else stock+sells]
    #     values.append(value)

    res = {
        "Products": [*products] * 2,
        "Units": [*stocks2, *sells2],
        "Name": ["stock"]*240 + ["sells"]*240
    }

    return res


def generateDotsData():
    n = 240
    shape = {
        "x_axis": [],
        "y_axis": [],
        "colors": []
    }
    df = pd.read_csv("AIDB3.csv")
    products = df["Product Label"]
    for i in range(n):
        # x_data = random.randint(0,100)
        y_data = random.randint(100, 250)
        # shape["x_axis"].append(x_data)
        shape["y_axis"].append(y_data)

    shape["colors"] = ["Restocking"] * n
    shape["x_axis"] = products

    # print(len(shape["x_axis"]))
    # print(len(shape["colors"]))
    # print(len(shape["y_axis"]))
    return shape
