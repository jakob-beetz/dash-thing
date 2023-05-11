import streamlit as st
from PIL import Image, ImageDraw, ImageOps

import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import numpy as np

def main():
    # Set up the sidebar
    st.sidebar.title("Image Editor")
    image_file = st.sidebar.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    overlay_file = st.sidebar.file_uploader("Choose an overlay file", type=["jpg", "jpeg", "png"])

    # Set up the main window
    st.title("Image Editor")
    if image_file is None:
        st.warning("Please upload an image file.")
        return
    image = Image.open(image_file)

    if overlay_file is None:
        st.warning("Please upload an overlay file.")
        return
    overlay = Image.open(overlay_file)

    # Initialize canvas to display image
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",
        stroke_width=3,
        stroke_color="rgba(255, 0, 0, 1)",
        background_image=image,
        height=image.height,
        width=image.width,
        drawing_mode="transform",
        display_toolbar=True,
        key="canvas",
    )

    # Apply transformations to the overlay image
    if canvas_result.image_data is not None:
        result = Image.fromarray(canvas_result.image_data.astype("uint8"), mode="RGBA")
        # Create a blank white image to overlay the transformed overlay image onto
        blank = Image.new("RGBA", image.size, (255, 255, 255, 255))
        # Resize the overlay image to fit the transformed bounding box
        overlay_resized = overlay.resize(result.size)
        # Overlay the resized overlay image onto the blank image
        blank.alpha_composite(overlay_resized, dest=(int(canvas_result.object_coords[0]), int(canvas_result.object_coords[1])))
        # Update the result image with the overlaid image
        result = Image.alpha_composite(result, blank)
        st.image(result, caption="Edited Image", use_column_width=True)

if __name__ == "__main__":
    main()
