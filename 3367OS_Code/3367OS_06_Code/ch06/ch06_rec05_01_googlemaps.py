import csv
import gviz_api

def get_page_template():
    page_template = """
    <html>
      <script src="https://www.google.com/jsapi" type="text/javascript"></script>
      <script>
        google.load('visualization', '1', {packages:['geochart', 'table']});

        google.setOnLoadCallback(drawMap);
        function drawMap() {
            var json_data = new google.visualization.DataTable(%s, 0.6);
            
            var options = {colorAxis: {colors: ['#eee', 'green']}};
            var mymap = new google.visualization.GeoChart(
                                document.getElementById('map_div'));
            mymap.draw(json_data, options);
            
            var mytable = new google.visualization.Table(
                                document.getElementById('table_div'));
            mytable.draw(json_data, {showRowNumber: true})
        }
      </script>
      <body>
        <H1>Median Monthly Disposable Salary World Countries</H1>

        <div id="map_div"></div>
        <hr />
        <div id="table_div"></div>

        <div id="source">
        <hr />
        <small>
        Source: 
        <a href="http://www.numbeo.com/cost-of-living/prices_by_country.jsp?displayCurrency=EUR&itemId=105">
        http://www.numbeo.com/cost-of-living/prices_by_country.jsp?displayCurrency=EUR&itemId=105
        </a>
        </small>
        </div>
      </body>
    </html>
    """
    return page_template


def main():
    # Load data from CVS file
    afile = "median-dpi-countries.csv"
    datarows = []
    with open(afile, 'r') as f:
        reader = csv.reader(f)
        reader.next()  # skip header
        for row in reader:
            datarows.append(row)

    # Describe data
    description = {"country": ("string", "Country"),
                       "dpi": ("number", "EUR"), }

    # Build list of dictionaries from loaded data
    data = []
    for each in datarows:
        data.append({"country": each[0],
                     "dpi": (float(each[1]), each[1])})

    # Instantiate DataTable with structure defined in 'description'
    data_table = gviz_api.DataTable(description)

    # Load it into gviz_api.DataTable
    data_table.LoadData(data)

    # Creating a JSon string
    json = data_table.ToJSon(columns_order=("country", "dpi"),
                             order_by="country", )
    
    # Put JSON string into the template
    # and save to output.html
    with open('output.html', 'w') as out:
        out.write(get_page_template() % (json,))

if __name__ == '__main__':
    main()
