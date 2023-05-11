import streamlit as st
from PIL import Image, ImageDraw, ImageOps

def main():
    # Set up the sidebar
    st.sidebar.title("Image Editor")
    image_file = st.sidebar.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    overlay_file = st.sidebar.file_uploader("Choose an overlay file", type=["jpg", "jpeg", "png"])
    scale = st.sidebar.slider("Scale", min_value=0.1, max_value=10.0, step=0.1, value=1.0)
    rotation = st.sidebar.slider("Rotation", min_value=-180, max_value=180, step=1, value=0)

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

    # Scale and rotate the overlay image
    overlay = overlay.rotate(rotation, expand=True)
    overlay = overlay.resize((int(overlay.width * scale), int(overlay.height * scale)))

    # Draw the overlay onto the image
    image.paste(overlay, (0, 0), overlay)

    # Show the edited image
    st.image(image, caption="Edited Image", use_column_width=True)

if __name__ == "__main__":
    main()

