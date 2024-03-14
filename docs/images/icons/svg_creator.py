import svgwrite

def create_letter_svg(letters, font_family="Arial", font_size=72, filename="letters.svg"):
    """Creates an SVG image containing the provided letters.

    Args:
        letters (str): The letters to include in the SVG.
        font_family (str, optional): The font family to use. Defaults to "Arial".
        font_size (int, optional): The font size in pixels. Defaults to 72.
        filename (str, optional): The name of the output SVG file. Defaults to "letters.svg".
    """

    # Establish SVG drawing canvas
    dwg = svgwrite.Drawing(filename, profile='tiny') 

    # Calculate width based on number of letters and font size (this is approximate)
    text_width = font_size * len(letters) * 0.6 
    # Add padding based on font size
    padding = font_size * 0.2

    # Create a <text> element for the letters 
    text = dwg.text(
        letters,
        insert=('50%', '50%'),  # Center text
        font_family=font_family,
        font_size=font_size,
        text_anchor='middle' 
    )

    # Create a <tspan> element for alignment and add the text 
    tspan = dwg.tspan(text, dy="0.35em", dominant_baseline="central") # Adjust 'dy' if needed
    # tspan.add(text) 
    dwg.add(tspan) 
    # tspan = dwg.tspan(letters, dy="0.35em", dominant_baseline="central") # Adjust 'dy' if needed
    # dwg.add(tspan) 

    # Adjust viewBox for proper display
    dwg.viewbox(
        minx=-padding,
        miny=-padding,
        width=text_width + 2*padding,
        height=font_size + 2*padding
    )

    dwg.save()

# Example usage
create_letter_svg("Hello World", font_family="Times New Roman", font_size=48)