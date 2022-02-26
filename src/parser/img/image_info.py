# coding: utf-8
import logging
import numpy as np
from PIL import Image
from typing import Union
from ..dataclass.shape import Shape
from ..dataclass.area_info import AreaInfo
from ..common.config import APP_CONFIG
from ..common import log_load
from ..web.response_img import ResponseImg
from ..cache.pickle_cache import PickleCache
from ..cache.text_cache import TextCache
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger

_PICKLE_CACHE: PickleCache = None
_TEXT_CACHE: TextCache = None


class ImageInfo:
    """Gets various image data like is inherited and pixel data"""
    @staticmethod
    def get_image_pixels_by_mode(image: Image.Image, dtype='int8'):
        """Get a numpy array of an image so that one can access values[x][y]."""
        # https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
        width, height = image.size
        if image.mode == "RGB":
            channels = 3
        elif image.mode == "L":
            channels = 1
        elif image.mode == "P":
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            return None
        pixel_values = np.array(image.getdata(), dtype=dtype).reshape(
            (height, width, channels))
        # pixel_values = numpy.array(pixel_values).reshape((width, height))
        return pixel_values

    @staticmethod
    def get_image_pixels(image: Image.Image, dtype='int8', reshape=True):
        """Get a numpy array of an image so that one can access values[x][y]."""
        if reshape:
            width, height = image.size
            pixel_values = np.array(
                image.getdata(), dtype=dtype).reshape((height, width))
        else:
            pixel_values = np.array(
                image.getdata(), dtype=dtype)
        return pixel_values

    @staticmethod
    def get_area_info(url: str, **kwargs) -> AreaInfo:
        """
        Gets Area info and shape if shape is available

        Args:
            url (str): Url of image

        Keyword Arguments:
            allow_cache (bool, optional) If ``False`` caching is ignored. Default ``True``

        Raises:
            Exception: [description]
            e: [description]

        Returns:
            AreaInfo: Area Info with optionl shape.
        """
        global _PICKLE_CACHE
        allow_cache = bool(kwargs.get('allow_cache', True))

        def get_cord(px: np.ndarray, color_index: int) -> Union[Shape, None]:
            # Tested this method against images in GNU. Result are perfect on images viewed.
            # Cordinates are exact. Borders are 1 px in size
            def zero_runs(a):
                # https://coderedirect.com/questions/302557/find-indexes-of-repeated-elements-in-an-array-python-numpy
                iszero = np.concatenate(
                    ([0], np.equal(a, 0).view(np.int8), [0]))
                absdiff = np.abs(np.diff(iszero))
                ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
                return ranges
            # to find a actual block must match several pixels in a row on the horizontal plane.
            # words have the same index color as non shape we are looking for.
            i_rows = px.shape[0]
            cords = None
            x1_y1 = None
            x2_y2 = None
            r1 = None
            r2 = None
            for y in range(0, i_rows):
                row = px[y, :]
                # start_seq = search_sequence_numpy(row, seq)
                runs = zero_runs(np.diff(row))
                # runs of 7 or more, to illustrate filter
                f_runs = runs[runs[:, 1]-runs[:, 0] >
                              APP_CONFIG.pixel_map_min_shape_width]
                if not x1_y1 is None:
                    for r in f_runs:
                        index = int(r[-1])  # last element
                        v = row[index]
                        if v == color_index:
                            x2_y2 = index, int(y),
                            r2 = r
                            break
                if x1_y1 is None:
                    for r in f_runs:
                        index = int(r[0])
                        v = row[index]
                        if v == color_index:
                            x1_y1 = index,  int(y)
                            r1 = r
                            break
                if x1_y1 and x2_y2:
                    # compare top border pixel length with bottom border
                    # the number should match or something is wrong
                    if (r1 == r2).all():
                        cords = x1_y1 + x2_y2
                    else:
                        msg = f"ImageInfo.get_area_info(). Image to and bottom borders did not mathc! Url: {url}"
                        logger.warning(msg)
                if not cords is None:
                    break
            if cords is None:
                return None
            return Shape(x1=cords[0], y1=cords[1], x2=cords[2], y2=cords[3])

        r_img = ResponseImg(url=url, cache_seconds=0)
        if _PICKLE_CACHE is None:
            _PICKLE_CACHE = PickleCache(tmp_dir=APP_CONFIG.cache_dir)
        seconds = _PICKLE_CACHE.seconds
        if allow_cache is False:
            _PICKLE_CACHE.seconds = 0.0
        try:
            filename = r_img.url_hash + '_ai.pkl'
            obj: AreaInfo = _PICKLE_CACHE.fetch_from_cache(filename=filename)
            if obj:
                return obj

            im = r_img.img
            pix = ImageInfo.get_image_pixels(im)
            row = pix[0, :]  # row 0
            found_px = -1
            # images are expected to be indexed png files
            # find the first pixel that does not have index of 0
            # if first pixes is 1 then not inherited, if 3 inherited
            for px in row:
                if px != 0:
                    found_px = px
                    break
            if found_px == -1:
                msg = f"Failed to find colored pixel in first row of image pixels. Url: {url}"
                raise Exception(msg)

            cord = get_cord(pix, APP_CONFIG.pixel_map_no_link)
            ai = AreaInfo(
                is_inherited=found_px == APP_CONFIG.pixel_inherit,
                shape=cord
            )

            _PICKLE_CACHE.save_in_cache(filename=filename, content=ai)
            return ai
        except Exception as e:
            logger.error(e)
            raise e
        finally:
            # resotore cache time
            _PICKLE_CACHE.seconds = seconds

    @staticmethod
    def is_inherit_img(url: str) -> bool:
        global _TEXT_CACHE
        r_img = ResponseImg(url=url, cache_seconds=0)
        if _TEXT_CACHE is None:
            _TEXT_CACHE = TextCache(tmp_dir=APP_CONFIG.cache_dir)
        try:
            filename = r_img.url_hash + '.txt'
            result = -1
            txt = _TEXT_CACHE.fetch_from_cache(filename=filename)
            if txt:
                result = int(txt)
                return result == APP_CONFIG.pixel_inherit
            im = r_img.img
            pix = ImageInfo.get_image_pixels(im)
            row = pix[0, :]  # row 0
            # images are expected to be indexed png files
            # find the first pixel that does not have index of 0
            # if first pixes is 1 then not inherited, if 3 inherited
            for px in row:
                if px != 0:
                    result = px
                    break
            if result == -1:
                msg = f"Failed to find colored pixel in first row of image pixels. Url: {url}"
                raise Exception(msg)
            content = str(result)
            _TEXT_CACHE.save_in_cache(filename=filename, content=content)
            return result == APP_CONFIG.pixel_inherit
        except Exception as e:
            logger.error(e)
            raise e
