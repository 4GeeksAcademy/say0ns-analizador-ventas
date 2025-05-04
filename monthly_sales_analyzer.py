# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]


def total_sales_by_product(data, product_key):
    total_sales=[]
    for day in data:
        total_sales.append(day[product_key])        
    total=sum(total_sales)
    return total


def average_daily_sales(data, product_key):
    avg_sales=[]
    for day in data:
        avg_sales.append(day[product_key])
    avg=sum(avg_sales)/len(avg_sales)
    return avg


def best_selling_day(data):
    datacopy=sales_data.copy()
    dia_max=max(data,key=lambda d: d["product_a"]+d["product_b"]+d["product_c"])
    suma=dia_max["product_a"]+dia_max["product_b"]+dia_max["product_c"]
    return f"Day {dia_max["day"]} and total of {suma}"


def days_above_threshold(data, product_key, threshold):
    count=0
    datacopy=sales_data.copy()
    days_above=[]
    for day in data:
        if day[product_key]>threshold:
            days_above.append(day["day"])
            count+=1
    print(f"Days when {product_key} exceed {threshold} are :{days_above}")
    return count
    


def top_product(data):
    datacopy=sales_data.copy()
    a=[]
    b=[]
    c=[]
    for day in data:
        a.append(day["product_a"])
        b.append(day["product_b"])
        c.append(day["product_c"])
    ventas_a=sum(a)
    ventas_b=sum(b)
    ventas_c=sum(c)
    
    if ventas_a>ventas_b or ventas_a>ventas_c:
        return f"product a with {ventas_a}"
    elif ventas_b>ventas_a or ventas_b>ventas_c:
        return f"product b with {ventas_b}"
    elif ventas_c>ventas_a or ventas_c>ventas_b:
        return f"product c with {ventas_c}"


def worst_selling_day(data):
    datacopy=sales_data.copy()
    dia_min=min(data,key=lambda d: d["product_a"]+d["product_b"]+d["product_c"])
    suma=dia_min["product_a"]+dia_min["product_b"]+dia_min["product_c"]
    return f"Day {dia_min["day"]} and total of {suma}"




# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("Day with lowest total sales:", worst_selling_day(sales_data))

