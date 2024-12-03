import yaml



def count_class(data, class_name):
    count = 0
    if isinstance(data, dict): 
        for key, value in data.items(): 
            if key == class_name:  
                count += 1
            count += count_class(value, class_name) 
    if isinstance(data, list):
        for item in data:
            count += count_class(item, class_name)
    return count

# use fields as class_name
def tables_and_columns(data, class_name):
    table_names = []
    column_names = []
    if isinstance(data, list):
        for item in data:
            if "." in item:
                table = item.split(".")[0]
                column = item.split(".")[1]
                table_names.append(table)
                column_names.append(column)

    return table_names, column_names



file_name = "C:\\Users\\fan\\sample.yaml"

with open(file_name, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)


class_name = 'title'
title_count = count_class(data, class_name)
print(f"'{class_name}' appears {title_count} times")

class_name = 'fields'
tables, columns = tables_and_columns(data, class_name)
print(f"Tables: {tables}")
print(f"Columns: {columns}")
