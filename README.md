# Simple Image Gallery

This allows you to set up an autoplay image slideshow.

## Usage

1. Add image files to `img` 
2. Run `python generate_data_json.py` (must use python3)
3. Run `python -m http.server 8000` to start a web server
4. Navigate to [http://localhost:8000](http://localhost:8000) to view the
   gallery.

To change autoplay settings, look in `index.html`. 
