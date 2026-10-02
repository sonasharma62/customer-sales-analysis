import pandas as pd
import matplotlib.pyplot as plt


print("Customer Sales Analysis project")

data = {
    "Customer": ["Sona", "Rahul", "Priya", "Amit", "Neha"],
    "City": ["Delhi", "Mumbai", "Kolkata", "Delhi", "Mumbai"],
    "Product": ["Laptop", "Mobile", "Chair", "Laptop", "Mobile"],
    "Quantity": [2, 3, 4, 1, 2],
    "Sales": [100000, 60000, 20000, 50000, 40000],
    "Profit": [15000, 9000, 4000, 7000, 6000]
}

df = pd.DataFrame(data)

# print(df)

total_sales = df["Sales"].sum()
print("Total Sales",total_sales)

total_profit = df["Profit"].sum()
print("Total profit", total_profit)


total_quantity = df["Quantity"].sum()
print("Total quantity",total_quantity)

average_sales = df["Sales"].mean()
print("average Sales",average_sales)

highest_sales = df["Sales"].max()
print("highest_sales",highest_sales)


product_sales = df.groupby("Product")["Sales"].sum()
plt.bar(product_sales.index, product_sales.values)

plt.title("Product wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.savefig("Product_sales.png")
plt.show()

highest_product = product_sales.idxmax()

print("Highest Selling Product:",highest_product)

print("Product-wise Sales:")
print(product_sales)


city_sales = df.groupby("City")["Sales"].sum()
print("City-wise Sales: ")
print(city_sales)



df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

print("Profit Margin: ")
print(df[["Product", "Profit_Margin"]])



# ------ City wise Sales Chart------------#


plt.bar(city_sales.index, city_sales.values)

plt.title("City wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")

plt.savefig("City_sales.png")
plt.show()


print("\n===========FINAL PROJECT SUMMARY ===========")

print("Total Sales",total_sales)
print("Total Profit", total_profit)
print("Total Quatity", total_quantity)
print("Average Sales", average_sales)
print("Highest Sales", highest_sales)
print("Highest Selling Product:", highest_product)