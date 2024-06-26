"""Plotly Dash HTML layout override."""

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            <link rel="shortcut icon" type="image/png" href="/static/img/WWA_Amsbach_logo.svg">
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/WWA_Amsbach_logo.svg" class="logo" />
                    <h1>Lake Monitoring Data Overview </h1>
                </a>
                <nav>
                    <a href="/Waterlevels/"><h3>Water levels</h3></a>
                    <a href="/Depthprofiles/"><h3>Depth profiles</h3></a>
                    <a href="/DepthProfileTrends/"><h3>Depth trends</h3></a>
                    <a href="/MeanConcentrations/"><h3>Mean concentration trends</h3></a>
                     <a href="/SpecieRelations/"><h3>Specie Relationships</h3></a>
                </nav>
              </div>
            </header>
            
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""
