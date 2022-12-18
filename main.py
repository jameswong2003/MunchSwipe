import csv_writer

data = ['McDonalds', '$', '4/5', 'my house']
write_data = csv_writer.CSV_Retrieve('database/data.csv')
write_data.add_restaurant(data)