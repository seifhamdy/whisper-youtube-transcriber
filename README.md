# YouTube Transcription Downloader

## About

YouTube Transcription Downloader is a Python script that allows you to download transcriptions from YouTube videos. You can either provide a file containing YouTube links or search for videos using keywords. The script utilizes the `youtubesearchpython`, `whisper`, `pytube`, and `pandas` libraries to fetch and transcribe the audio from YouTube videos. The transcriptions are then saved to a file for further analysis or processing.

## Built With

- [youtubesearchpython](https://github.com/alexmercerind/youtube-search-python)
- [whisper](https://github.com/OpenAI/whisper)
- [pytube](https://github.com/pytube/pytube)
- [pandas](https://github.com/pandas-dev/pandas)

## Usage

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Prepare your YouTube links or keywords based on the desired functionality.
   - To download from links, create a file called `links.txt` and add the YouTube links, each on a separate line.
   - To search for videos, use the `--keyword` option with your desired keyword(s) and an optional `--limit` to specify the number of search results.
4. Run the script using the following command:

   ```shell
   python script.py --links links.txt
   ```

   or

    ```shell
    python script.py --keyword "your_keyword_here" --limit 5
    ```

5. The transcriptions will be saved to the transcriptions.txt file in the same directory.

## TODO

- [ ] Add an option to specify the output file path for the transcriptions.
- [ ] Enhance error handling and provide meaningful error messages.
- [ ] Improve logging and progress tracking during the transcription process.
- [ ] Add support for more output formats, such as CSV or Excel.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
