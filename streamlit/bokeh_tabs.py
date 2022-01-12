# copied work

import bokeh
import bokeh.models
import markdown
import streamlit as st


def main():

    tabs = bokeh.models.Tabs(
        tabs=[
            layout_panel(),
            widgets_tables_panel(),
        ]
    )
    st.bokeh_chart(tabs)



def _chart():
    circle_chart = bokeh.plotting.figure(sizing_mode="stretch_both")
    circle_chart.circle(
        [1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5
    )
    return circle_chart



def layout_panel():
    text = """
    ## My Vision on the Bokeh Streamlit Integration

    I believe the integration with Bokeh **can give Streamlit Super Powers** if improved slightly.

    For example

    - Wrapping the Bokeh api into a more **Streamlit like Api** like `st.bokeh.datatable(my_dataframe)`
    - Enabling **Python Callbacks** for advanced interactivity. I have a gut feeling it's easy to integrate because
      - Streamlit and Bokeh are both Tornado Applications.
      - There are already a lot of tutorials on integrations with Flask, Django and Jupyter Notebooks.

    I believe the integration with Bokeh also can have a downside.
    Personally I find the Bokeh documentation and api hard to learn, navigate and use.
    And I start spending a lot of time on layout and formatting because I can!
    Is it **Pandoras Box** that I've opened?

    I believe it should be considered whether the improved integration should be with Bokeh or
    [Panel](https://github.com/holoviz/panel). Panel could provide integration to the full suite of
    PyViz tools and more advanced layouts and widgets.

    I will be adding more examples when I get the time.
    """
    return bokeh.models.Panel(child=_markdown(text), title="Vision")


def widgets_tables_panel():
    text = """
    ## My Vision on the Bokeh Streamlit Integration

    I believe the integration with Bokeh **can give Streamlit Super Powers** if improved slightly.

    For example

    - Wrapping the Bokeh api into a more **Streamlit like Api** like `st.bokeh.datatable(my_dataframe)`
    - Enabling **Python Callbacks** for advanced interactivity. I have a gut feeling it's easy to integrate because
      - Streamlit and Bokeh are both Tornado Applications.
      - There are already a lot of tutorials on integrations with Flask, Django and Jupyter Notebooks.

    I believe the integration with Bokeh also can have a downside.
    Personally I find the Bokeh documentation and api hard to learn, navigate and use.
    And I start spending a lot of time on layout and formatting because I can!
    Is it **Pandoras Box** that I've opened?

    I believe it should be considered whether the improved integration should be with Bokeh or
    [Panel](https://github.com/holoviz/panel). Panel could provide integration to the full suite of
    PyViz tools and more advanced layouts and widgets.

    I will be adding more examples when I get the time.
    """
    return bokeh.models.Panel(child=_markdown(text), title="Vision")


def vision_panel():
    text = """
## My Vision on the Bokeh Streamlit Integration

I believe the integration with Bokeh **can give Streamlit Super Powers** if improved slightly.

For example

- Wrapping the Bokeh api into a more **Streamlit like Api** like `st.bokeh.datatable(my_dataframe)`
- Enabling **Python Callbacks** for advanced interactivity. I have a gut feeling it's easy to integrate because
  - Streamlit and Bokeh are both Tornado Applications.
  - There are already a lot of tutorials on integrations with Flask, Django and Jupyter Notebooks.

I believe the integration with Bokeh also can have a downside.
Personally I find the Bokeh documentation and api hard to learn, navigate and use.
And I start spending a lot of time on layout and formatting because I can!
Is it **Pandoras Box** that I've opened?

I believe it should be considered whether the improved integration should be with Bokeh or
[Panel](https://github.com/holoviz/panel). Panel could provide integration to the full suite of
PyViz tools and more advanced layouts and widgets.

I will be adding more examples when I get the time.
"""
    return bokeh.models.Panel(child=_markdown(text), title="Vision")

def _markdown(text):
    return bokeh.models.widgets.markups.Div(
        text=markdown.markdown(text), sizing_mode="stretch_width"
    )


main()

