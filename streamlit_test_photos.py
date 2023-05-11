import streamlit as st
import PIL
from exif import Image
from collections import defaultdict
import pandas as pd

st.set_page_config(page_title="Geolocating Photos Application",
                   page_icon="🌍",
                   layout="wide",
                   initial_sidebar_state="expanded")

left, right = st.columns([5, 3])

st.sidebar.title("Geolocating Photos Application")
st.sidebar.markdown("Upload an Image and Get Its location on a Map")


def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


info_dict = defaultdict(list)


def collect_info_dict(file, image):
    info_dict["name"].append(file.name)

    if "make" in dir(image):
        info_dict["make"].append(image.make)
    if "model" in dir(image):
        info_dict["model"].append(image.model)
    if "datetime" in dir(image):
        info_dict["datetime"].append(image.datetime)

    if "gps_latitude" in dir(image):
        info_dict["latitude"].append(decimal_coords(
            image.gps_latitude, image.gps_latitude_ref))
        info_dict["longitude"].append(decimal_coords(
            image.gps_longitude, image.gps_longitude_ref))
    else:
        right.error("The Image have No Coordinates")

    return info_dict


def create_df(d):
    return pd.DataFrame.from_dict(d)


def main():
    file = st.sidebar.file_uploader("Choose a file")
    if file is not None:
        img = Image(file)
        left.image(PIL.Image.open(file))
        if img.has_exif:
            st.success("This image has EXIF Metadata. Hold on...")
            result = collect_info_dict(file, img)
            right.write(result)
            df = create_df(result)
            if 'latitude' in result.keys():
                st.map(df)
        else:
            st.error("The Image has no EXIF information")


if __name__ == "__main__":
    main()
