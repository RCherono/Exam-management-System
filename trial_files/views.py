# views.py

from django.shortcuts import render
from django.db import connection
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def render_graph(request):
    # Connect to the PostgreSQL database
    with connection.cursor() as cursor:
        cursor.execute("SELECT column1, column2 FROM your_table;")
        rows = cursor.fetchall()

    # Convert data to a Pandas DataFrame
    df = pd.DataFrame(rows, columns=['column1', 'column2'])

    # Plotting using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(df['column1'], df['column2'])
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Your Title')
    plt.grid(True)

    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Embed the plot into the HTML template
    graphic = base64.b64encode(image_png).decode('utf-8')

    context = {'graphic': graphic}
    return render(request, 'your_template.html', context)
    # views.py

    from django.shortcuts import render
    from django.db import connection
    import pandas as pd
    import matplotlib.pyplot as plt
    from io import BytesIO
    import base64
    
    def render_graph(request):
        # Connect to the PostgreSQL database
        with connection.cursor() as cursor:
            cursor.execute("SELECT column1, column2 FROM your_table;")
            rows = cursor.fetchall()
    
        # Convert data to a Pandas DataFrame
        df = pd.DataFrame(rows, columns=['column1', 'column2'])
    
        # Plotting using Matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(df['column1'], df['column2'])
        plt.xlabel('X-axis label')
        plt.ylabel('Y-axis label')
        plt.title('Your Title')
        plt.grid(True)
    
        # Save plot to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
    
        # Embed the plot into the HTML template
        graphic = base64.b64encode(image_png).decode('utf-8')
    
        context = {'graphic': graphic}
        return render(request, 'your_template.html', context)
    