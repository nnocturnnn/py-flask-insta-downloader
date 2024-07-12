# py-flask-insta-downloader

## Description

`py-flask-insta-downloader` is a web application built using Flask that allows users to download images from Instagram. This tool provides a simple interface for fetching and downloading images from Instagram posts by providing the URL of the post.

## Features

- Download images from Instagram posts by URL.
- Simple and intuitive web interface.
- Lightweight and easy to deploy.

## Installation

To set up and run the `py-flask-insta-downloader`, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/nnocturnnn/py-flask-insta-downloader.git
    ```

2. Navigate to the project directory:

    ```sh
    cd py-flask-insta-downloader
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Set the Flask application environment variable:

    ```sh
    export FLASK_APP=app.py
    ```

6. Run the Flask development server:

    ```sh
    flask run
    ```

7. Open your web browser and navigate to:

    ```
    http://127.0.0.1:5000
    ```

## Usage

1. Open the web application in your browser.
2. Enter the URL of the Instagram post containing the image you want to download.
3. Click the "Download" button.
4. The image will be fetched and a download link will be provided.

## Contributing

Contributions are welcome! If you'd like to contribute to `py-flask-insta-downloader`, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement your changes.
4. Test your changes thoroughly.
5. Commit and push your changes to your forked repository.
6. Submit a pull request with a detailed description of your changes.

## License

`py-flask-insta-downloader` is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
